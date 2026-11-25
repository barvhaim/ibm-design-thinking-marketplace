---
name: user-stories
description: Write user stories, which are short, specific tasks a user must complete to reach a goal. Each traces to a Hill and gets acceptance criteria, a size and an owner, ready for a sprint, and can optionally become GitHub issues once the user confirms. Use when someone asks "write user stories", "break this Hill into tasks", "build our backlog", "add acceptance criteria", "plan the sprint", or "turn this into issues".
argument-hint: "[Hill, roadmap stage or feature] [facilitate]"
---

# User Stories

> IBM Enterprise Design Thinking · Plan your work · Make and Reflect · ~30 min

Requirements written as features say what to build. User stories say what a user must be able to do, so every piece of work can be checked against the value it delivers. A good user story is a short, specific sentence about a single user task, such as "A user can upload her profile picture from her computer". It traces back to a Hill and has acceptance criteria that show when it's really done. Stories turn intent into work the team can pick up in a sprint without losing sight of the user.

## When to use it
- Shortly after writing Hills, to break each Hill into the tasks users must complete.
- When Stage 1 of an experience-based roadmap needs to become sprint-ready work.
- At sprint planning, to select and define the next set of stories.
- When a backlog full of tickets that read like features needs reframing around users.

## Inputs
- Upstream artifacts in `design-thinking/`: `hills-*` (required), `to-be-scenario-map-*` (the user's future steps), `experience-based-roadmap-*` (what's in Stage 1), `prioritization-grid-*`, `needs-statements-*` and any earlier `user-stories-*`.
- What to ask the user for if missing: the Hill or goal, the target user, the sprint length and team members, and the team's definition of done.
- With no Hills, suggest `/edt-plan:hills` first. If the user tasks are unclear, suggest `/edt-ideate:to-be-scenario-map` to map them out.

## Co-create with Claude
1. **Ground.** List `design-thinking/` and read the upstream artifacts. Restate the Hills and the to-be steps the stories must cover.
2. **Write the stories.** Diverge on every task the user needs to complete to reach the goal, walking through the to-be scenario step by step.
   - Keep each story granular, one task per story, as a short specific sentence: `<specific user> can <task> [so that <outcome>]`.
   - If the team prefers it, use `As a <user>, I want <task>, so that <outcome>`.
   - Name the actual user role, not "the user", when the team serves more than one.
3. **Trace and challenge.** Link each story to a Hill, or to the Foundation for technical enablers.
   - Flag stories that serve no Hill. If the team is asked to deliver one, think critically about whether it's really in the users' or clients' best interest, and record the answer.
   - Split stories that hide several tasks. Merge stories that are really steps of one task.
4. **Prioritize.** Choose the set for the next sprint, based on the team's most important priorities right now. Use Stage 1 of the roadmap or the No-brainers on the grid if they exist. The rest stay in the backlog.
5. **Define acceptance criteria** before anyone implements a selected story. Write 3–5 testable criteria per story. Each should describe something a user or tester can observe, and `Given… when… then…` works well. Cover the main path, at least one edge or error case, and any accessibility or performance expectation.
6. **Size and assign.** Give each story a rough size (S, M or L). Ask the user who owns each one. Don't assign people yourself. Check that each owner has the skills and the authority to meet the acceptance criteria, and flag any gaps.
7. **Play back.** Write the Playback section and save the artifact.
8. **Optional: create issues.** Only offer this after the artifact is saved. Never do it automatically. See the next section.

## Turning stories into GitHub issues (only after the user confirms)
1. Ask whether they want issues created, and for which stories. If they don't say yes, stop here.
2. Check the setup with `gh auth status` and `gh repo view --json nameWithOwner`. Tell the user which repo the issues will go to and wait for confirmation. If `gh` is missing or not authenticated, tell the user to run `gh auth login` themselves, and stop.
3. Check for duplicates with `gh issue list --state all --search "<story title>"`. Check the available labels with `gh label list`. Use only existing labels unless the user approves new ones.
4. Show the full batch first: the title, labels and body of each issue. The body holds the story, its Hill, the acceptance criteria as a `- [ ]` checklist, and the path to the artifact. Get an explicit yes for the batch.
5. Create the issues one at a time with `gh issue create --title "<title>" --body-file <tmp-file> [--label <label>]`, then write each returned URL into the story's **Issue** field in the artifact.
6. If the user uses another tracker that is connected through a tool, the same rules apply: confirm first, show the batch, and record the links.

## Facilitate a live session
**Agenda (30 min)**
| Time | Step | What happens |
| --- | --- | --- |
| 0:00 | Intro | Review the Hills and the to-be scenario. Explain the story format with one example |
| 0:03 | Write | Silent writing, one task per sticky, placed under the scenario step it belongs to |
| 0:12 | Prioritize | Cluster duplicates, link stories to Hills, and pick the sprint set |
| 0:20 | Define | Pairs write acceptance criteria for the selected stories |
| 0:26 | Assign | Size the stories, choose owners, check skills and authority |
| 0:29 | Playback | Read the sprint set aloud |

**Prompts to read aloud**
- "What does the user need to do here? One task per sticky, starting with a verb."
- "Which Hill does this story move us toward? If none, why are we doing it?"
- "How would a tester know this is done, without asking us?"
- "Does the owner have what they need, both the skills and the authority, to finish this?"

**Materials:** the Hills and to-be scenario posted on the wall, sticky notes, markers, a timer and the team's sprint board.

**Board layout:** the to-be scenario steps run across the top. Stories go under each step in a backlog lane. A "This sprint" lane sits below with space for acceptance criteria. Add a "Challenged or parked" corner.

**After the session:** digitize every story with its criteria and owner into the Output template, then offer to create issues as described above.

## Output
Save to `design-thinking/user-stories-<topic>.md` using this template:

```markdown
# User Stories: <project · sprint or Hill>
Hills: <links> · Scenario: <to-be-scenario-map file> · Sprint: <number and dates>

## Backlog
| ID | Story | Hill | Basis (Evidence / Assumption) | Size | Status |
| --- | --- | --- | --- | --- | --- |
| US-01 | <user> can <task> | Hill 1 | needs-statements-x.md N2 | M | Sprint |

## This sprint

### US-01: <short title>
- **Story:** <specific user> can <task> so that <outcome>.
- **Hill:** … · **Need:** …
- **Acceptance criteria:**
  - [ ] Given … when … then …
  - [ ] …
- **Size:** S / M / L · **Owner:** … · **Issue:** <URL once created>
- **Assumptions / questions:** …

## Challenged or parked
- <story>: <why it doesn't serve a Hill, and the decision made>

## Playback
- Key takeaways: <3–5 bullets>
- Assumptions and questions to validate: …
- Next activity: …
```

## Quality checks
- **One user, one task, one sentence.** If a story contains "and" or a list, split it.
- **It's a user task, not a system task.** "The system caches results" isn't a story. Make it a criterion or a Foundation item.
- **Every story traces to a Hill or the Foundation.** Orphans are challenged and the decision is recorded.
- **Acceptance criteria are written before implementation,** and they're testable and observable, with no "works well" or "is fast". Include at least one edge case.
- **Check stories against INVEST:** independent, negotiable, valuable, estimable, small and testable.
- **Owners are chosen by the team, not by Claude,** and each owner can actually deliver the story.
- **Issues are created only after an explicit yes,** with no duplicates and links written back into the artifact.

## Next
- `/edt-plan:prioritization-grid`: rank a large backlog before the sprint.
- `/edt-test:paper-prototypes` or `/edt-test:wireframes`: make the stories concrete before building.
- `/edt-align:daily-syncs`: track progress on the sprint set.
- `/edt-align:playbacks`: run a Delivery Playback against the acceptance criteria.

## Source
[IBM Enterprise Design Thinking Toolkit: User Stories](https://www.ibm.com/downloads/documents/us-en/137a3e34823ed9a8)
