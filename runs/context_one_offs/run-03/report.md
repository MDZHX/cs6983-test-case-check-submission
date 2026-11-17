# context_one_offs / full case / run-03

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

**Agent's reply:** Got it—I’ll keep future drafts warmer and more direct, acknowledge good news, and retain the personal context you provide. For familiar colleagues, I’ll use first names and sign simply “Jane.”

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -1 +1,8 @@
-(memory is empty)
+=== /memories/email_preferences.md ===
+# Jane's email preferences
+
+- With familiar faculty collaborators, use a warm, informal, concise voice: "Hi Ravi," rather than "Dear Prof. Mehta," and sign simply "Jane" rather than a formal closing and full name.
+- Acknowledge the recipient's good news enthusiastically when replying (e.g., congratulations on a grant), rather than focusing only on scheduling.
+- Preserve personal context Jane explicitly supplies for the email; do not replace her stated reason with a vague "conflict."
+- Favor direct, natural phrasing such as "I need to push Thursday" over formal apologies or stiff rescheduling language.
+- State proposed scheduling alternatives clearly. In her edited example, Jane added a specific availability window; do not assume that window applies to future meetings or invent availability.
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

**Agent's reply:** Noted—for class announcements, I’ll keep it brief and logistical, omit private reasons, and sign “Prof. Doe.”

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -5,4 +5,6 @@
 - Acknowledge the recipient's good news enthusiastically when replying (e.g., congratulations on a grant), rather than focusing only on scheduling.
