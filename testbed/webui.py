"""Human mode: a local web page where a person plays the professor.

Python's standard library only: a small HTTP server on this machine serves one page. The page
polls /state to learn what to show and posts the person's answers to /submit. The case runs
in the main thread and waits at each step where the person must act (Bridge.ask).

Order of a human run (METRICS.md):
  intro (participant.md) -> each feedback round: edit the draft, see the assistant's reply
  -> the final draft -> survey part 1 -> memory reveal -> survey part 2 -> done
"""

import html
import json
import queue
import re
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from . import survey
from .trace import now
from .users import HumanUser


class Bridge:
    """What the page should show now, and the person's answers coming back."""

    def __init__(self):
        self._lock = threading.Lock()
        self._answers: queue.Queue = queue.Queue()
        self._seq = 0
        self._state = {"seq": 0, "step": "working", "message": "Starting..."}
        self.served_seq = -1
        self.card_html = ""  # the participant card, sent with every state so the page can keep it on hand

    def show(self, step: str, **data) -> int:
        with self._lock:
            self._seq += 1
            self._state = {"seq": self._seq, "step": step, "needs_answer": False, **data}
            return self._seq

    def ask(self, step: str, **data) -> dict:
        """Show a step and wait for the person to submit it."""
        with self._lock:
            self._seq += 1
            self._state = {"seq": self._seq, "step": step, "needs_answer": True, **data}
        answer = self._answers.get()
        answer["answered_at"] = now()
        return answer

    def state(self) -> dict:
        with self._lock:
            self.served_seq = self._state["seq"]
            return {**self._state, "card_html": self.card_html}

    def submit(self, answer: dict) -> tuple[bool, str]:
        with self._lock:
            if not self._state.get("needs_answer") or answer.get("seq") != self._state["seq"]:
                return False, "stale"
            self._seq += 1  # a new seq, so the page replaces the submitted form with a wait screen
            self._state = {"seq": self._seq, "step": "working", "needs_answer": False, "message": "One moment..."}
        self._answers.put(answer)
        return True, "ok"


def markdown_to_html(text: str) -> str:
    """Enough Markdown for a participant card: headings, lists, bold, paragraphs.
    <!-- comments --> are notes for the case author and are not shown."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    def inline(s):
        s = html.escape(s)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        return re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    out, para, lst = [], [], None

    def flush():
        nonlocal para, lst
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para = []
        if lst:
            out.append(f"<{lst[0]}>" + "".join(f"<li>{inline(i)}</li>" for i in lst[1]) + f"</{lst[0]}>")
            lst = None
    for line in text.splitlines():
        m_h = re.match(r"(#{1,3}) +(.*)", line)
        m_ul = re.match(r"\s*[-*] +(.*)", line)
        m_ol = re.match(r"\s*\d+\. +(.*)", line)
        if m_h:
            flush()
            n = len(m_h.group(1)) + 1
            out.append(f"<h{n}>{inline(m_h.group(2))}</h{n}>")
        elif m_ul or m_ol:
            kind = "ul" if m_ul else "ol"
            if para:
                flush()
            if lst and lst[0] != kind:
                flush()
            lst = lst or (kind, [])
            lst[1].append((m_ul or m_ol).group(1))
        elif not line.strip():
            flush()
        elif lst and line.startswith("  "):
            lst[1][-1] += " " + line.strip()
        else:
            if lst:
                flush()
            para.append(line.strip())
    flush()
    return "\n".join(out)


def _handler(bridge: Bridge):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):  # keep the facilitator's terminal quiet
            pass

        def _send(self, code: int, body: bytes, kind: str):
            self.send_response(code)
            self.send_header("Content-Type", kind)
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            if self.path == "/":
                self._send(200, PAGE.encode(), "text/html; charset=utf-8")
            elif self.path == "/state":
                self._send(200, json.dumps(bridge.state()).encode(), "application/json")
            else:
                self._send(404, b"not found", "text/plain")

        def do_POST(self):
            if self.path != "/submit":
                return self._send(404, b"not found", "text/plain")
            try:
                answer = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
            except ValueError:
                return self._send(400, b'{"ok": false}', "application/json")
            ok, why = bridge.submit(answer)
            self._send(200 if ok else 409, json.dumps({"ok": ok, "why": why}).encode(), "application/json")
    return Handler


def _survey(bridge: Bridge, part: int, items: list) -> dict:
    answer = bridge.ask("survey", part=part, scale=survey.SCALE, scale_labels=survey.SCALE_LABELS,
                        questions=[{"name": n, "text": t} for n, t in items])
    lo, hi = survey.SCALE
    out = {}
    for name, _ in items:
        v = answer.get("answers", {}).get(name)
        if not isinstance(v, int) or not lo <= v <= hi:
            raise ValueError(f"survey answer {name}={v!r} is not in {lo}-{hi}")
        out[name] = v
    return {"answers": out, "answered_at": answer["answered_at"]}


def run_human(llm, case: dict, participant: str, port: int, run_case, save):
    """Serve the page, play the case with the person, run the survey, then save the run with
    save(run result, survey) and return what it returns. The page says "Saving..." while save runs and
    shows the end screen only after it returns, so stopping the program after that loses nothing.
    Listens on all of the container's interfaces; compose.yaml publishes the port to this machine only."""
    bridge = Bridge()
    server = ThreadingHTTPServer(("0.0.0.0", port), _handler(bridge))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    url = f"http://localhost:{server.server_address[1]}/"
    print(f"human mode: open {url} in a browser for participant {participant} (Ctrl-C to abort)")
    try:
        bridge.card_html = markdown_to_html((case["folder"] / "participant.md").read_text())
        bridge.ask("intro", persona=case["persona"]["name"])
        started = now()
        res = run_case(llm, case, user=HumanUser(bridge, case, participant))
        part1 = _survey(bridge, 1, survey.BEFORE_REVEAL)
        bridge.ask("reveal", memory=res["memory_after_sessions"])
        part2 = _survey(bridge, 2, survey.AFTER_REVEAL)
        bridge.show("working", message="Saving your answers. Please keep this page open...")
        result = {"participant": participant, "case": case["id"], "started_at": started,
                  "answers": {**part1["answers"], **part2["answers"]},
                  "before_reveal_answered_at": part1["answered_at"],
                  "after_reveal_answered_at": part2["answered_at"],
                  "scale": f"{survey.SCALE[0]} = {survey.SCALE_LABELS[0]}, {survey.SCALE[1]} = {survey.SCALE_LABELS[1]}",
                  "questions": {n: t for n, t in survey.BEFORE_REVEAL + survey.AFTER_REVEAL}}
        saved = save(res, result)
        done = bridge.show("done")
        deadline = time.time() + 5
        while bridge.served_seq < done and time.time() < deadline:  # let the page show "done"
            time.sleep(0.1)
        return saved
    except BaseException:
        bridge.show("error")
        time.sleep(1)
        raise
    finally:
        server.shutdown()


PAGE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Email assistant study</title>
<style>
  :root { --bg: #f6f5f2; --card: #ffffff; --ink: #1f2328; --muted: #646a73; --line: #dcdad4;
          --accent: #2f5d8a; --accent-ink: #ffffff; --soft: #eef2f6; }
  @media (prefers-color-scheme: dark) {
    :root { --bg: #17191c; --card: #212428; --ink: #e8e6e3; --muted: #a0a5ad; --line: #3a3e44;
            --accent: #7fa8d1; --accent-ink: #10151b; --soft: #2a3038; }
  }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--bg); color: var(--ink);
         font: 16px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
  header { border-bottom: 1px solid var(--line); background: var(--card); }
  header div, main { max-width: 780px; margin: 0 auto; padding: 14px 16px; }
  header div { display: flex; justify-content: space-between; color: var(--muted); font-size: 14px; }
  main { padding-top: 24px; padding-bottom: 60px; }
  h1 { font-size: 22px; margin: 0 0 16px; }
  h2 { font-size: 18px; margin: 24px 0 8px; }
  h3 { font-size: 16px; margin: 20px 0 6px; }
  .card { background: var(--card); border: 1px solid var(--line); border-radius: 10px; padding: 16px 18px;
          margin: 0 0 16px; }
  .label { font-size: 13px; font-weight: 600; color: var(--muted); text-transform: uppercase;
           letter-spacing: .04em; margin: 0 0 6px; }
  .meta { color: var(--muted); font-size: 14px; margin: 4px 0 0; }
  .email { white-space: pre-wrap; font-family: inherit; font-size: 15px; line-height: 1.55; margin: 0; }
  .incoming { background: var(--soft); }
  .request { border-left: 4px solid var(--muted); }
  .draftcard { border: 2px solid var(--accent); }
  /* wide screens: the role card on the left, always visible; the task on the right */
  body.wide header div, body.wide main { max-width: 1240px; }
  .layout { display: grid; grid-template-columns: minmax(280px, 360px) minmax(0, 1fr); gap: 24px;
            align-items: start; }
  .side { position: sticky; top: 16px; max-height: calc(100vh - 32px); overflow-y: auto;
          background: var(--soft); border: 1px solid var(--line); border-radius: 10px;
          padding: 14px 18px; font-size: 14px; line-height: 1.5; }
  .side h1 { font-size: 17px; margin: 0 0 8px; }
  .side h2 { font-size: 15px; margin: 16px 0 4px; }
  .side ul, .side ol { padding-left: 20px; }
  details.role { display: none; }
  /* narrow screens: one column; the role card becomes a panel to open */
  @media (max-width: 899px) {
    .layout { grid-template-columns: minmax(0, 1fr); }
    .side { display: none; }
    details.role { display: block; }
  }
  textarea { width: 100%; border: 1px solid var(--line); border-radius: 8px; padding: 12px;
             font-family: inherit; font-size: 15px; line-height: 1.55; background: var(--card); color: var(--ink);
             resize: vertical; }
  textarea.draft { min-height: 300px; }
  textarea.comment { min-height: 70px; }
  button { background: var(--accent); color: var(--accent-ink); border: 0; border-radius: 8px;
           padding: 11px 22px; font-family: inherit; font-size: 15px; font-weight: 600; cursor: pointer; }
  button:disabled { opacity: .5; cursor: default; }
  .actions { display: flex; justify-content: flex-end; gap: 12px; align-items: center; margin-top: 12px; }
  .hint { color: var(--muted); font-size: 14px; }
  .q { margin: 0 0 22px; }
  .scale { display: grid; grid-template-columns: repeat(7, 1fr); gap: 6px; margin-top: 8px; }
  .scale label { display: flex; flex-direction: column; align-items: center; gap: 4px; padding: 8px 0;
                 border: 1px solid var(--line); border-radius: 8px; cursor: pointer; font-size: 14px; }
  .scale input { margin: 0; }
  .ends { display: flex; justify-content: space-between; color: var(--muted); font-size: 13px; margin-top: 4px; }
  .file { font-family: ui-monospace, Menlo, monospace; font-size: 13px; color: var(--muted); margin: 0 0 6px; }
  .memory { white-space: pre-wrap; font: 14px/1.5 ui-monospace, Menlo, monospace; margin: 0; }
  details.role { background: var(--soft); border: 1px solid var(--line); border-radius: 10px;
                 padding: 10px 18px; margin: 0 0 16px; }
  details.role summary { cursor: pointer; font-weight: 600; font-size: 15px; }
  details.role[open] summary { margin-bottom: 4px; }
  details.role > div { max-height: 45vh; overflow-y: auto; }  /* the draft stays in view */
  .center { text-align: center; color: var(--muted); padding: 60px 0; }
  .spinner { width: 28px; height: 28px; border: 3px solid var(--line); border-top-color: var(--accent);
             border-radius: 50%; margin: 0 auto 14px; animation: spin 1s linear infinite; }
  @keyframes spin { to { transform: rotate(360deg); } }
</style>
</head>
<body>
<header><div><span id="who">Email assistant study</span><span id="progress"></span></div></header>
<main id="app"><div class="center"><div class="spinner"></div>Loading...</div></main>
<script>
let seq = -1, state = null;
const app = document.getElementById("app");

function el(tag, attrs, ...kids) {
  const e = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs || {})) {
    if (k === "html") e.innerHTML = v; else if (k.startsWith("on")) e[k] = v; else e.setAttribute(k, v);
  }
  for (const k of kids.flat()) if (k != null) e.append(k.nodeType ? k : document.createTextNode(k));
  return e;
}
function card(label, ...kids) { return el("div", {class: "card"}, label ? el("p", {class: "label"}, label) : null, ...kids); }
function email(text) { return el("pre", {class: "email"}, text || ""); }
function header(t) {
  const lines = [el("p", {class: "meta"}, "To: " + t.to.join("; "))];
  if (t.cc && t.cc.length) lines.push(el("p", {class: "meta"}, "Cc: " + t.cc.join("; ")));
  return lines;
}
function incoming(t) {
  if (!t.incoming) return null;
  return el("div", {class: "card incoming"}, el("p", {class: "label"}, "The email you received"),
    el("p", {class: "meta"}, "From: " + t.incoming.from), el("p", {class: "meta"}, "Subject: " + t.incoming.subject),
    el("div", {style: "height:10px"}), email(t.incoming.body));
}
function request(t) {
  return el("div", {class: "card request"}, el("p", {class: "label"}, "Your request to the assistant (written for you)"),
            email(t.request));
}
async function submit(data, button) {
  if (button) button.disabled = true;
  const r = await fetch("/submit", {method: "POST", headers: {"Content-Type": "application/json"},
                                    body: JSON.stringify({seq: state.seq, ...data})});
  if (!r.ok && button) button.disabled = false;
  poll();
}
const WITH_ROLE = new Set(["revise", "reply", "final", "reveal"]);  // pages that show the role card
let roleOpen = false;  // narrow screens: the panel stays as the participant left it, from page to page
function role(s) {
  if (!s.card_html) return null;
  const d = el("details", {class: "role"}, el("summary", {}, "Your role (click to show or hide)"),
               el("div", {html: s.card_html}));
  d.open = roleOpen;
  d.ontoggle = () => { roleOpen = d.open; };
  return d;
}
function next(label, data) {
  const b = el("button", {onclick: () => submit(data || {}, b)}, label || "Continue");
  return el("div", {class: "actions"}, b);
}

