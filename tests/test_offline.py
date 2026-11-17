"""End-to-end plumbing test with a scripted fake OpenAI client: no API calls, no cost.

  docker compose run --rm --entrypoint python testbed tests/test_offline.py
"""

import os
import sys

if __name__ == "__main__" and os.environ.get("TESTBED_IN_DOCKER") != "1":  # set by the Dockerfile
    sys.exit("Run this through Docker, from the repository folder (see README.md), e.g.\n"
             "  docker compose run --rm testbed cases/<case> --validate")

import json
import shutil
import socket
import threading
import time
import urllib.error
import urllib.request
import tempfile
from pathlib import Path
from types import SimpleNamespace as NS

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import run  # noqa: E402
from testbed import config  # noqa: E402
from testbed.case import CaseError, load_case  # noqa: E402
from testbed.memory import MemoryStore  # noqa: E402


def _usage():
    return NS(input_tokens=1000, output_tokens=100, input_tokens_details=NS(cached_tokens=0))


def _call(name, args, i):
    return NS(type="function_call", call_id=f"c{i}", name=name, arguments=json.dumps(args))


def _say(text):
    return NS(type="message", content=[NS(type="output_text", text=text)])


def _judge(kw):
    """Plays the judge: labels every item it is given (first preference wrong_scope, the rest correct)."""
    prompt = kw["input"][0]["content"]
    if "ANSWER-KEY ITEMS" in prompt:
        items = json.loads(prompt.split("ANSWER-KEY ITEMS\n\n", 1)[1])
        out = [{"id": it["id"], "memory_quote": "", "reason": "fake",
                "outcome": ("wrong_scope" if n == 0 else "correct") if it["type"] == "preference"
                else "not_saved" if it["type"] == "one-off" else "retired",
                "scope_error": "too_narrow" if n == 0 and it["type"] == "preference" else "none"}
               for n, it in enumerate(items)]
    else:
        checks = json.loads(prompt.split("CHECKLIST\n\n", 1)[1])
        out = [{"id": c["id"], "holds": c["kind"] == "must", "draft_quote": "", "reason": "fake"} for c in checks]
    return NS(output=[_say(json.dumps({"items": out}))], usage=_usage())


class FakeResponses:
    """Plays a plausible agent: views memory, drafts, and saves a note after a revision."""
    n = 0

    def create(self, **kw):
        FakeResponses.n += 1
        i = FakeResponses.n
        if "text" in kw:
            return _judge(kw)
        convo, last = kw["input"], kw["input"][-1]
        names = [it["name"] for it in convo if it.get("type") == "function_call"]
        if last.get("role") == "user" and "edited it before sending" in last["content"]:
            item = _call("memory", {"command": "create", "path": "/memories/notes.md",
                                    "file_text": "- Students: sign Jane"}, i)
        elif last.get("type") == "function_call_output" and names[-1] == "memory" and "save_draft" in names:
            item = _say("Noted for next time.")
        elif "memory" not in names:
            item = _call("memory", {"command": "view", "path": "/memories"}, i)
        elif "save_draft" not in names:
            item = _call("save_draft", {"subject": "Update", "body": "Hi all,\n\nQuiz moves to Monday.\n\nJane"}, i)
        else:
            item = _say("Draft saved.")
        return NS(output=[NS(type="reasoning"), item], usage=_usage())


def test_memory_store():
    m = MemoryStore()
    assert m.call({"command": "create", "path": "/memories/a.md", "file_text": "x\ny"}).startswith("File created")
    assert "     2\ty" in m.call({"command": "view", "path": "/memories/a.md"})
    assert m.call({"command": "str_replace", "path": "/memories/a.md", "old_str": "y", "new_str": "z"}) \
        == "The memory file has been edited."
    assert m.call({"command": "insert", "path": "/memories/a.md", "insert_line": 0, "insert_text": "top"}) \
        .endswith("edited.")
    assert m.files["/memories/a.md"] == "top\nx\nz"
    assert "outside" in m.call({"command": "view", "path": "/etc/passwd"})
    assert "outside" in m.call({"command": "view", "path": "/memories/../x"})
    assert m.call({"command": "rename", "old_path": "/memories/a.md", "new_path": "/memories/b.md"}) \
        .startswith("Successfully")
    assert m.call({"command": "delete", "path": "/memories/b.md"}).startswith("Successfully")
    assert m.files == {}


