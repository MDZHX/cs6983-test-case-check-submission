# Team metrics

The core metrics, survey and interview shared by all three test cases. Every case uses these exact
names: `testbed/scorer.py` writes `reward.json`, and `testbed/survey.py` holds the survey.

## What we measure

The agent decides alone what to learn from an edit and how widely it applies, and the professor can't see it.

- **Memory**: did it learn the right things, at the right scope? (objective)
- **Draft**: does the next email come out right? (objective)
- **User**: does she know what it learned, and does she agree? (subjective, human mode only)

## Answer key (each case provides one)

- **Preferences**: lasting rules, each with its scope (who or what situations it applies to).
- **One-offs**: one-time edits that should not become rules.
- **Outdated**: her old practice that later edits replaced, each with what replaced it. It counts as
  retired only if memory drops it or says she no longer does it; a "past exception" or "it depends"
  still counts as kept. (Optional: a case includes these only if her practice changes.)
- **Draft checklist**: `must` / `must_not` for the final email.

When her practice changes, split the change into these items; don't add a new item type:

| What happens | Answer-key items |
|---|---|
| She starts doing Y | preference Y |
| She stops doing X | outdated X |
| She changes X to X′ (a new value or scope) | preference X′ + outdated X |
| She does Z once | one-off Z |

The judge scores what the memory says at the end, not how the agent edited it, so editing a note,
replacing it, or keeping it marked "no longer" all score the same.

Each item must be either inferable by a careful reader of the feedback rounds, or stated as the
professor's own view in the case's `participant.md` (things only the user knows).

## Objective metrics (`reward.json`, both modes)

An LLM judge scores the memory after the last feedback round against the answer key. Each item gets exactly one outcome.

| Metric | Value | Definition |
|---|---|---|
| `prefs_correct` | count | Preferences saved with the right scope |
| `prefs_wrong_scope` | count | Preferences saved, but too narrow, too broad, or tied to the wrong cue |
| `prefs_missed` | count | Preferences not saved |
| `one_offs_wrongly_saved` | count | One-offs saved as rules to repeat |
| `outdated_kept` | count | Outdated practice that memory still presents as current, instead of deleting it or marking it as replaced |
| `draft_correct` | 0/1 | A draft was saved, every `must` holds, and no `must_not` holds |
| `draft_asked_clarification` | 0/1 | The final task ended with a question to the professor instead of a draft |

`prefs_correct + prefs_wrong_scope + prefs_missed` = the number of preferences in the key.

**A run shows a breakdown** if any memory error count (`prefs_wrong_scope`, `prefs_missed`,
`one_offs_wrongly_saved`, `outdated_kept`) is above 0 (memory breakdown), or if `draft_correct = 0` (draft breakdown).

The judge's label, supporting quote, and reason for each item go in `reward_details.json`, with every judge call exactly as sent and received (instructions, input, output), so every number can be checked by hand.

## Subjective metrics (survey, human mode only)

Rated 1 (strongly disagree) to 7 (strongly agree). Participants are told at the start that the assistant learns from their edits.

| Metric | Item | When |
|---|---|---|
| `perceived_understanding` | "I know what the assistant learned from my edits." | Before the memory reveal |
| `perceived_control` | "I could control what the assistant learned from my edits." | Before the memory reveal |
| `cognitive_load` | "Getting the drafts right took a lot of effort." | Before the memory reveal |
| `memory_agreement` | "What the assistant saved matches what I meant." | After the memory reveal |

High understanding before the reveal with low agreement after it means she thought she knew what was learned and was wrong.

## Interview (after the survey)

1. Before you saw the memory, what did you think the assistant had learned from you?
2. Was anything it saved wrong, too broad, or too narrow?
3. Did the final draft match what you expected? Why or why not?
4. How would you want to tell the assistant what to learn, or what not to?

## Who created and tested each case

| Case | Created by | Tested (video) by |
|---|---|---|
| `disclosure_committee` | Zihan Xue | Sanjana Nilesh Brahmbhatt |
| `context_one_offs` | Sanjana Nilesh Brahmbhatt | Jinbo Hu |
| `extension_drift` | Jinbo Hu | Zihan Xue |
