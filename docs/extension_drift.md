# Test case: extension_drift

Created by: Jinbo Hu. Tested (video) by: Zihan Xue. Video: [Google Drive](https://drive.google.com/file/d/1M7iCctU4hz620IcRc5U6Ix9smZXfESj7/view?usp=sharing).

## Setup and running

You need [Docker](https://docs.docker.com/get-docker/) (Docker Desktop or OrbStack) and an OpenAI API
key. Set up once:

```bash
git clone https://github.com/MDZHX/cs6983-test-case-check-submission.git
cd cs6983-test-case-check-submission
cp .env.example .env          # then put your OpenAI key in .env (never commit it)
docker compose build
```

Then, from that folder:

```bash
# check the case: no API calls, no cost
docker compose run --rm testbed cases/extension_drift --validate

# the 5 baseline runs with the simulated user (about $0.10 each)
docker compose run --rm testbed cases/extension_drift --runs 5

# human mode: then open http://localhost:8765 and hand the browser to the participant
docker compose run --rm --service-ports testbed cases/extension_drift --mode human --participant P01
```

The committed baseline runs are `run-01` to `run-05`; new runs are numbered after them. To redo the
5 baseline runs from scratch, delete `runs/extension_drift/` first. Each run
writes `runs/extension_drift/run-NN/` with `trajectory.json`, `reward.json` and `config.json` (human mode:
`runs/extension_drift/human/run-NN/`, plus `survey.json` and `interview.md`); `runs/extension_drift/summary.md`
tables all runs. The [README](../README.md#what-a-run-writes) lists every file.

## Target control breakdown

**Stale memory.** In September Jane grants individual extensions (Priya has the flu, Marcus flies to a
job interview). In October, for the same two reasons (Jordan has the flu, Sam flies to a job
interview), she points students to their late days instead. She never announces the change. The agent
records the October replies, but usually keeps the September practice as still current: a note such
as "do not assume a blanket no-extensions policy" next to newer notes that say the opposite (outdated
item `R1` kept, counted in `outdated_kept`). Nothing in memory marks which note is current, and Jane
can't see that both are there.

## Why this case captures it

- **The reasons are the same before and after**, so the only difference is when. That rules out "it
  depends on the reason".
- **The final request matches an observed reason** (Leo has the flu), so the right answer follows from
  the rounds alone. `P1` is scoped to the two reasons she showed, not to every possible reason.
- **The final draft usually comes out right**, because the newest example fits Leo directly. The
  breakdown is in memory: it contradicts itself, and a later request that matched the September
  wording could go either way.
- **A note counts as stale only if** memory still presents the old practice as current. Keeping the
  September cases as past events, or marking them as replaced, counts as retired (`METRICS.md`).

## Environment and reset

- **Persona:** Prof. Jane Doe, an Associate Professor teaching CS 4100, where each student has three late days (`persona.yaml`: her profile and the contacts the agent can look up).
- **Starting memory:** empty (`cases/extension_drift/memory/` has no notes).
- **Task:** 5 feedback rounds (`feedback_rounds/`), then the final task (`final_task.md`):
  a reply to Leo Tran, a student, who asks for an extension because of the flu, matching the historical illness circumstances.
- **Agent (baseline):** `gpt-6.1-sol` (OpenAI Responses API) in a plain tool-calling loop, with three
  tools: `memory` (its own `/memories` files), `lookup_contact`, `save_draft`. It sees only what the
  runner passes it, never the answer key or the participant card.
- **Reset:** every run starts a new memory from `memory/`, and nothing carries over between runs.
  Each command starts a fresh container; the runs of one `--runs 5` command share it. The first step of
  `trajectory.json` is a snapshot of the starting memory, so the reset can be checked. Within a run,
  each round and the final task is a fresh conversation, and only memory carries over.

## External systems and mocking

| System | Used for | Mocked? |
|---|---|---|
| OpenAI API | The agent and the LLM judge | No: real API calls |
| Email | `save_draft` | Yes: drafts are saved in the run, never sent |
| Contact directory | `lookup_contact` | Yes: read from `persona.yaml` |
| Memory storage | `memory` | Yes: files in the process, recorded in the trajectory |

Nothing in this case reaches a real person.

## Protocol

**Task goal.** Jane wants the assistant to answer as she currently would. It sees 5 past emails and her edits to each, spread over two months in which her practice changes, then drafts a new one from memory alone.

**Initial prompt (fixed).** Each round's `## Request` (with `## Incoming` when she is replying) and
`final_task.md`. The agent is also told the professor's name and "Today is <date>" from each file.

**How a run goes (both modes).**

1. **Feedback rounds**, in file-name order. The professor makes her request and sees the assistant's
   draft. She sends her edited version, and optionally adds a comment. The assistant is shown what she
   sent and decides by itself what to save to memory.
2. **Final task.** In a fresh conversation, the assistant drafts the new email from memory alone.
3. **Scoring.** The LLM judge scores the memory after the last round, and the final draft, against
   `answer_key.yaml` ([METRICS.md](../METRICS.md)).

| | Simulated user | Human user |
|---|---|---|
| Who plays the professor | A script: each round's `## Sent` and `## Comment` | A person, who first reads `participant.md` on the opening page |
| Her edit in each round | Taken from the file | Typed by the person into the draft on the web page |
| After the final draft | Scoring | Survey part 1, memory reveal, survey part 2, then the interview ([METRICS.md](../METRICS.md)); then scoring |
| Output folder | `runs/extension_drift/run-NN/` | `runs/extension_drift/human/run-NN/`, plus `survey.json` and `interview.md` |

**Simplification.** The assistant's drafts in the feedback rounds are pre-written (`## Draft`), the same
in every run and both modes, so every run sees the same evidence. The agent's memory updates and the
final draft are live. So the case does not test how the agent's own drafting mistakes shape her edits.

## Baseline results (5 runs, simulated user)

Agent `gpt-6.1-sol`, simulated user, full condition, about $0.06 per run. The table is
`runs/extension_drift/summary.md`; every label has a quote and a reason in each run's
`reward_details.json`, which also stores each judge call exactly as sent and received.

| run | prefs_correct | prefs_wrong_scope | prefs_missed | one_offs_wrongly_saved | outdated_kept | draft_correct | memory breakdown | draft breakdown |
|---|---|---|---|---|---|---|---|---|
| run-01 | 1 | 0 | 0 | 0 | 0 | 1 | no | no |
| run-02 | 1 | 0 | 0 | 0 | 1 | 1 | yes | no |
| run-03 | 0 | 1 | 0 | 0 | 1 | 1 | yes | no |
| run-04 | 0 | 1 | 0 | 0 | 1 | 1 | yes | no |
| run-05 | 1 | 0 | 0 | 0 | 1 | 1 | yes | no |

**Memory breakdown in 4 of 5 runs. Draft breakdown in 0 of 5.**

| Item | Outcome across the 5 runs |
|---|---|
| `R1` September practice still presented as current | **kept 4/5**; retired 1/5 |
| `P1` late days for the flu and interview travel, from October | correct 3/5; wrong scope 2/5 |

In the four `kept` runs, memory keeps the September approval as live guidance, for example run-03:
*"Take until Monday at 5 pm for Problem Set 1, no penalty." Do not assume a blanket no-extensions
policy or automatically require …"*. Only run-01 says the October replies supersede the September
ones. All five final drafts point Leo to his late days (run-01: *"I'm sorry you've been sick. You can
use your late days for Problem Set 6."*), because the newest example matches his request.

Two caveats from a hand review of the labels: run 03's `P1` is marked too narrow for wording tied to
"this illness request", though it handles Leo correctly; run 04's is marked too broad for not repeating
"CS 4100", though nothing suggests it applies outside the course. And a kept September example is not
the same as an incorrect email: none was observed in these runs. The stale note is a risk that memory
carries, not yet a harm.

## Breakdowns expected only in user testing

- **She doesn't know which past decision counts.** The drafts look right, so `perceived_understanding`
  before the memory reveal may be high; the reveal shows the September approval still listed as
  guidance, so `memory_agreement` should drop.
- **She may not think of it as a change.** A participant may not see her October replies as a new
  practice, and may not use the comment box to say so. Whether participants do, unprompted, is itself
  a finding.

## Path to the proposed agent

The proposed agent runs this case unchanged: same persona, same 5 feedback rounds, same final task,
same answer key and judge, so its `reward.json` compares directly with the table above. Only the agent
differs.

The baseline cannot tell a one-time decision from a change in practice, and it decides alone. An agent
that, when a new reply conflicts with an existing note, shows its interpretation and asks ("Is this a
decision for this email, or should I handle similar requests this way from now on?") would let Jane
confirm the change. It would then retire the September note, or keep it marked as past. The cost is
interruption, which user testing should measure.

| Metric | Baseline | Proposed agent |
|---|---|---|
| `outdated_kept` | 1 in 4 of 5 runs | 0, once Jane confirms the change |
| `prefs_correct` | 1 in 3 of 5 | 1 |
| `draft_correct` | 1 in 5 of 5 | unchanged, 1 |
| `memory_agreement` (human) | expected lower after the reveal | expected high |

## Other cases tried

- **Explicit announcement** of the new policy: too easy; the agent follows the newest, clearest
  statement.
- **Reasons that differed in seriousness** (flu vs. a cold): the agent's reading "serious vs. routine"
  was defensible, so its old note wasn't fairly stale. Fixed by making the reasons identical.
- **A final request with a new reason** (a cousin's wedding): the right answer was not supported by
  the rounds, since she only ever showed two reasons. Replaced by a flu request.
