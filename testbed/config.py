"""Model, pricing, and budget settings. Change these here, not in the code."""

from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]  # the folder that holds run.py
# OPENAI_API_KEY comes from the environment (Docker passes it from .env) or from .env next to run.py.
# .env is git-ignored: never commit it.
load_dotenv(ROOT / ".env")

AGENT_NAME = "email-assistant-baseline"  # recorded in config.json
MODEL = "gpt-6.1-sol"          # the agent
JUDGE_MODEL = "gpt-6.1-sol"    # scores memory and the final draft (testbed/scorer.py)
REASONING_EFFORT = None        # None = API default; or "low" / "medium" / "high"
MAX_OUTPUT_TOKENS = 16_000
MAX_TURNS = 20                 # tool-loop iterations per user turn

# USD per million tokens (verify on OpenAI's pricing page)
PRICE_IN, PRICE_CACHED_IN, PRICE_OUT = 2.00, 0.10, 10.00

# Rough per-call token guesses for the printed cost estimate. Calibrated on the 2026-10-29 runs
# (about $0.02 per one-session run) with about 2x headroom.
EST_IN_PER_CALL, EST_OUT_PER_CALL, EST_CALLS_PER_TURN = 1_500, 250, 4
EST_JUDGE_CALLS = 2            # memory judge + draft judge, per run

RUNS_DIR = ROOT / "runs"

DEFAULT_BUDGET_USD = 3.00      # per `run.py` invocation; override with --budget
