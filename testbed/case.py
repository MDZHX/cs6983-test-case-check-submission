"""Load and validate a test case: one folder under cases/ (template: cases/_template/).

  cases/<case id>/
    persona.yaml       the professor and her contacts
    memory/            starting memory: memory/notes.md is /memories/notes.md (missing or empty = empty memory)
    feedback_rounds/*.md   the professor revises drafts and the agent updates memory; run in file-name order.
                       The file name (without .md) is the round id.
    final_task.md      the new request the agent drafts from memory alone
    answer_key.yaml    what the scorer checks: preferences, one_offs, outdated, must, must_not
    participant.md     the persona card and steps for a person playing the professor (human mode)

The case id is the folder name. Only the runner reads these files, and it passes the agent
only what the agent should see (testbed/runner.py); the answer key goes to the scorer alone.

A feedback-round or final-task file is front matter plus "## " sections:

  ---
  to: david.hirsch@univ.edu        # one address or a list; cc: works the same way
  date: 2026-10-06                 # required: the agent is told "Today is <date>"
  subject: Faculty meeting         # optional: the draft's subject line
  incoming_from: laura.chen@univ.edu       # for a reply: who wrote the incoming email
  incoming_subject: Task force             # and its subject; the body goes in "## Incoming"
  ---
  ## Incoming      (reply only)
  ## Request       what the professor asks for (both files)
  ## Draft         the pre-written draft the agent "made" (feedback rounds only)
  ## Sent          what the professor actually sent (feedback rounds only; the simulated user's script)
  ## Comment       optional words the professor adds after the revision (feedback rounds only)
"""

import hashlib
import re
from datetime import date
from pathlib import Path

import yaml

SESSION_SECTIONS = {"Request", "Draft", "Sent", "Comment", "Incoming"}
FINAL_SECTIONS = {"Request", "Incoming"}
FRONT_KEYS = {"to", "cc", "date", "subject", "incoming_from", "incoming_subject"}
KEY_KEYS = {"preferences", "one_offs", "outdated", "must", "must_not"}
# answer-key item kinds: (field, the text it needs, default id prefix)
ITEM_KINDS = (("preferences", "rule", "P"), ("one_offs", "edit", "O"), ("outdated", "practice", "R"))


class CaseError(ValueError):
    pass


def _as_list(v) -> list:
    return [] if v is None else v if isinstance(v, list) else [v]


def _date(path: Path, v, errors: list) -> str:
    if v is None:
        errors.append(f"{path.name}: needs 'date' in the front matter")
        return ""
    try:
        return (v if isinstance(v, date) else date.fromisoformat(str(v))).isoformat()
    except ValueError:
        errors.append(f"{path.name}: date {v!r} is not YYYY-MM-DD")
        return ""


def _yaml(path: Path, errors: list, required: bool = True) -> dict:
    if not path.exists():
        if required:
            errors.append(f"missing {path.name}")
        return {}
    try:
        data = yaml.safe_load(path.read_text()) or {}
    except yaml.YAMLError as e:
        errors.append(f"{path.name}: not valid YAML ({e})")
        return {}
    if not isinstance(data, dict):
        errors.append(f"{path.name}: must be a YAML mapping")
        return {}
    return data


def parse_markdown(path: Path, allowed: set, errors: list) -> tuple[dict, dict]:
    """(front matter, {section name: text}) for a feedback-round or final-task file."""
    text = path.read_text()
    front = {}
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if m:
        try:
            front = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as e:
            errors.append(f"{path.name}: front matter is not valid YAML ({e})")
        text = text[m.end():]
    for k in set(front) - FRONT_KEYS:
        errors.append(f"{path.name}: unknown front-matter field {k!r} (allowed: {', '.join(sorted(FRONT_KEYS))})")
    sections, name, lines = {}, None, []
    for line in text.splitlines():
        h = re.match(r"## +(.+?)\s*$", line)
        if h:
            if name:
                sections[name] = "\n".join(lines).strip()
            name, lines = h.group(1), []
            if name not in allowed:
                errors.append(f"{path.name}: unknown section '## {name}' (allowed: {', '.join(sorted(allowed))})")
            if name in sections:
                errors.append(f"{path.name}: section '## {name}' appears twice")
        elif name:
            lines.append(line)
        elif line.strip():
            errors.append(f"{path.name}: text before the first '## ' section: {line.strip()[:60]!r}")
    if name:
        sections[name] = "\n".join(lines).strip()
    return front, sections


def _task(path: Path, front: dict, sections: dict, persona: dict, errors: list, warnings: list) -> dict:
    """The fields the runner needs from a feedback round or the final task."""
    t = {"to": _as_list(front.get("to")), "cc": _as_list(front.get("cc")), "subject": front.get("subject"),
         "request": sections.get("Request", "")}
    if not t["request"]:
        errors.append(f"{path.name}: needs a '## Request' section")
    if front.get("incoming_from") or sections.get("Incoming"):
        t["incoming"] = {"from": front.get("incoming_from"), "subject": front.get("incoming_subject"),
                         "body": sections.get("Incoming", "")}
        for key, where in (("from", "incoming_from"), ("subject", "incoming_subject"), ("body", "## Incoming")):
            if not t["incoming"][key]:
                errors.append(f"{path.name}: a reply needs {where}")
        if not t["to"]:
            t["to"] = [t["incoming"]["from"]]
    if not t["to"]:
        errors.append(f"{path.name}: needs 'to' in the front matter (or incoming_from for a reply)")
    known = {c["email"].lower() for c in persona.get("contacts", [])}
    for addr in t["to"] + t["cc"] + ([t["incoming"]["from"]] if t.get("incoming") else []):
        if addr and addr.lower() not in known:
            warnings.append(f"{path.name}: {addr} is not in persona.yaml's contacts")
    return t


