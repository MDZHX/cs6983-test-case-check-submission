"""report.md: one run as a readable trace, ending with how it was scored.

The numbers come from testbed/scorer.py; this file only lays them out next to the
trace, with the judge's quote for each label, so a person can check them.
"""

CONDITION_LABEL = {"full": "full case", "none": "baseline: no memory", "seed": "baseline: seed memory only"}

REVIEW_BLOCK = """## Reviewer notes

- Do the judge's labels look right? (yes / no, which ones):
- What went wrong, in one or two sentences:
"""


def _block(text: str | None) -> str:
    return "```\n" + (text or "(none)").strip() + "\n```"


def _memory(files: dict) -> list[str]:
    return [f"`{p}`\n{_block(c)}\n" for p, c in files.items()] or ["(empty)", ""]


def _diff(text: str) -> str:
    return "```diff\n" + text + "\n```"


def _final_output(f: dict) -> list[str]:
    if f["outcome"] == "drafted":
        out = [f"**Draft** (subject: {f['draft']['subject']}):", _block(f["draft"]["body"])]
    else:
        out = ["**No draft. The agent replied in chat:**", _block(f["reply"])]
    facts = (f"Read memory before drafting: {'yes' if f['read_memory_before_drafting'] else '**no**'}. "
             f"Looked up a contact: {'yes' if f['looked_up_contact'] else 'no'}.")
    return out + ["", facts, ""]


def run_report(case: dict, res: dict, condition: str, run_name: str, reward: dict, details: dict) -> str:
    out = [f"# {case['id']} / {CONDITION_LABEL[condition]} / {run_name}", "",
           "## Starting memory", "", *_memory(res["start_memory"])]
    for s in res["sessions"]:
        out += [f"## Feedback round {s['id']} ({s['date']})", "", f"**Request:** {s['request'].strip()}", "",
                "**Draft (pre-written):**", _block(s["draft"]), "", "**Sent by the professor:**", _block(s["sent"]), ""]
        if s["comment"]:
            out += [f"**Comment:** {s['comment'].strip()}", ""]
        out += [f"**Agent's reply:** {s['reply'].strip()}", "", "**What the agent changed in memory:**",
                _diff(s["memory_diff"]), ""]
    f = res["final"]
    out += ["## Final task", "", f"**Request:** {f['request'].strip()}", "",
            *_final_output(f),
            "## Memory at the end", "", *_memory(res["end_memory"]), *_scoring(reward, details), REVIEW_BLOCK]
    return "\n".join(out) + "\n"


def _scoring(reward: dict, details: dict) -> list[str]:
    out = ["## Scoring", "", "`reward.json`: " + ", ".join(f"`{k}` = {v}" for k, v in reward.items()), ""]
    items = details.get("memory_items")
    if isinstance(items, list):
        out += ["**Memory after the last feedback round, item by item:**", "",
                "| item | type | outcome | scope error | memory quote | reason |", "|---|---|---|---|---|---|"]
        for m in items:
            text = m.get("rule") or m.get("edit") or f"{m['practice']} (replaced by: {m['replaced_by']})"
            out.append(f"| {m['id']}: {_cell(text)} | {m['type']} | **{m['outcome']}** | "
                       f"{m['scope_error'] if m['scope_error'] != 'none' else ''} | {_cell(m['memory_quote'])} | "
                       f"{_cell(m['reason'])} |")
        out.append("")
    elif items:
        out += [f"Memory: {items}", ""]
    checks = details.get("draft_checks")
    if isinstance(checks, list) and checks:
        out += ["**Final draft checklist:**", "", "| check | statement | passed | draft quote | reason |",
                "|---|---|---|---|---|"]
        for c in checks:
            out.append(f"| {c['kind']} | {_cell(c['statement'])} | {'yes' if c['passed'] else '**no**'} | "
                       f"{_cell(c['draft_quote'])} | {_cell(c['reason'])} |")
        out.append("")
    elif checks:
        out += [f"Final draft: {checks}", ""]
    return out


def _cell(text) -> str:
    return " ".join(str(text or "").split()).replace("|", "\\|")
