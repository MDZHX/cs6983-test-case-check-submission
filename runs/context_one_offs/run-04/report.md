# context_one_offs / full case / run-04

## Starting memory

(empty)

## Feedback round 01_peer_reschedule (2026-09-14)

**Request:** Tell Ravi I need to push Thursday's meeting. My mom is having surgery and I'm flying to Chicago Wednesday night. Next Tuesday?

**Draft (pre-written):**
```
Dear Prof. Mehta,

I'm afraid I need to reschedule our Thursday meeting due to a conflict. Would next Tuesday work for you instead?

Best regards,
Jane Doe
```

**Sent by the professor:**
```
Hi Ravi,

Congratulations on the NSF grant! That's fantastic news.

I need to push Thursday. My mom is having surgery and I'm flying to Chicago Wednesday night. Could we do next Tuesday, any time after 2?

Jane
```

**Agent's reply:** Got it—I’ll keep future drafts to close colleagues warm and direct, acknowledge their news, and preserve the personal context you provide.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -1 +1,7 @@
-(memory is empty)
+=== /memories/email_preferences.md ===
+# Jane's email writing preferences
+
+- For familiar faculty collaborators such as Ravi Mehta, use a warm, informal, concise tone: "Hi Ravi," and sign "Jane", rather than titles or a formal closing.
+- Acknowledge good news in the incoming email enthusiastically before addressing logistics (e.g., congratulations on a grant).
+- Preserve personal context Jane explicitly supplies for the email rather than replacing it with a generic "conflict."
+- Use direct, natural scheduling language, such as "I need to push Thursday" and "Could we do next Tuesday...?" Include any availability Jane supplies; do not invent it.
```

## Feedback round 02_class_office_hours (2026-09-15)

**Request:** Tell the class I'm moving Thursday's office hours, I have a doctor's appointment. Friday 2 to 3 works. Our usual room is booked Friday, so it'll be in WVH 210.

**Draft (pre-written):**
```
Hi everyone,

Because of a doctor's appointment, I need to move this Thursday's office hours. I'll hold them on Friday from 2 to 3 pm instead, in WVH 210, since our usual room is booked.

Best,
Jane
```

**Sent by the professor:**
```
Hi everyone,

This week's office hours are moving from Thursday to Friday, 2 to 3 pm, in WVH 210 (our usual room is booked that day).

Prof. Doe
```

**Agent's reply:** Noted—future class announcements will be brief, omit personal reasons, and use “Prof. Doe” as the sign-off.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -5,3 +5,4 @@
 - Acknowledge good news in the incoming email enthusiastically before addressing logistics (e.g., congratulations on a grant).
-- Preserve personal context Jane explicitly supplies for the email rather than replacing it with a generic "conflict."
+- For student-facing logistical announcements, omit personal reasons such as doctor's appointments even if Jane supplies them as context. Prefer a brief, direct announcement with the new day, time, and location; logistical explanations can go in parentheses.
+- For class emails, use "Hi everyone," and sign "Prof. Doe" without an additional closing such as "Best".
 - Use direct, natural scheduling language, such as "I need to push Thursday" and "Could we do next Tuesday...?" Include any availability Jane supplies; do not invent it.
```

## Feedback round 03_student_extension (2026-09-17)

**Request:** Jordan asked for an extension on Assignment 2 because he has other deadlines. Say no.

**Draft (pre-written):**
```
Hi Jordan,

Unfortunately, I can't grant an extension on Assignment 2. Good luck with your deadlines!

Best,
Jane
```

**Sent by the professor:**
```
Hi Jordan,

I can't grant an extension on Assignment 2, since other deadlines aren't grounds for one. You can still turn it in up to 24 hours late for a 10% penalty, and if you're stuck, come to office hours on Friday.

Prof. Doe
```

**Agent's reply:** Noted—I’ll keep student replies direct, explain the reason for a denial, include known alternatives or support, and sign “Prof. Doe” without an extra closing.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -8 +8,2 @@
 - Use direct, natural scheduling language, such as "I need to push Thursday" and "Could we do next Tuesday...?" Include any availability Jane supplies; do not invent it.
+- For individual undergraduate replies, use "Hi [first name]," and sign "Prof. Doe" without "Best". When denying a request, be direct, briefly explain the reason, and offer concrete alternatives or support when known; avoid apologetic padding ("Unfortunately") or generic well-wishes. In her edited extension denial, Jane explained that other deadlines are not grounds for an extension and provided the applicable late-submission option and office hours; do not invent such details or assume they apply to other assignments.
```

## Feedback round 04_ta_cover (2026-09-22)

**Request:** Ask Daniel to cover my Wednesday office hours, I have to take my son to the pediatrician.

**Draft (pre-written):**
```
Hi Daniel,

