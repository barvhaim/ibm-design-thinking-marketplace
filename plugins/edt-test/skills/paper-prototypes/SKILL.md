---
name: paper-prototypes
description: Plan, build and share a Paper Prototype, a fast and cheap hand-made model of an idea's task flow built from movable paper pieces, so you can discuss or test it before anyone writes code. Produces the purpose, a step-by-step task flow, a build list, a share plan and what you learned. Use early in an idea, or when someone says "let's mock it up quickly", "prototype this on paper", "test the concept before we build" or "try the flow with users".
argument-hint: "[idea or flow] [facilitate]"
---

# Paper Prototypes

> IBM Enterprise Design Thinking · Test your ideas · Make, then Observe · ~60 min

Paper is the cheapest way to give an abstract idea a concrete form. Paper, tape and a pen are enough to make a flow that someone can hold, react to and try. A paper prototype costs minutes to make, so nobody is attached to it. That makes people more willing to throw a piece away, and more willing to give honest criticism. The goal is to play and to learn while the stakes are low. Making also teaches the team something on its own: every piece you crumple up is a thing you now know doesn't work.

## When to use it
- In the first stages of an idea, before wireframes or code.
- When a Big Idea, a Storyboard or a To-be Scenario Map needs something tangible people can react to.
- When you want users or teammates to try a flow in person, at a workshop, a Playback or a sponsor user session.
- When the team keeps describing the idea in words and everyone pictures something different.

## Inputs
- From `design-thinking/`: `to-be-scenario-map-*`, `storyboards-*`, `big-idea-vignettes-*`, `hills-*`, `needs-statements-*` and `assumptions-and-questions-*`.
- Ask the user for:
  - the idea and the user it serves
  - who will see the prototype (peers, stakeholders or users)
  - whether the team is co-located, since paper works best in a room. A remote team can use `/edt-test:wireframes` instead.

## Co-create with Claude
Claude can't cut paper, but it can plan the prototype in detail, guide the build, and digitize the results afterward.

1. **Decide the purpose.** Pick what this prototype is for, because the purpose shapes everything else:
   - **Communicate** the idea to peers or stakeholders and get their reactions.
   - **Test** the idea with users to see whether it works.
   - **Explore** the idea by making it, so the team learns as it builds.

   Write down the Hill or the assumptions it should inform.
2. **Document the task flow.** Break the experience the user will go through into ordered steps, and be meticulous. For each step, record:
   - what the user sees
   - what they do
   - what happens next

   Include any error, empty or confirmation state that the flow needs. A missing step will stall the test.
3. **Write the build list.** Turn every step into paper pieces:
   - one base sheet per screen or surface
   - separate, movable pieces for anything that changes, such as menus, dialogs, messages, selected states and typed-in text (sticky notes work well for these)

   Label each piece with its step number. For each piece, give a rough ASCII sketch as a guide, not a design. Keep words and visual detail to the minimum the idea needs.
4. **Make it.** The team builds from the step list without skipping a step. Encourage fast attempts: try a layout, crumple it, try another. Log every discarded attempt with one line on why it didn't work. These are findings too.
5. **Plan the share.** Choose a mode that fits the purpose:
   - **Demo and ask:** walk peers or stakeholders through the flow, then ask for direct feedback.
   - **Let them drive:** give a user the scenario and have them complete the flow while thinking aloud. One teammate plays the "computer" and swaps pieces in response to taps, without speaking. For the scenario, script and neutral prompts, use `/edt-test:cognitive-walkthrough`.

   In both modes, someone takes plenty of notes.
6. **Digitize.** Ask for photos of each screen and the session notes. Claude reads the images, records each piece against its step, and sorts the feedback with `/edt-test:feedback-grid`.
7. **Play back** what you found and what you learned from making it.

## Facilitate a live session
**Agenda (60 min):**
- 0:00–0:05 · **Intro.** Explain the purpose and the Hill or assumption in focus, and reassure people that rough is the point.
- 0:05–0:15 · **Plan.** Teams of 2–3 write the task flow as numbered sticky notes in a row.
- 0:15–0:40 · **Make.** Build one piece per step, keep the pieces modular, and crumple freely.
- 0:40–0:55 · **Share.** Swap with another team, or bring in a sponsor user. One person plays the computer and one takes notes.
- 0:55–0:60 · **Playback.** Each team shares its top findings and one thing it learned from making.

**Prompts to read aloud:**
- "What is this prototype for: to show, to test, or to explore?"
- "Walk the flow step by step. What does the user see, what do they do, and what happens next?"
- "Use the fewest words and lines that still get the idea across."
- "If it isn't working, crumple it up and write down why."
- When sharing: "Don't explain it. Hand it over and watch."

**Materials:** colored paper, tape, pens and thick markers (they stop people from drawing too much detail), sticky notes, scissors, index cards, a cardboard base or clipboard, and transparency sheets for text fields (optional).

**Board layout:** run the task flow as a row of numbered steps across the top. Put the paper pieces for each step beneath it, a "crumpled" column of discarded attempts with their reasons, and a Feedback Grid at the end. On Mural, pin a photo of each piece under its step.

## Output
Save to `design-thinking/paper-prototypes-<topic>.md`:

```markdown
# Paper Prototype: <idea>

- Purpose: Communicate / Test / Explore
- Hill / assumptions it informs:
- For: <user or audience>
- Made by / date:

## Task flow
| Step | User sees | User does | What happens next |
| --- | --- | --- | --- |
| 1 | | | |

## Build list
| Piece | Step | Type (base / overlay / sticky) | Sketch or photo |
| --- | --- | --- | --- |

## Learned from making
| Tried | Why we dropped or changed it |
| --- | --- |

## Share sessions
| Who (role, group) | Mode (demo / let them drive) | Key observations (Evidence) |
| --- | --- | --- |

## Feedback
<summary, or a link to design-thinking/feedback-grid-<topic>.md>

## Assumptions checked
| Assumption | Validated / Invalidated / Inconclusive | Evidence |
| --- | --- | --- |

## Playback
- Key takeaways (3–5):
- Assumptions and questions to validate next:
- Recommended next activity:
```

## Quality checks
- The purpose is stated, and the share mode matches it. You can't "test" a prototype you only demonstrated.
- The task flow is complete enough that someone can reach the end without the maker narrating.
- Pieces are modular and rough, with no polished visuals. If people comment on color or font, it's too refined.
- Discarded attempts are logged with reasons. Making is learning.
- Feedback from users and feedback from teammates are kept apart, and only user feedback validates assumptions about users.
- Common pitfalls:
  - building only the happy path
  - spending the whole hour on one screen
  - explaining the prototype while someone is trying it
  - keeping the prototype to yourself instead of playing it back

## Next
- `/edt-test:cognitive-walkthrough`: run a proper test with users on the paper prototype.
- `/edt-test:feedback-grid`: sort the feedback and decide what changes.
- `/edt-test:wireframes`: move the surviving flow to digital low fidelity.
- `/edt-align:playbacks`: share the findings and what you learned with stakeholders.

## Source
[IBM Enterprise Design Thinking Toolkit: Paper Prototypes](https://www.ibm.com/downloads/documents/us-en/137a1e253e5bac09)
