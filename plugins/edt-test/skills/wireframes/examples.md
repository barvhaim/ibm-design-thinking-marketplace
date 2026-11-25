# Wireframes: format examples

These examples show the markup and the fidelity level only. The content is illustrative (a hypothetical expense flow), not research. Every snippet goes inside a `<section class="sec">` of the page built from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`. There is no separate wireframe file.

## Approaches as ASCII frames

Two truly different patterns for the key screen: start from the trip, or start from the receipt. Each ASCII frame stays within 28 characters by 9 lines, so it fits the frame without scrolling on narrow screens.

```html
<div class="frames">
  <figure class="frame" style="margin:0">
    <div class="frame-art" aria-hidden="true">+--------------------------+
| Trips needing receipts   |
| Austin, 3-5 Mar    $412  |
|      [Add receipts] [A1] |
| Boston, 20 Feb      $96  |
|      [Add receipts]      |
| Month closes in 4 days   |
|                     [Q1] |
+--------------------------+</div>
    <figcaption class="frame-cap"><span class="frame-n">Approach A · Trip list</span>
      <p>Start from the trip and attach receipts to it. Familiar to travelers, but slow when receipts arrive before the trip exists. <span class="pill" data-tone="good">Chosen</span></p>
      <p>[A1] Users think in trips, not receipts. [Q1] Does the close date create urgency, or anxiety?</p></figcaption>
  </figure>
  <figure class="frame" style="margin:0">
    <div class="frame-art" aria-hidden="true">+--------------------------+
| [ Snap a receipt ]       |
|                          |
| Unmatched receipts (2)   |
| [IMG] Taxi, 5 Mar    $38 |
| [IMG] Hotel, 3 Mar  $310 |
|                          |
| [ Match to a trip > ][A2]|
+--------------------------+</div>
    <figcaption class="frame-cap"><span class="frame-n">Approach B · Receipt first</span>
      <p>Capture each receipt on the spot and match it to a trip later. Fast in the moment, but adds a matching step.</p>
      <p>[A2] Users will come back to match receipts.</p></figcaption>
  </figure>
</div>
```

Keep the art flush against the opening `<div>` and the closing `</div>`, since `.frame-art` preserves whitespace.

## A screen as an SVG frame

Use SVG for any screen too big for ASCII, and for mid fidelity. A `viewBox` of `0 0 320 240` matches the frame's 4:3 shape and scales with it. Shapes use `stroke="currentColor"` and texts use `fill="currentColor"`, so the frame works in light and dark themes. Start the `<svg>` right after the opening `<div>`.

```html
<figure class="frame" style="margin:0">
  <div class="frame-art" aria-hidden="true"><svg viewBox="0 0 320 240" fill="none" stroke="currentColor" stroke-width="1.2" font-size="11">
<rect x="6" y="6" width="308" height="228" rx="4"/>
<line x1="6" y1="40" x2="314" y2="40"/>
<rect x="18" y="72" width="284" height="44"/>
<rect x="214" y="82" width="78" height="24" rx="3"/>
<rect x="18" y="124" width="284" height="44"/>
<rect x="214" y="134" width="78" height="24" rx="3"/>
<rect x="18" y="200" width="96" height="24" rx="3"/>
<g fill="currentColor" stroke="none">
<text x="18" y="28">Expenses</text><text x="302" y="28" text-anchor="end">Maya R. ▾</text>
<text x="18" y="62" font-weight="600">Trips needing receipts (2)</text><text x="302" y="62" text-anchor="end">[A1]</text>
<text x="28" y="90">Austin client visit</text><text x="28" y="106">3–5 Mar · $412</text>
<text x="253" y="98" text-anchor="middle" font-size="10">Add receipts</text>
<text x="28" y="142">Boston offsite</text><text x="28" y="158">20 Feb · $96</text>
<text x="253" y="150" text-anchor="middle" font-size="10">Add receipts</text>
<text x="18" y="190">Month closes in 4 days</text><text x="302" y="190" text-anchor="end">[Q1]</text>
<text x="66" y="216" text-anchor="middle" font-size="10">New expense</text>
</g></svg></div>
  <figcaption class="frame-cap"><span class="frame-n">Step 1 · Trips needing receipts</span>
    <p>Entry point. Shows only the trips still missing receipts, so the user sees what's left before the month closes.</p></figcaption>
</figure>
```

An image placeholder is a gray box with an X and a label:

```html
<rect x="18" y="72" width="120" height="90" fill="currentColor" fill-opacity=".12"/>
<line x1="18" y1="72" x2="138" y2="162"/><line x1="138" y1="72" x2="18" y2="162"/>
<text x="78" y="178" text-anchor="middle" fill="currentColor" stroke="none">Receipt photo</text>
```

## Quick test of the approaches

One row per approach, one column per persona. Each cell holds the persona's first move and an outcome pill. Report counts of simulated users, never percentages.

```html
<div class="table-wrap"><table>
  <thead><tr><th>Approach</th><th>SU-1 Dana <span class="pill" data-tag="simulated">Simulated</span></th><th>SU-3 Iris <span class="pill" data-tag="simulated">Simulated</span></th></tr></thead>
  <tbody>
    <tr><td>A · Trip list</td><td>Taps "Add receipts" on Austin <span class="pill" data-tone="good">Found</span></td><td>Looks for a camera button first <span class="pill" data-tone="warn">Hesitated</span></td></tr>
    <tr><td>B · Receipt first</td><td>Unsure what "unmatched" means <span class="pill" data-tone="warn">Hesitated</span></td><td>Snaps the taxi receipt <span class="pill" data-tone="good">Found</span></td></tr>
  </tbody>
</table></div>

<details class="transcript">
  <summary>Quick test: SU-3 Iris on approach A <span class="pill" data-tag="simulated">Simulated</span></summary>
  <div class="turns">
    <div class="turn"><span class="who">Facilitator</span><p>You're back from Austin and want your $412 back. What would you do first here?</p></div>
    <div class="turn sim"><span class="who">SU-3 Iris</span><p>I'd look for a camera button. The receipts are in my bag, not in some trip. I don't see one, so… "Add receipts", I suppose? I'd expect it to open the camera.</p></div>
  </div>
</details>
```