const views = {
  working: s => el("div", {class: "center"}, el("div", {class: "spinner"}), s.message || "One moment..."),
  intro: s => [el("div", {class: "card", html: s.card_html}),
    card("How each email works",
      el("p", {}, "Your request to the assistant is already written for you: you asked for this email earlier. " +
                  "The assistant has drafted it. Your job is to edit the draft into what you would actually send."),
      el("p", {class: "hint"}, "This card stays available at the top of every page, under \"Your role\".")),
    next("Start")],
  revise: s => {
    const draft = el("textarea", {class: "draft"}); draft.value = s.draft;
    const comment = el("textarea", {class: "comment", placeholder: "Optional"});
    const send = el("button", {onclick: () => submit({sent: draft.value, comment: comment.value}, send)}, "Send");
    return [el("h1", {}, "Email " + s.number + " of " + s.total), role(s), incoming(s), request(s),
      el("div", {class: "card draftcard"},
         el("p", {class: "label"}, "The assistant's draft: edit it into what you would actually send"),
         header(s), s.subject ? el("p", {class: "meta"}, "Subject: " + s.subject) : null,
         el("div", {style: "height:8px"}), draft),
      card("Anything you want to tell the assistant?", comment),
      el("div", {class: "actions"}, el("span", {class: "hint"}, "Sending shows the assistant your final version."), send)];
  },
  reply: s => [el("h1", {}, "The assistant replied"), role(s), card(null, email(s.reply || "(no reply)")), next()],
  final: s => [el("h1", {}, "A new email"), role(s), incoming(s), request(s),
    s.draft ? el("div", {class: "card draftcard"},
                 el("p", {class: "label"}, "The assistant's draft (just read it; no need to edit)"), header(s),
                 el("p", {class: "meta"}, "Subject: " + s.draft.subject), el("div", {style: "height:8px"}), email(s.draft.body))
            : card("The assistant replied instead of drafting", email(s.reply)),
    next("Continue to the questions")],
  survey: s => {
    const answers = {};
    const go = el("button", {disabled: "", onclick: () => submit({answers}, go)}, "Continue");
    const qs = s.questions.map(q => {
      const opts = [];
      for (let v = s.scale[0]; v <= s.scale[1]; v++) {
        opts.push(el("label", {}, el("input", {type: "radio", name: q.name, value: v, onchange: () => {
          answers[q.name] = v;
          if (Object.keys(answers).length === s.questions.length) go.disabled = false;
        }}), String(v)));
      }
      return el("div", {class: "q"}, el("div", {}, q.text), el("div", {class: "scale"}, opts),
                el("div", {class: "ends"}, el("span", {}, s.scale_labels[0]), el("span", {}, s.scale_labels[1])));
    });
    return [el("h1", {}, s.part === 1 ? "A few questions" : "One more question"), card(null, qs),
            el("div", {class: "actions"}, el("span", {class: "hint"}, "Answer every question to continue."), go)];
  },
  reveal: s => {
    const files = Object.entries(s.memory);
    return [el("h1", {}, "What the assistant saved about you"), role(s),
      el("p", {class: "hint"}, "This is everything in the assistant's memory after the emails you edited."),
      files.length ? files.map(([path, text]) => card(null, el("p", {class: "file"}, path), el("pre", {class: "memory"}, text)))
                   : card(null, "The memory is empty."),
      next()];
  },
  done: s => el("div", {class: "center"}, el("h1", {}, "Thank you"), "You're finished, and your answers are saved. Please let the facilitator know."),
  error: s => el("div", {class: "center"}, el("h1", {}, "Something went wrong"), "Please let the facilitator know."),
};

async function poll() {
  try {
    const r = await fetch("/state", {cache: "no-store"});
    const s = await r.json();
    if (s.seq !== seq) {
      seq = s.seq; state = s;
      const content = [views[s.step] ? views[s.step](s) : "Unknown step"].flat(Infinity).filter(x => x != null);
      const wide = WITH_ROLE.has(s.step) && !!s.card_html;
      document.body.classList.toggle("wide", wide);
      if (wide) {
        app.replaceChildren(el("div", {class: "layout"},
          el("aside", {class: "side"}, el("p", {class: "label"}, "Your role"), el("div", {html: s.card_html})),
          el("div", {}, ...content)));
      } else {
        app.replaceChildren(...content);
      }
      document.getElementById("progress").textContent = s.step === "revise" ? "Email " + s.number + " of " + s.total : "";
      window.scrollTo(0, 0);
    }
  } catch (e) { /* the run has ended or the server is restarting */ }
}
poll();
setInterval(poll, 700);
</script>
</body>
</html>
"""