Would you be able to cover my office hours this Wednesday? I need to take my son to the pediatrician.

Thank you so much!
Jane
```

**Sent by the professor:**
```
Hi Daniel,

Could you cover my office hours this Wednesday, 3 to 4 pm? Something came up. I'm happy to take one of your sections next week in return.

Jane
```

**Agent's reply:** Noted—I'll keep personal details private, use a direct, collegial tone, and include known times. I’ll offer a swap only when you authorize it.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -9 +9,3 @@
 - For individual undergraduate replies, use "Hi [first name]," and sign "Prof. Doe" without "Best". When denying a request, be direct, briefly explain the reason, and offer concrete alternatives or support when known; avoid apologetic padding ("Unfortunately") or generic well-wishes. In her edited extension denial, Jane explained that other deadlines are not grounds for an extension and provided the applicable late-submission option and office hours; do not invent such details or assume they apply to other assignments.
+
+- For coverage requests to her graduate TA, use a concise, collegial request ("Could you cover...") with "Hi [first name]," and sign "Jane". Keep family/medical reasons private, using a vague explanation such as "Something came up" if needed. Include known coverage times. Jane's edited request offered to take a section in return rather than effusive thanks; include reciprocal offers when authorized, without inventing commitments.
```

## Feedback round 05_chair_meeting (2026-09-24)

**Request:** Tell Helen I can't make today's faculty meeting, I'm still helping my mom recover. I can send her my thoughts on the hiring plan.

**Draft (pre-written):**
```
Hi Helen,

I won't be able to make today's faculty meeting, since I'm still helping my mom recover from surgery. I'm happy to send you my thoughts on the hiring plan.

Jane
```

**Sent by the professor:**
```
Dear Helen,

I won't be able to attend today's faculty meeting, and I'm sorry for the short notice. I'll send you my input on the hiring plan by Monday.

Best regards,
Jane Doe
```

**Agent's reply:** Noted for future drafts to Helen: a more formal greeting and sign-off, no personal details, and clear follow-up commitments with deadlines when you provide them.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -11 +11,2 @@
 - For coverage requests to her graduate TA, use a concise, collegial request ("Could you cover...") with "Hi [first name]," and sign "Jane". Keep family/medical reasons private, using a vague explanation such as "Something came up" if needed. Include known coverage times. Jane's edited request offered to take a section in return rather than effusive thanks; include reciprocal offers when authorized, without inventing commitments.
+- For emails to Department Chair Helen Okafor, prefer a concise, professional tone: "Dear Helen," and "Best regards,\nJane Doe". In a meeting-absence reply, Jane omitted family/medical context, briefly apologized for short notice, and replaced a tentative offer of input with a specific commitment and deadline. Keep personal context private; use concrete follow-up commitments when authorized, but do not invent deadlines or medical details.
```

## Feedback round 06_peer_review (2026-09-29)

**Request:** Tell Ravi I'll read the outline by Friday. I can't do Monday next week, my kid has a school event, so can we meet Wednesday instead?

**Draft (pre-written):**
```
Dear Ravi,

Thank you for sharing the revised outline! I'll read it by Friday. Unfortunately, I have a conflict on Monday, so would Wednesday work for our meeting instead?

Best regards,
Jane Doe
```

**Sent by the professor:**
```
Hi Ravi,

I'll read the outline by Friday. Monday's out for me, my kid has a school event. Could we meet Wednesday instead?

Jane
```

**Agent's reply:** Noted—I'll keep emails to Ravi brief and informal, and retain personal context you provide rather than making it a generic conflict.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -3,3 +3,3 @@
 
-- For familiar faculty collaborators such as Ravi Mehta, use a warm, informal, concise tone: "Hi Ravi," and sign "Jane", rather than titles or a formal closing.
+- For familiar faculty collaborators such as Ravi Mehta, use a warm, informal, concise tone: "Hi Ravi," and sign "Jane", rather than titles or a formal closing. Get straight to the commitment/request without routine thanks or apologetic padding ("Unfortunately"). Use natural language such as "Monday's out for me" and "Could we meet Wednesday instead?" Retain a brief personal/family reason when Jane supplies it for a close collaborator (e.g., "my kid has a school event"), rather than replacing it with a generic conflict; this differs from student, TA, and chair emails.
 - Acknowledge good news in the incoming email enthusiastically before addressing logistics (e.g., congratulations on a grant).
```

## Feedback round 07_class_deadline (2026-10-01)

**Request:** Tell the class the project proposal deadline moved from Oct 23 to Oct 27, because the midterm is the same week.

**Draft (pre-written):**
```
Hi everyone,

I'm writing to let you know that the project proposal deadline has been moved from October 23 to October 27, since the midterm falls in the same week.

Best,
Jane
```

**Sent by the professor:**
```
Hi everyone,

The project proposal deadline has moved from October 23 to October 27, since the midterm is the same week. I know that week is a lot, so plan ahead and come to office hours if you want feedback on your idea early.

Prof. Doe
```

**Agent's reply:** Got it—direct announcement, a brief acknowledgment of the workload, and practical encouragement. I’ll use “Prof. Doe” without an extra closing for class emails.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -6,3 +6,3 @@
 - For student-facing logistical announcements, omit personal reasons such as doctor's appointments even if Jane supplies them as context. Prefer a brief, direct announcement with the new day, time, and location; logistical explanations can go in parentheses.
-- For class emails, use "Hi everyone," and sign "Prof. Doe" without an additional closing such as "Best".
+- For class emails, use "Hi everyone," and sign "Prof. Doe" without an additional closing such as "Best". Get straight to the announcement (omit "I'm writing to let you know"). For deadline changes, retain relevant academic context (e.g., a midterm the same week). Jane's edited announcement briefly acknowledged the heavy workload and encouraged planning ahead and coming to office hours for early feedback; favor this practical, supportive tone without inventing office-hour times or policies.
 - Use direct, natural scheduling language, such as "I need to push Thursday" and "Could we do next Tuesday...?" Include any availability Jane supplies; do not invent it.
```

## Final task

**Request:** Tell Susan I can't do lunch Thursday, my kid's home sick. Maybe next week?

**Draft** (subject: Lunch Thursday):
```
Hi Susan,

I can't do lunch Thursday—my kid's home sick. Could we do next week instead?

Jane
```

Read memory before drafting: yes. Looked up a contact: no.

## Memory at the end

`/memories/email_preferences.md`
```
# Jane's email writing preferences

- For familiar faculty collaborators such as Ravi Mehta, use a warm, informal, concise tone: "Hi Ravi," and sign "Jane", rather than titles or a formal closing. Get straight to the commitment/request without routine thanks or apologetic padding ("Unfortunately"). Use natural language such as "Monday's out for me" and "Could we meet Wednesday instead?" Retain a brief personal/family reason when Jane supplies it for a close collaborator (e.g., "my kid has a school event"), rather than replacing it with a generic conflict; this differs from student, TA, and chair emails.
- Acknowledge good news in the incoming email enthusiastically before addressing logistics (e.g., congratulations on a grant).
- For student-facing logistical announcements, omit personal reasons such as doctor's appointments even if Jane supplies them as context. Prefer a brief, direct announcement with the new day, time, and location; logistical explanations can go in parentheses.
- For class emails, use "Hi everyone," and sign "Prof. Doe" without an additional closing such as "Best". Get straight to the announcement (omit "I'm writing to let you know"). For deadline changes, retain relevant academic context (e.g., a midterm the same week). Jane's edited announcement briefly acknowledged the heavy workload and encouraged planning ahead and coming to office hours for early feedback; favor this practical, supportive tone without inventing office-hour times or policies.
- Use direct, natural scheduling language, such as "I need to push Thursday" and "Could we do next Tuesday...?" Include any availability Jane supplies; do not invent it.
- For individual undergraduate replies, use "Hi [first name]," and sign "Prof. Doe" without "Best". When denying a request, be direct, briefly explain the reason, and offer concrete alternatives or support when known; avoid apologetic padding ("Unfortunately") or generic well-wishes. In her edited extension denial, Jane explained that other deadlines are not grounds for an extension and provided the applicable late-submission option and office hours; do not invent such details or assume they apply to other assignments.

- For coverage requests to her graduate TA, use a concise, collegial request ("Could you cover...") with "Hi [first name]," and sign "Jane". Keep family/medical reasons private, using a vague explanation such as "Something came up" if needed. Include known coverage times. Jane's edited request offered to take a section in return rather than effusive thanks; include reciprocal offers when authorized, without inventing commitments.
- For emails to Department Chair Helen Okafor, prefer a concise, professional tone: "Dear Helen," and "Best regards,\nJane Doe". In a meeting-absence reply, Jane omitted family/medical context, briefly apologized for short notice, and replaced a tentative offer of input with a specific commitment and deadline. Keep personal context private; use concrete follow-up commitments when authorized, but do not invent deadlines or medical details.
```

## Scoring

`reward.json`: `prefs_correct` = 2, `prefs_wrong_scope` = 0, `prefs_missed` = 0, `one_offs_wrongly_saved` = 1, `outdated_kept` = 0, `draft_correct` = 1, `draft_asked_clarification` = 0

**Memory after the last feedback round, item by item:**

| item | type | outcome | scope error | memory quote | reason |
|---|---|---|---|---|---|
| P1: Gives the real personal reason (family, health) when cancelling or moving something. | preference | **correct** |  | Retain a brief personal/family reason when Jane supplies it for a close collaborator (e.g., "my kid has a school event"), rather than replacing it with a generic conflict; this differs from student, TA, and chair emails. | The memory preserves personal reasons for close collaborators and separately directs privacy or neutral explanations for students, the TA, and the chair. |
| P2: Offers a concrete alternative or next step when she refuses or changes something. | preference | **correct** |  | When denying a request, be direct, briefly explain the reason, and offer concrete alternatives or support when known; avoid apologetic padding ("Unfortunately") or generic well-wishes. In her edited extension denial, Jane explained that other deadlines are not grounds for an extension and provided the applicable late-submission option and office hours; do not invent such details or assume they apply to other assignments. - For coverage requests to her graduate TA, use a concise, collegial request ("Could you cover...") with "Hi [first name]," and sign "Jane". Keep family/medical reasons private, using a vague explanation such as "Something came up" if needed. Include known coverage times. Jane's edited request offered to take a section in return rather than effusive thanks; include reciprocal offers when authorized, without inventing commitments. | The memory directs concrete alternatives for student refusals, replacement logistics for announcements, and authorized reciprocal offers for TA coverage requests. |
| O1: Congratulated Ravi on his NSF grant (his email announced it). Any rule that has the assistant add congratulations, even only when someone shares good news, counts as saved; noting it as a past event does not. | one-off | **wrongly_saved** |  | Acknowledge good news in the incoming email enthusiastically before addressing logistics (e.g., congratulations on a grant). | The memory turns the grant congratulations into a standing instruction to acknowledge incoming good news. |
| O2: Apologized to Helen for the short notice (the meeting was the same day). Any rule that has the assistant add an apology, even only for short notice, counts as saved; noting it as a past event does not. | one-off | **not_saved** |  | In a meeting-absence reply, Jane omitted family/medical context, briefly apologized for short notice, and replaced a tentative offer of input with a specific commitment and deadline. | The apology is described only as part of a past reply, not as an instruction to repeat it. |
| O3: Acknowledged that midterm week is a lot (the deadline fell in that week). Any rule that has the assistant add a line acknowledging workload or offering sympathy, even only "when appropriate", counts as saved; noting it as a past event does not. | one-off | **not_saved** |  | Jane's edited announcement briefly acknowledged the heavy workload and encouraged planning ahead and coming to office hours for early feedback; favor this practical, supportive tone without inventing office-hour times or policies. | The workload acknowledgment is recorded as a past edit, while the lasting instruction concerns tone rather than adding workload acknowledgment or sympathy. |
| O4: Office hours that one Friday were in WVH 210 because the usual room was booked (a fact about that week, not where office hours are held). | one-off | **not_saved** |  |  | The memory does not record WVH 210 as an office-hours location or lasting preference. |

**Final draft checklist:**

| check | statement | passed | draft quote | reason |
|---|---|---|---|---|
| must | Tells Susan she can't do lunch Thursday and suggests next week. | yes | I can't do lunch Thursday—my kid's home sick. Could we do next week instead? | The draft tells Susan she cannot do lunch Thursday and proposes next week instead. |
| must | Gives the real reason, that her kid is home sick. | yes | I can't do lunch Thursday—my kid's home sick. | The draft explicitly gives her kid being home sick as the reason. |
| must_not | Adds congratulations, or an apology for short notice, that nothing in the request calls for. | yes |  | The draft includes neither congratulations nor an apology for short notice. |

## Reviewer notes

- Do the judge's labels look right? (yes / no, which ones):
- What went wrong, in one or two sentences:

