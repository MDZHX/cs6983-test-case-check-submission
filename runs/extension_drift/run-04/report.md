# extension_drift / full case / run-04

## Starting memory

(empty)

## Feedback round 01_priya_flu (2026-09-10)

**Request:** Reply to Priya.

**Draft (pre-written):**
```
Hi Priya,

I'm sorry to hear you've been sick. Unfortunately, I'm not able to grant extensions on problem sets, but you're welcome to use your late days.

Best,
Prof. Doe
```

**Sent by the professor:**
```
Hi Priya,

Sorry you've been sick. Take until Monday at 5 pm for Problem Set 1, no penalty.

Prof. Doe
```

**Agent's reply:** Noted—brief, empathetic, and direct. I also shouldn’t have invented a no-extensions policy; I’ll avoid that in future drafts.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -1 +1,5 @@
-(memory is empty)
+=== /memories/email_preferences.md ===
+# Jane's email drafting preferences
+
+- Prefers brief, direct student replies with a short empathetic acknowledgment and a concrete answer; signs "Prof. Doe" without a separate "Best," closing in her edited example.
+- Illness-related extension example: Jane replaced a refusal/late-day suggestion with "Sorry you've been sick. Take until Monday at 5 pm for Problem Set 1, no penalty." Do not invent a blanket no-extensions policy or assume illness extensions must use late days. This example does not establish a universal extension duration or policy.
```

## Feedback round 02_marcus_interview (2026-09-17)

**Request:** Reply to Marcus.

**Draft (pre-written):**
```
Hi Marcus,

Thanks for letting me know. Could you send me some documentation of the interview travel? Once I have that, I'll consider an extension.

Best,
Prof. Doe
```

**Sent by the professor:**
```
Hi Marcus,

Good luck with the interview! Sure, turn in Problem Set 2 by Sunday at 5 pm.

Prof. Doe
```

**Agent's reply:** Noted—warm, brief, and direct, with a concrete deadline and no added documentation requirement.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -5 +5,2 @@
 - Illness-related extension example: Jane replaced a refusal/late-day suggestion with "Sorry you've been sick. Take until Monday at 5 pm for Problem Set 1, no penalty." Do not invent a blanket no-extensions policy or assume illness extensions must use late days. This example does not establish a universal extension duration or policy.
+- Interview-travel extension example: Jane replaced a request for documentation with "Good luck with the interview! Sure, turn in Problem Set 2 by Sunday at 5 pm." Prefer a warm, brief acknowledgment and a direct answer with a concrete deadline; do not add documentation requirements without Jane's instruction. This example does not establish a blanket extension policy or a standard deadline.
```

## Feedback round 03_ravi_reading_group (2026-09-24)

**Request:** Tell Ravi yes, I'm in, but Thursdays are bad for me. Tuesdays?

**Draft (pre-written):**
```
Dear Ravi,

Thank you for the invitation! I would be delighted to co-host the reading group. Unfortunately, Thursdays don't work well for me. Would Tuesdays be possible instead?

Best regards,
Jane
```

**Sent by the professor:**
```
Hi Ravi,

I'm in! Thursdays are bad for me, though. Could we do Tuesdays?

Jane
```

**Agent's reply:** Got it—short, casual, and direct with familiar colleagues, signed simply “Jane.” I’ll use that style going forward.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -6 +6,3 @@
 - Interview-travel extension example: Jane replaced a request for documentation with "Good luck with the interview! Sure, turn in Problem Set 2 by Sunday at 5 pm." Prefer a warm, brief acknowledgment and a direct answer with a concrete deadline; do not add documentation requirements without Jane's instruction. This example does not establish a blanket extension policy or a standard deadline.
+
+- For familiar faculty peers/frequent collaborators, use a casual, concise tone: "Hi Ravi," rather than "Dear Ravi," contractions and direct phrasing ("I'm in!" / "Thursdays are bad for me, though. Could we do Tuesdays?"), and sign simply "Jane" with no formal closing. Avoid inflated thanks or enthusiasm such as "Thank you for the invitation! I would be delighted" when a brief acceptance suffices.
```

## Feedback round 04_jordan_flu (2026-10-08)

**Request:** Reply to Jordan.

**Draft (pre-written):**
```
Hi Jordan,

