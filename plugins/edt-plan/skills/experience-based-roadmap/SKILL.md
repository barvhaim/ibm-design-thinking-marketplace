---
name: experience-based-roadmap
description: Turn a long-term vision into a three-stage roadmap of user outcomes ("Our user can…"). Stage 1 is what we know we'll build, Stage 2 what we think we'll build, Stage 3 what we might build, and each stage is a complete, usable slice. Use when a team asks "build our roadmap", "what's our MVP", "what goes in v1 versus later", or "slice this vision into releases", or when a feature-list roadmap needs reframing around users.
argument-hint: "[product, Hill or vision] [facilitate]"
---

# Experience-based Roadmap

> IBM Enterprise Design Thinking · Plan your work · Reflect · ~60 min

Feature roadmaps say what the team will ship. Experience-based roadmaps say what users will be able to do, and when. In this activity the team reflects together to scope a long-term experience into stages. Each stage gives users at least one complete task they can achieve. That matches what a minimum viable product really is: delivering just enough to learn how to move forward. A true MVP is a full experience that works, so it's functional, reliable, usable and even delightful. Think of a thin slice of pizza that still has crust, sauce and toppings, not a crust with no toppings. The result gives the team clarity for near-term action and a vision for the long-term outcome.

## When to use it
- Once the team has identified users' real problems and needs and has ideas for addressing them.
- When defining an MVP or a first release, so it delivers a complete experience rather than one layer of the stack.
- When an existing roadmap is a list of features and nobody can say what a user gets at each step.
- After prioritizing, to turn "what matters" into "what comes when".

## Inputs
- Upstream artifacts in `design-thinking/`: `hills-*` (the long-term vision), `to-be-scenario-map-*`, `big-idea-vignettes-*`, `prioritization-grid-*`, `needs-statements-*` and `user-stories-*`.
- What to ask the user for if missing: the long-term vision or Hills, the target user, the ideas or capabilities in play, the release horizon (for example, quarters), and hard constraints such as commitments, dependencies and capacity.
- If there are no needs statements and no ideas yet, this activity is premature. Suggest `/edt-synthesize:needs-statements` or `/edt-ideate:big-idea-vignettes`.

## Co-create with Claude
1. **Ground.** List `design-thinking/` and read the upstream artifacts. Restate the vision and the Hills it serves, the target user, and the candidate ideas, with tags. Confirm what "short term" and "long term" mean in calendar terms for this team.
2. **Set up the frame.** Head the roadmap "Our <user> can… / will be able to…". Short term goes on the left and long term on the right.
3. **Ideate user tasks.** Finish the sentence with as many user tasks as possible, drawing on the to-be scenario, the grid and the stories. Ask the user to add more.
   - Convert feature language into experience language as you go, for example "SSO integration" becomes "Our user can sign in with their work account". Point out each conversion.
   - Infrastructure that doesn't map to a user task goes in a separate "Enablers" list. It isn't a roadmap item.
4. **Sort.** Place each task on the continuum from short term to long term, relative to the others. For each task, ask:
   - Does it depend on another task?
   - How important is it? Use the prioritization grid if one exists.
   - How confident are we that users need it? Check the evidence tags.
   - Does it need to happen soon, or can it wait?
5. **Establish three stages.** Draw two lines that divide the continuum into three stages:
   - **Stage 1, we know we'll build this.** It's committed and backed by evidence.
   - **Stage 2, we think we'll build this.** It's likely, but it depends on what Stage 1 teaches.
   - **Stage 3, we might build this.** It's the vision, still open.
6. **Check each stage is a slice.** Every stage must let the user complete at least one end-to-end task. Walk the user through that task and check it against the pyramid: functional, reliable, usable, delightful. If Stage 1 is "the backend" or "the data model", it's a layer, not a slice, so rework it.
7. **Write the promotion criteria.** For Stage 2 and Stage 3 items, note what evidence or result would move them forward a stage. This links the roadmap to learning instead of dates.
8. **Play back.** Narrate each stage as a short user story, for example "In Stage 1, <user> can…". Stage 1 feeds the next planning session. Write the Playback section and save the artifact.

## Facilitate a live session
**Agenda (60 min)**
| Time | Step | What happens |
| --- | --- | --- |
| 0:00 | Intro | Why experiences beat features, the MVP pizza slice, the rules |
| 0:07 | Set up | Write "Our user can…" across the top of the sheet. Label it Short term on the left and Long term on the right |
| 0:10 | Ideate | Silent writing of user tasks, one per sticky, finishing the sentence |
| 0:22 | Sort | Post the stickies and reposition them relative to each other: now or later? |
| 0:37 | Establish | Draw two lines to make three stages. Check that each stage holds at least one complete task |
| 0:50 | Playback | One person plays back each stage. Pull the Stage 1 stickies for the next planning session |

**Prompts to read aloud**
- "Finish the sentence: our user can… Start each sticky with a verb the user does."
- "If we shipped only this stage, could a user finish a real task end to end?"
- "Is this a slice of the pizza, or just the crust?"
- "What would we need to learn to move this from 'we think' to 'we know'?"

**Materials:** a large sheet of paper or a Mural canvas, sticky notes, markers, a timer, and the Hills and prioritization grid posted nearby.

**Board layout:** across the top, "Our user can… / will be able to…". Along a horizontal axis, Short term on the left and Long term on the right. Later, two vertical lines create Stage 1 "We know", Stage 2 "We think" and Stage 3 "We might". Keep a strip at the bottom for Enablers and a Parking lot.

**After the session:** digitize the stickies stage by stage into the Output template, keeping each one's wording.

## Output
Save to `design-thinking/experience-based-roadmap-<topic>.md` using this template:

```markdown
# Experience-based Roadmap: <product or Hill>
Vision: <long-term outcome> · Hills: <links> · Horizon: <for example Q1–Q4>

## Our <user> can…

### Stage 1: we know we'll build this (<timeframe>)
End-to-end task a user can complete: <one sentence>
| Our user can… | Hill | Basis (Evidence / Assumption) | Depends on |
| --- | --- | --- | --- |
Slice check: [ ] functional [ ] reliable [ ] usable [ ] delightful

### Stage 2: we think we'll build this (<timeframe>)
End-to-end task: …
| Our user can… | Hill | Basis | Moves to Stage 1 if… |
| --- | --- | --- | --- |

### Stage 3: we might build this
End-to-end task: …
| Our user can… | Hill | Basis | Moves forward if… |
| --- | --- | --- | --- |

## Enablers (not user outcomes)
- <technical groundwork, and which stage needs it>

## Parked
- <task>: <why>

## Playback
- Key takeaways: <3–5 bullets>
- Assumptions and questions to validate: …
- Next activity: …
```

## Quality checks
- **Experiences, not features.** Every item starts "Our user can…" followed by a user action and outcome. Reject component names like "API v2", "dashboard" or "ML model".
- **The items are written from the user's point of view.** You should be able to read any item to a sponsor user and have them nod or object.
- **Each stage contains at least one complete task,** usable end to end. A stage that only makes sense after the next one ships is a layer, not a slice.
- **Confidence falls honestly from left to right.** Stage 1 items carry Evidence. Stage 3 items can be Assumptions, but they're labelled.
- **Stage 1 is concrete enough to write user stories from tomorrow.** Stage 3 is still ambitious enough to inspire.
- **No firm dates are promised for Stage 3,** and Stage 2 dates depend on what Stage 1 teaches.
- **Every item traces to a Hill.** Items that don't are challenged or parked.

## Next
- `/edt-plan:user-stories`: break the Stage 1 items into stories with acceptance criteria.
- `/edt-plan:assumptions-and-questions`: list what must be learned to promote Stage 2 items.
- `/edt-plan:research-plan`: schedule that learning ahead of the next iteration.
- `/edt-align:playbacks`: play the roadmap back to stakeholders and sponsor users.

## Source
[IBM Enterprise Design Thinking Toolkit: Experience-based Roadmap](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac15)
