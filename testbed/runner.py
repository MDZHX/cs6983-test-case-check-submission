"""Play one test case: the feedback rounds, then the final task.

Every round is a fresh conversation; only memory carries over.

Feedback round (the agent's memory update is live):
  Professor: <request + recipients' contact cards>           from the case
  Agent:     views /memories, then saves <draft>             pre-filled: the case author wrote the draft
  Professor: "I edited it before sending. Here's what went out: <sent>"  (+ optional comment)
             simulated mode: from the case; human mode: the participant's edit (testbed/users.py)
  Agent:     decides what, if anything, to write to memory   LIVE

Final task:
  Professor: <request + contact cards>                       from the case
  Agent:     reads memory, drafts                            LIVE

Controls skip the feedback rounds: "none" also starts from empty memory
(the model's default behavior), "seed" starts from the starting memory (the effect of
the rounds themselves).
"""

import difflib
import json

from . import agent
from .memory import MemoryStore
from .trace import Trace
from .tools import DRAFT_SAVED, Desk
from .users import ScriptedUser

SENT_TEMPLATE = "I edited it before sending. Here's what went out:\n\n---\n{sent}\n---"
UNCHANGED = "I sent it as is."


def revision_message(draft: str, sent: str, comment: str | None) -> str:
    same = " ".join(sent.split()) == " ".join(draft.split())  # ignore line wrapping
    msg = UNCHANGED if same else SENT_TEMPLATE.format(sent=sent.strip())
    return msg + ("\n\n" + comment.strip() if comment else "")


def contact_line(persona: dict, addr: str) -> str:
    c = next((c for c in persona["contacts"] if c["email"].lower() == addr.lower()), None)
    return f"{c['name']} <{c['email']}> ({c['role']})" if c else addr


def task_message(persona: dict, t: dict) -> str:
    """What Jane types, plus the header an email client would show the assistant."""
    lines = [t["request"].strip(), "", "To: " + "; ".join(contact_line(persona, a) for a in t["to"])]
    if t["cc"]:
        lines.append("Cc: " + "; ".join(contact_line(persona, a) for a in t["cc"]))
    if t.get("incoming"):
        m = t["incoming"]
        lines += ["", "Replying to:", f"From: {contact_line(persona, m['from'])}", f"Subject: {m['subject']}",
                  "", m["body"].strip()]
    return "\n".join(lines)


def mem_diff(before: str, after: str) -> str:
    d = difflib.unified_diff(before.splitlines(), after.splitlines(), "before", "after", lineterm="", n=1)
    return "\n".join(d) or "(no change)"


def _tool_calls(convo: list, start: int) -> list[dict]:
    return [it for it in convo[start:] if it.get("type") == "function_call"]


