---
name: user-stories
description: Writes user stories as an HTML artifact. Each is one user task tied to a Hill, a need and the simulated personas it serves, with acceptance criteria checked by walking each persona through the story, plus a size and an owner. Can create GitHub issues, but only after the user confirms. Use when someone asks "write user stories", "break this Hill into tasks", "build our backlog", "add acceptance criteria", "plan the sprint" or "turn this into issues".
argument-hint: "[Hill, roadmap stage or feature] [facilitate]"
---

# User Stories

> IBM Enterprise Design Thinking · Plan your work · Make and Reflect · ~30 min

Requirements written as features say what to build. User stories say what a user must be able to do, so every piece of work can be checked against the value it delivers. A good user story is a short, specific sentence about a single user task, such as "A user can upload her profile picture from her computer". It traces back to a Hill and a need, names the user it's for, and has acceptance criteria that show when it's really done. Stories turn intent into work the team can pick up in a sprint without losing sight of the user.

## When to use it
- Shortly after writing Hills, to break each Hill into the tasks users must complete.
- When Stage 1 of an experience-based roadmap needs to become sprint-ready work.
- At sprint planning, to select and define the next set of stories.
- When a backlog full of tickets that read like features needs reframing around users.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of `hills-*` (required), `to-be-scenario-map-*` (the user's future steps), `experience-based-roadmap-*` (what's in Stage 1), `prioritization-grid-*`, `needs-statements-*` and any earlier `user-stories-*`.
- **The simulated user panel,** `design-thinking/simulated-users.html`. Create it if it's missing (see `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`).
- **Ask the user only for:** the sprint length and team members, the team's definition of done, and who owns each story. Claude never assigns owners.
- With no Hills, suggest `/edt-plan:hills` first. If the user tasks are unclear, suggest `/edt-ideate:to-be-scenario-map` to map them out.

## Co-create with Claude
1. **Ground.** List `design-thinking/` and read the upstream data. Restate the Hills, the needs and the to-be steps the stories must cover, keeping each one's tag.
2. **Write the stories.** Diverge on every task the user needs to complete to reach the goal, walking through the to-be scenario step by step.
   - Keep each story granular, one task per story, as a short specific sentence: `<specific user> can <task> [so that <outcome>]`. If the team prefers it, use `As a <user>, I want <task>, so that <outcome>`.
   - Name the actual user role, not "the user", when the team serves more than one.
   - Reference who the story is for: the persona IDs (`SU-…`) or real users (`S…`) it serves, and the need it meets, by its needs-statement ID.
3. **Trace and challenge.** Link each story to a Hill, or to the Foundation for technical enablers.
   - Flag stories that serve no Hill. If the team is asked to deliver one, think critically about whether it's really in the users' or clients' best interest, and record the answer.
   - Split stories that hide several tasks. Merge stories that are really steps of one task.
4. **Prioritize.** Choose the set for the next sprint, based on the team's most important priorities right now. Use Stage 1 of the roadmap or the No-brainers on the grid if they exist. Sort the rest into Next and Later, and keep a list of challenged or parked stories.
5. **Define acceptance criteria** before anyone implements a selected story. Write 3–5 testable criteria per story, each describing something a user or tester can observe; `Given… when… then…` works well. Cover the main path, at least one edge or error case, and any accessibility or performance expectation.
6. **Walk each simulated persona through the story.** For each sprint story, take the personas it references plus one it doesn't obviously fit, such as the edge case. Run each one separately, in character:
   - Narrate the story's steps as they would happen ("You open… you see… what do you do next?"), and let the persona act from their real habits, including skipping steps, using a workaround or giving up.
   - Check every criterion against what the persona did. Look for a step the criteria don't cover, and for a criterion that would pass while the persona still fails.
   - Add or rewrite criteria for each gap. Tag criteria that came from a walk-through `simulated`, with the persona's ID.

   Record each walk-through as a transcript, and mark each story as pass or gap per persona. If every persona passes every story, the walk-through was too polite, so rerun it with the skeptic and the edge case. A simulated walk-through sharpens the criteria; it isn't acceptance. Real acceptance happens with real users at a Delivery Playback.
7. **Size and assign.** Give each story a rough size (S, M or L). Ask the user who owns each one. Don't assign people yourself. Check that each owner has the skills and the authority to meet the acceptance criteria, and flag any gaps.
8. **Play back.** Put the stories and criteria that rest only on simulated walk-throughs at the top of "Validate next". Then publish the page.
9. **Optional: create issues.** Only offer this after the page is saved. Never do it automatically. See the next section.

## Turning stories into GitHub issues (only after the user confirms)
1. Ask whether they want issues created, and for which stories. If they don't say yes, stop here.
2. Check the setup with `gh auth status` and `gh repo view --json nameWithOwner`. Tell the user which repo the issues will go to and wait for confirmation. If `gh` is missing or not authenticated, tell the user to run `gh auth login` themselves, and stop.
3. Check for duplicates with `gh issue list --state all --search "<story title>"`. Check the available labels with `gh label list`. Use only existing labels unless the user approves new ones.
4. Show the full batch first: the title, labels and body of each issue. The body holds the story, its Hill, its need, the users it serves (marking simulated personas as simulated), the acceptance criteria as a `- [ ]` checklist, and the path to the page. Get an explicit yes for the batch.
5. Create the issues one at a time with `gh issue create --title "<title>" --body-file <tmp-file> [--label <label>]`. Write each returned URL into the story's `issue` field in `#edt-data` and its row on the page, then republish.
6. If the user uses another tracker that is connected through a tool, the same rules apply: confirm first, show the batch, and record the links.

## Facilitate a live session
Produce `design-thinking/user-stories-<topic>-kit.html`. It needs:
- **Agenda table (30 min):**
  - 0:00–0:03 Intro: review the Hills and the to-be scenario, and explain the story format with one example
  - 0:03–0:12 Write: silent writing, one task per sticky, placed under the scenario step it belongs to
  - 0:12–0:20 Prioritize: cluster duplicates, link stories to Hills, and pick the sprint set
  - 0:20–0:26 Define: pairs write acceptance criteria for the selected stories
  - 0:26–0:29 Assign: size the stories, choose owners, and check skills and authority
  - 0:29–0:30 Playback: read the sprint set aloud
- **Prompts to read aloud:**
  - "What does the user need to do here? One task per sticky, starting with a verb."
  - "Which Hill does this story move us toward? If none, why are we doing it?"
  - "How would a tester know this is done, without asking us?"
  - "Does the owner have what they need, both the skills and the authority, to finish this?"
- **Materials:** the Hills and to-be scenario posted on the wall, sticky notes, markers, a timer and the team's sprint board.
- **An empty board:** the to-be steps as column heads over an empty backlog lane, empty `.cols` for This sprint, Next, Later and Challenged or parked, and an empty acceptance-criteria table per sprint story.

After the session, read the photos or the board export and build the results page with every story, criterion and owner. Offer to run the persona walk-throughs (step 6) on the sprint set, then offer to create issues as described above.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/user-stories-<topic>.html`.
- **Title:** `<Project> User Stories`, for example "Claims Intake User Stories".
- **Sections:**
  1. **By priority:** `.cols` with This sprint, Next, Later, and Challenged or parked. Each story is a `.note` whose `data-tag` is the basis of the need behind it, and whose `src` reads "US-01 · Hill 1 · SU-2 · M".
  2. **Backlog:** a table of ID, story, users (persona or source pills), Hill, need, size, owner, status and issue link.
  3. **Sprint stories:** for each one, an `h3` with the story, then a table of acceptance criteria with each criterion's origin (team, or a `simulated` pill with the persona ID) and the walk-through result per persona as a `data-tone` pill (pass or gap).
  4. **Persona walk-throughs:** a `details.transcript` per persona per story.
  5. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "project": "", "sprint": { "n": "", "dates": "", "length": "" }, "hills": ["H1"],
    "stories": [{ "id": "US-01", "text": "<user> can <task> so that <outcome>", "user": "",
      "for": ["SU-2"], "need": "NS1", "hill": "H1", "tag": "simulated",
      "priority": "sprint|next|later|parked", "size": "M", "owner": "", "issue": "",
      "criteria": [{ "text": "Given … when … then …", "origin": "team|SU-2", "tag": null }],
      "walkthroughs": [{ "persona": "SU-2", "result": "pass|gap", "gap": "", "note": "N5" }] }],
    "parked": [{ "story": "", "why": "", "decision": "" }] }
  ```
  A criterion added from a walk-through has `tag` set to `"simulated"`. `items` holds every story note and every walk-through note.

## Quality checks
- **One user, one task, one sentence.** If a story contains "and" or a list, split it.
- **It's a user task, not a system task.** "The system caches results" isn't a story. Make it a criterion or a Foundation item.
- **Every story traces to a Hill or the Foundation, and names its user and need.** Orphans are challenged and the decision is recorded. Persona IDs refer to personas in the panel.
- **Acceptance criteria are written before implementation,** and they're testable and observable, with no "works well" or "is fast". Include at least one edge case.
- **Check stories against INVEST:** independent, negotiable, valuable, estimable, small and testable.
- **The walk-throughs found something.** They include a persona the story wasn't written for, the personas behave like different people, and at least one story has a gap. Criteria from walk-throughs are tagged `simulated`, and passing a simulated walk-through is never reported as acceptance.
- **Owners are chosen by the team, not by Claude,** and each owner can actually deliver the story.
- **Issues are created only after an explicit yes,** for a confirmed repo, with no duplicates, only existing labels unless the user approves new ones, the full batch shown first, and links written back into the page.

## Next
- `/edt-plan:prioritization-grid`: rank a large backlog before the sprint.
- `/edt-test:paper-prototypes` or `/edt-test:wireframes`: make the stories concrete before building.
- `/edt-test:cognitive-walkthrough`: walk simulated users through the built flow.
- `/edt-align:daily-syncs`: track progress on the sprint set.
- `/edt-align:playbacks`: run a Delivery Playback against the acceptance criteria with real users.

## Source
[IBM Enterprise Design Thinking Toolkit: User Stories](https://www.ibm.com/downloads/documents/us-en/137a3e34823ed9a8)
