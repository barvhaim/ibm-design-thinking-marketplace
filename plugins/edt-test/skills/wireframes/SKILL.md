---
name: wireframes
description: Draws low-fidelity Wireframes of a digital flow inside an HTML artifact, as grayscale ASCII or SVG frames. It sketches 2–3 different approaches first, runs a quick simulated test of each, then wireframes the chosen flow with annotations and the assumptions to test. Use when the team is just talking about ideas, or someone says "wireframe this", "sketch the screens", "mock up the flow", "what would this look like" or "I need something to show users".
argument-hint: "[flow or Hill] [ascii | svg] [facilitate]"
---

# Wireframes

> IBM Enterprise Design Thinking · Test your ideas · Make, then Reflect · ~60 min

When a team only talks about an idea, everyone pictures a different interface. Wireframes give the idea a concrete form quickly. They are rough digital sketches of screens and flows that people can point at, argue about and test. Keep fidelity deliberately low. That way feedback lands on the flow, the content and whether user needs are met, and nobody spends the session on colors and pixels. Changes are still cheap at this stage, so make lots of variations and throw most of them away.

## When to use it
- When conversations about an idea go in circles and nobody has drawn anything yet.
- After a To-be Scenario Map, Storyboard or Big Idea Vignette, to turn the chosen idea into screens.
- When you need screens for a Cognitive Walkthrough, simulated or with remote users.
- Use `/edt-test:paper-prototypes` instead when it's earlier still and the team is in one room.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of:
  - the user and outcome: `hills-*`, `needs-statements-*`
  - the flow: `to-be-scenario-map-*`, `storyboards-*`, `big-idea-vignettes-*`
  - what to check: `assumptions-and-questions-*`, plus the `assumption` and `simulated` entries in upstream `items`
  - earlier rounds: `wireframes-*`, `feedback-grid-*`, `cognitive-walkthrough-*`
- **The repo's UI, if it has one.** Skim its routes, navigation and components, so the wireframes respect the real structure and constraints. Don't copy its styling.
- **The simulated user panel,** `design-thinking/simulated-users.html`. If it's missing, create it first, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`.
- **Ask the user only for:** the flow's start and end, if no upstream page gives them.

If there is no user or outcome to anchor the screens, say so. A wireframe without a Hill is a guess about features. Suggest `/edt-plan:hills` or `/edt-ideate:to-be-scenario-map` first.

## Co-create with Claude
1. **Gather.** Restate the user, their need and the Hill at the top of the page. Every screen has to serve them. List the upstream assumptions and simulated claims this flow depends on.
2. **Map the flow.** Take the steps from the To-be Scenario Map or Storyboard and list every screen and state the complete experience needs: entry point, main path, and any empty, error or confirmation states the flow will hit.
3. **Diverge first.** For the key screen, draw 2–3 truly different approaches before filling in any detail. Different approaches means different patterns, such as a wizard versus a single form, a list versus a board, or inline editing versus a dialog.
4. **Run a quick simulated test of each approach.** Pick 2–3 contrasting personas from the panel, such as the novice, the expert and the edge case. Give each persona a one-line scenario in their words and show them one approach at a time, as a separate short session, as if they'd never seen the others. Rotate the order across personas. Ask only:
   - "What would you do first here?"
   - "What do you expect to happen?"
   - "Is anything unclear?"

   The persona answers in character, from what's drawn in the frame and nothing else. Record their first move and whether they found the way forward (Found), hesitated (Hesitated) or went the wrong way (Lost). Keep the transcripts, and tag the notes `simulated`. If one approach wins with every persona, check whether you drew the others to lose.
5. **Pick a direction.** Show the user the approaches and the quick-test results, as input, not a verdict. Ask them to pick one, merge them, or ask for more.
6. **Fill in the chosen direction.** Wireframe every screen in the flow:
   - Include every element the task needs.
   - Use real content from the domain, with labels, sample data and copy. Never use lorem ipsum, because people can't react to content that isn't there.
   - Mark annotations in the art: `[A1]` for an assumption and `[Q1]` for a question. Explain each one in the frame's caption.
7. **Iterate.** Explore variations on the parts that carry the most risk:
   - How could the user's options be communicated to them?
   - Which other interface pattern could do this job?

   Record each variation as kept or dropped, with a reason.
8. **Play back regularly.** Share the page at intervals, collect the reactions with `/edt-test:feedback-grid`, and move every assumption and question raised into the list to test. When the whole flow is drawn, run `/edt-test:cognitive-walkthrough` on it.

### Drawing rules (deliberately low fidelity)
The wireframes live inside the page as `.frames`, one `figure.frame` per screen or approach. There is no separate file.
- **Labels:** `frame-n` reads `Step N · <screen>` for screens and `Approach A · <pattern>` for approaches. The caption says the screen's purpose in the flow and explains its annotations.
- **Grayscale only.** Draw in `currentColor`, with gray fills from `currentColor` at low opacity, so the frame works in light and dark themes. No colors, brand, icons, shadows, gradients or animation. Images are boxes with an X and a label.
- **ASCII** (the default, fastest): boxes, `[Button]`, `( ) radio`, `[x] checkbox`, `[____]` inputs and `[IMG]` placeholders. A frame shows about 28 characters by 9 lines before it scrolls, so ASCII suits approach sketches and small screens. Split a bigger screen into two frames, or use SVG.
- **SVG** (`svg`, or any screen too big for ASCII): an inline `<svg viewBox="0 0 320 240">` with `fill="none" stroke="currentColor"` shapes and `<text fill="currentColor">` labels. It scales to the frame. A few lines of inline HTML using only `currentColor` borders work too.
- **Mid fidelity** means a real layout grid, realistic component types and final copy, still in grayscale and still in SVG. Move up to it only once the flow has survived a test.

[examples.md](examples.md) shows an ASCII frame, an SVG frame and a quick-test table.

## Facilitate a live session
Produce `design-thinking/wireframes-<topic>-kit.html`. It needs:
- **Agenda table (60 min):**
  - 0:00–0:05 Intro: present the Hill and the flow to cover; rough is the goal
  - 0:05–0:15 Gather: pin up the needs, Hills, the To-be Scenario Map and the Storyboards, and walk through them
  - 0:15–0:30 Sketch: each person silently sketches at least three different takes on the key screen
  - 0:30–0:45 Iterate: pin up the sketches, borrow and combine ideas, and develop the strongest direction across the whole flow
  - 0:45–0:60 Playback: walk the flow, capture feedback on a Feedback Grid, and mark the assumptions and questions to test
- **Prompts to read aloud:**
  - "Which user need, or which part of the Hill, does this screen serve?"
  - "Draw a different way to do the same job. What pattern haven't we tried?"
  - "How will the user know what their options are here?"
  - "What are we assuming here? Write it on a sticky note and put it on the sketch."
- **Materials:** paper with printed device frames, thick markers (they keep the detail down), sticky notes and dot stickers. Digitally, use a grayscale low-fi kit in Mural or a design tool.
- **Board layout:** the flow steps run left to right as empty `.frames`, with room under each step for sketch variations and the chosen one on top. Assumption and question notes go on the sketches they concern, and a Feedback Grid sits at the end.
- **Clean test frames:** for a session with real users, include the chosen screens without annotation markers, so the facilitator can show them one at a time and play the computer.

After the session, read the photos and redraw the sketches as frames on the results page, keeping each note's tag.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/wireframes-<topic>.html`. The wireframes are drawn on this page.
- **Title:** `<Flow> Wireframes`, for example "Trip Receipts Wireframes". Put the fidelity and round in `.meta`.
- **Sections:**
  1. **User and Hill:** a `.stmts` with the Hill's `Who`, `What` and `Wow` parts and its source pill.
  2. **Flow:** a table of step, screen, purpose and the states it needs.
  3. **Approaches:** `.frames`, one per approach for the key screen. Each caption names the pattern and its trade-off, with a `data-tone="good"` "Chosen" pill on the one you kept.
  4. **Quick test:** a table with one row per approach and one column per persona, each cell holding the first move and a `data-tone` pill (`good` Found, `warn` Hesitated, `bad` Lost). Then one `.cluster` of `simulated` notes per approach.
  5. **Screens:** `.frames` for the whole chosen flow, in step order, including empty, error and confirmation states.
  6. **Variations explored:** a table of screen, variation, pattern, and kept or dropped with the reason.
  7. **Assumptions and questions to test:** a table of ID, the item with its tag pill, where it came from (an upstream page or a screen), the quick-test signal, and how to test it. The quick-test signal is a `data-tag="simulated"` pill reading "Simulated: supported" or "Simulated: contradicted", or "Untested". Nothing here is Validated until real users have tried it.
  8. **Feedback so far:** tagged notes in one `.cluster` per feedback group (Users, Simulated users, Team and stakeholders), each saying what changed, or a link to the `feedback-grid-*` page.
  9. **Quick-test transcripts:** a `details.transcript` per persona and approach, with persona turns as `turn sim`.
  10. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "hill": { "who": "", "what": "", "wow": "", "from": "design-thinking/hills-receipts.html" },
    "fidelity": "low|mid", "art": "ascii|svg",
    "flow": [{ "step": 1, "screen": "", "purpose": "", "states": ["empty", "error"] }],
    "approaches": [{ "id": "A", "pattern": "", "tradeoff": "", "chosen": true,
                     "quick_test": [{ "persona": "SU-1", "first_move": "", "result": "found|hesitated|lost", "notes": ["N2"] }] }],
    "screens": [{ "step": 1, "name": "", "approach": "A", "annotations": ["A1", "Q1"] }],
    "variations": [{ "screen": 2, "variation": "", "pattern": "", "kept": false, "why": "" }],
    "to_test": [{ "id": "A1", "text": "", "tag": "assumption|question", "from": "", "signal": "simulated-supported|simulated-contradicted|untested", "test": "" }],
    "feedback": [{ "note": "N7", "group": "user|simulated|teammate|stakeholder", "change": "" }] }
  ```
  `items` holds every note and annotation, with `group` set to `"Approach <id>"`, `"Step <n>"` or `"Feedback / <group>"`.

## Quality checks
- Every screen traces back to a step in the flow and to a user need or a Hill.
- The flow is complete: someone can reach the goal without the designer narrating.
- The team diverged before it converged, with at least two real alternatives for the key screen.
- Fidelity stays low: grayscale, `currentColor`, no polish. If the feedback is about colors or fonts, strip it back. Each frame's art fits without scrolling.
- The content is real, and the assumptions and questions are marked in the art and listed for testing.
- The quick test personas behave differently and don't all like every approach. A persona reacts only to what's drawn, never to the designer's intent.
- Quick-test results are counts of simulated users ("2 of 3 hesitated on approach B"), never percentages, and never mark anything Validated. Team reactions at a Playback are teammate feedback, not user validation.
- Common pitfalls:
  - wireframing the solution the team already decided on
  - covering only the happy path
  - jumping to mid fidelity before testing
  - one perfect screen instead of a whole rough flow

## Next
- `/edt-test:cognitive-walkthrough`: walk the whole flow, with simulated users and then real ones.
- `/edt-test:feedback-grid`: sort the feedback from playbacks and tests.
- `/edt-align:playbacks`: show the flow and the open assumptions to stakeholders.
- `/edt-plan:user-stories`: turn a tested flow into stories for delivery.

## Source
[IBM Enterprise Design Thinking Toolkit: Wireframes](https://www.ibm.com/downloads/documents/us-en/137a3e34823ed9a6)
