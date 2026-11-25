---
name: wireframes
description: Create low- to mid-fidelity Wireframes of a digital UI, as ASCII or a single grayscale HTML file, to get quick feedback on flow and content before visual design or code. Explores variations and marks the assumptions to test. Use when the team is just talking about ideas, or someone says "wireframe this", "sketch the screens", "mock up the flow", "what would this look like" or "I need something clickable to show users".
argument-hint: "[flow or Hill] [ascii | html] [facilitate]"
---

# Wireframes

> IBM Enterprise Design Thinking · Test your ideas · Make, then Reflect · ~60 min

When a team only talks about an idea, everyone pictures a different interface. Wireframes give the idea a concrete form quickly. They are rough digital sketches of screens and flows that people can point at, argue about and test. Keep fidelity deliberately low. That way feedback lands on the flow, the content and whether user needs are met, and nobody spends the session on colors and pixels. Changes are still cheap at this stage, so make lots of variations and throw most of them away.

## When to use it
- When conversations about an idea go in circles and nobody has drawn anything yet.
- After a To-be Scenario Map, Storyboard or Big Idea Vignette, to turn the chosen idea into screens.
- When you need something clickable for a Cognitive Walkthrough with remote users.
- Use `/edt-test:paper-prototypes` instead when it's earlier still and the team is in one room.

## Inputs
- From `design-thinking/`: `hills-*`, `needs-statements-*`, `to-be-scenario-map-*`, `storyboards-*`, `big-idea-vignettes-*` and `assumptions-and-questions-*`.
- If the repo already has a UI, skim its routes, navigation and components, so the wireframes respect the real structure and constraints. Don't copy its styling.
- Ask the user for:
  - the target user and the outcome, ideally a Hill
  - the flow to cover, with its start and end
  - who will give feedback
  - the format: ASCII (the default, fastest) or HTML (clickable, good for showing users)

If there is no user or outcome to anchor the screens, say so. A wireframe without a Hill is a guess about features. Suggest `/edt-plan:hills` or `/edt-ideate:to-be-scenario-map` first.

## Co-create with Claude
1. **Gather.** Restate the user, their need and the Hill in two or three lines at the top of the artifact. Every screen has to serve them.
2. **Map the flow.** Take the steps from the To-be Scenario Map or Storyboard and list every screen and state the complete experience needs: entry point, main path, and any empty, error or confirmation states the flow will hit.
3. **Sketch at low fidelity, and diverge first.** For the key screen, draw 2–3 truly different approaches in ASCII before filling in any detail. Different approaches means different patterns, such as a wizard versus a single form, a list versus a board, or inline editing versus a dialog. Ask the user to pick one, merge them, or ask for more.
4. **Fill in the chosen direction.** Wireframe every screen in the flow:
   - Include every element the task needs.
   - Use real content from the domain, with labels, sample data and copy. Never use lorem ipsum, because people can't react to content that isn't there.
   - Mark annotations inline: `[A1]` for an assumption and `[Q1]` for a question.
5. **Iterate.** Explore variations on the parts that carry the most risk:
   - How could the user's options be communicated to them?
   - Which other interface pattern could do this job?
   Record each variation as kept or dropped, with a reason.
6. **Render the format the user chose.**
   - **ASCII:** inline in the artifact, one block per screen, about 60 characters wide, using boxes, `[Button]`, `( ) radio`, `[x] checkbox`, `[____]` inputs and `[ IMG ]` placeholders.
   - **HTML:** one self-contained file at `design-thinking/wireframes-<topic>.html`, following the rules below. Link it from the markdown artifact. For a starting skeleton, see [examples.md](examples.md).
7. **Play back regularly.** Share the screens at intervals, collect the reactions with `/edt-test:feedback-grid`, and move every assumption and question raised into the list to test with users.

