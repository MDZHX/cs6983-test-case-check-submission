# context_one_offs / full case / run-02

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

**Agent's reply:** Got it—I’ll keep future drafts warmer and more direct with close colleagues, acknowledge their good news, and preserve the personal context you provide.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -1 +1,8 @@
-(memory is empty)
+=== /memories/email_preferences.md ===
+# Jane's email preferences
+
+- With familiar faculty collaborators such as Ravi Mehta, use a warm, informal, concise voice: “Hi Ravi,” and sign simply “Jane,” rather than titles, formal apologies, or “Best regards, Jane Doe.”
+- Acknowledge good news in the message being answered with genuine enthusiasm (e.g., congratulations on a grant) before addressing scheduling.
+- Preserve personal context Jane explicitly provides for inclusion rather than replacing it with a vague “conflict.” Keep the explanation direct and natural.
+- Use straightforward scheduling language (e.g., “I need to push Thursday” and “Could we do next Tuesday...?”).
+- In one edited scheduling reply, Jane added a specific availability window; include such windows when provided, but do not assume that window is a standing preference.
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

**Agent's reply:** Noted—for class announcements, I’ll keep it brief, leave out personal reasons, and sign “Prof. Doe.”

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -5,4 +5,5 @@
 - Acknowledge good news in the message being answered with genuine enthusiasm (e.g., congratulations on a grant) before addressing scheduling.
-- Preserve personal context Jane explicitly provides for inclusion rather than replacing it with a vague “conflict.” Keep the explanation direct and natural.
+- Preserve personal context Jane explicitly provides for inclusion in personal/collaborator messages; do not assume background context belongs in every email. In a class announcement edit, Jane omitted her doctor's appointment entirely and stated only the schedule change.
 - Use straightforward scheduling language (e.g., “I need to push Thursday” and “Could we do next Tuesday...?”).
 - In one edited scheduling reply, Jane added a specific availability window; include such windows when provided, but do not assume that window is a standing preference.
+- For class announcements, prefer a brief, direct message with “Hi everyone,” and the signature “Prof. Doe” (no “Best,”). Put scheduling and location details in a compact paragraph; a short parenthetical can explain a room change.
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

**Agent's reply:** Noted—future student replies will be direct, briefly explain the decision, offer relevant options when known, and use “Prof. Doe” as the sign-off.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -9 +9,4 @@
 - For class announcements, prefer a brief, direct message with “Hi everyone,” and the signature “Prof. Doe” (no “Best,”). Put scheduling and location details in a compact paragraph; a short parenthetical can explain a room change.
+
+- In individual student replies, prefer a direct, firm but helpful tone: state the decision and brief reason without softening it with “Unfortunately” or generic encouragement such as “Good luck with your deadlines!” Sign “Prof. Doe” without a closing like “Best.”
+- When denying a student request, include applicable alternatives and concrete support when known. In an edited Assignment 2 extension denial, Jane explained that other deadlines aren't grounds for an extension, mentioned submission up to 24 hours late for a 10% penalty, and invited Jordan to Friday office hours. Treat those specifics as context for that reply, not universal course policy or a standing office-hours schedule.
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

**Agent's reply:** Noted—I'll keep TA coverage requests brief and direct, leave personal reasons vague, and include specific times when known. I’ll offer a swap only when you’ve authorized it.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -12 +12,3 @@
 - When denying a student request, include applicable alternatives and concrete support when known. In an edited Assignment 2 extension denial, Jane explained that other deadlines aren't grounds for an extension, mentioned submission up to 24 hours late for a 10% penalty, and invited Jordan to Friday office hours. Treat those specifics as context for that reply, not universal course policy or a standing office-hours schedule.
+
+- For coverage requests to her TA, prefer concise, direct wording (“Could you cover...?”), “Hi [first name],” and signature “Jane,” without effusive thanks. In an edited request to Daniel, Jane replaced the personal/family medical explanation with “Something came up,” specified the office-hours time, and offered to cover one of his sections in return. Keep personal reasons vague in this context; include known scheduling details, and offer reciprocity when Jane authorizes it rather than inventing a commitment. The specific time and swap were for that request, not standing arrangements.
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

**Agent's reply:** Noted. For emails to Helen, I’ll use a more formal greeting and sign-off, leave out personal medical details, and keep follow-up commitments clear without inventing deadlines.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -14 +14,3 @@
 - For coverage requests to her TA, prefer concise, direct wording (“Could you cover...?”), “Hi [first name],” and signature “Jane,” without effusive thanks. In an edited request to Daniel, Jane replaced the personal/family medical explanation with “Something came up,” specified the office-hours time, and offered to cover one of his sections in return. Keep personal reasons vague in this context; include known scheduling details, and offer reciprocity when Jane authorizes it rather than inventing a commitment. The specific time and swap were for that request, not standing arrangements.
+
+- For messages to Department Chair Helen Okafor, favor a concise, professional tone: “Dear Helen,” and “Best regards,\nJane Doe.” In an edited faculty-meeting absence reply, Jane omitted family medical context, added a brief apology for short notice, and replaced a tentative offer of hiring-plan thoughts with a concrete commitment and deadline. Keep personal reasons private in this context; use specific follow-up commitments when authorized, without inventing deadlines. The Monday deadline was specific to that email.
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

**Agent's reply:** Noted—I'll keep replies to Ravi brief and conversational, skip unnecessary thanks, and preserve personal context you explicitly include.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -4,2 +4,3 @@
 - With familiar faculty collaborators such as Ravi Mehta, use a warm, informal, concise voice: “Hi Ravi,” and sign simply “Jane,” rather than titles, formal apologies, or “Best regards, Jane Doe.”
+- In a revised outline/scheduling reply to Ravi, Jane went straight to the commitment without thanking him for sharing the outline, used conversational wording (“Monday's out for me”), and kept the explicitly supplied reason (“my kid has a school event”). Avoid generic acknowledgments and formal conflict language in routine replies to close collaborators.
 - Acknowledge good news in the message being answered with genuine enthusiasm (e.g., congratulations on a grant) before addressing scheduling.
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

**Agent's reply:** Noted—I'll keep class announcements direct, sign “Prof. Doe,” and include practical, supportive guidance when relevant.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -9,3 +9,3 @@
 - In one edited scheduling reply, Jane added a specific availability window; include such windows when provided, but do not assume that window is a standing preference.
-- For class announcements, prefer a brief, direct message with “Hi everyone,” and the signature “Prof. Doe” (no “Best,”). Put scheduling and location details in a compact paragraph; a short parenthetical can explain a room change.
+- For class announcements, prefer a brief, direct message with “Hi everyone,” and the signature “Prof. Doe” (no “Best,”). Put scheduling and location details in a compact paragraph; a short parenthetical can explain a room change. State changes directly rather than using “I'm writing to let you know.” In a project-deadline announcement edit, Jane acknowledged the heavy workload conversationally (“I know that week is a lot”) and encouraged planning ahead and visiting office hours for early feedback; favor concrete, supportive guidance when relevant, without inventing office-hours times.
 
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
# Jane's email preferences

- With familiar faculty collaborators such as Ravi Mehta, use a warm, informal, concise voice: “Hi Ravi,” and sign simply “Jane,” rather than titles, formal apologies, or “Best regards, Jane Doe.”
- In a revised outline/scheduling reply to Ravi, Jane went straight to the commitment without thanking him for sharing the outline, used conversational wording (“Monday's out for me”), and kept the explicitly supplied reason (“my kid has a school event”). Avoid generic acknowledgments and formal conflict language in routine replies to close collaborators.
- Acknowledge good news in the message being answered with genuine enthusiasm (e.g., congratulations on a grant) before addressing scheduling.
- Preserve personal context Jane explicitly provides for inclusion in personal/collaborator messages; do not assume background context belongs in every email. In a class announcement edit, Jane omitted her doctor's appointment entirely and stated only the schedule change.
- Use straightforward scheduling language (e.g., “I need to push Thursday” and “Could we do next Tuesday...?”).
- In one edited scheduling reply, Jane added a specific availability window; include such windows when provided, but do not assume that window is a standing preference.
- For class announcements, prefer a brief, direct message with “Hi everyone,” and the signature “Prof. Doe” (no “Best,”). Put scheduling and location details in a compact paragraph; a short parenthetical can explain a room change. State changes directly rather than using “I'm writing to let you know.” In a project-deadline announcement edit, Jane acknowledged the heavy workload conversationally (“I know that week is a lot”) and encouraged planning ahead and visiting office hours for early feedback; favor concrete, supportive guidance when relevant, without inventing office-hours times.

- In individual student replies, prefer a direct, firm but helpful tone: state the decision and brief reason without softening it with “Unfortunately” or generic encouragement such as “Good luck with your deadlines!” Sign “Prof. Doe” without a closing like “Best.”
- When denying a student request, include applicable alternatives and concrete support when known. In an edited Assignment 2 extension denial, Jane explained that other deadlines aren't grounds for an extension, mentioned submission up to 24 hours late for a 10% penalty, and invited Jordan to Friday office hours. Treat those specifics as context for that reply, not universal course policy or a standing office-hours schedule.

- For coverage requests to her TA, prefer concise, direct wording (“Could you cover...?”), “Hi [first name],” and signature “Jane,” without effusive thanks. In an edited request to Daniel, Jane replaced the personal/family medical explanation with “Something came up,” specified the office-hours time, and offered to cover one of his sections in return. Keep personal reasons vague in this context; include known scheduling details, and offer reciprocity when Jane authorizes it rather than inventing a commitment. The specific time and swap were for that request, not standing arrangements.

- For messages to Department Chair Helen Okafor, favor a concise, professional tone: “Dear Helen,” and “Best regards,\nJane Doe.” In an edited faculty-meeting absence reply, Jane omitted family medical context, added a brief apology for short notice, and replaced a tentative offer of hiring-plan thoughts with a concrete commitment and deadline. Keep personal reasons private in this context; use specific follow-up commitments when authorized, without inventing deadlines. The Monday deadline was specific to that email.
```

## Scoring

`reward.json`: `prefs_correct` = 2, `prefs_wrong_scope` = 0, `prefs_missed` = 0, `one_offs_wrongly_saved` = 1, `outdated_kept` = 0, `draft_correct` = 1, `draft_asked_clarification` = 0

**Memory after the last feedback round, item by item:**

| item | type | outcome | scope error | memory quote | reason |
|---|---|---|---|---|---|
| P1: Gives the real personal reason (family, health) when cancelling or moving something. | preference | **correct** |  | Preserve personal context Jane explicitly provides for inclusion in personal/collaborator messages; do not assume background context belongs in every email. In a class announcement edit, Jane omitted her doctor's appointment entirely and stated only the schedule change. | The memory preserves supplied personal reasons for collaborator messages while separately directing neutral or private handling for students, the TA, and the chair. |
| P2: Offers a concrete alternative or next step when she refuses or changes something. | preference | **correct** |  | When denying a student request, include applicable alternatives and concrete support when known. | The memory calls for alternatives and support for students, reinforces concrete guidance in class announcements, and includes authorized reciprocity for TA coverage requests. |
| O1: Congratulated Ravi on his NSF grant (his email announced it). Any rule that has the assistant add congratulations, even only when someone shares good news, counts as saved; noting it as a past event does not. | one-off | **wrongly_saved** |  | Acknowledge good news in the message being answered with genuine enthusiasm (e.g., congratulations on a grant) before addressing scheduling. | The memory turns the grant congratulations into a lasting rule to acknowledge good news enthusiastically. |
| O2: Apologized to Helen for the short notice (the meeting was the same day). Any rule that has the assistant add an apology, even only for short notice, counts as saved; noting it as a past event does not. | one-off | **not_saved** |  | In an edited faculty-meeting absence reply, Jane omitted family medical context, added a brief apology for short notice, and replaced a tentative offer of hiring-plan thoughts with a concrete commitment and deadline. | The apology is recorded only as a past edit, not as an instruction to repeat it. |
| O3: Acknowledged that midterm week is a lot (the deadline fell in that week). Any rule that has the assistant add a line acknowledging workload or offering sympathy, even only "when appropriate", counts as saved; noting it as a past event does not. | one-off | **not_saved** |  | In a project-deadline announcement edit, Jane acknowledged the heavy workload conversationally (“I know that week is a lot”) and encouraged planning ahead and visiting office hours for early feedback; favor concrete, supportive guidance when relevant, without inventing office-hours times. | The workload acknowledgment is a past example, while the lasting instruction concerns concrete guidance rather than adding sympathy or workload acknowledgments. |
| O4: Office hours that one Friday were in WVH 210 because the usual room was booked (a fact about that week, not where office hours are held). | one-off | **not_saved** |  |  | The memory does not record WVH 210 as a standing office-hours location. |

**Final draft checklist:**

| check | statement | passed | draft quote | reason |
|---|---|---|---|---|
| must | Tells Susan she can't do lunch Thursday and suggests next week. | yes | I can't do lunch Thursday—my kid's home sick. Could we do next week instead? | The draft tells Susan she cannot do lunch Thursday and proposes next week. |
| must | Gives the real reason, that her kid is home sick. | yes | I can't do lunch Thursday—my kid's home sick. | The draft explicitly gives her kid being home sick as the reason. |
| must_not | Adds congratulations, or an apology for short notice, that nothing in the request calls for. | yes |  | The draft includes neither congratulations nor an apology for short notice. |

## Reviewer notes

- Do the judge's labels look right? (yes / no, which ones):
- What went wrong, in one or two sentences:

