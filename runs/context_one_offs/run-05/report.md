# context_one_offs / full case / run-05

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

**Agent's reply:** Got it—I’ll keep future drafts to close colleagues warm and direct, acknowledge their news, and include the personal context you provide rather than reducing it to “a conflict.”

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -1 +1,9 @@
-(memory is empty)
+=== /memories/email_preferences.md ===
+# Jane's email-writing preferences
+
+Based on her edited email to Ravi Mehta (faculty peer and frequent collaborator):
+- Use a warm, informal peer tone: “Hi Ravi,” and sign off simply “Jane,” rather than formal titles or “Best regards, Jane Doe.”
+- Acknowledge and celebrate good news in the message being answered.
+- Keep wording concise and direct (e.g., “I need to push Thursday”) rather than stiff or apologetic boilerplate.
+- Include personal context Jane explicitly provides for the email rather than replacing it with a vague “conflict.”
+- State scheduling proposals clearly; include specific availability when Jane supplies it, without inventing times.
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

**Agent's reply:** Noted—for class announcements, I’ll keep it brief, leave out personal medical details, and sign “Prof. Doe.”

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -9 +9,8 @@
 - State scheduling proposals clearly; include specific availability when Jane supplies it, without inventing times.
+
+
+Based on her edited announcement to CS 4100 students:
+- Keep class announcements brief and direct: “Hi everyone,” followed by the logistical update, without extra explanation or a closing pleasantry.
+- Sign student-facing announcements “Prof. Doe” rather than “Jane.”
+- Omit personal medical context in class announcements, even when supplied as background; her edited office-hours announcement removed the doctor's appointment. The personal-context preference above applies to faculty-peer correspondence, not automatically to students.
+- Combine the new day, time, and location in one sentence; a short parenthetical can explain a room change.
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

**Agent's reply:** Noted. For student replies, I’ll be direct, briefly explain the decision, include practical options when known, and sign “Prof. Doe.”

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -16 +16,6 @@
 - Combine the new day, time, and location in one sentence; a short parenthetical can explain a room change.
+
+Based on her edited extension denial to Jordan Lee (undergraduate student):
+- For individual student replies, use “Hi [first name],” and sign “Prof. Doe,” not “Jane.”
+- Deny requests directly with a brief reason; avoid apologetic padding such as “Unfortunately” and generic encouragement such as “Good luck with your deadlines!”
+- Pair a firm denial with practical next steps, such as applicable late-submission options and office-hours help, when those details are known. Do not invent policies or office-hours schedules.
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

**Agent's reply:** Noted—I'll keep TA requests concise and collegial, leave out family or medical details, and include specific times when provided. I'll offer a swap only when you've authorized one.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -21 +21,7 @@
 - Pair a firm denial with practical next steps, such as applicable late-submission options and office-hours help, when those details are known. Do not invent policies or office-hours schedules.
+
+Based on her edited coverage request to Daniel Kim (PhD student and course TA):
+- Use a concise, collegial request: “Hi Daniel,” “Could you cover…?” and sign simply “Jane.” Avoid effusive thanks.
+- Keep family/medical reasons private in TA correspondence; use a brief “Something came up” rather than mentioning her child or pediatrician. Personal context shared with the assistant is not automatically for inclusion.
+- State the specific coverage window when known; do not invent times.
+- She offered to take one of the TA's sections the following week in return; favor reciprocal framing for coverage requests when authorized, without inventing commitments.
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

**Agent's reply:** Noted—I'll use a more formal tone with Helen, leave out personal family details, and include a brief apology for short notice. I'll make follow-up commitments specific when you've authorized them.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -27 +27,8 @@
 - She offered to take one of the TA's sections the following week in return; favor reciprocal framing for coverage requests when authorized, without inventing commitments.
+
+
+Based on her edited reply to Helen Okafor (department chair):
+- Use a more formal tone for the chair: “Dear Helen,” and “Best regards,\nJane Doe.” This differs from her informal collaborator correspondence.
+- Keep family/medical context private in chair correspondence; her revision omitted the reason for missing the meeting, even though provided in the request. Never add medical details not supplied.
+- For short-notice meeting absences, state inability to attend directly and include a brief apology for the short notice.
+- Prefer a clear follow-up commitment over a tentative offer when authorized; her revision used “I'll send you my input on the hiring plan by Monday.” Do not invent deadlines or commitments for future drafts.
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

**Agent's reply:** Got it—short, informal, and direct with Ravi, keeping the personal context you provide and signing simply “Jane.”

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -6,3 +6,3 @@
 - Acknowledge and celebrate good news in the message being answered.
-- Keep wording concise and direct (e.g., “I need to push Thursday”) rather than stiff or apologetic boilerplate.
+- Keep wording concise and direct (e.g., “I need to push Thursday” or “Monday's out for me”) rather than stiff or apologetic boilerplate. In her outline reply she omitted “Thank you for sharing” and “Unfortunately,” stated “I'll read the outline by Friday,” and asked “Could we meet Wednesday instead?”
 - Include personal context Jane explicitly provides for the email rather than replacing it with a vague “conflict.”
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

**Agent's reply:** Noted for future class announcements: lead directly with the update, acknowledge students’ workload with practical guidance, and sign “Prof. Doe.”

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -12,3 +12,4 @@
 Based on her edited announcement to CS 4100 students:
-- Keep class announcements brief and direct: “Hi everyone,” followed by the logistical update, without extra explanation or a closing pleasantry.
+- Keep class announcements brief and direct: “Hi everyone,” followed immediately by the logistical update; omit meta-introductions such as “I'm writing to let you know” and closing pleasantries.
+- A brief, warm acknowledgment of student workload and practical guidance can follow the update. In her proposal-deadline announcement she added: “I know that week is a lot, so plan ahead and come to office hours if you want feedback on your idea early.” Avoid inventing office-hours schedules.
 - Sign student-facing announcements “Prof. Doe” rather than “Jane.”
```

## Final task

**Request:** Tell Susan I can't do lunch Thursday, my kid's home sick. Maybe next week?

**Draft** (subject: Lunch Thursday):
```
Hi Susan,

I can't do lunch Thursday—my kid's home sick. Could we try next week instead?

Jane
```

Read memory before drafting: yes. Looked up a contact: no.

## Memory at the end

`/memories/email_preferences.md`
```
# Jane's email-writing preferences

Based on her edited email to Ravi Mehta (faculty peer and frequent collaborator):
- Use a warm, informal peer tone: “Hi Ravi,” and sign off simply “Jane,” rather than formal titles or “Best regards, Jane Doe.”
- Acknowledge and celebrate good news in the message being answered.
- Keep wording concise and direct (e.g., “I need to push Thursday” or “Monday's out for me”) rather than stiff or apologetic boilerplate. In her outline reply she omitted “Thank you for sharing” and “Unfortunately,” stated “I'll read the outline by Friday,” and asked “Could we meet Wednesday instead?”
- Include personal context Jane explicitly provides for the email rather than replacing it with a vague “conflict.”
- State scheduling proposals clearly; include specific availability when Jane supplies it, without inventing times.


Based on her edited announcement to CS 4100 students:
- Keep class announcements brief and direct: “Hi everyone,” followed immediately by the logistical update; omit meta-introductions such as “I'm writing to let you know” and closing pleasantries.
- A brief, warm acknowledgment of student workload and practical guidance can follow the update. In her proposal-deadline announcement she added: “I know that week is a lot, so plan ahead and come to office hours if you want feedback on your idea early.” Avoid inventing office-hours schedules.
- Sign student-facing announcements “Prof. Doe” rather than “Jane.”
- Omit personal medical context in class announcements, even when supplied as background; her edited office-hours announcement removed the doctor's appointment. The personal-context preference above applies to faculty-peer correspondence, not automatically to students.
- Combine the new day, time, and location in one sentence; a short parenthetical can explain a room change.

Based on her edited extension denial to Jordan Lee (undergraduate student):
- For individual student replies, use “Hi [first name],” and sign “Prof. Doe,” not “Jane.”
- Deny requests directly with a brief reason; avoid apologetic padding such as “Unfortunately” and generic encouragement such as “Good luck with your deadlines!”
- Pair a firm denial with practical next steps, such as applicable late-submission options and office-hours help, when those details are known. Do not invent policies or office-hours schedules.

Based on her edited coverage request to Daniel Kim (PhD student and course TA):
- Use a concise, collegial request: “Hi Daniel,” “Could you cover…?” and sign simply “Jane.” Avoid effusive thanks.
- Keep family/medical reasons private in TA correspondence; use a brief “Something came up” rather than mentioning her child or pediatrician. Personal context shared with the assistant is not automatically for inclusion.
- State the specific coverage window when known; do not invent times.
- She offered to take one of the TA's sections the following week in return; favor reciprocal framing for coverage requests when authorized, without inventing commitments.


Based on her edited reply to Helen Okafor (department chair):
- Use a more formal tone for the chair: “Dear Helen,” and “Best regards,\nJane Doe.” This differs from her informal collaborator correspondence.
- Keep family/medical context private in chair correspondence; her revision omitted the reason for missing the meeting, even though provided in the request. Never add medical details not supplied.
- For short-notice meeting absences, state inability to attend directly and include a brief apology for the short notice.
- Prefer a clear follow-up commitment over a tentative offer when authorized; her revision used “I'll send you my input on the hiring plan by Monday.” Do not invent deadlines or commitments for future drafts.
```

## Scoring

`reward.json`: `prefs_correct` = 2, `prefs_wrong_scope` = 0, `prefs_missed` = 0, `one_offs_wrongly_saved` = 3, `outdated_kept` = 0, `draft_correct` = 1, `draft_asked_clarification` = 0

**Memory after the last feedback round, item by item:**

| item | type | outcome | scope error | memory quote | reason |
|---|---|---|---|---|---|
| P1: Gives the real personal reason (family, health) when cancelling or moving something. | preference | **correct** |  | - Include personal context Jane explicitly provides for the email rather than replacing it with a vague “conflict.” | The memory applies this rule to faculty-peer correspondence and separately directs that personal medical or family context be omitted for students, the TA, and the chair. |
| P2: Offers a concrete alternative or next step when she refuses or changes something. | preference | **correct** |  | - Pair a firm denial with practical next steps, such as applicable late-submission options and office-hours help, when those details are known. Do not invent policies or office-hours schedules. | The memory prescribes practical next steps for student denials, practical guidance in announcements, and authorized reciprocal coverage offers for the TA. |
| O1: Congratulated Ravi on his NSF grant (his email announced it). Any rule that has the assistant add congratulations, even only when someone shares good news, counts as saved; noting it as a past event does not. | one-off | **wrongly_saved** |  | - Acknowledge and celebrate good news in the message being answered. | The memory turns the one-time congratulations into a repeatable rule for replies to good news. |
| O2: Apologized to Helen for the short notice (the meeting was the same day). Any rule that has the assistant add an apology, even only for short notice, counts as saved; noting it as a past event does not. | one-off | **wrongly_saved** |  | - For short-notice meeting absences, state inability to attend directly and include a brief apology for the short notice. | The memory explicitly makes the short-notice apology a lasting instruction. |
| O3: Acknowledged that midterm week is a lot (the deadline fell in that week). Any rule that has the assistant add a line acknowledging workload or offering sympathy, even only "when appropriate", counts as saved; noting it as a past event does not. | one-off | **wrongly_saved** |  | - A brief, warm acknowledgment of student workload and practical guidance can follow the update. | The memory generalizes the workload acknowledgment into guidance for future class announcements. |
| O4: Office hours that one Friday were in WVH 210 because the usual room was booked (a fact about that week, not where office hours are held). | one-off | **not_saved** |  |  | The memory does not record WVH 210 as the regular office-hours location or otherwise instruct the assistant to reuse that week's room. |

**Final draft checklist:**

| check | statement | passed | draft quote | reason |
|---|---|---|---|---|
| must | Tells Susan she can't do lunch Thursday and suggests next week. | yes | I can't do lunch Thursday—my kid's home sick. Could we try next week instead? | The draft tells Susan she cannot do lunch Thursday and suggests next week instead. |
| must | Gives the real reason, that her kid is home sick. | yes | I can't do lunch Thursday—my kid's home sick. | The draft explicitly gives her kid being home sick as the reason. |
| must_not | Adds congratulations, or an apology for short notice, that nothing in the request calls for. | yes |  | The draft includes neither congratulations nor an apology for short notice. |

## Reviewer notes

- Do the judge's labels look right? (yes / no, which ones):
- What went wrong, in one or two sentences:

