---
name: hopes-and-fears
description: Gathers a team's hopes and fears for upcoming work, anonymously if wanted, and clusters them on an HTML artifact into themes, risks with owners and early-warning signs, and working agreements. It can seed the wall with labeled simulated user and stakeholder voices. Use at a kickoff, onboarding, or the start of a project, sprint or quarter, or when the user says "hopes and fears", "kickoff activity", "what is everyone worried about?" or "align expectations".
argument-hint: "[project, sprint or initiative] [facilitate]"
---

# Hopes and Fears

> IBM Enterprise Design Thinking · Align your team · Reflect · ~30 min

Before a big commitment of work, a team rarely says out loud what it hopes for or what keeps it up at night. Hopes and Fears makes both visible. Hopes show the team's shared picture of success. Fears show the risks while they are still cheap to address. It is a fast way to get to know each other and align on intent, which is the Reflect part of the Loop. It also puts the diverse empowered teams principle into practice: everyone writes, so every voice is on the wall, not only the loudest or most senior.

**Simulated users here.** The hopes and fears on this wall belong to real teammates, so Claude never simulates a teammate or writes a hope or fear as if someone on the team said it. Simulation has one optional job: seeding the wall with a few hopes and fears from simulated users and stakeholders in the panel, tagged `simulated`, so the team also hears voices from outside the room. Seeds sit in their own cluster and never count as team input.

## When to use it
- Anything that feels like a beginning: a project, initiative, sprint, quarter, iteration, release cycle, or any other large commitment of work.
- A new teammate, stakeholder or Sponsor User joins.
- The team is forming. Use it as the opening activity of a kickoff workshop.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of:
  - **Context:** `hills-*`, `stakeholder-map-*`, `workshop-planner-*`, `assumptions-and-questions-*`
  - **History:** earlier `hopes-and-fears-*` and `retrospectives-*` pages, to see which past fears came true
- **The team's own input:** pasted notes, survey or chat replies, a Mural or whiteboard export, or a photo of the wall. Claude can read images.
- **The simulated user panel,** `design-thinking/simulated-users.html`, only if the team wants seeds. Create it if it's missing (see `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`).
- **Ask the user only for:** what is beginning and its horizon, who is on the team by role or discipline, whether input should be anonymous, and whether to seed the wall with simulated voices.
- If only the user's own input is available, say so, and offer to collect the rest asynchronously (step 2). Never fill the gap with invented teammates.

## Co-create with Claude
1. **Set the frame.** Name the work you're about to begin and its horizon. Ask whether input should be anonymous. Fears come out more honestly when names are not attached.
2. **Collect silently.** Claude drafts a short async ask that the user can post in chat or a form. It includes the starter phrases and the rule of one idea per note:
   - **Hopes:** "I hope…", "It would be great if…"
   - **Fears:** "I'm concerned that…", "This would be great, but…"

   Suggest prompting for three kinds of hopes and fears: about **user outcomes** (did we keep users at the center?), about **how we'll work together**, and about **delivery**. The user contributes their own as well.
3. **Digitize.** Turn every input into one note, keeping the author's wording. Split notes that hold several ideas. Merge only exact duplicates, and count them, because several people writing the same thing is a signal. If input is anonymous, record no names and don't guess authors from their style; the source is "Team, anonymous", or the role if the team agreed to share roles. Tag each note:
   - `assumption`: the default, because these are beliefs about the future.
   - `evidence`: the note rests on something observed, with its source, for example "the last two releases slipped (S2, Q2 retro)".
   - `question`: an open unknown, for example "Will we get Sponsor User access?"
4. **Seed outside voices (optional).** Only after the team's notes are in, so the seeds don't anchor anyone, role-play 2–3 user personas and any stakeholder personas from the panel, one at a time and in character. Ask each: "Hearing that this team is starting <work>, what do you hope it does for you? What are you worried it will do to you?" Keep it realistic: users are often indifferent or wary ("Another tool I'll have to learn."). Add 1–2 hopes and fears per persona as `simulated` notes with the persona ID, in a cluster of their own in each column.
5. **Cluster.** Group the team's hopes into themes and its fears into themes, and give each theme a short title and a count, such as *Workflow*, *Alignment*, *Constraints* or *User value*. Look for **mirrored themes**: the same topic on both sides, for example hoping for smooth sprint planning while fearing too many meetings. Mirrored themes are where the team most needs an agreement. If seeds were used, point out where users' fears match the team's or where nobody on the team raised them.
6. **Hang it up: decide how you'll work.** For each major theme, draft:
   - **From hopes:** a working agreement that makes the hope more likely, with a way to check it's being kept.
   - **From fears:** a risk entry with an early-warning sign, a mitigation and an owner. Fears that are really unknowns become questions to validate.

   A fear raised only by a simulated user is a question to validate, not a team risk, unless the team adopts it. Then it becomes a team note with the team as its source. Claude proposes the drafts, and the team decides.
7. **Playback.** Draft two short summaries, one for the hopes and one for the fears, so that two different people can present them. Publish the page where the team will see it again, and schedule a revisit at the next retrospective.