def test_cases():
    config.RUNS_DIR = Path(tempfile.mkdtemp())
    client = NS(responses=FakeResponses())
    folders = sorted(p.parent for p in (ROOT / "cases").glob("*/final_task.md"))
    assert len(folders) >= 2, folders  # the template and at least one real case
    for folder in folders:
        assert run.main([str(folder), "--validate"]) == 0, folder
    committee = str(ROOT / "cases" / "disclosure_committee")
    assert run.main([committee, "--runs", "2", "--budget", "5"], client=client) == 0
    assert run.main([committee, "--runs", "1", "--condition", "none", "--budget", "5"], client=client) == 0

    base = config.RUNS_DIR / "disclosure_committee"
    assert sorted(p.name for p in base.glob("run-*")) == ["run-01", "run-02"]
    run1 = base / "run-01"
    for name in ("trajectory.json", "reward.json", "config.json", "reward_details.json", "report.md"):
        assert (run1 / name).exists(), name

    reward = json.loads((run1 / "reward.json").read_text())
    assert reward == {"prefs_correct": 1, "prefs_wrong_scope": 1, "prefs_missed": 0, "one_offs_wrongly_saved": 0,
                      "outdated_kept": 0, "draft_correct": 1, "draft_asked_clarification": 0}, reward

    calls = json.loads((run1 / "reward_details.json").read_text())["judge_calls"]
    assert [c["judge"] for c in calls] == ["memory_judgment", "draft_judgment"], calls
    assert all(c["instructions"] and c["input"] and c["output"] for c in calls)

    steps = json.loads((run1 / "trajectory.json").read_text())["steps"]
    assert all(st["timestamp"].endswith("Z") and "T" in st["timestamp"] for st in steps)
    assert [st["timestamp"] for st in steps] == sorted(st["timestamp"] for st in steps)
    kinds = {st["type"] for st in steps}
    assert {"session_start", "message", "tool_call", "tool_result", "memory_snapshot"} <= kinds, kinds
    assert steps[0]["type"] == "memory_snapshot" and steps[0]["files"] == {}  # reset: starts from seed memory
    sessions = [st for st in steps if st["type"] == "session_start"]
    assert len(sessions) == 9 and sessions[-1]["session"] == "final"
    assert any(st.get("prefilled") for st in steps)
    assert any(st["type"] == "tool_call" and st["tool"] == "save_draft" and not st.get("prefilled") for st in steps)

    cfg = json.loads((run1 / "config.json").read_text())
    assert cfg["mode"] == "simulated_user" and cfg["condition"] == "full" and cfg["model"]["id"] == config.MODEL
    details = json.loads((run1 / "reward_details.json").read_text())
    assert details["memory_items"][0]["scope_error"] == "too_narrow"
    assert "## Scoring" in (run1 / "report.md").read_text()

    control = json.loads((base / "no_memory" / "run-01" / "reward.json").read_text())
    assert "prefs_correct" not in control and control["draft_correct"] == 1, control
    summary = (base / "summary.md").read_text()
    assert "Memory breakdown in 2 of 2 runs; draft breakdown in 0 of 2 runs." in summary, summary

    # a case with an outdated item: the judge is asked kept | retired, and outdated_kept is reported
    drift = str(ROOT / "cases" / "extension_drift")
    assert run.main([drift, "--runs", "1", "--budget", "5"], client=client) == 0
    drift_run = config.RUNS_DIR / "extension_drift" / "run-01"
    assert json.loads((drift_run / "reward.json").read_text())["outdated_kept"] == 0
    assert "| outdated | **retired** |" in (drift_run / "report.md").read_text()


def test_case_errors():
    """A broken case folder is rejected with every problem listed, before any API call."""
    tmp = Path(tempfile.mkdtemp()) / "xx_broken"
    shutil.copytree(ROOT / "cases" / "_template", tmp)
    key = tmp / "answer_key.yaml"
    text = key.read_text()
    replaced_by = next(line for line in text.splitlines() if line.strip().startswith("replaced_by:"))
    key.write_text(text.replace("evidence: [01_office_hours]     #", "evidence: [02_missing]     #")
                   .replace(replaced_by + "\n", ""))  # an outdated item without replaced_by
    (tmp / "feedback_rounds" / "01_office_hours.md").write_text("---\nto: cs4100-students@univ.edu\n---\n## Request\nx\n")
    try:
        load_case(tmp)
    except CaseError as e:
        msg = str(e)
        assert "02_missing" in msg and "## Draft" in msg and "## Sent" in msg and "replaced_by" in msg, msg
    else:
        raise AssertionError("broken case was accepted")


