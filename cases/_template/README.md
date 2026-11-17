# Case template

Copy this folder to `cases/<case_id>/` (lowercase letters, digits, underscores), fill in each file,
and check it without any API calls:

    docker compose run --rm testbed cases/<case_id> --validate

## The files

| File | What it is | Read by |
|---|---|---|
| `persona.yaml` | The professor and her contacts | the agent |
| `memory/` | Starting memory: `memory/notes.md` becomes `/memories/notes.md`. Empty folder = empty memory. | the agent |
| `feedback_rounds/NN_name.md` | One past email each, run in file-name order (format below) | the agent |
| `final_task.md` | The new request, drafted from memory alone (same format, `## Request` only) | the agent |
| `answer_key.yaml` | What the scorer checks: preferences with scope, one-offs, outdated practice, `must` / `must_not` | the scorer only |
| `participant.md` | The persona card for human mode, including what she'd want remembered | the participant |

## A feedback round

```markdown
---
to: cs4100-students@univ.edu     # or, for a reply: incoming_from and incoming_subject
date: 2026-09-08                 # required: the agent is told "Today is <date>"
---
## Incoming
(only for a reply: the email she is answering)

## Request
What she asks the assistant for.

## Draft
The draft she sees, written as if by the assistant.

## Sent
What she actually sent. In simulated mode this is her edit; in human mode the participant writes it.

## Comment
(optional) Anything she tells the assistant after sending.
```

Each round and the final task is a fresh conversation; only memory carries over.

## Rules for a fair case

- Every answer-key item is either something a careful reader of the rounds could work out, or stated as
  the professor's own view in `participant.md`. Have a teammate who didn't write the case check this.
- The request never decides the answer. The assistant has to choose, and her edits show what she wants.
- The final task is a situation no single round covers, so learning one note per email isn't enough.
- Starting memory must be correct as of the first round: if the agent starts from bad memory, its
  mistakes are ours. A later round may change her practice; the old note is then an `outdated` item.

The case's target breakdown and why it captures it go in its write-up (`docs/<case_id>.md`). This
README is not part of the case and is ignored by the code.
