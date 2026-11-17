# context_one_offs: run summary

One row per run, read from its reward.json. Memory breakdown: any of prefs_wrong_scope, prefs_missed, one_offs_wrongly_saved, outdated_kept above 0. Draft breakdown: draft_correct = 0.

## full case: starting memory, feedback rounds, final task

| run | mode | prefs_correct | prefs_wrong_scope | prefs_missed | one_offs_wrongly_saved | outdated_kept | draft_correct | draft_asked_clarification | memory breakdown | draft breakdown |
|---|---|---|---|---|---|---|---|---|---|---|
| run-01 | simulated_user | 0 | 2 | 0 | 2 | 0 | 0 | 0 | yes | yes |
| run-02 | simulated_user | 2 | 0 | 0 | 1 | 0 | 1 | 0 | yes | no |
| run-03 | simulated_user | 2 | 0 | 0 | 1 | 0 | 1 | 0 | yes | no |
| run-04 | simulated_user | 2 | 0 | 0 | 1 | 0 | 1 | 0 | yes | no |
| run-05 | simulated_user | 2 | 0 | 0 | 3 | 0 | 1 | 0 | yes | no |

Memory breakdown in 5 of 5 runs; draft breakdown in 1 of 5 runs.

## control: final task only, empty memory (the model's default)

| run | mode | prefs_correct | prefs_wrong_scope | prefs_missed | one_offs_wrongly_saved | outdated_kept | draft_correct | draft_asked_clarification | memory breakdown | draft breakdown |
|---|---|---|---|---|---|---|---|---|---|---|
| run-01 | simulated_user | - | - | - | - | - | 1 | 0 | - | no |
| run-02 | simulated_user | - | - | - | - | - | 1 | 0 | - | no |
| run-03 | simulated_user | - | - | - | - | - | 1 | 0 | - | no |

Memory breakdown in 0 of 3 runs; draft breakdown in 0 of 3 runs.