def _free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def _http(port, path, data=None):
    req = urllib.request.Request(f"http://127.0.0.1:{port}{path}", method="POST" if data is not None else "GET",
                                 data=json.dumps(data).encode() if data is not None else None,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            return json.loads(r.read() or b"null") if path != "/" else r.read().decode()
    except urllib.error.HTTPError as e:
        return json.loads(e.read())


def test_human_mode():
    """A scripted 'participant' clicks through the local web page, as a person would."""
    config.RUNS_DIR = Path(tempfile.mkdtemp())
    port = _free_port()
    committee = str(ROOT / "cases" / "disclosure_committee")
    client = NS(responses=FakeResponses())
    result = {}
    t = threading.Thread(target=lambda: result.update(code=run.main(
        [committee, "--mode", "human", "--participant", "P99", "--port", str(port), "--budget", "5"],
        client=client)), daemon=True)
    t.start()
    seen, deadline = [], time.time() + 60
    saved_when_done = None  # is the run already on disk when the page first shows the end screen?
    while t.is_alive() and time.time() < deadline:
        try:
            st = _http(port, "/state")
        except OSError:
            time.sleep(0.05)
            continue
        if not st.get("needs_answer"):
            if st["step"] == "done" and saved_when_done is None:
                saved_when_done = (config.RUNS_DIR / "disclosure_committee" / "human" / "run-01"
                                   / "reward.json").exists()
            time.sleep(0.02)
            continue
        seen.append(st["step"])
        if st["step"] == "revise":
            answer = {"sent": st["draft"] + "\n(edited by P99)",
                      "comment": "only for this one" if st["number"] == 2 else ""}
        elif st["step"] == "survey":
            answer = {"answers": {q["name"]: 5 for q in st["questions"]}}
        else:
            answer = {}
        assert "<h2>" in st["card_html"] and "Elena" in st["card_html"], st["step"]  # on every page
        if st["step"] == "intro":
            assert "Elena" in _http(port, "/") or "Email assistant study" in _http(port, "/")
            assert _http(port, "/submit", {"seq": st["seq"] - 1})["ok"] is False  # stale answers are refused
        assert _http(port, "/submit", {"seq": st["seq"], **answer})["ok"], st["step"]
    t.join(10)
    assert result.get("code") == 0, (result, seen)
    assert saved_when_done is True, saved_when_done  # "Thank you" appears only after the run is saved
    assert seen == ["intro"] + ["revise", "reply"] * 8 + ["final", "survey", "reveal", "survey"], seen

    run_dir = config.RUNS_DIR / "disclosure_committee" / "human" / "run-01"
    for name in ("trajectory.json", "reward.json", "config.json", "survey.json", "interview.md"):
        assert (run_dir / name).exists(), name
    cfg = json.loads((run_dir / "config.json").read_text())
    assert cfg["mode"] == "human_user" and cfg["participant"] == "P99"
    answers = json.loads((run_dir / "survey.json").read_text())["answers"]
    assert answers == {"perceived_understanding": 5, "perceived_control": 5, "cognitive_load": 5,
                       "memory_agreement": 5}, answers
    steps = json.loads((run_dir / "trajectory.json").read_text())["steps"]
    revisions = [st["text"] for st in steps if st["type"] == "message" and st["role"] == "user"
                 and st["text"].startswith("I edited it")]
    assert len(revisions) == 8 and all("(edited by P99)" in r for r in revisions)
    assert revisions[1].endswith("only for this one") and not revisions[0].endswith("only for this one")
    assert "## 1. Before you saw the memory" in (run_dir / "interview.md").read_text()
    assert "human mode" in (config.RUNS_DIR / "disclosure_committee" / "summary.md").read_text()


if __name__ == "__main__":
    test_case_errors()
    test_memory_store()
    test_cases()
    test_human_mode()
    print("\nall offline tests passed")