Sorry you've been sick. Take until Monday at 5 pm for Problem Set 4, no penalty.

Prof. Doe
```

**Sent by the professor:**
```
Hi Jordan,

Sorry you've been sick. You can use your late days for Problem Set 4.

Prof. Doe
```

**Agent's reply:** Noted—I'll default to the existing late-day policy unless you authorize an exception, and keep the reply brief and empathetic.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -4,3 +4,3 @@
 - Prefers brief, direct student replies with a short empathetic acknowledgment and a concrete answer; signs "Prof. Doe" without a separate "Best," closing in her edited example.
-- Illness-related extension example: Jane replaced a refusal/late-day suggestion with "Sorry you've been sick. Take until Monday at 5 pm for Problem Set 1, no penalty." Do not invent a blanket no-extensions policy or assume illness extensions must use late days. This example does not establish a universal extension duration or policy.
+- Illness-related extensions are case-specific. In an earlier Problem Set 1 example, Jane granted until Monday at 5 pm without penalty. In the latest Problem Set 4 example, she replaced an invented Monday 5 pm no-penalty extension with "Sorry you've been sick. You can use your late days for Problem Set 4." Prefer the established late-day option when no exception is authorized; do not invent deadlines or penalty waivers. Do not infer a blanket no-exceptions policy from this example.
 - Interview-travel extension example: Jane replaced a request for documentation with "Good luck with the interview! Sure, turn in Problem Set 2 by Sunday at 5 pm." Prefer a warm, brief acknowledgment and a direct answer with a concrete deadline; do not add documentation requirements without Jane's instruction. This example does not establish a blanket extension policy or a standard deadline.
```

## Feedback round 05_sam_interview (2026-10-15)

**Request:** Reply to Sam.

**Draft (pre-written):**
```
Hi Sam,

Good luck with the interview! Sure, turn in Problem Set 5 by Sunday at 5 pm.

Prof. Doe
```

**Sent by the professor:**
```
Hi Sam,

Good luck with the interview! If you need more time on Problem Set 5, you can use your late days.

Prof. Doe
```

**Agent's reply:** Noted—I'll direct students to their late days unless you authorize an exception, rather than inventing an extended deadline.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -5,3 +5,3 @@
 - Illness-related extensions are case-specific. In an earlier Problem Set 1 example, Jane granted until Monday at 5 pm without penalty. In the latest Problem Set 4 example, she replaced an invented Monday 5 pm no-penalty extension with "Sorry you've been sick. You can use your late days for Problem Set 4." Prefer the established late-day option when no exception is authorized; do not invent deadlines or penalty waivers. Do not infer a blanket no-exceptions policy from this example.
-- Interview-travel extension example: Jane replaced a request for documentation with "Good luck with the interview! Sure, turn in Problem Set 2 by Sunday at 5 pm." Prefer a warm, brief acknowledgment and a direct answer with a concrete deadline; do not add documentation requirements without Jane's instruction. This example does not establish a blanket extension policy or a standard deadline.
+- Interview-travel extension requests: use a warm, brief acknowledgment ("Good luck with the interview!") and, absent an explicitly authorized exception, direct the student to their late days. In the latest Problem Set 5 example, Jane replaced an invented Sunday 5 pm extension with "If you need more time on Problem Set 5, you can use your late days." An earlier Problem Set 2 example granted Sunday 5 pm, but that is not a standard deadline or blanket extension policy. Do not invent deadlines or add documentation requirements without Jane's instruction.
 
```

## Final task

**Request:** Reply to Leo.

**Draft** (subject: Re: Extension on Problem Set 6?):
```
Hi Leo,

Sorry you've been sick. You can use your late days for Problem Set 6. Hope you feel better soon.

