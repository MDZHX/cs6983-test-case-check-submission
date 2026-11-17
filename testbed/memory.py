"""The agent's long-term memory: a /memories directory of text files.

Command names, arguments, and return strings follow Anthropic's memory tool
(`memory_20250818`, https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool).
Anthropic runs that tool client-side, so the application implements every
command; we do the same here, backed by a dict instead of a disk, and expose
it to the OpenAI model as an ordinary function tool.
"""

import json

ROOT = "/memories"

MEMORY_TOOL = {
    "type": "function",
    "name": "memory",
    "description": (
        "Your persistent memory directory, /memories. It is the only thing kept between sessions. "
        "Commands: view (a directory listing, or a file with line numbers; optional view_range [start, end]), "
        "create (create or overwrite a file with file_text), str_replace (replace old_str with new_str; "
        "old_str must appear exactly once), insert (insert insert_text after line insert_line; 0 = top), "
        "delete (a file or directory), rename (old_path to new_path). All paths must start with /memories. "
        "Keep the directory organized: update or delete files that are out of date rather than piling up new ones."
    ),
    # Strict mode (every field required, unused ones null): without it the model sometimes emitted
    # malformed arguments padded with thousands of whitespace characters.
    "parameters": {
        "type": "object",
        "properties": {
            "command": {"type": "string", "enum": ["view", "create", "str_replace", "insert", "delete", "rename"]},
            "path": {"type": ["string", "null"]},
            "view_range": {"type": ["array", "null"], "items": {"type": "integer"}},
            "file_text": {"type": ["string", "null"]},
            "old_str": {"type": ["string", "null"]},
            "new_str": {"type": ["string", "null"]},
            "insert_line": {"type": ["integer", "null"]},
            "insert_text": {"type": ["string", "null"]},
            "old_path": {"type": ["string", "null"]},
            "new_path": {"type": ["string", "null"]},
        },
        "required": ["command", "path", "view_range", "file_text", "old_str", "new_str", "insert_line",
                     "insert_text", "old_path", "new_path"],
        "additionalProperties": False,
    },
    "strict": True,
}

# Auto-injected by the Claude API whenever the memory tool is enabled (quoted from the docs above).
# OpenAI does not inject anything, so we add it to the system prompt ourselves.
MEMORY_PROTOCOL = """IMPORTANT: ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE.
MEMORY PROTOCOL:
1. Use the `view` command of your `memory` tool to check for earlier progress.
2. ... (work on the task) ...
   - As you make progress, record status / progress / thoughts etc in your memory.
ASSUME INTERRUPTION: Your context window might be reset at any moment, so you risk losing any progress that is not recorded in your memory directory."""

# The docs suggest scoping what gets written ("Only write down information relevant to <topic>...").
MEMORY_TOPIC = "Only write down information relevant to {first_name}'s email writing preferences in your memory system."


def _size(n: int) -> str:
    return f"{n / 1024:.1f}K"


class MemoryStore:
    def __init__(self, files: dict[str, str] | None = None):
        self.files: dict[str, str] = dict(files or {})
        self.log: list[dict] = []  # every command the agent ran, with its result

    def snapshot(self) -> dict[str, str]:
        return dict(sorted(self.files.items()))

    def dump(self) -> str:
        """All files concatenated, for reports."""
        if not self.files:
            return "(memory is empty)"
        return "\n\n".join(f"=== {p} ===\n{c.rstrip()}" for p, c in sorted(self.files.items()))

    def _valid(self, path: str | None) -> bool:
        return bool(path) and (path == ROOT or path.startswith(ROOT + "/")) and ".." not in path

    def _is_dir(self, path: str) -> bool:
        return path == ROOT or any(p.startswith(path.rstrip("/") + "/") for p in self.files)

    def call(self, args: dict) -> str:
        args = {k: v for k, v in args.items() if v is not None}  # strict mode sends null for unused fields
        out = self._run(args)
        self.log.append({"args": args, "result": out})
        return out

    def _run(self, a: dict) -> str:
        cmd = a.get("command")
        if cmd == "rename":
            old, new = a.get("old_path"), a.get("new_path")
            if not (self._valid(old) and self._valid(new)) or old == ROOT:
                return "Error: paths must be inside /memories, and /memories itself cannot be renamed"
            moved = {p: c for p, c in self.files.items() if p == old or p.startswith(old + "/")}
            if not moved:
                return f"Error: The path {old} does not exist"
            if new in self.files or self._is_dir(new):
                return f"Error: The destination {new} already exists"
            for p, c in moved.items():
                del self.files[p]
                self.files[new + p[len(old):]] = c
            return f"Successfully renamed {old} to {new}"

        path = a.get("path")
        if not self._valid(path):
            return f"Error: The path {path} is outside /memories"
        path = path.rstrip("/") or ROOT

        if cmd == "view":
            if path in self.files:
                lines = self.files[path].split("\n")
                if a.get("view_range"):
                    start, end = a["view_range"][0], a["view_range"][-1]
                    end = len(lines) if end == -1 else end
                    numbered = [(i, lines[i - 1]) for i in range(max(start, 1), min(end, len(lines)) + 1)]
                else:
                    numbered = list(enumerate(lines, 1))
                body = "\n".join(f"{i:6d}\t{l}" for i, l in numbered)
                return f"Here's the content of {path} with line numbers:\n{body}"
            if self._is_dir(path):
                inside = sorted(p for p in self.files if p.startswith(path.rstrip("/") + "/"))
                total = sum(len(self.files[p]) for p in inside)
                rows = [f"{_size(total)}\t{path}"] + [f"{_size(len(self.files[p]))}\t{p}" for p in inside]
                return ("Here're the files and directories up to 2 levels deep in "
                        f"{path}, excluding hidden items and node_modules:\n" + "\n".join(rows))
            return f"The path {path} does not exist. Please provide a valid path."

        if cmd == "create":
            if path == ROOT:
                return "Error: cannot create a file at /memories itself"
            self.files[path] = a.get("file_text", "")
            return f"File created successfully at: {path}"

        if cmd in ("str_replace", "insert") and path not in self.files:
            return f"Error: The path {path} does not exist. Please provide a valid path."

        if cmd == "str_replace":
            old, new, text = a.get("old_str", ""), a.get("new_str") or "", self.files[path]
            hits = [i + 1 for i, l in enumerate(text.split("\n")) if old and old in l]
            count = text.count(old) if old else 0
            if count == 0:
                return f"No replacement was performed, old_str `{old}` did not appear verbatim in {path}."
            if count > 1:
                return (f"No replacement was performed. Multiple occurrences of old_str `{old}` in lines: "
                        f"{hits}. Please ensure it is unique")
            self.files[path] = text.replace(old, new, 1)
            return "The memory file has been edited."

        if cmd == "insert":
            lines = self.files[path].split("\n")
            n = a.get("insert_line", 0)
            if not isinstance(n, int) or n < 0 or n > len(lines):
                return (f"Error: Invalid `insert_line` parameter: {n}. It should be within the range of "
                        f"lines of the file: [0, {len(lines)}]")
            lines[n:n] = [a.get("insert_text", "").rstrip("\n")]
            self.files[path] = "\n".join(lines)
            return f"The file {path} has been edited."

        if cmd == "delete":
            if path == ROOT:
                return "Error: /memories itself cannot be deleted"
            doomed = [p for p in self.files if p == path or p.startswith(path + "/")]
            if not doomed:
                return f"Error: The path {path} does not exist"
            for p in doomed:
                del self.files[p]
            return f"Successfully deleted {path}"

        return json.dumps({"error": f"unknown command {cmd!r}"})
