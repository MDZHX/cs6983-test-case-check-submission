# context_one_offs / baseline: no memory / run-01

## Starting memory

(empty)

## Final task

**Request:** Tell Susan I can't do lunch Thursday, my kid's home sick. Maybe next week?

**Draft** (subject: Lunch Thursday):
```
Hi Susan,

Sorry, I can't make lunch Thursday—my kid's home sick. Could we try for next week instead?

Jane
```

Read memory before drafting: yes. Looked up a contact: no.

## Memory at the end

(empty)

## Scoring

`reward.json`: `draft_correct` = 1, `draft_asked_clarification` = 0

Memory: not scored: control run, no feedback rounds

**Final draft checklist:**

| check | statement | passed | draft quote | reason |
|---|---|---|---|---|
| must | Tells Susan she can't do lunch Thursday and suggests next week. | yes | Sorry, I can't make lunch Thursday—my kid's home sick. Could we try for next week instead? | The draft tells Susan she cannot make lunch Thursday and suggests next week instead. |
| must | Gives the real reason, that her kid is home sick. | yes | Sorry, I can't make lunch Thursday—my kid's home sick. | The draft explicitly gives her child being home sick as the reason. |
| must_not | Adds congratulations, or an apology for short notice, that nothing in the request calls for. | yes |  | The draft adds neither congratulations nor an apology for short notice; its general apology is for being unable to attend. |

## Reviewer notes

- Do the judge's labels look right? (yes / no, which ones):
- What went wrong, in one or two sentences:

