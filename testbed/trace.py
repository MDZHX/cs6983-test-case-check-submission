"""The run's event log, written out as trajectory.json.

Every message, tool call, and tool result is recorded the moment it happens, with a
UTC timestamp in ISO 8601 ("2026-11-15T20:41:07.123Z"). The conversation sent to the
model can't carry extra fields, so the log is kept alongside it.

`scenario_date` on a session marks the date in the case's story (the email's date);
`timestamp` is always the real time of the run.
"""

from datetime import datetime, timezone


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


class Trace:
    def __init__(self):
        self.steps: list[dict] = []
        self.session: str | None = None

    def add(self, type: str, **fields) -> dict:
        step = {"timestamp": now(), "session": self.session, "type": type, **fields}
        self.steps.append(step)
        return step

    def start_session(self, session_id: str, kind: str, scenario_date: str) -> None:
        self.session = session_id
        self.add("session_start", kind=kind, scenario_date=scenario_date)
