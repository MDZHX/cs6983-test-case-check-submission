"""Objective metrics for one run (METRICS.md), written to reward.json.

Memory metrics: an LLM judge reads the memory after the last feedback round and
gives each answer-key item exactly one outcome:
  preference -> correct | wrong_scope | missed
  one-off    -> wrongly_saved | not_saved
  outdated   -> kept | retired
Draft metric: the judge checks the final draft against each must / must_not line.
draft_asked_clarification is read straight from the run (no draft was saved).

Every label comes with the memory text or draft sentence it relied on, saved in
reward_details.json, so any number can be checked by hand. reward_details.json also keeps every
judge call exactly as sent and received (judge_calls: instructions, input, output), so the rule
that produced a label is part of the run, even if scorer.py changes later.
"""

import json

from . import config

PREF_OUTCOMES = ["correct", "wrong_scope", "missed"]
ONE_OFF_OUTCOMES = ["wrongly_saved", "not_saved"]
OUTDATED_OUTCOMES = ["kept", "retired"]
SCOPE_ERRORS = ["too_narrow", "too_broad", "wrong_cue", "none"]

MEMORY_JUDGE = """You check what an email assistant has learned about its user. You get the assistant's \
memory files and a list of answer-key items written by the person who designed the test. Give every item \
exactly one outcome. Judge only what the memory says; do not guess what the assistant meant.

Preferences (lasting rules the assistant should have learned, each with a scope):
- correct: the memory states this rule, in any wording, and an assistant following the memory would apply it \
to the situations in the item's scope and not beyond. Hedged wording ("usually", "may") is fine.
- wrong_scope: the memory captures the rule's content, but for the wrong situations. Pick the scope error:
  too_narrow: covers clearly fewer situations than the scope, e.g. notes about specific people or one email \
where the scope is a whole group, so a new person in that group would not be covered.
  too_broad: covers situations outside the scope, e.g. a rule for everyone where the scope is one group.
  wrong_cue: tied to a different feature than the scope, e.g. the topic of the email instead of the recipient.
- missed: nothing in the memory states this rule, even narrowly.

One-offs (edits that should NOT become habits):
- wrongly_saved: the memory records it as something to repeat, a habit, or a lasting preference.
- not_saved: the memory does not record it as something to repeat (including not mentioning it at all).

Outdated practice (something the user used to do that later edits replaced; replaced_by says with what):
- retired: the memory does not mention the old practice, or it says the user no longer does it (stopped, \
changed, replaced by the newer practice).
- kept: anything else. The memory mentions the old practice without saying the user stopped: as a rule, as a \
caution against the newer practice, or as a past example, exception, or "it depends" that could still apply. \
Calling it an earlier exception, or saying not to generalize it, is not enough: unless the memory says the user no \
longer does it, it is kept.

For each item, quote the memory text your outcome relies on, copied exactly (empty string if none), and give \
a one-sentence reason. For one-offs, outdated practice, and preferences that are not wrong_scope, set \
scope_error to "none"."""

DRAFT_JUDGE = """You check an email draft against a checklist written by the person who designed the test. \
For each line, decide whether the statement holds for the draft. "must" lines should hold; "must_not" lines \
describe things that should not happen, so for those, holds = true means the draft DOES do the thing. Judge \
what the draft says, including paraphrases and euphemisms. Quote the draft sentence your answer relies on, \
copied exactly (empty string if none), and give a one-sentence reason."""


def _schema(name: str, item_props: dict) -> dict:
    return {"format": {"type": "json_schema", "name": name, "strict": True, "schema": {
        "type": "object", "additionalProperties": False, "required": ["items"],
        "properties": {"items": {"type": "array", "items": {
            "type": "object", "additionalProperties": False, "required": list(item_props),
            "properties": item_props}}}}}}


MEMORY_SCHEMA = _schema("memory_judgment", {
    "id": {"type": "string"},
    "outcome": {"type": "string", "enum": PREF_OUTCOMES + ONE_OFF_OUTCOMES + OUTDATED_OUTCOMES},
    "scope_error": {"type": "string", "enum": SCOPE_ERRORS},
    "memory_quote": {"type": "string"},
    "reason": {"type": "string"},
})
DRAFT_SCHEMA = _schema("draft_judgment", {
    "id": {"type": "string"},
    "holds": {"type": "boolean"},
    "draft_quote": {"type": "string"},
    "reason": {"type": "string"},
})


def _ask(llm, instructions: str, prompt: str, schema: dict, calls: list) -> list[dict]:
    resp = llm.create(model=config.JUDGE_MODEL, instructions=instructions,
                      input=[{"role": "user", "content": prompt}], text=schema)
    text = "".join(c.text for it in resp.output if it.type == "message" for c in it.content
                   if c.type == "output_text")
    items = json.loads(text)["items"]
    calls.append({"judge": schema["format"]["name"], "model": config.JUDGE_MODEL,
                  "instructions": instructions, "input": prompt, "output": items})
    return items