**HTML rules (deliberately low fidelity):**
- One file, with inline CSS and at most a few lines of JS. No external fonts, images, CDNs or frameworks, so it opens offline from disk.
- Grayscale only: white, two or three grays, near-black. One system sans-serif font. No brand colors, icons, shadows, gradients or animation. Images are gray boxes with an X and a label.
- Each screen is a section labeled `Step N · <name>`. Buttons and links that move the flow forward jump to the next screen, so testers can click through it. Controls that don't do anything look normal, and a banner says that not everything works.
- A banner at the top: "Low-fidelity wireframe for feedback on flow and content, not visual design."
- Annotations sit in a margin that a single checkbox can hide, so you can hide them during user tests.
- Use real `<button>`, `<a>` and `<label>` elements, so the wireframe works with a keyboard.
- **Mid fidelity** means a real layout grid, realistic component types and final copy, still in grayscale. Move up to it only once the flow has survived a test.

## Facilitate a live session
**Agenda (60 min):**
- 0:00–0:05 · **Intro.** Present the Hill and the flow to cover, and say that rough is the goal.
- 0:05–0:15 · **Gather.** Pin up the needs, Hills, the To-be Scenario Map and the Storyboards, and walk through them.
- 0:15–0:30 · **Sketch.** Each person sketches at least three different takes on the key screen, silently.
- 0:30–0:45 · **Iterate.** Pin up the sketches, borrow and combine ideas, and develop the strongest direction across the whole flow.
- 0:45–0:60 · **Playback.** Walk the flow, capture feedback on a Feedback Grid, and mark the assumptions and questions to test with users.

**Prompts to read aloud:**
- "Which user need, or which part of the Hill, does this screen serve?"
- "Draw a different way to do the same job. What pattern haven't we tried?"
- "How will the user know what their options are here?"
- "What are we assuming here? Write it on a sticky note and put it on the sketch."

**Materials:** paper with printed device frames, thick markers (they keep the detail down), sticky notes and dot stickers. Digitally, use a grayscale low-fi kit in Mural or a design tool.

**Board layout:** the flow steps run left to right. Under each step, a column holds the sketch variations, with the chosen one on top. Assumption and question sticky notes go on the sketches they concern, and a Feedback Grid sits at the end. Afterward, share photos, and Claude turns them into ASCII or HTML.

## Output
Save to `design-thinking/wireframes-<topic>.md`, plus `design-thinking/wireframes-<topic>.html` if you chose HTML:

```markdown
# Wireframes: <flow>

- User and need / Hill:
- Fidelity: low / mid · Format: ASCII / HTML (<path>)
- Built from: <upstream artifacts>

## Flow
1. <screen> → 2. <screen> → …

## Variations explored
| Screen | Variation | Pattern / idea | Kept? Why |
| --- | --- | --- | --- |

## Screens
### Step 1 · <name>
<ASCII block, or a link to the HTML section>
- Purpose in the flow:
- Annotations: [A1] … [Q1] …

## Assumptions and questions to test
| ID | Item | Tag (Assumption / Question) | How to test |
| --- | --- | --- | --- |

## Feedback so far
| Feedback | Source (who, group) | Tag | Change made |
| --- | --- | --- | --- |

## Playback
- Key takeaways (3–5):
- Assumptions and questions to validate next:
- Recommended next activity:
```

## Quality checks
- Every screen traces back to a step in the flow and to a user need or a Hill.
- The flow is complete: someone can reach the goal without the designer narrating.
- The team diverged before it converged, with at least two real alternatives for the key screen.
- Fidelity stays low. If the feedback is about colors or fonts, strip the polish back.
- The content is real, and the assumptions and questions are marked and listed for testing.
- Team reactions at a Playback are recorded as teammate feedback, not as user validation.
- Common pitfalls:
  - wireframing the solution the team already decided on
  - covering only the happy path
  - jumping to mid fidelity before testing
  - one perfect screen instead of a whole rough flow

## Next
- `/edt-test:cognitive-walkthrough`: test the flow with real users.
- `/edt-test:feedback-grid`: sort the feedback from playbacks and tests.
- `/edt-align:playbacks`: show the flow and the open assumptions to stakeholders.
- `/edt-plan:user-stories`: turn a tested flow into stories for delivery.

## Source
[IBM Enterprise Design Thinking Toolkit: Wireframes](https://www.ibm.com/downloads/documents/us-en/137a3e34823ed9a6)
