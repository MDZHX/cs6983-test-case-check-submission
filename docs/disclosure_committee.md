# Test case: disclosure_committee

Created by: Zihan Xue. Tested (video) by: Sanjana Nilesh Brahmbhatt. Video: [Google Drive](https://drive.google.com/file/d/1oQQeCpbtT-Rfdvsu7CAHQgF3uUsU1vmy/view?usp=sharing).

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
docker compose run --rm testbed cases/disclosure_committee --validate

# the 5 baseline runs with the simulated user (about $0.10 each)
docker compose run --rm testbed cases/disclosure_committee --runs 5

# human mode: then open http://localhost:8765 and hand the browser to the participant
docker compose run --rm --service-ports testbed cases/disclosure_committee --mode human --participant P01
```

The committed baseline runs are `run-01` to `run-05`; new runs are numbered after them. To redo the
5 baseline runs from scratch, delete `runs/disclosure_committee/` first. Each run
writes `runs/disclosure_committee/run-NN/` with `trajectory.json`, `reward.json` and `config.json` (human mode:
`runs/disclosure_committee/human/run-NN/`, plus `survey.json` and `interview.md`); `runs/disclosure_committee/summary.md`
tables all runs. The [README](../README.md#what-a-run-writes) lists every file.

## Target control breakdown

**Piecing together.** Elena's rule is about a group: no personal reasons to anyone who evaluates her
for promotion. No single email states it. It has to be pieced together from her edits to the chair,
Margaret and Ken, from facts mentioned only in passing (who is on her promotion committee appears only
in Margaret's email and signature and in Ken's email), and from the contrast with people she does tell,
like Sam. The agent never joins the pieces: it saves notes about the specific people it saw (the chair,
Margaret, Ken) and ties its general rule to the topic ("promotion-review correspondence"), which the
scorer records as `P1` `wrong_scope` (too narrow or wrong cue). So when Priya, a committee member it has
never written to, invites her to dinner, it gives the personal reason. Elena can't see the narrow notes
until the wrong draft appears.

## Why this case captures it

- **The rule goes against the model's default.** By default the model explains itself to the chair and
  keeps students out of personal matters. Elena does the opposite, so the right behavior has to come
  from what it learned, not from its prior.
- **The simpler readings are ruled out.**
  - Sam is senior faculty, yet she gives him the real reason (round 3), so the split isn't "students vs.
    faculty".
  - Ken's email is friendly and not about her promotion, yet she cuts the reason (round 7), so the rule
    is about who the person is, not the topic.
- **Committee membership isn't on the contact cards.** It appears only in Margaret's email and
  signature (round 5: "the committee (Ken Ito, Priya Shah and I)") and Ken's email (round 7), so the
  agent has to infer the group from the emails.
- **The final email falls outside both easy readings.** Priya has no note of her own, and a dinner
  invitation is not promotion review, so neither a note about one person nor a rule about the topic
  covers her; only the rule about the group does.
- **Fairness.** Priya's committee role is stated in round 5, and round 7 shows the rule holds off-topic
  (Ken's seminar invitation), after the agent has formed its topic-based note. Her persona also states
  the review chain (committee, then the dean, then the provost). Every revision also
  changes other things (greetings, sign-offs, wording), as real edits do.

## Environment and reset

- **Persona:** Prof. Elena Park, an Associate Professor going up for promotion to full professor, who is caring for her father (`persona.yaml`: her profile and the contacts the agent can look up).
- **Starting memory:** empty (`cases/disclosure_committee/memory/` has no notes).
- **Task:** 8 feedback rounds (`feedback_rounds/`), then the final task (`final_task.md`):
  a reply to Prof. Priya Shah, a member of her promotion committee, declining a dinner invitation.
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

**Task goal.** Elena wants the assistant to draft her emails the way she would send them, including whom she tells about her father's care. It sees 8 past emails and her edits to each, then drafts a new one from memory alone.

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
| Output folder | `runs/disclosure_committee/run-NN/` | `runs/disclosure_committee/human/run-NN/`, plus `survey.json` and `interview.md` |

**Simplification.** The assistant's drafts in the feedback rounds are pre-written (`## Draft`), the same
in every run and both modes, so every run sees the same evidence. The agent's memory updates and the
final draft are live. So the case does not test how the agent's own drafting mistakes shape her edits.

## Baseline results (5 runs, simulated user)

Agent `gpt-6.1-sol`, simulated user, full condition, about $0.09 per run. The table is
`runs/disclosure_committee/summary.md`; every label has a quote and a reason in each run's
`reward_details.json`, which also stores each judge call exactly as sent and received. The runs were
scored with the final answer key: `P1`'s scope was tightened after the runs to say that a rule tied to
promotion topics counts as `wrong_cue`. The agent never sees the key, so the runs themselves are
unaffected.

| run | prefs_correct | prefs_wrong_scope | prefs_missed | one_offs_wrongly_saved | outdated_kept | draft_correct | memory breakdown | draft breakdown |
|---|---|---|---|---|---|---|---|---|
| run-01 | 0 | 2 | 0 | 1 | 0 | 0 | yes | yes |
| run-02 | 0 | 2 | 0 | 1 | 0 | 0 | yes | yes |
| run-03 | 0 | 2 | 0 | 1 | 0 | 0 | yes | yes |
| run-04 | 0 | 2 | 0 | 1 | 0 | 0 | yes | yes |
| run-05 | 0 | 2 | 0 | 1 | 0 | 0 | yes | yes |

**Memory breakdown in 5 of 5 runs. Draft breakdown in 5 of 5.**

| Item | Outcome across the 5 runs |
|---|---|
| `P1` no personal reasons to evaluators | **wrong scope 5/5** (wrong cue: tied to the topic; or too narrow: the chair and named members only) |
| `P2` the real reason to everyone else | wrong scope 5/5 (separate notes per person or group) |
| `O3` the thank-you she asked for, saved as a habit | wrongly saved 5/5 |
| `O1`, `O2` the date fix, the room | not saved 5/5 (correct) |

Every run writes the same sentence to Priya: *"I can't make dinner on Friday—I'll be in Chicago with my
dad."* The agent reads its memory before drafting in every run (and looks up Priya in 4 of 5), but
nothing it saved reaches her:

- Its general rule is tied to the topic, for example run-01: *"For evaluative/promotion correspondence,
  favor concise, work-focused explanations … rather than … elaborate personal disclosure."* A dinner
  invitation is not promotion correspondence.
- Even the run closest to the right rule (run-03: *"Even in a friendly seminar exchange, account for
  the recipient's promotion-review role"*) fails, because **no run's memory records that Priya is on
  the committee.** The only evidence is one line in Margaret's email (round 5), and the agent never
  saves it. Her contact card says only "Professor".

**The control shows the failure is the model's default, which learning should have overridden.**
With empty memory and only the final task (`--condition none`, 3 runs), the draft is the same sentence
in 3 of 3. So memory had no effect on this email. On an evaluator its rule does reach, it works: with
the dean as the final recipient (see Other cases tried), the trained agent kept her dad out in 5 of 5
runs while the control leaked it in 3 of 3. The same memory works where its wording reaches and fails
where it does not, because it never learned "the people who evaluate her" as a group.

## Breakdowns expected only in user testing

- **She sees the failure before she sees why.** The final draft to Priya comes before the survey, so
  a participant playing Elena should notice the leak. `perceived_understanding` and
  `perceived_control` should be low, and the memory reveal should explain it: careful notes about the
  chair, Margaret and Ken, and a rule about "promotion correspondence", but nothing about Priya.
  `memory_agreement` should be mixed: the notes are accurate, just too specific.
- **A comment may fix it, which is itself a finding.** A participant can tell the assistant "never
  give family reasons to anyone on my committee". If the agent saves that, the final draft may come out
  right. How many participants think to state the rule, and in which round, shows whether the comment
  box is enough control. Interview question 4 probes this.
- **Her own edits will vary.** A person may not strip the reason as consistently as the script, or
  may strip more. Runs where she is consistent and the draft still leaks are the strongest evidence.
- **Effort.** `cognitive_load` should be moderate to high: she has to keep track of who is on her
  committee across eight emails, which is exactly what the agent fails to do.

## Path to the proposed agent

The proposed agent runs this case unchanged: same persona, same 8 feedback rounds, same final task,
same answer key and judge, so its `reward.json` compares directly with the table above. Only the agent
differs.

The baseline's failure has two parts, and the proposed agent has to address both:

1. **It never forms the group.** It writes one note per email and ties the general rule to a topic.
   An agent that keeps learned rules with an explicit scope ("applies to: the chair, her promotion
   committee, the dean"), and consolidates notes across rounds, would have one rule to apply to Priya.
2. **It drops the fact that defines the group.** Priya's committee role appears once, in passing. An
   agent that records who belongs to a scope when it sees it would know Priya is covered.

Showing Elena what it learned would catch both: she could see "promotion correspondence" and correct
it to "anyone on my committee". Expected changes:

| Metric | Baseline | Proposed agent |
|---|---|---|
| `prefs_wrong_scope` | 2 in 5 of 5 runs | 0: `P1` and `P2` stored with their group scope |
| `draft_correct` | 0 in 5 of 5 | 1: no mention of her dad to Priya |
| `one_offs_wrongly_saved` | 1 (`O3`) | unchanged unless the agent also asks about one-time edits |
| `memory_agreement` (human) | expected mixed | expected high |
| `perceived_control` (human) | expected low | expected high |

## Other cases tried

- **The dean as the final recipient** (same rounds; the dean invites her to a task force). In an earlier
  version, without the review chain in her persona, the agent leaked her dad's care in 4 of 4 runs, but so did the no-memory control,
  and nothing in the case said the dean judges her promotion, so the link was unsupported. With the
  review chain added to her persona, the drafts were correct in 5 of 5 (control: 0 of 3): the topic
  rule stretched to the dean. Memory still broke in 5 of 5. Replaced by Priya, whom neither a person
  note nor the topic rule covers.
- **Final recipients who do not evaluate her** (Leo, a PhD student; Raj, another department; Mei, a
  co-PI). The right answer there is to give the reason, which is also the model's default, so a
  learning failure cannot show in the draft.
- **Sam joining her committee** (Sam, whom she told about her dad in round 3, becomes an evaluator;
  stated in his own email, or only in Margaret's). The quiet version failed in 3 of 3 runs because the
  agent never saved the fact from Margaret's email, which is the failure this case keeps. Rejected
  because it also tests a change in Sam's role, mixing in the stale-memory angle; Priya, new to the
  agent, isolates piecing together.
- **After her promotion** (she starts giving evaluators real reasons again). A stale-memory case,
  which the team covers with `extension_drift`.
- **Diagnostic variants** (the rule stated outright in Margaret's email; seeded starting memory;
  the agent prompt without its line limiting memory to email preferences). Used to locate the cause, not as test cases.
- **Other failure types on the same persona** (one-off edits saved as habits, a phrase reused word
  for word). Most produced correct drafts, because the model is cautious when it applies memory; the
  one-off angle became the team's `context_one_offs` case.
