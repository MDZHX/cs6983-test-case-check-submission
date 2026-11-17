"""The team's survey and interview (METRICS.md), used in human mode.

Names are the core subjective metric names and must match METRICS.md exactly.
Each item is rated 1 (strongly disagree) to 7 (strongly agree).
"""

SCALE = (1, 7)
SCALE_LABELS = ("Strongly disagree", "Strongly agree")

# Asked after the final draft, before the participant sees the assistant's memory.
BEFORE_REVEAL = [
    ("perceived_understanding", "I know what the assistant learned from my edits."),
    ("perceived_control", "I could control what the assistant learned from my edits."),
    ("cognitive_load", "Getting the drafts right took a lot of effort."),
]

# Asked after the memory reveal.
AFTER_REVEAL = [
    ("memory_agreement", "What the assistant saved matches what I meant."),
]

INTERVIEW = [
    "Before you saw the memory, what did you think the assistant had learned from you?",
    "Was anything it saved wrong, too broad, or too narrow?",
    "Did the final draft match what you expected? Why or why not?",
    "How would you want to tell the assistant what to learn, or what not to?",
]


def interview_template(case_id: str, participant: str) -> str:
    out = [f"# Interview notes: {case_id}, participant {participant}", "",
           "Filled in by the facilitator after the survey. Ask each question; follow up briefly.", ""]
    for i, q in enumerate(INTERVIEW, 1):
        out += [f"## {i}. {q}", "", "", ""]
    return "\n".join(out)