-- Preserve personal context Jane explicitly supplies for the email; do not replace her stated reason with a vague "conflict."
+- Tailor personal context to the audience: preserve supplied personal context with familiar collaborators, but omit private reasons (e.g., a doctor's appointment) from class announcements, as in Jane's edited office-hours notice.
 - Favor direct, natural phrasing such as "I need to push Thursday" over formal apologies or stiff rescheduling language.
 - State proposed scheduling alternatives clearly. In her edited example, Jane added a specific availability window; do not assume that window applies to future meetings or invent availability.
+
+- For class announcements, keep the message brief and logistical; use "Hi everyone," and sign "Prof. Doe" without "Best." State schedule changes directly and put room-booking explanations in a short parenthetical when useful.
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

**Agent's reply:** Noted for future student replies: be direct, explain the reason, offer concrete options when known, and sign “Prof. Doe.”

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -10 +10,3 @@
 - For class announcements, keep the message brief and logistical; use "Hi everyone," and sign "Prof. Doe" without "Best." State schedule changes directly and put room-booking explanations in a short parenthetical when useful.
+- For individual student replies, use a direct, matter-of-fact but helpful tone; sign "Prof. Doe" without "Best." When denying a request, give a concise reason and, when known, practical alternatives or support rather than generic well-wishes or an unnecessary "Unfortunately."
+- In her edited Assignment 2 extension reply, Jane explained that other deadlines aren't grounds for an extension and offered the applicable late-submission option and office hours. Include such specifics only when established; do not assume that example's 24-hour/10% late policy or Friday office hours apply to other assignments or dates.
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

**Agent's reply:** Noted for future drafts: direct wording, specific times when known, and personal reasons kept private. I’ll also keep the tone collegial without effusive thanks.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -12 +12,2 @@
 - In her edited Assignment 2 extension reply, Jane explained that other deadlines aren't grounds for an extension and offered the applicable late-submission option and office hours. Include such specifics only when established; do not assume that example's 24-hour/10% late policy or Friday office hours apply to other assignments or dates.
+- For coverage requests to her TA, use concise, direct wording ("Could you cover...") and sign "Jane"; avoid effusive thanks. Keep personal/family medical reasons private ("Something came up"). Include the specific coverage time when known, without inventing it. In her edited example, Jane offered to take one of the TA's sections the following week in return; consider reciprocity when appropriate, but do not invent commitments.
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

**Agent's reply:** Noted—I'll use a more professional tone with Helen, keep family details private, and favor clear follow-up commitments when you've provided them.

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -13 +13,2 @@
 - For coverage requests to her TA, use concise, direct wording ("Could you cover...") and sign "Jane"; avoid effusive thanks. Keep personal/family medical reasons private ("Something came up"). Include the specific coverage time when known, without inventing it. In her edited example, Jane offered to take one of the TA's sections the following week in return; consider reciprocity when appropriate, but do not invent commitments.
+- For messages to the department chair, favor a concise, professional tone: "Dear Helen," and "Best regards,\nJane Doe" in her edited faculty-meeting reply. She omitted the family medical reason, briefly apologized for short notice, and replaced a tentative offer with a concrete follow-up commitment. Keep private family details out of such notices; never add medical details not supplied. Include follow-up deadlines only when established, not by reusing this example's Monday deadline.
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

**Agent's reply:** Noted—I'll keep replies to Ravi brief and informal, preserve the personal context you provide, and sign simply “Jane.”

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -14 +14,2 @@
 - For messages to the department chair, favor a concise, professional tone: "Dear Helen," and "Best regards,\nJane Doe" in her edited faculty-meeting reply. She omitted the family medical reason, briefly apologized for short notice, and replaced a tentative offer with a concrete follow-up commitment. Keep private family details out of such notices; never add medical details not supplied. Include follow-up deadlines only when established, not by reusing this example's Monday deadline.
+- In her edited paper-outline reply to Ravi, Jane went straight to the commitment without thanking him for sharing the outline, retained the supplied reason "my kid has a school event," and asked simply "Could we meet Wednesday instead?" For familiar collaborators, avoid filler acknowledgments, generic "conflict" substitutions for supplied personal context, and unnecessary "Unfortunately."
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

**Agent's reply:** Noted—future class announcements will be direct and concise, with a brief supportive note when relevant, and signed “Prof. Doe.”

**What the agent changed in memory:**
```diff
--- before
+++ after
@@ -9,3 +9,3 @@
 
-- For class announcements, keep the message brief and logistical; use "Hi everyone," and sign "Prof. Doe" without "Best." State schedule changes directly and put room-booking explanations in a short parenthetical when useful.
+- For class announcements, keep the message brief and logistical; use "Hi everyone," and sign "Prof. Doe" without "Best." State schedule changes directly (omit preambles such as "I'm writing to let you know") and put room-booking explanations in a short parenthetical when useful. In her edited proposal-deadline announcement, Jane acknowledged a heavy midterm week and encouraged students to plan ahead and come to office hours for early feedback: pair logistics with brief, practical support when relevant, without inventing office-hours times.
 - For individual student replies, use a direct, matter-of-fact but helpful tone; sign "Prof. Doe" without "Best." When denying a request, give a concise reason and, when known, practical alternatives or support rather than generic well-wishes or an unnecessary "Unfortunately."
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
# Jane's email preferences

- With familiar faculty collaborators, use a warm, informal, concise voice: "Hi Ravi," rather than "Dear Prof. Mehta," and sign simply "Jane" rather than a formal closing and full name.
- Acknowledge the recipient's good news enthusiastically when replying (e.g., congratulations on a grant), rather than focusing only on scheduling.
- Tailor personal context to the audience: preserve supplied personal context with familiar collaborators, but omit private reasons (e.g., a doctor's appointment) from class announcements, as in Jane's edited office-hours notice.
- Favor direct, natural phrasing such as "I need to push Thursday" over formal apologies or stiff rescheduling language.
- State proposed scheduling alternatives clearly. In her edited example, Jane added a specific availability window; do not assume that window applies to future meetings or invent availability.

- For class announcements, keep the message brief and logistical; use "Hi everyone," and sign "Prof. Doe" without "Best." State schedule changes directly (omit preambles such as "I'm writing to let you know") and put room-booking explanations in a short parenthetical when useful. In her edited proposal-deadline announcement, Jane acknowledged a heavy midterm week and encouraged students to plan ahead and come to office hours for early feedback: pair logistics with brief, practical support when relevant, without inventing office-hours times.
- For individual student replies, use a direct, matter-of-fact but helpful tone; sign "Prof. Doe" without "Best." When denying a request, give a concise reason and, when known, practical alternatives or support rather than generic well-wishes or an unnecessary "Unfortunately."
- In her edited Assignment 2 extension reply, Jane explained that other deadlines aren't grounds for an extension and offered the applicable late-submission option and office hours. Include such specifics only when established; do not assume that example's 24-hour/10% late policy or Friday office hours apply to other assignments or dates.
- For coverage requests to her TA, use concise, direct wording ("Could you cover...") and sign "Jane"; avoid effusive thanks. Keep personal/family medical reasons private ("Something came up"). Include the specific coverage time when known, without inventing it. In her edited example, Jane offered to take one of the TA's sections the following week in return; consider reciprocity when appropriate, but do not invent commitments.
- For messages to the department chair, favor a concise, professional tone: "Dear Helen," and "Best regards,\nJane Doe" in her edited faculty-meeting reply. She omitted the family medical reason, briefly apologized for short notice, and replaced a tentative offer with a concrete follow-up commitment. Keep private family details out of such notices; never add medical details not supplied. Include follow-up deadlines only when established, not by reusing this example's Monday deadline.
- In her edited paper-outline reply to Ravi, Jane went straight to the commitment without thanking him for sharing the outline, retained the supplied reason "my kid has a school event," and asked simply "Could we meet Wednesday instead?" For familiar collaborators, avoid filler acknowledgments, generic "conflict" substitutions for supplied personal context, and unnecessary "Unfortunately."
```

## Scoring

`reward.json`: `prefs_correct` = 2, `prefs_wrong_scope` = 0, `prefs_missed` = 0, `one_offs_wrongly_saved` = 1, `outdated_kept` = 0, `draft_correct` = 1, `draft_asked_clarification` = 0

**Memory after the last feedback round, item by item:**

| item | type | outcome | scope error | memory quote | reason |
|---|---|---|---|---|---|
| P1: Gives the real personal reason (family, health) when cancelling or moving something. | preference | **correct** |  | Tailor personal context to the audience: preserve supplied personal context with familiar collaborators, but omit private reasons (e.g., a doctor's appointment) from class announcements, as in Jane's edited office-hours notice. | The memory preserves real personal context for familiar collaborators while separately directing privacy for students, the TA, and the chair. |
| P2: Offers a concrete alternative or next step when she refuses or changes something. | preference | **correct** |  | When denying a request, give a concise reason and, when known, practical alternatives or support rather than generic well-wishes or an unnecessary "Unfortunately." - In her edited Assignment 2 extension reply, Jane explained that other deadlines aren't grounds for an extension and offered the applicable late-submission option and office hours. Include such specifics only when established; do not assume that example's 24-hour/10% late policy or Friday office hours apply to other assignments or dates. - For coverage requests to her TA, use concise, direct wording ("Could you cover...") and sign "Jane"; avoid effusive thanks. Keep personal/family medical reasons private ("Something came up"). Include the specific coverage time when known, without inventing it. In her edited example, Jane offered to take one of the TA's sections the following week in return; consider reciprocity when appropriate, but do not invent commitments. | The memory directs practical alternatives for students and reciprocal next steps for TA coverage requests, without inventing specifics. |
| O1: Congratulated Ravi on his NSF grant (his email announced it). Any rule that has the assistant add congratulations, even only when someone shares good news, counts as saved; noting it as a past event does not. | one-off | **wrongly_saved** |  | Acknowledge the recipient's good news enthusiastically when replying (e.g., congratulations on a grant), rather than focusing only on scheduling. | The memory turns the grant congratulations into a lasting rule for replies containing good news. |
| O2: Apologized to Helen for the short notice (the meeting was the same day). Any rule that has the assistant add an apology, even only for short notice, counts as saved; noting it as a past event does not. | one-off | **not_saved** |  | She omitted the family medical reason, briefly apologized for short notice, and replaced a tentative offer with a concrete follow-up commitment. | The apology is described as a past edit, not as an instruction to apologize in future messages. |
| O3: Acknowledged that midterm week is a lot (the deadline fell in that week). Any rule that has the assistant add a line acknowledging workload or offering sympathy, even only "when appropriate", counts as saved; noting it as a past event does not. | one-off | **not_saved** |  | In her edited proposal-deadline announcement, Jane acknowledged a heavy midterm week and encouraged students to plan ahead and come to office hours for early feedback: pair logistics with brief, practical support when relevant, without inventing office-hours times. | The workload acknowledgment is historical, while the lasting instruction calls for practical support rather than workload acknowledgment or sympathy. |
| O4: Office hours that one Friday were in WVH 210 because the usual room was booked (a fact about that week, not where office hours are held). | one-off | **not_saved** |  |  | The memory does not save WVH 210 as an office-hours location or make that week's room assignment a recurring practice. |

**Final draft checklist:**

| check | statement | passed | draft quote | reason |
|---|---|---|---|---|
| must | Tells Susan she can't do lunch Thursday and suggests next week. | yes | I can't do lunch Thursday—my kid's home sick. Could we try next week instead? | The draft tells Susan she cannot do lunch Thursday and suggests meeting next week instead. |
| must | Gives the real reason, that her kid is home sick. | yes | I can't do lunch Thursday—my kid's home sick. | The draft explicitly gives her child being home sick as the reason. |
| must_not | Adds congratulations, or an apology for short notice, that nothing in the request calls for. | yes |  | The draft adds neither congratulations nor an apology for short notice. |

## Reviewer notes

- Do the judge's labels look right? (yes / no, which ones):
- What went wrong, in one or two sentences:

