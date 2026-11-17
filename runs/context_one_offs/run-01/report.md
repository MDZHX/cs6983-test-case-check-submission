# context_one_offs / full case / run-01

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

**Agent's reply:** Got it—I’ll keep future drafts warmer and more direct with Ravi, acknowledge his news, and include the personal context you provide rather than making it vague.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -1 +1,8 @@
-(memory is empty)
+=== /memories/email_preferences.md ===
+# Jane's email-writing preferences
+
+- With Ravi Mehta (frequent faculty collaborator), use a warm, informal peer tone: “Hi Ravi,” and sign “Jane,” not formal titles or “Best regards, Jane Doe.”
+- Acknowledge and celebrate good news in the message being answered before moving to scheduling or other business.
+- Keep messages short and direct, with natural contractions and plain wording (e.g., “I need to push Thursday”).
+- When Jane supplies a personal reason for a scheduling change, include it naturally rather than replacing it with a vague “conflict.”
+- Offer a concrete rescheduling option; include an availability window when Jane supplies one. Do not infer that a one-time window is recurring availability.
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

**Agent's reply:** Noted—for class announcements, I’ll keep it brief, omit personal appointment details, and sign “Prof. Doe.”

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -6,3 +6,4 @@
 - Keep messages short and direct, with natural contractions and plain wording (e.g., “I need to push Thursday”).
-- When Jane supplies a personal reason for a scheduling change, include it naturally rather than replacing it with a vague “conflict.”
+- Tailor personal scheduling reasons to the audience: in class announcements, omit personal details such as a doctor's appointment and simply state the change. Jane supplying a reason does not necessarily mean she wants it included.
 - Offer a concrete rescheduling option; include an availability window when Jane supplies one. Do not infer that a one-time window is recurring availability.
+- For class announcements, use “Hi everyone,” and sign “Prof. Doe” without an added closing such as “Best.” Keep schedule changes compact; include the new day, time, and room, with a brief parenthetical room explanation if relevant.
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

**Agent's reply:** Noted for future drafts: direct refusal with a brief reason, concrete alternatives when confirmed, and “Prof. Doe” as the sign-off for student emails.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -9 +9,4 @@
 - For class announcements, use “Hi everyone,” and sign “Prof. Doe” without an added closing such as “Best.” Keep schedule changes compact; include the new day, time, and room, with a brief parenthetical room explanation if relevant.
+
+- For individual undergraduate emails, use “Hi [first name],” and sign “Prof. Doe” without an added closing.
+- When denying a student request, be direct and briefly explain the grounds rather than adding “Unfortunately” or generic encouragement. Where confirmed, offer concrete alternatives such as the late-submission option or office hours; do not invent policies or assume one instance establishes recurring availability.
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

**Agent's reply:** Noted—I'll keep future TA coverage requests brief, leave out personal details, and include the specific time when known.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -12 +12,2 @@
 - When denying a student request, be direct and briefly explain the grounds rather than adding “Unfortunately” or generic encouragement. Where confirmed, offer concrete alternatives such as the late-submission option or office hours; do not invent policies or assume one instance establishes recurring availability.
+- For coverage requests to her PhD TA, use a concise, collegial request (“Could you cover…”), “Hi [first name],” and sign “Jane” without effusive thanks. Keep personal/family medical reasons private (e.g., “Something came up”), even when Jane supplies them as background. Include the specific coverage time when known; do not invent it. Jane's edited example offered to take one of the TA's sections the following week in return; consider reciprocity when appropriate, without inventing commitments.
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

**Agent's reply:** Noted for future drafts to Helen: a more formal greeting and closing, no family medical details, and a clear follow-up commitment when you’ve provided one.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -13 +13,2 @@
 - For coverage requests to her PhD TA, use a concise, collegial request (“Could you cover…”), “Hi [first name],” and sign “Jane” without effusive thanks. Keep personal/family medical reasons private (e.g., “Something came up”), even when Jane supplies them as background. Include the specific coverage time when known; do not invent it. Jane's edited example offered to take one of the TA's sections the following week in return; consider reciprocity when appropriate, without inventing commitments.