def _answer_key(key: dict, session_ids: set, errors: list, warnings: list) -> dict:
    for k in set(key) - KEY_KEYS:
        errors.append(f"answer_key.yaml: unknown field {k!r} (allowed: {', '.join(sorted(KEY_KEYS))})")
    out = {k: _as_list(key.get(k)) for k in KEY_KEYS}
    if not any(out[kind] for kind, _, _ in ITEM_KINDS):
        warnings.append("answer_key.yaml has no preferences, one_offs or outdated, so the memory metrics "
                        "can't be scored")
    if not out["must"] and not out["must_not"]:
        warnings.append("answer_key.yaml has no must / must_not, so draft_correct can't be scored")
    seen = set()
    for kind, text_field, prefix in ITEM_KINDS:
        for i, item in enumerate(out[kind]):
            where = f"answer_key.yaml {kind}[{i}]"
            if not isinstance(item, dict):
                errors.append(f"{where}: must be a mapping")
                continue
            item.setdefault("id", prefix + str(i + 1))
            if item["id"] in seen:
                errors.append(f"{where}: duplicate id {item['id']!r}")
            seen.add(item["id"])
            if not item.get(text_field):
                errors.append(f"{where}: needs '{text_field}'")
            if kind == "preferences" and not item.get("scope"):
                errors.append(f"{where}: needs 'scope' (who or which situations the rule applies to)")
            if kind == "outdated" and not item.get("replaced_by"):
                errors.append(f"{where}: needs 'replaced_by' (the later practice that replaced it)")
            item["evidence"] = _as_list(item.get("evidence"))
            for sid in item["evidence"]:
                if sid not in session_ids:
                    errors.append(f"{where}: evidence {sid!r} is not a file in feedback_rounds/")
    for k in ("must", "must_not"):
        if not all(isinstance(s, str) and s.strip() for s in out[k]):
            errors.append(f"answer_key.yaml {k}: each line must be a non-empty statement")
    return out


def _persona(path: Path, errors: list) -> dict:
    p = _yaml(path, errors)
    for key in ("name", "first_name", "email", "description", "contacts"):
        if p and key not in p:
            errors.append(f"persona.yaml: missing '{key}'")
    return p


def _memory(folder: Path) -> dict:
    if not folder.is_dir():
        return {}
    return {"/memories/" + p.relative_to(folder).as_posix(): p.read_text().rstrip("\n")
            for p in sorted(folder.rglob("*")) if p.is_file() and not p.name.startswith(".")}


def case_hash(folder: Path) -> str:
    """One sha256 over every file in the case folder, so config.json pins the exact case that ran."""
    h = hashlib.sha256()
    for p in sorted(folder.rglob("*")):
        if p.is_file() and not p.name.startswith("."):
            h.update(p.relative_to(folder).as_posix().encode() + b"\0" + p.read_bytes() + b"\0")
    return h.hexdigest()


def load_case(path) -> tuple[dict, list[str]]:
    """Returns (case, warnings). Raises CaseError listing every problem found."""
    folder = Path(path)
    if not (folder / "final_task.md").is_file():
        raise CaseError(f"{folder} is not a case folder (no final_task.md)")
    errors, warnings = [], []
    persona = _persona(folder / "persona.yaml", errors)
    c = {"id": folder.name, "folder": folder, "persona": persona, "seed_memory": _memory(folder / "memory"),
         "feedback_sessions": []}
    if not re.fullmatch(r"[a-z0-9_]+", c["id"]):
        errors.append(f"folder name {c['id']!r} is the case id: use lowercase letters, digits, underscores")

    files = sorted((folder / "feedback_rounds").glob("*.md")) if (folder / "feedback_rounds").is_dir() else []
    for f in files:
        front, sec = parse_markdown(f, SESSION_SECTIONS, errors)
        s = _task(f, front, sec, persona, errors, warnings)
        s.update(id=f.stem, date=_date(f, front.get("date"), errors), draft=sec.get("Draft", ""), sent=sec.get("Sent", ""),
                 comment=sec.get("Comment") or None)
        for key in ("Draft", "Sent"):
            if not sec.get(key):
                errors.append(f"{f.name}: needs a '## {key}' section")
        c["feedback_sessions"].append(s)

    final_path = folder / "final_task.md"
    front, sec = parse_markdown(final_path, FINAL_SECTIONS, errors)
    f = _task(final_path, front, sec, persona, errors, warnings)
    f.update(id="final", date=_date(final_path, front.get("date"), errors))
    dates = [s["date"] for s in c["feedback_sessions"]] + [f["date"]]
    if all(dates) and dates != sorted(dates):
        warnings.append("dates go backwards: feedback rounds run in file-name order, and the final task comes last")
    key = _answer_key(_yaml(folder / "answer_key.yaml", errors), {s["id"] for s in c["feedback_sessions"]},
                      errors, warnings)
    f["must"], f["must_not"] = key["must"], key["must_not"]
    c["final_task"], c["answer_key"] = f, key

    if not (folder / "participant.md").is_file():
        warnings.append("no participant.md, so the case isn't ready for human mode")
    if errors:
        raise CaseError("\n  ".join([f"{folder.name} has errors:"] + errors))
    return c, warnings