def feedback_session(llm, case: dict, s: dict, memory: MemoryStore, trace: Trace, user, number: int) -> dict:
    persona = case["persona"]
    trace.start_session(s["id"], "feedback", s["date"])
    desk = Desk(persona["contacts"])
    view = memory.call({"command": "view", "path": "/memories"})  # the pre-filled agent turn looks first
    subject = s.get("subject") or (f"Re: {s['incoming']['subject']}" if s.get("incoming") else "(no subject)")
    convo = [
        {"role": "user", "content": task_message(persona, s)},
        {"type": "function_call", "call_id": "call_prefill_view", "name": "memory",
         "arguments": json.dumps({"command": "view", "path": "/memories"})},
        {"type": "function_call_output", "call_id": "call_prefill_view", "output": view},
        {"type": "function_call", "call_id": "call_prefill_draft", "name": "save_draft",
         "arguments": json.dumps({"subject": subject, "body": s["draft"].strip()})},
        {"type": "function_call_output", "call_id": "call_prefill_draft", "output": DRAFT_SAVED},
        {"role": "assistant", "content": "I've saved a draft for you to review."},
    ]
    log_from, before = len(memory.log), memory.dump()
    # The scripted part of the session, logged in order. "prefilled" marks agent turns the case author wrote.
    trace.add("message", role="user", text=convo[0]["content"])
    for i in (1, 3):
        call, result = convo[i], convo[i + 1]
        trace.add("tool_call", role="assistant", prefilled=True, tool=call["name"], tool_call_id=call["call_id"],
                  arguments=json.loads(call["arguments"]))
        trace.add("tool_result", prefilled=True, tool=call["name"], tool_call_id=call["call_id"],
                  output=result["output"])
    trace.add("message", role="assistant", prefilled=True, text=convo[5]["content"])
    sent, comment = user.revise(s, number, len(case["feedback_sessions"]))
    msg = revision_message(s["draft"], sent, comment)
    convo.append({"role": "user", "content": msg})
    live_from = len(convo)
    trace.add("message", role="user", text=msg)
    user.working("The assistant is reading your edits...")

    def execute(name, args):
        return memory.call(args) if name == "memory" else desk.call(name, args)

    instructions = agent.system_prompt(persona, s["date"])
    reply = agent.run_turn(llm, instructions, convo, execute, trace)
    trace.add("memory_snapshot", files=memory.snapshot())
    user.show_reply(s, reply)
    ops = memory.log[log_from:]
    return {
        "id": s["id"], "date": s["date"], "request": s["request"], "draft": s["draft"], "sent": sent,
        "comment": comment, "reply": reply, "memory_ops": ops,
        "memory_after": memory.snapshot(), "memory_diff": (diff := mem_diff(before, memory.dump())),
        "wrote_memory": diff != "(no change)",
        "transcript": convo, "live_from": live_from,
    }


def final_task(llm, case: dict, memory: MemoryStore, trace: Trace, user) -> dict:
    persona, f = case["persona"], case["final_task"]
    desk = Desk(persona["contacts"])
    convo = [{"role": "user", "content": task_message(persona, f)}]
    trace.start_session("final", "final_task", f["date"])
    trace.add("message", role="user", text=convo[0]["content"])
    user.working("The assistant is drafting the new email...")

    def execute(name, args):
        return memory.call(args) if name == "memory" else desk.call(name, args)

    instructions = agent.system_prompt(persona, f["date"])
    reply = agent.run_turn(llm, instructions, convo, execute, trace)
    calls = _tool_calls(convo, 0)
    first_mem = next((i for i, c in enumerate(calls) if c["name"] == "memory"), None)
    first_draft = next((i for i, c in enumerate(calls) if c["name"] == "save_draft"), None)
    draft = desk.drafts[-1] if desk.drafts else None
    user.show_final(f, draft, reply)
    return {
        # "asked": the agent answered in chat without drafting, e.g. a clarifying question
        "request": f["request"], "outcome": "drafted" if draft else "asked", "draft": draft, "reply": reply,
        "read_memory_before_drafting": first_mem is not None and (first_draft is None or first_mem < first_draft),
        "looked_up_contact": any(c["name"] == "lookup_contact" for c in calls),
        "transcript": convo,
    }


def run_case(llm, case: dict, baseline: str | None = None, user=None) -> dict:
    """baseline: None (full case), "none" (empty memory, no rounds), "seed" (starting memory, no rounds).
    user: who plays the professor (testbed/users.py); scripted by default."""
    user = user or ScriptedUser()
    trace = Trace()
    memory = MemoryStore({} if baseline == "none" else case["seed_memory"])
    start = memory.snapshot()
    trace.add("memory_snapshot", files=start)  # starting state, so a reset can be checked
    sessions = [] if baseline else [feedback_session(llm, case, s, memory, trace, user, i + 1)
                                    for i, s in enumerate(case["feedback_sessions"])]
    memory_after_sessions = memory.snapshot()  # what the answer key is scored against
    final = final_task(llm, case, memory, trace, user)
    return {"baseline": baseline, "start_memory": start, "sessions": sessions,
            "memory_after_sessions": memory_after_sessions, "final": final,
            "end_memory": memory.snapshot(), "trace": trace.steps}
