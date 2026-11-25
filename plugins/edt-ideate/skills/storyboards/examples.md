# Storyboard page: worked example

> **Hypothetical example.** It shows the page's markup only. The personas are simulated, and nothing here is real user research.

- **Idea:** "Ready Desk" (`I7`), from a hypothetical Big Idea Vignettes round
- **Character:** SU-6 Sam Ilves, a new hire on her first day, from the simulated panel
- **Skeptic:** SU-8 Dot Marlowe, a facilities coordinator who owns the floor plan
- **Need:** new hires need a way to start working on day one, so that they don't spend the morning chasing IT and facilities

These snippets go inside `<main>` of a page built from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`. Escape `<`, `>` and `&` inside ASCII art.

## Frames: one ASCII, one SVG

Keep ASCII frames to about 24 characters wide. Draw SVG frames with `stroke="currentColor"` and `fill="none"`, and text with `fill="currentColor"`, so they follow the theme.

```html
<div class="frames">
  <figure class="frame" style="margin:0">
    <div class="frame-art" aria-hidden="true">   o    (where do I
  /|\    even sit?)
  / \   [phone]
______________________
 LOBBY  ▢ ▢ ▢    ▢ ▢</div>
    <figcaption class="frame-cap">
      <span class="frame-n">Frame 1 · Lobby, 8:55</span>
      <span class="mood" data-mood="low">Low</span>
      <p>Today, a first day starts with waiting.</p>
    </figcaption>
  </figure>
  <figure class="frame" style="margin:0">
    <div class="frame-art" aria-hidden="true"><svg viewBox="0 0 240 180" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round">
      <circle cx="70" cy="62" r="12"/><path d="M70 74v40M70 86l-18 16M70 86l18 16M70 114l-14 30M70 114l14 30"/>
      <rect x="140" y="58" width="64" height="42" rx="3"/><path d="M150 68l44 22M194 68l-44 22"/>
      <path d="M118 112h104M132 112v34M208 112v34"/>
      <text x="148" y="42" fill="currentColor" stroke="none" font-size="16" font-weight="700">NOTHING.</text>
    </svg></div>
    <figcaption class="frame-cap">
      <span class="frame-n">Frame 3 · Twist</span>
      <span class="mood" data-mood="low">Low</span>
      <p>Sam finds her desk, but the monitor is dead. “Of course.”</p>
      <p><span class="pill" data-tag="question">Q · broken desk</span></p>
    </figcaption>
  </figure>
</div>
```

## Reactions

One column per persona. Each note starts with the frame it's about. The skeptic objects to something specific.

```html
<div class="cols">
  <div class="col"><h3>SU-6 Sam, the character</h3><div class="notes">
    <article class="note" data-tag="simulated"><p>Frame 2: “Nobody sent me an app before day one. I'd have looked in my personal email, if anywhere.”</p><span class="src">SU-6 · reaction</span></article>
    <article class="note" data-tag="simulated"><p>Frame 4: “I wouldn't swap desks on day one. I'd sit at the broken one and wait for someone.”</p><span class="src">SU-6 · reaction</span></article>
  </div></div>
  <div class="col"><h3>SU-8 Dot, the skeptic</h3><div class="notes">
    <article class="note" data-tag="simulated"><p>Frame 4: “If people can swap desks, my floor plan is wrong by lunch. I'd turn that off.”</p><span class="src">SU-8 · reaction</span></article>
  </div></div>
</div>
```

## Labels

```html
<div class="notes">
  <article class="note" data-tag="assumption"><p>Frame 2: Sam would trust a desk assigned before she arrives.</p></article>
  <article class="note" data-tag="question"><p>Frame 3: What happens when the assigned desk is broken?</p></article>
</div>
```

## Data block (excerpt)

```json
{ "schema": "edt-artifact/1", "activity": "storyboards", "plugin": "edt-ideate", "topic": "ready desk",
  "date": "2026-11-25", "mode": "co-create",
  "upstream": ["design-thinking/big-idea-vignettes-new-hire-desk.html", "design-thinking/simulated-users.html"],
  "users": { "real": [], "simulated": ["SU-6", "SU-8"] },
  "content": {
    "idea": { "id": "I7", "headline": "Ready Desk", "source": "design-thinking/big-idea-vignettes-new-hire-desk.html" },
    "character": { "persona": "SU-6", "name": "Sam Ilves", "role": "New hire, first day" }, "skeptic": "SU-8",
    "frames": [
      { "n": 1, "title": "Lobby, 8:55", "art": "ascii", "thinks": "Where do I even sit?", "mood": "low", "labels": [] },
      { "n": 3, "title": "Twist", "art": "svg", "says": "Of course.", "burst": "NOTHING.", "mood": "low", "labels": ["N11"] } ],
    "reactions": [{ "persona": "SU-8", "as": "skeptic", "frame": 4, "note": "N7" }],
    "changes": [{ "frame": 4, "change": "Swapping now asks facilities first", "prompted_by": "N7" }] },
  "items": [{ "id": "N7", "text": "Frame 4: If people can swap desks, my floor plan is wrong by lunch.", "tag": "simulated", "source": "SU-8", "group": "Reactions / SU-8" }],
  "playback": { "takeaways": ["..."], "validate": [{ "text": "Facilities would accept self-service desk swaps", "tag": "simulated" }],
                "next": "/edt-test:feedback-grid" } }
```
