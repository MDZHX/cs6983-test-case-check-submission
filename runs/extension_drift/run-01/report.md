# extension_drift / full case / run-01

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

**Agent's reply:** Noted. I’ll keep replies brief and direct, and won’t assume extension requests must be denied or charged against late days.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -1 +1,5 @@
-(memory is empty)
+=== /memories/email_preferences.md ===
+# Jane's email preferences
+
+- Prefers brief, direct student replies: a short empathetic acknowledgment, a concrete decision, and the sign-off “Prof. Doe,” without an extra closing such as “Best.”
+- In an illness-related extension reply, Jane replaced an unsupported refusal/use-late-days response with a specific no-penalty extension (until Monday at 5 pm). Do not invent a blanket no-extensions policy or assume illness requests must use late days. This example is not a standing policy to grant all extensions.
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

**Agent's reply:** Noted—brief, warm, and direct, with a specific deadline and no unnecessary documentation request. I’ll use that approach in future drafts.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -5 +5,2 @@
 - In an illness-related extension reply, Jane replaced an unsupported refusal/use-late-days response with a specific no-penalty extension (until Monday at 5 pm). Do not invent a blanket no-extensions policy or assume illness requests must use late days. This example is not a standing policy to grant all extensions.
+- In a job-interview travel extension reply, Jane replaced a request for documentation and conditional consideration with a warm wish (“Good luck with the interview!”) and a direct extension to Sunday at 5 pm. Avoid adding documentation requirements without Jane's instruction. This example does not establish a blanket extension policy.
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

**Agent's reply:** Got it—short, casual, and direct with familiar collaborators, signed simply “Jane.”

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -6 +6,3 @@
 - In a job-interview travel extension reply, Jane replaced a request for documentation and conditional consideration with a warm wish (“Good luck with the interview!”) and a direct extension to Sunday at 5 pm. Avoid adding documentation requirements without Jane's instruction. This example does not establish a blanket extension policy.
