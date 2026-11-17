"""Run a test case against the baseline email agent, score it, and write one folder per run.

Runs inside Docker only; from the repository folder:

  docker compose run --rm testbed cases/disclosure_committee --validate
  docker compose run --rm testbed cases/disclosure_committee --runs 5
  docker compose run --rm testbed cases/disclosure_committee --runs 2 --condition none
  docker compose run --rm --service-ports testbed cases/disclosure_committee --mode human --participant P01

--validate      check the case folder and print a cost estimate; makes no API calls
--runs N        repeat N times (default 1); each run gets the next free folder run-01, run-02, ...
--condition     full (default): the whole case, the baseline runs for the milestone
                none: control, final task only with empty memory (the model's default behavior)
                seed: control, final task only from the starting memory (what the sessions changed)
--mode          simulated (default): a script plays the professor, from the case files
                human: a person plays the professor on a web page at http://localhost:8765 (one run,
                       full case); the run folder also gets survey.json and interview.md (for the facilitator)
--participant   human mode: the participant's id, e.g. P01 (no names)
--budget X      stop once this invocation has spent $X (default in testbed/config.py)

Each run writes runs/<case id>/[<control>/]run-NN/ with trajectory.json, reward.json, config.json,
reward_details.json (the judge's label and quote for every metric) and report.md (the readable trace).
runs/<case id>/summary.md is rebuilt after every invocation: all runs' metrics and breakdown counts.
"""

import os
import sys

if __name__ == "__main__" and os.environ.get("TESTBED_IN_DOCKER") != "1":  # set by the Dockerfile
    sys.exit("Run this through Docker, from the repository folder (see README.md), e.g.\n"
             "  docker compose run --rm testbed cases/<case> --validate")

import argparse

from testbed import config
from testbed.agent import LLM, BudgetExceeded
from testbed.case import CaseError, load_case
from testbed.outputs import breakdowns, build_config, next_run_dir, write_run, write_summary
from testbed.runner import run_case
from testbed.scorer import score
from testbed.survey import interview_template
from testbed.trace import now
from testbed.users import ScriptedUser


def _rel(path) -> str:
    try:
        return str(path.relative_to(config.ROOT))
    except ValueError:
        return str(path)


def estimate(case: dict, condition: str) -> float:
    sessions = len(case["feedback_sessions"]) if condition == "full" else 0
    calls = (sessions + 1) * config.EST_CALLS_PER_TURN + config.EST_JUDGE_CALLS
    return calls * (config.EST_IN_PER_CALL * config.PRICE_IN + config.EST_OUT_PER_CALL * config.PRICE_OUT) / 1e6


def main(argv=None, client=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("case", help="a case folder, e.g. cases/disclosure_committee")
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--condition", choices=["full", "none", "seed"], default="full")
    ap.add_argument("--mode", choices=["simulated", "human"], default="simulated")
    ap.add_argument("--participant")
    ap.add_argument("--port", type=int, default=8765, help=argparse.SUPPRESS)  # must match compose.yaml
    ap.add_argument("--validate", action="store_true")
    ap.add_argument("--budget", type=float, default=config.DEFAULT_BUDGET_USD)
    a = ap.parse_args(argv)
    if a.mode == "human":
        if not a.participant:
            ap.error("human mode needs --participant, e.g. --participant P01")
        if a.runs != 1 or a.condition != "full":
            ap.error("human mode runs the full case once (no --runs or --condition)")

    try:
        case, warnings = load_case(a.case)
    except (CaseError, OSError) as e:
        print(f"ERROR: {e}")
        return 1
    for w in warnings:
        print(f"warning: {w}")
    key = case["answer_key"]
    print(f"{case['id']}: {len(case['feedback_sessions'])} feedback round(s) + final task; answer key: "
          f"{len(key['preferences'])} preference(s), {len(key['one_offs'])} one-off(s), "
          f"{len(key['outdated'])} outdated; "
          f"{len(case['final_task']['must'])} must, {len(case['final_task']['must_not'])} must_not")
    print(f"agent {config.MODEL}, judge {config.JUDGE_MODEL}, mode {a.mode}, condition {a.condition}")
    print(f"rough estimate: ${estimate(case, a.condition) * a.runs:.2f} for {a.runs} run(s) (budget ${a.budget:.2f})")
    if a.validate:
        print("OK" if not warnings else "OK with warnings")
        return 0

    llm = LLM(budget_usd=a.budget, client=client)
    if a.mode == "human":
        return human_run(a, case, llm)
    try:
        for _ in range(a.runs):
            spent_before, started = llm.usage.cost, now()
            res = run_case(llm, case, baseline=None if a.condition == "full" else a.condition)
            reward, details = score(llm, case, res)
            cfg = build_config(case, a.condition, "simulated_user", ScriptedUser.description, started, now(),
                               llm.usage.cost - spent_before)
            run_dir = next_run_dir(case["id"], a.condition)
            write_run(run_dir, case, res, a.condition, reward, details, cfg)
            mem, draft = breakdowns(reward)
            print(f"{_rel(run_dir)}: {reward}  memory breakdown: {mem}, draft breakdown: {draft}"
                  f"  (total so far ${llm.usage.cost:.3f})")
    except BudgetExceeded as e:
        print(f"stopped: {e}")
    print(f"\n-> {_rel(write_summary(case))}")
    print(f"spent ${llm.usage.cost:.3f} ({llm.usage.calls} API calls)")
    return 0


def human_run(a, case: dict, llm) -> int:
    from testbed.webui import run_human
    if not (case["folder"] / "participant.md").is_file():
        print("ERROR: human mode needs the case's participant.md")
        return 1
    started = now()

    def save(res: dict, answers: dict):
        """Runs while the page says "Saving..."; the end screen appears only after this returns."""
        finished = now()
        print("participant finished; scoring and saving (don't stop the program yet)...")
        reward, details = score(llm, case, res)
        cfg = build_config(case, "full", "human_user",
                           f"person: participant {a.participant}, on the local web page (testbed/webui.py)",
                           started, finished, llm.usage.cost, participant=a.participant)
        run_dir = next_run_dir(case["id"], "human")
        write_run(run_dir, case, res, "full", reward, details, cfg, answers,
                  interview_template(case["id"], a.participant))
        print(f"{_rel(run_dir)}: {reward}")
        print(f"survey: {answers['answers']}")
        print(f"-> {_rel(write_summary(case))}")
        return run_dir

    try:
        run_dir = run_human(llm, case, a.participant, a.port, run_case, save)
    except (BudgetExceeded, KeyboardInterrupt) as e:
        print(f"stopped: {e or 'interrupted'}; nothing was written")
        return 1
    print(f"saved. -> fill in {_rel(run_dir / 'interview.md')} during the interview")
    print(f"spent ${llm.usage.cost:.3f} ({llm.usage.calls} API calls)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