def _memory_text(files: dict) -> str:
    return "\n\n".join(f"=== {p} ===\n{c}" for p, c in files.items()) or "(the memory is empty)"


def judge_memory(llm, key: dict, files: dict, calls: list) -> list[dict]:
    items = ([{"id": p["id"], "type": "preference", "rule": p["rule"], "scope": p["scope"]}
              for p in key["preferences"]]
             + [{"id": o["id"], "type": "one-off", "edit": o["edit"]} for o in key["one_offs"]]
             + [{"id": o["id"], "type": "outdated", "practice": o["practice"], "replaced_by": o["replaced_by"]}
                for o in key["outdated"]])
    outcomes = {"preference": PREF_OUTCOMES, "one-off": ONE_OFF_OUTCOMES, "outdated": OUTDATED_OUTCOMES}
    allowed = {i["id"]: outcomes[i["type"]] for i in items}
    prompt = (f"MEMORY FILES\n\n{_memory_text(files)}\n\nANSWER-KEY ITEMS\n\n{json.dumps(items, indent=2)}")
    for _ in range(2):  # one retry if the judge skips, repeats, or mislabels an item
        out = _ask(llm, MEMORY_JUDGE, prompt, MEMORY_SCHEMA, calls)
        by_id = {o["id"]: o for o in out}
        if sorted(by_id) == sorted(allowed) and len(out) == len(allowed) \
                and all(by_id[i]["outcome"] in allowed[i] for i in allowed):
            break
    else:
        raise RuntimeError(f"memory judge gave invalid labels: {out}")
    return [{**i, **{k: by_id[i["id"]][k] for k in ("outcome", "scope_error", "memory_quote", "reason")}}
            for i in items]


def judge_draft(llm, final_task: dict, draft: dict, calls: list) -> list[dict]:
    checks = ([{"id": f"must_{n + 1}", "kind": "must", "statement": s} for n, s in enumerate(final_task["must"])]
              + [{"id": f"must_not_{n + 1}", "kind": "must_not", "statement": s}
                 for n, s in enumerate(final_task["must_not"])])
    prompt = (f"DRAFT\n\nSubject: {draft['subject']}\n\n{draft['body']}\n\n"
              f"CHECKLIST\n\n{json.dumps(checks, indent=2)}")
    ids = sorted(c["id"] for c in checks)
    for _ in range(2):
        out = _ask(llm, DRAFT_JUDGE, prompt, DRAFT_SCHEMA, calls)
        by_id = {o["id"]: o for o in out}
        if sorted(by_id) == ids and len(out) == len(ids):
            break
    else:
        raise RuntimeError(f"draft judge gave invalid labels: {out}")
    return [{**c, **{k: by_id[c["id"]][k] for k in ("holds", "draft_quote", "reason")},
             "passed": by_id[c["id"]]["holds"] == (c["kind"] == "must")} for c in checks]


def score(llm, case: dict, res: dict) -> tuple[dict, dict]:
    """Returns (reward, details). A metric is left out of reward when it can't be scored: the case gives no
    answer for it, or (memory metrics) the run is a control that skipped the feedback rounds."""
    reward, details, calls = {}, {}, []
    key = case["answer_key"]
    if res["baseline"]:
        details["memory_items"] = "not scored: control run, no feedback rounds"
    elif key["preferences"] or key["one_offs"] or key["outdated"]:
        mem = judge_memory(llm, key, res["memory_after_sessions"], calls)
        count = lambda o: sum(m["outcome"] == o for m in mem)  # noqa: E731
        reward.update(prefs_correct=count("correct"), prefs_wrong_scope=count("wrong_scope"),
                      prefs_missed=count("missed"), one_offs_wrongly_saved=count("wrongly_saved"),
                      outdated_kept=count("kept"))
        details["memory_items"] = mem
    else:
        details["memory_items"] = "not scored: the case has no answer_key"

    final, ft = res["final"], case["final_task"]
    asked = final["outcome"] != "drafted"
    if ft["must"] or ft["must_not"]:
        checks = [] if asked else judge_draft(llm, ft, final["draft"], calls)
        reward["draft_correct"] = int(not asked and all(c["passed"] for c in checks))
        details["draft_checks"] = checks if checks else "no draft was saved"
    else:
        details["draft_checks"] = "not scored: the final task has no must / must_not"
    reward["draft_asked_clarification"] = int(asked)
    details["judge_calls"] = calls  # every call in order, retries included
    details["final_draft"] = final["draft"]
    details["final_reply"] = final["reply"]
    details["memory_after_sessions"] = res["memory_after_sessions"]
    return reward, details