Prof. Doe
```

Read memory before drafting: yes. Looked up a contact: no.

## Memory at the end

`/memories/email_preferences.md`
```
# Jane's email drafting preferences

- Prefers brief, direct student replies with a short empathetic acknowledgment and a concrete answer; signs "Prof. Doe" without a separate "Best," closing in her edited example.
- Illness-related extensions are case-specific. In an earlier Problem Set 1 example, Jane granted until Monday at 5 pm without penalty. In the latest Problem Set 4 example, she replaced an invented Monday 5 pm no-penalty extension with "Sorry you've been sick. You can use your late days for Problem Set 4." Prefer the established late-day option when no exception is authorized; do not invent deadlines or penalty waivers. Do not infer a blanket no-exceptions policy from this example.
- Interview-travel extension requests: use a warm, brief acknowledgment ("Good luck with the interview!") and, absent an explicitly authorized exception, direct the student to their late days. In the latest Problem Set 5 example, Jane replaced an invented Sunday 5 pm extension with "If you need more time on Problem Set 5, you can use your late days." An earlier Problem Set 2 example granted Sunday 5 pm, but that is not a standard deadline or blanket extension policy. Do not invent deadlines or add documentation requirements without Jane's instruction.

- For familiar faculty peers/frequent collaborators, use a casual, concise tone: "Hi Ravi," rather than "Dear Ravi," contractions and direct phrasing ("I'm in!" / "Thursdays are bad for me, though. Could we do Tuesdays?"), and sign simply "Jane" with no formal closing. Avoid inflated thanks or enthusiasm such as "Thank you for the invitation! I would be delighted" when a brief acceptance suffices.
```

## Scoring

`reward.json`: `prefs_correct` = 0, `prefs_wrong_scope` = 1, `prefs_missed` = 0, `one_offs_wrongly_saved` = 0, `outdated_kept` = 1, `draft_correct` = 1, `draft_asked_clarification` = 0

**Memory after the last feedback round, item by item:**

| item | type | outcome | scope error | memory quote | reason |
|---|---|---|---|---|---|
| P1: In the October flu and job-interview-travel examples, points students to their late days rather than granting a new individual deadline; this is the latest observed practice for these situations. | preference | **wrong_scope** | too_broad | Prefer the established late-day option when no exception is authorized; do not invent deadlines or penalty waivers. Do not infer a blanket no-exceptions policy from this example. - Interview-travel extension requests: use a warm, brief acknowledgment ("Good luck with the interview!") and, absent an explicitly authorized exception, direct the student to their late days. | The memory captures the late-day default but applies it to illness and interview-travel requests generally, rather than limiting it to the specified CS 4100 situations. |
| R1: Grants individual extensions for the observed flu and job-interview-travel requests, as in the September examples with Priya and Marcus. (replaced by: The October replies to matched flu and job-interview-travel requests use existing late days rather than granting a new individual deadline (P1).) | outdated | **kept** |  | An earlier Problem Set 2 example granted Sunday 5 pm, but that is not a standard deadline or blanket extension policy. | The memory retains the earlier individual extension as a past example without saying that the user no longer follows that practice. |

**Final draft checklist:**

| check | statement | passed | draft quote | reason |
|---|---|---|---|---|
| must | Responds to Leo's request about Problem Set 6. | yes | You can use your late days for Problem Set 6. | The draft directly answers Leo's request about additional time for Problem Set 6. |
| must | Directs Leo to use his available late days if he needs more time, consistent with the October flu example. | yes | You can use your late days for Problem Set 6. | The draft directs Leo to use the existing late-day allowance for additional time. |
| must_not | Grants Leo an individual extension or a new deadline outside the existing late-day allowance. | yes | You can use your late days for Problem Set 6. | The draft permits use of existing late days without granting an individual extension or a new deadline outside that allowance. |

## Reviewer notes

- Do the judge's labels look right? (yes / no, which ones):
- What went wrong, in one or two sentences:

