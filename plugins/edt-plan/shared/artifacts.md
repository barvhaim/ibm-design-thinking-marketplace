# HTML artifacts

Every activity produces one self-contained HTML page. All activities share a single template, so a team's walls look like one toolkit and the next activity can read the last one.

## Build the page

1. **Look at a finished page.** `${CLAUDE_PLUGIN_ROOT}/shared/example-empathy-map.html` shows what a finished page looks like.
2. **Start from the template.** Read `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`. Copy the `<title>`, the metas, the font `<link>`, the whole `<style>` block and the closing `<script>` unchanged. Don't restyle the page or add colors; the template's tokens already cover light and dark themes.
3. **Fill in the header.**
   - **`<title>`:** a short name, `<Topic> <Activity>`, such as "Release Engineer Empathy Map" or "Checkout Hills". Two to five words, with no dash or colon.
   - **Eyebrow:** the toolkit category and the Loop phase.
   - **`h1`:** the activity name, with the topic or user in `.topic`.
   - **`.meta`:** the date, the mode, the upstream artifacts the page builds on, and the users involved (real and simulated).
   - **Simulated banner:** keep `.sim-banner` if anything on the page is simulated, and delete it otherwise.
4. **Build `<main>`.** Use one `<section class="sec">` per part of the activity, built from the components below. Every user-derived item must be a note, dot or pill with a `data-tag`. Keep your words specific: real quotes, named phases, real counts.
5. **End `<main>` with the Playback section,** which has three parts:
   - **Key takeaways:** 3 to 5.
   - **Validate next:** simulated and assumed claims that matter most.
   - **Recommended next:** the next activity as a `.cmd` chip.
6. **Fill in the footer.**
   - **Sources:** one row per source, with `S1…` for real sources and `SU-1…` for simulated users.
   - **Method link:** the activity's toolkit deck.
7. **Fill in `#edt-data`.** Put a JSON mirror of the content (see [Data block](#data-block)) in `<script type="application/json" id="edt-data">`, so other activities can read the page without parsing the HTML.
8. **Write no `<!doctype>`, `<html>`, `<head>` or `<body>` tags.** The page starts with `<title>`. Artifact publishing adds the document skeleton, and browsers render the file fine when opened locally.

## Save, publish, and show

- **Save** the page to `design-thinking/<skill-name>-<topic-slug>.html` at the project root, creating the folder if needed. Write a new version over the same file, unless the user asks to keep the old one. In that case, add a date suffix to the new file's name.
- **Publish.** If this session has an **Artifact** tool, publish the saved file as an artifact:
  - `description`: one sentence.
  - `icon`: one generic word such as `board`, `map`, `chart`, `people` or `idea`, on the first publish only.

  On later changes, republish the same file path, so the link stays the same. Give the user the link.
- **Without an Artifact tool**, give the user the file path and offer to open it with `open <file>` (macOS) or `xdg-open <file>` (Linux).
- **Facilitator kits** (`facilitate` mode) are pages too: `design-thinking/<skill-name>-<topic>-kit.html`. A kit holds:
  - an agenda table with times
  - prompts to read aloud
  - materials
  - the board layout, drawn with the same board components but left empty, or seeded with examples labeled Assumption
  - an empty capture section

  After the session, Claude turns photos or exports of the wall into the results page.

## Read upstream activities

List `design-thinking/`, then read the JSON in each relevant page's `#edt-data` block. A quick way to extract it:

```bash
python3 -c "import re,sys,json;s=open(sys.argv[1]).read();print(json.dumps(json.loads(re.search(r'id=\"edt-data\">(.*?)</script>',s,re.S).group(1)),indent=1))" design-thinking/empathy-map-<topic>.html
```

Older Markdown artifacts (`*.md`) are still valid inputs; read them as text.

## Data block

The data block always has the same envelope. Put the activity's own structure under `content`.

```json
{
  "schema": "edt-artifact/1",
  "activity": "empathy-map",
  "plugin": "edt-synthesize",
  "topic": "release engineer",
  "date": "2026-11-25",
  "mode": "co-create",
  "upstream": ["design-thinking/interviews-release-engineers.html"],
  "users": { "real": [], "simulated": ["SU-1", "SU-2", "SU-3"] },
  "content": { },
  "items": [
    { "id": "N1", "text": "\"Just make an issue.\"", "tag": "simulated", "source": "SU-2", "group": "Says / Hand-offs" }
  ],
  "playback": {
    "takeaways": ["..."],
    "validate": [{ "text": "...", "tag": "simulated" }],
    "next": "/edt-synthesize:needs-statements"
  }
}
```

- `tag` is one of `evidence`, `simulated`, `assumption` or `question`.
- `source` holds source IDs: `S1` for a real source, `SU-1` for a simulated user.
- `items` lists every tagged note on the page, so later activities can trace any claim back to its origin.

## Components

Every note, dot or pill with a `data-tag` is counted by the header filter. The tags are:

| `data-tag` | Meaning | Looks like |
| --- | --- | --- |
| `evidence` | Observed or quoted from a real source | Yellow note |
| `simulated` | Produced by a simulated user | Lavender note with a dashed edge |
| `assumption` | Something the team believes, not yet tested | Pink note |
| `question` | An open unknown | Blue note |

**Sticky notes and clusters**
```html
<div class="cluster">
  <h4>Hand-offs with design</h4>
  <div class="notes">
    <article class="note" data-tag="evidence"><p>"Are the designs done?"</p><span class="src">S2 · interview, 12 Nov</span></article>
    <article class="note" data-tag="simulated"><p>Checks the design channel before every sprint start.</p><span class="src">SU-2 · simulated interview</span></article>
    <article class="note" data-tag="assumption"><p>Feels rushed by leadership near milestones.</p></article>
  </div>
</div>
```
Add `class="note wide"` for a note that should span the full row.

**Quadrants:** empathy map, feedback grid, hopes and fears. Use `.has-center` to put a user in the middle.
```html
<div class="quad has-center">
  <div class="q1"><h3 class="cell-h">Says</h3> …clusters… </div>
  <div class="qc"><div class="avatar" aria-hidden="true">R</div><p class="who">Rafa</p><p class="role">Release engineer, 6 years</p><span class="pill" data-tag="simulated">SU-2</span></div>
  <div class="q2"><h3 class="cell-h">Thinks</h3> … </div>
  <div class="q3"><h3 class="cell-h">Does</h3> … </div>
  <div class="q4"><h3 class="cell-h">Feels</h3> … </div>
</div>
```
Without a center, use `<div class="quad">` and four plain `<div>` cells in reading order.

**Scenario map:** phases across the top, rows down the side. Set `--cols` to the number of phases. On narrow screens the map scrolls sideways inside its own frame.
```html
<div class="scroll"><div class="map" style="--cols: 4">
  <div class="corner"></div><div class="ch">Discover<small>Phase 1</small></div> …one .ch per phase…
  <div class="rh">Doing</div><div><div class="notes">…notes…</div></div> …one cell per phase…
  <div class="rh">Thinking</div> …
  <div class="rh">Feeling</div><div><span class="mood" data-mood="low">Low</span><div class="notes">…</div></div> …
</div></div>
```

**Columns:** retrospectives, roadmaps, stakeholder groups, research plans.
```html
<div class="cols">
  <div class="col"><h3>Went well</h3><div class="notes">…</div></div>
  <div class="col"><h3>To improve</h3><div class="notes">…</div></div>
</div>
```

**Two-axis plot:** prioritization grid, stakeholder influence against interest. `--x` and `--y` run from 0 to 100. Number the dots and list them in the key beside the plot.
```html
<div class="plot-wrap">
  <div class="plot-frame">
    <div class="plot" role="img" aria-label="Ideas plotted by importance and feasibility">
      <span class="zone z-tl">Big bets</span><span class="zone z-tr">No-brainers</span>
      <span class="zone z-bl">Unwise</span><span class="zone z-br">Utilities</span>
      <span class="dot" data-tag="simulated" style="--x: 78; --y: 85">1</span>
    </div>
    <span class="axis x">Feasibility →</span><span class="axis y">Importance →</span>
  </div>
  <ol class="key"><li><span class="n">1</span><span>Release checklist bot <span class="pill" data-tag="simulated">rated by SU-1–SU-3</span></span></li></ol>
</div>
```

**Frames:** storyboards, big idea vignettes, prototype screens, roadmap horizons. The art can be ASCII text or an inline `<svg>` drawn in `currentColor`.
```html
<div class="frames">
  <figure class="frame" style="margin:0">
    <div class="frame-art" aria-hidden="true">┌──────────┐
│ ☐ deploy │
└──────────┘</div>
    <figcaption class="frame-cap"><span class="frame-n">Frame 1 · Setting</span><p>Rafa opens the release board at 8:40.</p></figcaption>
  </figure>
</div>
```

**Statements:** needs statements, Hills, AI intent and reasoning statements.
```html
<div class="stmts">
  <div class="stmt">
    <p class="say"><span class="part" data-label="User">A release engineer</span> needs a way to <span class="part" data-label="Need">see which designs are final</span> so that <span class="part" data-label="Goal">they can cut the build without chasing people</span>.</p>
    <p class="why"><span class="pill" data-tag="simulated">SU-1, SU-2</span><span class="pill" data-tag="evidence">S2</span> Built on: Says / Hand-offs, Feels / Deadline stress</p>
  </div>
</div>
```
For Hills, label the parts `Who`, `What` and `Wow`.

**Simulated users**
```html
<div class="personas">
  <article class="persona">
    <div class="persona-h"><h3>Rafa Okafor</h3><span class="id">SU-2</span></div>
    <p class="role">Release engineer, mid-size SaaS, 6 years</p>
    <blockquote>"I don't need another dashboard. I need to know who to wake up."</blockquote>
    <dl><dt>Goals</dt><dd>…</dd><dt>Pains</dt><dd>…</dd><dt>Context</dt><dd>…</dd><dt>Grounded in</dt><dd>S1 product docs; rest invented</dd></dl>
  </article>
</div>
```

**Transcripts:** simulated interviews and think-alouds. Mark each simulated turn with `class="turn sim"`.
```html
<details class="transcript">
  <summary>Interview with SU-2 Rafa Okafor <span class="pill" data-tag="simulated">Simulated</span></summary>
  <div class="turns">
    <div class="turn"><span class="who">Interviewer</span><p>Tell me about the last release that went wrong.</p></div>
    <div class="turn sim"><span class="who">SU-2 Rafa</span><p>Tuesday. Design pushed a change at 4pm…</p></div>
  </div>
</details>
```

**Tables:** wrap every table so it scrolls inside its own frame.
```html
<div class="table-wrap"><table><thead><tr><th>Assumption</th><th>Risk</th><th>Test</th></tr></thead><tbody><tr><td>…</td><td class="num">3</td><td>…</td></tr></tbody></table></div>
```

**Pills:** use `data-tag` for provenance, and `data-tone="good|warn|bad"` for status, such as Validated, Mixed or Invalidated.
```html
<span class="pill" data-tone="good">Validated</span> <span class="pill" data-tag="question">Open</span>
```