## Facilitate a live session
Produce `design-thinking/hopes-and-fears-<topic>-kit.html`. It needs:
- **Agenda table (30 min):**
  - 0–3 Intro. Explain why you're doing this and the ground rules: write before you talk, one idea per note, there are no bad ideas.
  - 3–10 Silent ideation. Everyone writes hopes and fears and posts them on the wall.
  - 10–20 Discuss and cluster. Circle and title the themes, and draw links between mirrored themes.
  - 20–25 Hang it up. Agree on 2–4 working agreements and the top risks.
  - 25–30 Playback. One person presents the Hopes, another presents the Fears.
- **Prompts to read aloud:**
  - "For the next seven minutes, silently write your hopes and fears about <work>. One idea per sticky note."
  - "Starters: I hope… · It would be great if… · I'm concerned that… · This would be great, but…"
  - "Include at least one hope or fear about our users, not only about us."
  - "Which fear would hurt most if it came true? What would we notice first?"
- **Materials:** a marker and a sticky-note pad for everyone, a large sheet or whiteboard, a timer, and dot stickers if you want to vote on the top fears.
- **Board layout:** an empty two-column board, Hopes on the left and Fears on the right, with room to circle and title clusters, plus a parking lot and an empty risks table. If the team wants seeds, add them as a separate cluster labeled simulated, to reveal after silent writing. On Mural, turn on anonymous stickies if the team wants them.
- **Tips:** leaders write fears too, which makes candor normal. Use "yes, and…" to build on a note instead of debating it. Watch the clock, and park off-topic issues instead of solving them now.

After the session, read the photos or the Mural export and build the results page, keeping each note's wording and tag.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/hopes-and-fears-<topic>.html`. Keep the simulated banner only if the wall holds seeds; delete it otherwise.
- **Title:** `<Topic> Hopes and Fears`, for example "Checkout Redesign Hopes and Fears".
- **Header `.meta`:** under Users, give the team's coverage ("6 of 8 teammates, anonymous") and any simulated personas used for seeds.
- **Sections:**
  1. **The wall:** `.cols` with two `.col`s, Hopes and Fears. Each holds titled `.cluster`s with counts in the title, such as "Workflow (4)", of tagged `.note`s. Seeds go in a last cluster per column titled "Users and stakeholders (simulated)".
  2. **Mirrored themes:** a table of theme, the hope side, the fear side, and the agreement needed.
  3. **How we'll work:** a table of working agreement, the hope it supports, and how we'll check it's kept.
  4. **Risks to watch:** a table of fear, early-warning sign, mitigation, owner, and a tag pill.
  5. **Parking lot:** `question` or `assumption` notes.
  6. **Playback:** the hopes and fears summaries as the takeaways, "Validate next" with the open questions and any simulated fears worth checking with real users, the revisit date, and the next activity.
- **`content` in `#edt-data`:**
  ```json
  { "beginning": "", "horizon": "", "anonymous": true,
    "participants": [{ "role": "", "count": 2 }], "coverage": "6 of 8 teammates",
    "hopes": [{ "theme": "", "notes": ["H1", "H2"], "count": 3 }],
    "fears": [{ "theme": "", "notes": ["F1"], "count": 1 }],
    "seeds": { "personas": ["SU-1", "SU-6"], "notes": ["H9", "F8"] },
    "mirrored": [{ "theme": "", "hope": "H2", "fear": "F3", "agreement": "A1" }],
    "agreements": [{ "id": "A1", "text": "", "supports": "", "check": "" }],
    "risks": [{ "fear": "F3", "sign": "", "mitigation": "", "owner": "", "tag": "assumption" }],
    "parking_lot": [""], "revisit": "2026-12-16" }
  ```
  `items` holds every note, with `group` set to `"Hopes / <theme>"` or `"Fears / <theme>"`.

## Quality checks
- Every team note traces to a participant. Claude added no hopes or fears of its own, and it says when the input is partial.
- Every seed is tagged `simulated` with its persona ID, sits in its own cluster, was added after silent writing, and counts toward no team theme or duplicate count.
- Each note holds one idea, in the author's wording. Themes are titled and counted.
- Anonymous input stays anonymous on the page and in `#edt-data`.
- At least one hope or fear concerns users or user outcomes. If none does, flag it to the team; seeds can start that conversation but don't replace it.
- Every major fear has an early-warning sign and an owner, not only a mitigation.
- The working agreements are concrete and checkable, for example "Design and engineering pair on every story before estimation". "Communicate better" is too vague.
- Simulated seeds sound like different people and include indifference or pushback, not only enthusiasm for the project.
- Pitfalls:
  - Skipping the silent writing, so the loudest voices dominate
  - Treating fears as complaints to argue with
  - Filing the board away and never revisiting it

## Next
- `/edt-plan:assumptions-and-questions`: turn the riskiest fears and open questions into assumptions to test.
- `/edt-synthesize:stakeholder-map`: follow up if the fears center on stakeholders or alignment.
- `/edt-align:daily-syncs`: set up the cadence that keeps the working agreements alive.
- `/edt-align:retrospectives`: revisit this board at the end of the iteration. Which hopes came true, and which fears?
- `/edt-core:workshop-planner`: build this activity into a full kickoff agenda.

## Source
[IBM Enterprise Design Thinking Toolkit: Hopes and Fears](https://www.ibm.com/downloads/documents/us-en/137a1e253e5bac0f)