+- For Department Chair Helen Okafor, use a concise, professional tone: “Dear Helen,” and close “Best regards,” followed by “Jane Doe.” In a meeting-absence reply, Jane omitted the family medical reason, briefly apologized for short notice, and replaced a tentative offer with a concrete follow-up commitment and deadline. Keep family medical details private; use deadlines only when supplied or confirmed, not invented.
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

**Agent's reply:** Noted—short and informal with Ravi, without extra thanks or apologies, and keeping the school-event reason.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -14 +14,2 @@
 - For Department Chair Helen Okafor, use a concise, professional tone: “Dear Helen,” and close “Best regards,” followed by “Jane Doe.” In a meeting-absence reply, Jane omitted the family medical reason, briefly apologized for short notice, and replaced a tentative offer with a concrete follow-up commitment and deadline. Keep family medical details private; use deadlines only when supplied or confirmed, not invented.
+- In routine replies to Ravi, skip generic thanks, enthusiasm, and apologetic padding; go straight to the commitment and scheduling request. Jane's edited outline reply retained the supplied nonmedical family reason (“my kid has a school event”) rather than a vague “conflict”; such details can be appropriate with this close collaborator, unlike private medical details or class announcements.
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

**Agent's reply:** Noted for future class announcements: lead directly with the change, acknowledge the workload, offer practical guidance, and sign “Prof. Doe” without a closing.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -15 +15,2 @@
 - In routine replies to Ravi, skip generic thanks, enthusiasm, and apologetic padding; go straight to the commitment and scheduling request. Jane's edited outline reply retained the supplied nonmedical family reason (“my kid has a school event”) rather than a vague “conflict”; such details can be appropriate with this close collaborator, unlike private medical details or class announcements.
