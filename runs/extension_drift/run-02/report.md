# extension_drift / full case / run-02

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

**Agent's reply:** Noted—brief, empathetic, and direct. I also shouldn’t have invented a no-extension policy; I’ll avoid that in future drafts.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -1 +1,6 @@
-(memory is empty)
+=== /memories/email_preferences.md ===
+# Jane's email preferences
+
+- Prefer brief, direct replies to students, with a short empathetic acknowledgment and a concrete answer. Example: “Sorry you've been sick. Take until Monday at 5 pm for Problem Set 1, no penalty.”
+- In the illness-related extension reply to Priya Nair for CS 4100 Problem Set 1, Jane chose a penalty-free extension until Monday at 5 pm rather than refusing an extension or directing the student to use late days. Do not assume a blanket no-extension policy; this example is not a universal extension policy either.
+- Student-email sign-off in this example: “Prof. Doe” without “Best,”.
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

**Agent's reply:** Noted—warm, brief, and direct, with a concrete deadline rather than a request for documentation.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -6 +6,3 @@
 - Student-email sign-off in this example: “Prof. Doe” without “Best,”.
+
+- For Marcus Bell's job-interview travel extension request, Jane replaced a request for documentation with a warm, direct approval: “Good luck with the interview! Sure, turn in Problem Set 2 by Sunday at 5 pm.” Avoid adding documentation hurdles without Jane's instruction; favor a concrete deadline. This is an example, not a blanket extension policy.
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

**Agent's reply:** Got it—short, casual, and direct with familiar collaborators. I’ll use that style going forward.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -8 +8,3 @@
 - For Marcus Bell's job-interview travel extension request, Jane replaced a request for documentation with a warm, direct approval: “Good luck with the interview! Sure, turn in Problem Set 2 by Sunday at 5 pm.” Avoid adding documentation hurdles without Jane's instruction; favor a concrete deadline. This is an example, not a blanket extension policy.
+
+- With familiar faculty collaborators such as Ravi Mehta, use a casual, concise tone: “Hi Ravi,” and sign off simply “Jane”. Jane edited a reading-group reply to: “I'm in! Thursdays are bad for me, though. Could we do Tuesdays?” Favor contractions and direct scheduling language over formal thanks, “I would be delighted,” “Unfortunately,” or “Best regards.”
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

**Agent's reply:** Noted—I'll avoid inventing extension deadlines and direct students to available late days for similar requests unless you specify otherwise.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -3,5 +3,6 @@
 
-- Prefer brief, direct replies to students, with a short empathetic acknowledgment and a concrete answer. Example: “Sorry you've been sick. Take until Monday at 5 pm for Problem Set 1, no penalty.”
+- Prefer brief, direct replies to students, with a short empathetic acknowledgment and a concrete answer. Do not automatically copy deadlines or extension terms from past replies; Jane's decisions vary by request.
 - In the illness-related extension reply to Priya Nair for CS 4100 Problem Set 1, Jane chose a penalty-free extension until Monday at 5 pm rather than refusing an extension or directing the student to use late days. Do not assume a blanket no-extension policy; this example is not a universal extension policy either.
 - Student-email sign-off in this example: “Prof. Doe” without “Best,”.
+- For Jordan Lee's flu-related CS 4100 Problem Set 4 extension request, Jane replaced an invented penalty-free Monday extension with: “Sorry you've been sick. You can use your late days for Problem Set 4.” For similar requests, prefer directing students to available late days rather than inventing an extra extension or deadline without Jane's authorization. This does not override her explicit case-by-case extension decisions.
 
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

**Agent's reply:** Noted—I'll point students to the existing late-day policy rather than inventing an extension deadline, unless you specify otherwise.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -8,3 +8,3 @@
 
-- For Marcus Bell's job-interview travel extension request, Jane replaced a request for documentation with a warm, direct approval: “Good luck with the interview! Sure, turn in Problem Set 2 by Sunday at 5 pm.” Avoid adding documentation hurdles without Jane's instruction; favor a concrete deadline. This is an example, not a blanket extension policy.
+- For job-interview travel requests, keep a warm acknowledgment (“Good luck with the interview!”) and avoid documentation hurdles. In Sam Ortiz's Problem Set 5 reply, Jane replaced an invented Sunday 5 pm extension with: “If you need more time on Problem Set 5, you can use your late days.” Default to the existing late-day policy rather than inventing a deadline or granting an extra extension. Jane previously explicitly approved a Sunday 5 pm extension for Marcus Bell's Problem Set 2, but that was case-specific, not a precedent to copy.
 
```

## Final task

**Request:** Reply to Leo.

**Draft** (subject: Re: Extension on Problem Set 6?):
```
Hi Leo,

Sorry you've been sick. You can use your late days for Problem Set 6. Hope you feel better soon!

Prof. Doe
```

Read memory before drafting: yes. Looked up a contact: no.

## Memory at the end

`/memories/email_preferences.md`
```
# Jane's email preferences

- Prefer brief, direct replies to students, with a short empathetic acknowledgment and a concrete answer. Do not automatically copy deadlines or extension terms from past replies; Jane's decisions vary by request.
- In the illness-related extension reply to Priya Nair for CS 4100 Problem Set 1, Jane chose a penalty-free extension until Monday at 5 pm rather than refusing an extension or directing the student to use late days. Do not assume a blanket no-extension policy; this example is not a universal extension policy either.
- Student-email sign-off in this example: “Prof. Doe” without “Best,”.
- For Jordan Lee's flu-related CS 4100 Problem Set 4 extension request, Jane replaced an invented penalty-free Monday extension with: “Sorry you've been sick. You can use your late days for Problem Set 4.” For similar requests, prefer directing students to available late days rather than inventing an extra extension or deadline without Jane's authorization. This does not override her explicit case-by-case extension decisions.

- For job-interview travel requests, keep a warm acknowledgment (“Good luck with the interview!”) and avoid documentation hurdles. In Sam Ortiz's Problem Set 5 reply, Jane replaced an invented Sunday 5 pm extension with: “If you need more time on Problem Set 5, you can use your late days.” Default to the existing late-day policy rather than inventing a deadline or granting an extra extension. Jane previously explicitly approved a Sunday 5 pm extension for Marcus Bell's Problem Set 2, but that was case-specific, not a precedent to copy.

- With familiar faculty collaborators such as Ravi Mehta, use a casual, concise tone: “Hi Ravi,” and sign off simply “Jane”. Jane edited a reading-group reply to: “I'm in! Thursdays are bad for me, though. Could we do Tuesdays?” Favor contractions and direct scheduling language over formal thanks, “I would be delighted,” “Unfortunately,” or “Best regards.”
```

## Scoring

`reward.json`: `prefs_correct` = 1, `prefs_wrong_scope` = 0, `prefs_missed` = 0, `one_offs_wrongly_saved` = 0, `outdated_kept` = 1, `draft_correct` = 1, `draft_asked_clarification` = 0

**Memory after the last feedback round, item by item:**

| item | type | outcome | scope error | memory quote | reason |
|---|---|---|---|---|---|
| P1: In the October flu and job-interview-travel examples, points students to their late days rather than granting a new individual deadline; this is the latest observed practice for these situations. | preference | **correct** |  | For Jordan Lee's flu-related CS 4100 Problem Set 4 extension request, Jane replaced an invented penalty-free Monday extension with: “Sorry you've been sick. You can use your late days for Problem Set 4.” For similar requests, prefer directing students to available late days rather than inventing an extra extension or deadline without Jane's authorization. This does not override her explicit case-by-case extension decisions. - For job-interview travel requests, keep a warm acknowledgment (“Good luck with the interview!”) and avoid documentation hurdles. In Sam Ortiz's Problem Set 5 reply, Jane replaced an invented Sunday 5 pm extension with: “If you need more time on Problem Set 5, you can use your late days.” Default to the existing late-day policy rather than inventing a deadline or granting an extra extension. | The memory generalizes the late-day approach to similar flu requests and job-interview travel requests, covering new students while allowing explicit case-by-case exceptions. |
| R1: Grants individual extensions for the observed flu and job-interview-travel requests, as in the September examples with Priya and Marcus. (replaced by: The October replies to matched flu and job-interview-travel requests use existing late days rather than granting a new individual deadline (P1).) | outdated | **kept** |  | In the illness-related extension reply to Priya Nair for CS 4100 Problem Set 1, Jane chose a penalty-free extension until Monday at 5 pm rather than refusing an extension or directing the student to use late days. Do not assume a blanket no-extension policy; this example is not a universal extension policy either. | The memory preserves the earlier individual extension as a case-specific example without saying Jane no longer follows that practice. |

**Final draft checklist:**

| check | statement | passed | draft quote | reason |
|---|---|---|---|---|
| must | Responds to Leo's request about Problem Set 6. | yes | You can use your late days for Problem Set 6. | The draft directly addresses Leo's request for more time on Problem Set 6. |
| must | Directs Leo to use his available late days if he needs more time, consistent with the October flu example. | yes | You can use your late days for Problem Set 6. | The draft directs Leo to use his existing late-day allowance for additional time. |
| must_not | Grants Leo an individual extension or a new deadline outside the existing late-day allowance. | yes | You can use your late days for Problem Set 6. | The draft permits use of existing late days without granting a separate extension or new deadline. |

## Reviewer notes

- Do the judge's labels look right? (yes / no, which ones):
- What went wrong, in one or two sentences:

