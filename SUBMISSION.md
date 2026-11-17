# Submission: Curate your test cases

CS 6983. This page is the team's single submission link. It points to everything submitted: one
repository (this one) for all three test cases, one document per case, one video per case, and the
team's shared metrics. How to install and run the testbed is in the [README](README.md).

## The three test cases

| Case | Control breakdown | Document | Baseline runs (5, simulated user) | Video | Created by | Tested (video) by |
|---|---|---|---|---|---|---|
| `disclosure_committee` | Piecing together: it learns too little | [docs/disclosure_committee.md](docs/disclosure_committee.md) | [runs/disclosure_committee/](runs/disclosure_committee/summary.md): memory 5/5, draft 5/5 | [Video](https://drive.google.com/file/d/1oQQeCpbtT-Rfdvsu7CAHQgF3uUsU1vmy/view?usp=sharing) | Zihan Xue | Sanjana Nilesh Brahmbhatt |
| `context_one_offs` | Unwanted learning: it learns what she never wanted learned | [docs/context_one_offs.md](docs/context_one_offs.md) | [runs/context_one_offs/](runs/context_one_offs/summary.md): memory 5/5, draft 1/5 | [Video](https://drive.google.com/file/d/1ohcoBMQdTVOzd3MEi9adv8moOESP7sqN/view?usp=sharing) | Sanjana Nilesh Brahmbhatt | Jinbo Hu |
| `extension_drift` | Stale memory: old notes are never retired | [docs/extension_drift.md](docs/extension_drift.md) | [runs/extension_drift/](runs/extension_drift/summary.md): memory 4/5, draft 0/5 | [Video](https://drive.google.com/file/d/1M7iCctU4hz620IcRc5U6Ix9smZXfESj7/view?usp=sharing) | Jinbo Hu | Zihan Xue |

"Memory" and "draft" count the runs that showed each breakdown; each document explains them and
describes the breakdowns expected only in user testing. The videos are on Google Drive and are not
in the repository.

## Shared by the team

[METRICS.md](METRICS.md) is the team's shared list: the answer key format, the core objective metrics
(`reward.json`, the same names in every case), the subjective metrics (the survey), the interview
questions, and who created and tested each case.

## Where each required part is

| Required | Where |
|---|---|
| Environment, task, simulated-user script | `cases/<case>/`: `persona.yaml`, `memory/`, `feedback_rounds/` (the script the simulated user follows), `final_task.md`, `answer_key.yaml`, `participant.md` (the human participant's card) |
| Everything needed to build it | `Dockerfile`, `compose.yaml`, `pyproject.toml`, `uv.lock`, `run.py`, `testbed/`. No Docker image and no API keys are committed; `.env.example` shows where the key goes. |
| Run outputs | `runs/<case>/run-01` … `run-05`, each with `trajectory.json`, `reward.json`, `config.json`, plus `reward_details.json` (judge labels) and `report.md` (readable trace). `runs/<case>/summary.md` tables all runs. `no_memory/` holds the control runs that two documents cite. |
| Document | `docs/<case>.md`: setup and running, the target breakdown and why the case captures it, environment and reset, external systems and mocking, protocol for both modes, baseline results, breakdowns expected in user testing, path to the proposed agent, and other cases tried |
| Readiness for user testing | Human mode (`--mode human`, a local web page) with the survey and interview in place; see each document's Protocol |
| Video | The links above, and in the header of each document |
