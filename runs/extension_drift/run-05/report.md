# extension_drift / full case / run-05

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
+# Jane's email preferences
+
+- Favor brief, direct student replies: a short empathetic acknowledgment, a clear decision, and the signature "Prof. Doe"; no extra closing needed.
+- In the Priya Nair illness-extension example, Jane replaced a refusal/use-late-days draft with: "Sorry you've been sick. Take until Monday at 5 pm for Problem Set 1, no penalty." Do not invent a blanket no-extensions policy or assume illness extensions must use late days. This example is not a general authorization to grant future extensions or choose deadlines without Jane's direction.
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

**Agent's reply:** Noted—brief, encouraging, and direct, without an added documentation requirement.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -5 +5,2 @@
 - In the Priya Nair illness-extension example, Jane replaced a refusal/use-late-days draft with: "Sorry you've been sick. Take until Monday at 5 pm for Problem Set 1, no penalty." Do not invent a blanket no-extensions policy or assume illness extensions must use late days. This example is not a general authorization to grant future extensions or choose deadlines without Jane's direction.
+- In the Marcus Bell interview-travel example, Jane replaced a request for documentation with a warm, direct approval: "Good luck with the interview! Sure, turn in Problem Set 2 by Sunday at 5 pm." Avoid adding documentation requirements without Jane's direction. This example does not authorize granting all future extensions or inventing deadlines.
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

**Agent's reply:** Got it—short, casual, and direct with familiar colleagues. I’ll use that style going forward.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -6 +6,3 @@
 - In the Marcus Bell interview-travel example, Jane replaced a request for documentation with a warm, direct approval: "Good luck with the interview! Sure, turn in Problem Set 2 by Sunday at 5 pm." Avoid adding documentation requirements without Jane's direction. This example does not authorize granting all future extensions or inventing deadlines.
+
+- For familiar faculty peers/frequent collaborators, use a casual, concise tone: "Hi Ravi," and sign simply "Jane" without a formal closing. Prefer direct phrasing and contractions ("I'm in!", "Thursdays are bad for me, though. Could we do Tuesdays?") over formal thanks, "delighted," or "Best regards."
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

**Agent's reply:** Noted—I'll point students to their late days for similar requests rather than inventing a new deadline or penalty-free extension.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -6,2 +6,3 @@
 - In the Marcus Bell interview-travel example, Jane replaced a request for documentation with a warm, direct approval: "Good luck with the interview! Sure, turn in Problem Set 2 by Sunday at 5 pm." Avoid adding documentation requirements without Jane's direction. This example does not authorize granting all future extensions or inventing deadlines.
+- In the Jordan Lee flu/Problem Set 4 example, Jane replaced an invented Monday-at-5-pm penalty-free extension with: "Sorry you've been sick. You can use your late days for Problem Set 4." For similar requests, prefer briefly acknowledging illness and pointing to available late days rather than inventing a deadline or granting a penalty-free exception. Illness alone does not imply an exception; follow Jane's explicit direction when provided.
 
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

**Agent's reply:** Noted—I'll keep the warm acknowledgment and point students to their late days rather than inventing an extension deadline.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -7,2 +7,3 @@
 - In the Jordan Lee flu/Problem Set 4 example, Jane replaced an invented Monday-at-5-pm penalty-free extension with: "Sorry you've been sick. You can use your late days for Problem Set 4." For similar requests, prefer briefly acknowledging illness and pointing to available late days rather than inventing a deadline or granting a penalty-free exception. Illness alone does not imply an exception; follow Jane's explicit direction when provided.
+- In the Sam Ortiz interview-travel/Problem Set 5 example, Jane replaced an invented Sunday-at-5-pm extension with: "Good luck with the interview! If you need more time on Problem Set 5, you can use your late days." For interview-travel requests, prefer a warm acknowledgment and pointing to late days rather than granting an extension or choosing a new deadline without Jane's direction. The earlier Marcus example is not a standing exception for interviews.
 
```

## Final task

**Request:** Reply to Leo.

**Draft** (subject: Re: Extension on Problem Set 6?):
```
Hi Leo,

Sorry you've been sick. You can use your late days for Problem Set 6.

Prof. Doe
```

Read memory before drafting: yes. Looked up a contact: no.

## Memory at the end

`/memories/email_preferences.md`
```
# Jane's email preferences

- Favor brief, direct student replies: a short empathetic acknowledgment, a clear decision, and the signature "Prof. Doe"; no extra closing needed.
- In the Priya Nair illness-extension example, Jane replaced a refusal/use-late-days draft with: "Sorry you've been sick. Take until Monday at 5 pm for Problem Set 1, no penalty." Do not invent a blanket no-extensions policy or assume illness extensions must use late days. This example is not a general authorization to grant future extensions or choose deadlines without Jane's direction.
- In the Marcus Bell interview-travel example, Jane replaced a request for documentation with a warm, direct approval: "Good luck with the interview! Sure, turn in Problem Set 2 by Sunday at 5 pm." Avoid adding documentation requirements without Jane's direction. This example does not authorize granting all future extensions or inventing deadlines.
- In the Jordan Lee flu/Problem Set 4 example, Jane replaced an invented Monday-at-5-pm penalty-free extension with: "Sorry you've been sick. You can use your late days for Problem Set 4." For similar requests, prefer briefly acknowledging illness and pointing to available late days rather than inventing a deadline or granting a penalty-free exception. Illness alone does not imply an exception; follow Jane's explicit direction when provided.
- In the Sam Ortiz interview-travel/Problem Set 5 example, Jane replaced an invented Sunday-at-5-pm extension with: "Good luck with the interview! If you need more time on Problem Set 5, you can use your late days." For interview-travel requests, prefer a warm acknowledgment and pointing to late days rather than granting an extension or choosing a new deadline without Jane's direction. The earlier Marcus example is not a standing exception for interviews.

- For familiar faculty peers/frequent collaborators, use a casual, concise tone: "Hi Ravi," and sign simply "Jane" without a formal closing. Prefer direct phrasing and contractions ("I'm in!", "Thursdays are bad for me, though. Could we do Tuesdays?") over formal thanks, "delighted," or "Best regards."
```

## Scoring

`reward.json`: `prefs_correct` = 1, `prefs_wrong_scope` = 0, `prefs_missed` = 0, `one_offs_wrongly_saved` = 0, `outdated_kept` = 1, `draft_correct` = 1, `draft_asked_clarification` = 0

**Memory after the last feedback round, item by item:**

| item | type | outcome | scope error | memory quote | reason |
|---|---|---|---|---|---|
| P1: In the October flu and job-interview-travel examples, points students to their late days rather than granting a new individual deadline; this is the latest observed practice for these situations. | preference | **correct** |  | For similar requests, prefer briefly acknowledging illness and pointing to available late days rather than inventing a deadline or granting a penalty-free exception. Illness alone does not imply an exception; follow Jane's explicit direction when provided. - In the Sam Ortiz interview-travel/Problem Set 5 example, Jane replaced an invented Sunday-at-5-pm extension with: "Good luck with the interview! If you need more time on Problem Set 5, you can use your late days." For interview-travel requests, prefer a warm acknowledgment and pointing to late days rather than granting an extension or choosing a new deadline without Jane's direction. | The memory generalizes the later flu and interview-travel replies to similar requests, directing students to late days rather than inventing individual extensions. |
| R1: Grants individual extensions for the observed flu and job-interview-travel requests, as in the September examples with Priya and Marcus. (replaced by: The October replies to matched flu and job-interview-travel requests use existing late days rather than granting a new individual deadline (P1).) | outdated | **kept** |  | - In the Priya Nair illness-extension example, Jane replaced a refusal/use-late-days draft with: "Sorry you've been sick. Take until Monday at 5 pm for Problem Set 1, no penalty." Do not invent a blanket no-extensions policy or assume illness extensions must use late days. This example is not a general authorization to grant future extensions or choose deadlines without Jane's direction. - In the Marcus Bell interview-travel example, Jane replaced a request for documentation with a warm, direct approval: "Good luck with the interview! Sure, turn in Problem Set 2 by Sunday at 5 pm." Avoid adding documentation requirements without Jane's direction. This example does not authorize granting all future extensions or inventing deadlines. | The memory preserves the earlier individual extensions as examples without explicitly stating that Jane stopped that practice or that the later late-days practice superseded it. |

**Final draft checklist:**

| check | statement | passed | draft quote | reason |
|---|---|---|---|---|
| must | Responds to Leo's request about Problem Set 6. | yes | You can use your late days for Problem Set 6. | The draft directly responds to Leo's request for more time on Problem Set 6. |
| must | Directs Leo to use his available late days if he needs more time, consistent with the October flu example. | yes | You can use your late days for Problem Set 6. | The draft directs Leo to use the existing late-day allowance rather than offering a separate accommodation. |
| must_not | Grants Leo an individual extension or a new deadline outside the existing late-day allowance. | yes | You can use your late days for Problem Set 6. | The draft permits only the use of existing late days and grants no individual extension or new deadline outside that allowance. |

## Reviewer notes

- Do the judge's labels look right? (yes / no, which ones):
- What went wrong, in one or two sentences:

