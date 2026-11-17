"""The email agent: system prompt, tool set, and the tool loop.

Memory follows Anthropic's memory tool: the agent has a `memory` tool over a
/memories directory and is told to view it before doing anything else. It
decides by itself, mid-conversation, whether the professor's revision is worth
writing down, where, and how broadly. Nothing reads or writes memory for it.
"""

import json
from dataclasses import dataclass, field

from openai import OpenAI

from . import config
from .memory import MEMORY_PROTOCOL, MEMORY_TOOL, MEMORY_TOPIC
from .tools import EMAIL_TOOLS

BASE_PROMPT = """You are the email assistant for {name} ({email}). {description}

{first_name} tells you what email to write, and you draft it in {first_name}'s voice with save_draft. \
{first_name} reviews every draft and sends it. You can look people up with lookup_contact. Today is {date}."""

TOOLS = EMAIL_TOOLS + [MEMORY_TOOL]


class BudgetExceeded(RuntimeError):
    pass


@dataclass
class Usage:
    input_tokens: int = 0
    cached_tokens: int = 0
    output_tokens: int = 0
    calls: int = 0

    def add(self, u) -> None:
        self.calls += 1
        self.input_tokens += u.input_tokens
        details = getattr(u, "input_tokens_details", None)
        self.cached_tokens += (getattr(details, "cached_tokens", 0) or 0) if details else 0
        self.output_tokens += u.output_tokens

    @property
    def cost(self) -> float:
        uncached = self.input_tokens - self.cached_tokens
        return (uncached * config.PRICE_IN + self.cached_tokens * config.PRICE_CACHED_IN
                + self.output_tokens * config.PRICE_OUT) / 1e6


@dataclass
class LLM:
    """One OpenAI client plus a running cost meter for the whole invocation."""
    budget_usd: float
    client: object = None
    usage: Usage = field(default_factory=Usage)

    def __post_init__(self):
        self.client = self.client or OpenAI()

    def create(self, **kw):
        if self.usage.cost > self.budget_usd:
            raise BudgetExceeded(f"spent ${self.usage.cost:.2f}, budget ${self.budget_usd:.2f}")
        if config.REASONING_EFFORT:
            kw["reasoning"] = {"effort": config.REASONING_EFFORT}
        resp = self.client.responses.create(max_output_tokens=config.MAX_OUTPUT_TOKENS, store=False, **kw)
        self.usage.add(resp.usage)
        return resp


def _parse(arguments: str | None) -> dict:
    try:
        return json.loads(arguments or "{}")
    except json.JSONDecodeError:
        return {}


def system_prompt(persona: dict, date: str) -> str:
    first = persona["first_name"]
    return (BASE_PROMPT.format(first_name=first, date=date, name=persona["name"], email=persona["email"],
                               description=persona["description"])
            + "\n\n" + MEMORY_PROTOCOL + "\n\n" + MEMORY_TOPIC.format(first_name=first))


def run_turn(llm: LLM, instructions: str, convo: list, execute, trace=None) -> str:
    """Run the tool loop until the model answers in plain text.

    `convo` is the session so far and is extended in place. `execute(name, args)`
    runs one tool call. Every model message, tool call, and tool result is also logged
    to `trace` (a testbed.trace.Trace) with a timestamp. Returns the final assistant text.
    """
    log = trace.add if trace else (lambda *a, **k: None)
    final_text = ""
    for _ in range(config.MAX_TURNS):
        resp = llm.create(model=config.MODEL, instructions=instructions, input=convo, tools=TOOLS)
        calls = []
        for item in resp.output:
            if item.type == "function_call":
                calls.append(item)
                convo.append({"type": "function_call", "call_id": item.call_id, "name": item.name,
                              "arguments": item.arguments})
                log("tool_call", role="assistant", tool=item.name, tool_call_id=item.call_id,
                    arguments=_parse(item.arguments))
            elif item.type == "message":
                final_text = "".join(c.text for c in item.content if c.type == "output_text")
                convo.append({"role": "assistant", "content": final_text})
                log("message", role="assistant", text=final_text)
            # reasoning items are not replayed (store=False, no encrypted content)
        if not calls:
            return final_text
        for call in calls:
            args = _parse(call.arguments)
            output = execute(call.name, args)
            convo.append({"type": "function_call_output", "call_id": call.call_id, "output": output})
            log("tool_result", tool=call.name, tool_call_id=call.call_id, output=output)
    raise RuntimeError(f"agent did not finish within {config.MAX_TURNS} tool-loop iterations")