+- In class deadline announcements, state the change directly (skip “I'm writing to let you know”). A brief academic reason such as a same-week midterm is appropriate. Jane's edited example paired acknowledgment of workload (“I know that week is a lot”) with practical encouragement to plan ahead and seek early idea feedback at office hours; use this supportive, concrete tone when relevant without inventing office-hour times.
```

## Final task

**Request:** Tell Susan I can't do lunch Thursday, my kid's home sick. Maybe next week?

**Draft** (subject: Lunch Thursday):
```
Hi Susan,

I can't make lunch Thursday after all. Could we do next week instead?

Jane
```

Read memory before drafting: yes. Looked up a contact: no.

## Memory at the end

`/memories/email_preferences.md`
```
# Jane's email-writing preferences

- With Ravi Mehta (frequent faculty collaborator), use a warm, informal peer tone: “Hi Ravi,” and sign “Jane,” not formal titles or “Best regards, Jane Doe.”
- Acknowledge and celebrate good news in the message being answered before moving to scheduling or other business.
- Keep messages short and direct, with natural contractions and plain wording (e.g., “I need to push Thursday”).
- Tailor personal scheduling reasons to the audience: in class announcements, omit personal details such as a doctor's appointment and simply state the change. Jane supplying a reason does not necessarily mean she wants it included.
- Offer a concrete rescheduling option; include an availability window when Jane supplies one. Do not infer that a one-time window is recurring availability.
- For class announcements, use “Hi everyone,” and sign “Prof. Doe” without an added closing such as “Best.” Keep schedule changes compact; include the new day, time, and room, with a brief parenthetical room explanation if relevant.

- For individual undergraduate emails, use “Hi [first name],” and sign “Prof. Doe” without an added closing.
- When denying a student request, be direct and briefly explain the grounds rather than adding “Unfortunately” or generic encouragement. Where confirmed, offer concrete alternatives such as the late-submission option or office hours; do not invent policies or assume one instance establishes recurring availability.
- For coverage requests to her PhD TA, use a concise, collegial request (“Could you cover…”), “Hi [first name],” and sign “Jane” without effusive thanks. Keep personal/family medical reasons private (e.g., “Something came up”), even when Jane supplies them as background. Include the specific coverage time when known; do not invent it. Jane's edited example offered to take one of the TA's sections the following week in return; consider reciprocity when appropriate, without inventing commitments.
- For Department Chair Helen Okafor, use a concise, professional tone: “Dear Helen,” and close “Best regards,” followed by “Jane Doe.” In a meeting-absence reply, Jane omitted the family medical reason, briefly apologized for short notice, and replaced a tentative offer with a concrete follow-up commitment and deadline. Keep family medical details private; use deadlines only when supplied or confirmed, not invented.
- In routine replies to Ravi, skip generic thanks, enthusiasm, and apologetic padding; go straight to the commitment and scheduling request. Jane's edited outline reply retained the supplied nonmedical family reason (“my kid has a school event”) rather than a vague “conflict”; such details can be appropriate with this close collaborator, unlike private medical details or class announcements.
- In class deadline announcements, state the change directly (skip “I'm writing to let you know”). A brief academic reason such as a same-week midterm is appropriate. Jane's edited example paired acknowledgment of workload (“I know that week is a lot”) with practical encouragement to plan ahead and seek early idea feedback at office hours; use this supportive, concrete tone when relevant without inventing office-hour times.
```

## Scoring

`reward.json`: `prefs_correct` = 0, `prefs_wrong_scope` = 2, `prefs_missed` = 0, `one_offs_wrongly_saved` = 2, `outdated_kept` = 0, `draft_correct` = 0, `draft_asked_clarification` = 0

**Memory after the last feedback round, item by item:**

| item | type | outcome | scope error | memory quote | reason |
|---|---|---|---|---|---|
| P1: Gives the real personal reason (family, health) when cancelling or moving something. | preference | **wrong_scope** | too_narrow | Jane's edited outline reply retained the supplied nonmedical family reason (“my kid has a school event”) rather than a vague “conflict”; such details can be appropriate with this close collaborator, unlike private medical details or class announcements. | The memory permits real nonmedical family reasons with Ravi but excludes medical details, narrowing the rule that covers both family and health reasons with familiar colleagues. |
| P2: Offers a concrete alternative or next step when she refuses or changes something. | preference | **wrong_scope** | too_broad | Offer a concrete rescheduling option; include an availability window when Jane supplies one. | The memory makes concrete rescheduling alternatives a general rule rather than limiting that preference to students and her TA. |
| O1: Congratulated Ravi on his NSF grant (his email announced it). Any rule that has the assistant add congratulations, even only when someone shares good news, counts as saved; noting it as a past event does not. | one-off | **wrongly_saved** |  | Acknowledge and celebrate good news in the message being answered before moving to scheduling or other business. | The memory turns the one-time congratulations into a standing instruction to celebrate incoming good news. |
| O2: Apologized to Helen for the short notice (the meeting was the same day). Any rule that has the assistant add an apology, even only for short notice, counts as saved; noting it as a past event does not. | one-off | **not_saved** |  | In a meeting-absence reply, Jane omitted the family medical reason, briefly apologized for short notice, and replaced a tentative offer with a concrete follow-up commitment and deadline. | The apology is recorded as a past edit, not as an instruction to apologize in future messages. |
| O3: Acknowledged that midterm week is a lot (the deadline fell in that week). Any rule that has the assistant add a line acknowledging workload or offering sympathy, even only "when appropriate", counts as saved; noting it as a past event does not. | one-off | **wrongly_saved** |  | Jane's edited example paired acknowledgment of workload (“I know that week is a lot”) with practical encouragement to plan ahead and seek early idea feedback at office hours; use this supportive, concrete tone when relevant without inventing office-hour times. | The instruction to reuse this supportive tone when relevant generalizes the workload acknowledgment beyond the original email. |
| O4: Office hours that one Friday were in WVH 210 because the usual room was booked (a fact about that week, not where office hours are held). | one-off | **not_saved** |  |  | The memory does not record WVH 210 as a recurring office-hours location. |

**Final draft checklist:**

| check | statement | passed | draft quote | reason |
|---|---|---|---|---|
| must | Tells Susan she can't do lunch Thursday and suggests next week. | yes | I can't make lunch Thursday after all. Could we do next week instead? | The draft tells Susan she cannot make lunch Thursday and suggests next week instead. |
| must | Gives the real reason, that her kid is home sick. | **no** |  | The draft gives no reason for canceling and does not mention her kid being home sick. |
| must_not | Adds congratulations, or an apology for short notice, that nothing in the request calls for. | yes |  | The draft includes neither congratulations nor an apology for short notice. |

## Reviewer notes

- Do the judge's labels look right? (yes / no, which ones):
- What went wrong, in one or two sentences:

