"""The agent's non-memory tools: contact lookup and drafting.

There is no inbox. Each task arrives in the professor's message (with the
recipients' contact cards and, for replies, the incoming email), so the only
thing that carries between sessions is memory.
"""

import json


def _fn(name: str, description: str, props: dict) -> dict:
    return {
        "type": "function",
        "name": name,
        "description": description,
        "parameters": {"type": "object", "properties": props, "required": list(props),
                       "additionalProperties": False},
        "strict": True,
    }


EMAIL_TOOLS = [
    _fn("lookup_contact",
        "Look up a person in the contacts directory by email address or name. Returns their role.",
        {"query": {"type": "string"}}),
    _fn("save_draft",
        "Save the email draft for the user to review. Nothing is sent. Saving again replaces the draft.",
        {"subject": {"type": "string"}, "body": {"type": "string"}}),
]

DRAFT_SAVED = json.dumps({"status": "draft saved; the user will review it"})


class Desk:
    """Contacts directory plus the drafts saved in the current session."""

    def __init__(self, contacts: list[dict]):
        self.contacts = contacts
        self.drafts: list[dict] = []

    def call(self, name: str, args: dict) -> str:
        if name == "lookup_contact":
            q = args["query"].strip().lower()
            hits = [c for c in self.contacts if q in c["email"].lower() or q in c["name"].lower()]
            return json.dumps(hits[:5] or {"error": f"no contact matching {args['query']!r}"})
        if name == "save_draft":
            self.drafts.append({"subject": args["subject"], "body": args["body"]})
            return DRAFT_SAVED
        return json.dumps({"error": f"unknown tool {name!r}"})
