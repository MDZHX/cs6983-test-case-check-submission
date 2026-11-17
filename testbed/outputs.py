"""The run folder: trajectory.json, reward.json, config.json (the milestone's three files),
plus reward_details.json and report.md for checking a run by hand.

Layout:
  runs/<case id>/run-01/ ...           the full case, simulated user (the baseline runs)
  runs/<case id>/human/run-01/         the full case, a person plays the professor (+ survey.json, interview.md)
  runs/<case id>/no_memory/run-01/     control: final task only, empty memory
  runs/<case id>/seed_only/run-01/     control: final task only, starting memory
  runs/<case id>/summary.md            every run's reward.json in one table, with breakdown counts
"""

import json
from pathlib import Path

from . import config
from .case import case_hash
from .report import run_report

CONDITION_DIR = {"full": "", "human": "human", "none": "no_memory", "seed": "seed_only"}
CONDITION_DESC = {
    "human": "full case, human mode: a person plays the professor",
    "full": "full case: starting memory, feedback rounds, final task",
    "none": "control: final task only, empty memory (the model's default)",
    "seed": "control: final task only, starting memory (skips the feedback rounds)",
}
MEMORY_ERRORS = ("prefs_wrong_scope", "prefs_missed", "one_offs_wrongly_saved", "outdated_kept")
CORE = ("prefs_correct", "prefs_wrong_scope", "prefs_missed", "one_offs_wrongly_saved", "outdated_kept",
        "draft_correct", "draft_asked_clarification")


def condition_dir(case_id: str, group: str) -> Path:
    """group: a condition (full | none | seed), or "human" for human-mode runs of the full case."""
    return config.RUNS_DIR / case_id / CONDITION_DIR[group]


def next_run_dir(case_id: str, group: str) -> Path:
    base = condition_dir(case_id, group)
    taken = [int(p.name[4:]) for p in base.glob("run-[0-9]*") if p.name[4:].isdigit()]
    d = base / f"run-{max(taken, default=0) + 1:02d}"
    d.mkdir(parents=True)
    return d


def _dump(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False, default=str) + "\n")


def build_config(case: dict, condition: str, mode: str, user: str,
                 started: str, finished: str, cost: float, participant: str | None = None) -> dict:
    return {
        "mode": mode,
        "user": user,
        **({"participant": participant} if participant else {}),
        "condition": condition,
        "condition_description": CONDITION_DESC[condition],
        "case": {"id": case["id"], "folder": _rel(case["folder"]),
                 "sha256_of_folder": case_hash(case["folder"])},
        "agent": {"name": config.AGENT_NAME, "loop": "testbed/agent.py run_turn",
                  "tools": ["memory", "lookup_contact", "save_draft"], "memory": "agent-managed /memories files"},
        "model": {"id": config.MODEL, "reasoning_effort": config.REASONING_EFFORT,
                  "max_output_tokens": config.MAX_OUTPUT_TOKENS, "api": "OpenAI Responses API, store=False"},
        "judge": {"model": config.JUDGE_MODEL, "code": "testbed/scorer.py"},
        "settings": {"max_tool_loop_iterations": config.MAX_TURNS,
                     "feedback_sessions": len(case["feedback_sessions"]) if condition == "full" else 0},
        "started_at": started,
        "finished_at": finished,
        "cost_usd": round(cost, 4),
    }


def _rel(path: Path) -> str:
    try:
        return Path(path).resolve().relative_to(config.ROOT).as_posix()
    except ValueError:
        return str(path)


def write_run(run_dir: Path, case: dict, res: dict, condition: str, reward: dict, details: dict,
              cfg: dict, survey_answers: dict | None = None, interview: str | None = None) -> None:
    _dump(run_dir / "trajectory.json", {"case": case["id"], "condition": condition, "mode": cfg["mode"],
                                        "steps": res["trace"]})
    _dump(run_dir / "reward.json", reward)
    _dump(run_dir / "reward_details.json", details)
    _dump(run_dir / "config.json", cfg)
    (run_dir / "report.md").write_text(run_report(case, res, condition, run_dir.name, reward, details))
    if survey_answers is not None:
        _dump(run_dir / "survey.json", survey_answers)
    if interview is not None:
        (run_dir / "interview.md").write_text(interview)


def breakdowns(reward: dict) -> tuple[str, str]:
    """('yes' | 'no' | '-') for the memory breakdown and the draft breakdown."""
    mem = "-" if "prefs_missed" not in reward else "yes" if any(reward.get(k, 0) > 0 for k in MEMORY_ERRORS) else "no"
    draft = "-" if "draft_correct" not in reward else "yes" if reward["draft_correct"] == 0 else "no"
    return mem, draft


def write_summary(case: dict) -> Path:
    """Rebuild runs/<case id>/summary.md from every run folder on disk."""
    out = [f"# {case['id']}: run summary", "",
           "One row per run, read from its reward.json. Memory breakdown: any of "
           "prefs_wrong_scope, prefs_missed, one_offs_wrongly_saved, outdated_kept above 0. Draft breakdown: draft_correct = 0.",
           ""]
    for condition in ("full", "human", "none", "seed"):
        runs = sorted(p for p in condition_dir(case["id"], condition).glob("run-[0-9]*") if p.is_dir())
        rows = []
        for r in runs:
            try:
                reward = json.loads((r / "reward.json").read_text())
                mode = json.loads((r / "config.json").read_text())["mode"]
            except (OSError, ValueError, KeyError):
                continue
            rows.append((r.name, mode, reward, *breakdowns(reward)))
        if not rows:
            continue
        out += [f"## {CONDITION_DESC[condition]}", "",
                "| run | mode | " + " | ".join(CORE) + " | memory breakdown | draft breakdown |",
                "|---" * (len(CORE) + 4) + "|"]
        for name, mode, reward, mem, draft in rows:
            out.append(f"| {name} | {mode} | " + " | ".join(str(reward.get(k, "-")) for k in CORE)
                       + f" | {mem} | {draft} |")
        n = len(rows)
        out += ["", f"Memory breakdown in {sum(r[3] == 'yes' for r in rows)} of {n} runs; "
                    f"draft breakdown in {sum(r[4] == 'yes' for r in rows)} of {n} runs.", ""]
    path = config.RUNS_DIR / case["id"] / "summary.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(out) + "\n")
    return path