+
+- With familiar faculty collaborators such as Ravi, prefers very brief, casual replies: “Hi Ravi,” contractions, a direct enthusiastic acceptance (“I'm in!”), and a simple scheduling question. Sign off “Jane” without a closing phrase. Avoid formal or padded language such as “Dear,” “Thank you for the invitation,” “I would be delighted,” or “Best regards.”
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

**Agent's reply:** Noted—I’ll direct similar requests to the available late days rather than inventing an extension or penalty waiver.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -4,3 +4,3 @@
 - Prefers brief, direct student replies: a short empathetic acknowledgment, a concrete decision, and the sign-off “Prof. Doe,” without an extra closing such as “Best.”
-- In an illness-related extension reply, Jane replaced an unsupported refusal/use-late-days response with a specific no-penalty extension (until Monday at 5 pm). Do not invent a blanket no-extensions policy or assume illness requests must use late days. This example is not a standing policy to grant all extensions.
+- Latest illness-extension correction (Jordan, CS 4100): Jane replaced an invented no-penalty extension until Monday at 5 pm with “You can use your late days for Problem Set 4.” For similar requests, prefer a brief empathetic acknowledgment and referral to the course late days rather than inventing a new deadline or penalty waiver. This supersedes the earlier conflicting illness-extension example; do not infer an absolute no-exceptions policy.
 - In a job-interview travel extension reply, Jane replaced a request for documentation and conditional consideration with a warm wish (“Good luck with the interview!”) and a direct extension to Sunday at 5 pm. Avoid adding documentation requirements without Jane's instruction. This example does not establish a blanket extension policy.
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

**Agent's reply:** Noted—I'll keep the warm acknowledgment and refer students to their late days rather than inventing an extension deadline.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -5,3 +5,3 @@
 - Latest illness-extension correction (Jordan, CS 4100): Jane replaced an invented no-penalty extension until Monday at 5 pm with “You can use your late days for Problem Set 4.” For similar requests, prefer a brief empathetic acknowledgment and referral to the course late days rather than inventing a new deadline or penalty waiver. This supersedes the earlier conflicting illness-extension example; do not infer an absolute no-exceptions policy.
-- In a job-interview travel extension reply, Jane replaced a request for documentation and conditional consideration with a warm wish (“Good luck with the interview!”) and a direct extension to Sunday at 5 pm. Avoid adding documentation requirements without Jane's instruction. This example does not establish a blanket extension policy.
+- Latest job-interview travel extension correction (Sam, CS 4100): Jane kept “Good luck with the interview!” but replaced an invented Sunday-at-5-pm extension with “If you need more time on Problem Set 5, you can use your late days.” For similar requests, warmly acknowledge the interview and refer to available course late days; do not invent a deadline or add documentation requirements. This supersedes the earlier job-interview example granting an extension; it does not establish an absolute no-exceptions policy.
 
```

## Final task

**Request:** Reply to Leo.

**Draft** (subject: Re: Extension on Problem Set 6?):
```
Hi Leo,

I'm sorry you've been sick. You can use your late days for Problem Set 6. I hope you feel better soon!

Prof. Doe
```

Read memory before drafting: yes. Looked up a contact: no.

## Memory at the end

`/memories/email_preferences.md`
```
# Jane's email preferences

- Prefers brief, direct student replies: a short empathetic acknowledgment, a concrete decision, and the sign-off “Prof. Doe,” without an extra closing such as “Best.”
- Latest illness-extension correction (Jordan, CS 4100): Jane replaced an invented no-penalty extension until Monday at 5 pm with “You can use your late days for Problem Set 4.” For similar requests, prefer a brief empathetic acknowledgment and referral to the course late days rather than inventing a new deadline or penalty waiver. This supersedes the earlier conflicting illness-extension example; do not infer an absolute no-exceptions policy.
- Latest job-interview travel extension correction (Sam, CS 4100): Jane kept “Good luck with the interview!” but replaced an invented Sunday-at-5-pm extension with “If you need more time on Problem Set 5, you can use your late days.” For similar requests, warmly acknowledge the interview and refer to available course late days; do not invent a deadline or add documentation requirements. This supersedes the earlier job-interview example granting an extension; it does not establish an absolute no-exceptions policy.

- With familiar faculty collaborators such as Ravi, prefers very brief, casual replies: “Hi Ravi,” contractions, a direct enthusiastic acceptance (“I'm in!”), and a simple scheduling question. Sign off “Jane” without a closing phrase. Avoid formal or padded language such as “Dear,” “Thank you for the invitation,” “I would be delighted,” or “Best regards.”
```

## Scoring

`reward.json`: `prefs_correct` = 1, `prefs_wrong_scope` = 0, `prefs_missed` = 0, `one_offs_wrongly_saved` = 0, `outdated_kept` = 0, `draft_correct` = 1, `draft_asked_clarification` = 0

**Memory after the last feedback round, item by item:**

| item | type | outcome | scope error | memory quote | reason |
|---|---|---|---|---|---|
| P1: In the October flu and job-interview-travel examples, points students to their late days rather than granting a new individual deadline; this is the latest observed practice for these situations. | preference | **correct** |  | - Latest illness-extension correction (Jordan, CS 4100): Jane replaced an invented no-penalty extension until Monday at 5 pm with “You can use your late days for Problem Set 4.” For similar requests, prefer a brief empathetic acknowledgment and referral to the course late days rather than inventing a new deadline or penalty waiver. This supersedes the earlier conflicting illness-extension example; do not infer an absolute no-exceptions policy. - Latest job-interview travel extension correction (Sam, CS 4100): Jane kept “Good luck with the interview!” but replaced an invented Sunday-at-5-pm extension with “If you need more time on Problem Set 5, you can use your late days.” For similar requests, warmly acknowledge the interview and refer to available course late days; do not invent a deadline or add documentation requirements. This supersedes the earlier job-interview example granting an extension; it does not establish an absolute no-exceptions policy. | The memory identifies late-day referrals as the latest practice for both CS 4100 circumstances and explicitly extends that guidance to similar requests without making it exception-free. |
| R1: Grants individual extensions for the observed flu and job-interview-travel requests, as in the September examples with Priya and Marcus. (replaced by: The October replies to matched flu and job-interview-travel requests use existing late days rather than granting a new individual deadline (P1).) | outdated | **retired** |  | This supersedes the earlier conflicting illness-extension example; do not infer an absolute no-exceptions policy. - Latest job-interview travel extension correction (Sam, CS 4100): Jane kept “Good luck with the interview!” but replaced an invented Sunday-at-5-pm extension with “If you need more time on Problem Set 5, you can use your late days.” For similar requests, warmly acknowledge the interview and refer to available course late days; do not invent a deadline or add documentation requirements. This supersedes the earlier job-interview example granting an extension; it does not establish an absolute no-exceptions policy. | The memory explicitly says the newer late-day guidance supersedes both earlier individual-extension examples. |

**Final draft checklist:**

| check | statement | passed | draft quote | reason |
|---|---|---|---|---|
| must | Responds to Leo's request about Problem Set 6. | yes | You can use your late days for Problem Set 6. | The draft directly addresses Leo's request for more time on Problem Set 6. |
| must | Directs Leo to use his available late days if he needs more time, consistent with the October flu example. | yes | You can use your late days for Problem Set 6. | The draft directs Leo to use his existing late-day allowance for additional time. |
| must_not | Grants Leo an individual extension or a new deadline outside the existing late-day allowance. | yes | You can use your late days for Problem Set 6. | The draft permits only the use of existing late days and does not grant an individual extension or a new deadline outside that allowance. |

## Reviewer notes

- Do the judge's labels look right? (yes / no, which ones):
- What went wrong, in one or two sentences:

