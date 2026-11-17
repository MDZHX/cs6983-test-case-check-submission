# Email memory testbed

CS 6983, milestone: test case check. **Graders: start at [SUBMISSION.md](SUBMISSION.md)**, which links every document, run and video. This README is the guide to the testbed itself.

A professor uses an AI assistant to draft her emails. She edits each draft before sending, and the
assistant decides by itself what to remember from her edits. The professor can't see what it saved.
These test cases ask: **does the assistant learn what she wants, at the right scope, and keep its
memory true over time?**

## The three test cases

Each shows a different way the assistant's memory goes wrong. Each has a write-up in [`docs/`](docs/).

| Case | Angle | What goes wrong |
|---|---|---|
| [`disclosure_committee`](cases/disclosure_committee) | Piecing together | The pieces of her rule, some only facts mentioned in passing, are never joined, so it learns too little |
| [`context_one_offs`](cases/context_one_offs) | Unwanted learning | It turns her reactions to a moment into rules she never wanted learned |
| [`extension_drift`](cases/extension_drift) | Stale memory | Her practice changes, but the old notes are never retired, so memory still says what she no longer does |

## How a test case works

1. **Feedback rounds.** For each past email, the professor asks for it, sees a draft, and sends her
   edited version. The assistant then decides what to write to its memory. This part is live.
2. **Final task.** A new request in a fresh conversation. The assistant drafts it from memory alone.
3. **Scoring.** An LLM judge compares the memory after the last round, and the final draft, against
   the case's answer key. The metrics are defined in [METRICS.md](METRICS.md).

Every case runs in two modes, with the same case, agent and scoring:

- **Simulated:** a script plays the professor (her edits come from the case files). Produces the
  objective metrics. This is how the 5 baseline runs are made.
- **Human:** a person plays the professor on a local web page, editing each draft, then sees the
  assistant's memory and answers a short survey.

## Setup (once)

Everything runs through Docker, so every run uses the same environment; `run.py` refuses to start
outside the container. You need [Docker](https://docs.docker.com/get-docker/) (Docker Desktop or
OrbStack) and an OpenAI API key.

```bash
git clone https://github.com/MDZHX/cs6983-test-case-check-submission.git
cd cs6983-test-case-check-submission
cp .env.example .env          # then put your key in .env (never commit it)
docker compose build          # again after any change to testbed/; case edits need no rebuild
```

## Run a test case

From this folder. Each command starts a fresh container, and every run starts from the case's starting
memory, so runs don't affect each other.

```bash
# check a case: no API calls, no cost
docker compose run --rm testbed cases/disclosure_committee --validate

# the baseline runs: 5 runs with the simulated user (about $0.10 each)
docker compose run --rm testbed cases/disclosure_committee --runs 5

# human mode: then open http://localhost:8765 and hand the browser to the participant
docker compose run --rm --service-ports testbed cases/disclosure_committee --mode human --participant P01

# check the setup and the code, with a fake model and judge (no cost); says nothing
# about how the real agent or judge behave. Run it once after setup.
docker compose run --rm --entrypoint python testbed tests/test_offline.py
```

The committed baseline runs are `run-01` to `run-05`; new runs are numbered after them (`run-06`, ...).
To redo the 5 baseline runs from scratch, delete `runs/<case>/` first.

## What a run writes

Each run writes one folder, `runs/<case>/run-NN/` (human mode: `runs/<case>/human/run-NN/`):

| File | What it is |
|---|---|
| `trajectory.json` | Every message, tool call, and tool result, in order, with UTC timestamps |
| `reward.json` | The objective metrics, with the same names in every case |
| `config.json` | Mode, agent, model, settings, and a hash of the case folder |
| `reward_details.json` | The judge's label, quote, and reason for each item, and every judge call exactly as sent and received |
| `report.md` | The whole run as a readable trace, with the scoring at the end |
| `survey.json`, `interview.md` | Human mode only: survey answers, and interview notes for the facilitator |

`runs/<case>/summary.md` puts every run's metrics in one table and counts the breakdowns.

## The environment

- **Agent (baseline):** `gpt-6.1-sol` (OpenAI Responses API) in a plain tool-calling loop. Its tools:
  `memory` (its own `/memories` files), `lookup_contact`, `save_draft`. It has no file access: it sees
  only what the runner passes it, never the answer key or the participant card.
- **Reset:** memory starts from the case's `memory/` folder on every run; nothing carries over.
- **External systems:** only the OpenAI API (agent and judge). Everything else is mocked: drafts are
  saved, never sent; contacts come from the case's `persona.yaml`; memory lives in the process.

## Where things are

| Path | What it is |
|---|---|
| [`cases/`](cases/) | One folder per test case. To write or change one, start from [`cases/_template/`](cases/_template/README.md). |
| [`docs/`](docs/) | One write-up per case |
| [`METRICS.md`](METRICS.md) | The team's metrics, survey, interview, and who made and tested each case |
| `runs/` | Each case's 5 baseline runs and `summary.md`; `no_memory/` holds the control runs the documents cite |
| `run.py` | The only entry point |
| `testbed/` | The engine: agent, memory, tools, case loader, runner, scorer, outputs, web page, survey. Shared by every case. |
| `tests/test_offline.py` | End-to-end test of the code with a fake model and judge (no cost) |
| `Dockerfile`, `compose.yaml` | The environment, and how it connects to this folder |
| `pyproject.toml`, `uv.lock`, `.python-version` | Python 3.12 and the exact packages, installed by [uv](https://docs.astral.sh/uv/) in the image |
| `testbed/config.py` | Model, prices, and the per-command budget (default $3) |
