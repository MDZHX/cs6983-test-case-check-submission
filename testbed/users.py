"""Who plays the professor. The runner calls the same methods in both modes; only the
source of the professor's revision differs.

  ScriptedUser   simulated mode: the revision and comment come from the feedback-round file
  HumanUser      human mode: a person edits the draft on a local web page (testbed/webui.py)

Everything the agent sees is built by the runner from what these return, so the agent
can't tell the two modes apart.
"""


def unwrap(text: str) -> str:
    """Join lines the case author hard-wrapped (long lines), so text reflows on the page.
    Short lines, like a greeting or "Best,", keep their line breaks."""
    out = []
    for line in text.strip().split("\n"):
        if out and len(out[-1]) >= 70 and line.strip() and out[-1].strip():
            out[-1] = out[-1].rstrip() + " " + line.strip()
        else:
            out.append(line)
    return "\n".join(out)


class ScriptedUser:
    description = "scripted: requests, revisions and comments come from the case files"

    def revise(self, round_: dict, number: int, total: int) -> tuple[str, str | None]:
        """The version the professor sent, plus an optional comment to the assistant."""
        return round_["sent"], round_.get("comment")

    def working(self, message: str) -> None:
        """The agent is busy (nothing to show in simulated mode)."""

    def show_reply(self, round_: dict, reply: str) -> None:
        """The agent's answer after the revision."""

    def show_final(self, final_task: dict, draft: dict | None, reply: str) -> None:
        """The agent's draft (or question) for the final task."""


class HumanUser:
    """A person at the local web page. Each call shows a page and, where the person must act, waits."""

    def __init__(self, bridge, case: dict, participant: str):
        self.bridge, self.case, self.participant = bridge, case, participant
        self.description = f"person: participant {participant}, on the local web page (testbed/webui.py)"

    def _task(self, t: dict) -> dict:
        from .runner import contact_line
        p = self.case["persona"]
        out = {"request": unwrap(t["request"]), "to": [contact_line(p, a) for a in t["to"]],
               "cc": [contact_line(p, a) for a in t["cc"]], "date": t["date"]}
        if t.get("incoming"):
            m = t["incoming"]
            out["incoming"] = {"from": contact_line(p, m["from"]), "subject": m["subject"], "body": unwrap(m["body"])}
        return out

    def revise(self, round_: dict, number: int, total: int) -> tuple[str, str | None]:
        answer = self.bridge.ask("revise", number=number, total=total, **self._task(round_),
                                 subject=round_.get("subject"), draft=unwrap(round_["draft"]))
        return answer["sent"], (answer.get("comment") or "").strip() or None

    def working(self, message: str) -> None:
        self.bridge.show("working", message=message)

    def show_reply(self, round_: dict, reply: str) -> None:
        self.bridge.ask("reply", reply=reply)

    def show_final(self, final_task: dict, draft: dict | None, reply: str) -> None:
        self.bridge.ask("final", **self._task(final_task), draft=draft, reply=reply)
