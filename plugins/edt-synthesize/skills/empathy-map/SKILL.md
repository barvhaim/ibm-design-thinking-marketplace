---
name: empathy-map
description: Builds an empathy map of one user (Says, Does, Thinks, Feels) as an HTML artifact. It draws on real research when you have it and simulated users when you don't, and it clusters the notes, surfaces tensions and labels every note's origin. Use when the user says "empathy map", "who is our user?", "get on the same page about our user", "synthesize interview notes" or "persona workshop", or right after an observation session.
argument-hint: "[user] [facilitate]"
---

# Empathy Map

> IBM Enterprise Design Thinking · Synthesize research · Reflect · ~30 min

What a team knows about its users is usually scattered across interview notes, support tickets, a sales call and a few people's memories. An empathy map puts all of it on one wall. The group reflects on its collective knowledge of one user and builds a shared understanding of that person's goals and motivations. The four quadrants separate what you can observe (what the user **says** and **does**) from what you have to infer (what they **think** and **feel**), and that split makes the gaps visible. You are not your user, so every note shows where it came from: real evidence, a simulated user, or a team assumption.

## When to use it
- Right after an observation session, such as interviews (real or simulated) or a contextual inquiry.
- Before an important decision, to check that the team agrees on who it's designing for.
- At kickoff, to surface what the team believes about its users.
- When onboarding someone new to the user.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of:
  - research: `interviews-*`, `contextual-inquiry-*`, `research-plan-*`
  - `simulated-users.html`
  - earlier `empathy-map-*` pages
- **Files the user points to,** such as transcripts, support tickets, survey verbatims or analytics. These are real evidence.
- **The simulated user panel.** If `design-thinking/simulated-users.html` doesn't exist, create it first, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`.
- **Ask the user only for:** which *one* user the map is for, if it isn't clear, and whether there is real research you haven't seen.

## Co-create with Claude
1. **Gather.** List `design-thinking/` and read the research. Build a source list: `S1…` for each real source, with its type and date, and `SU-…` for each simulated user who represents this user type.
2. **Simulate what's missing.** If no observation of this user exists yet, run a short simulated interview with each of 2–3 relevant personas from the panel, staying in character. Use 6–8 open questions about their last real week, their tools, their hand-offs and their worst recent moment. Ask for at least one story per persona. Keep the transcripts for the page. If real research exists, simulate only the quadrants it leaves thin.
3. **Set up.** Write the center of the map: an archetype name, the role, and a short description of who they are and what they do, in context. Use a real participant's name only with their permission.
4. **Capture.** Work through the sources one at a time, writing one note per observation in its quadrant:
   - **Says:** verbatim quotes, each with its source.
   - **Does:** actions and behaviors.
   - **Thinks:** beliefs and worries they may not voice.
   - **Feels:** an emotion *and* its cause, such as "anxious in release week because designs land late".

   Tag every note: `evidence` with its `S…` source, or `simulated` with its `SU-…` source. If the team infers something nobody voiced, tag it `assumption`, even when a simulated user's answers prompted it. Then ask the user what the team knows that isn't written down, and add that too, tagged.
5. **Cluster.** Within each quadrant, group related notes and give each group a title. Look for tensions *across* quadrants, such as saying one thing but doing another, or thinking what they won't say. These are often the strongest insights. Ask yourself: standing in their shoes, how would these parts of their life shape what they need?
6. **Playback.** Tell the map back as a short story about this user. Put the simulated and assumed claims the story depends on most at the top of "Validate next". Then publish the page.

## Facilitate a live session
Produce `design-thinking/empathy-map-<user>-kit.html`. It needs:
- **Agenda table (30 min):**
  - 0–3 Intro and norms (write before you talk, everyone participates, one observation per sticky, "yes, and…", parking lot, you are not your user)
  - 3–5 Setup
  - 5–15 Silent capture
  - 15–25 Cluster and tensions
  - 25–30 Playback
- **Prompts to read aloud,** one per quadrant, plus "Where do Says and Does disagree?" and "Can you imagine yourself in their shoes?"
- **Materials:** a large sheet or Mural, markers and sticky notes, dots. Use one sticky color for observed notes and another for hunches.
- **An empty quadrant board** with the user in the center. Optionally seed it with simulated users' notes so the team can react to them, labeled as simulated.

After the session, read the photos or the Mural export and build the results page, keeping each note's tag.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/empathy-map-<user>.html`. `${CLAUDE_PLUGIN_ROOT}/shared/example-empathy-map.html` shows a finished page.
- **Title:** `<User> Empathy Map`, for example "Release Engineer Empathy Map".
- **Sections:**
  1. **The map:** `.quad.has-center`, with Says, Thinks, Does and Feels in `q1`–`q4` and the user in `qc`. Each quadrant holds titled `.cluster`s of tagged `.note`s.
  2. **Tensions:** a table of insight, quadrants, number of supporting notes, and a tag pill.
  3. **What this suggests they need:** notes tagged `assumption`, to carry into Needs Statements.
  4. **Simulated sessions:** a `details.transcript` per simulated interview. Include this only when you ran any.
  5. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "user": { "name": "", "role": "", "context": "", "persona": "SU-2" },
    "quadrants": { "says": [{ "cluster": "", "notes": ["N1"] }], "thinks": [], "does": [], "feels": [] },
    "tensions": [{ "text": "", "quadrants": ["says", "does"], "notes": ["N1", "N4"], "tag": "simulated" }],
    "implications": [{ "text": "", "tag": "assumption" }] }
  ```
  `items` holds every note, with `group` set to `"<Quadrant> / <cluster>"`.

## Quality checks
- The map covers one user. If the notes describe two different people, split them into two maps.
- The center describes a specific person in context, not a demographic.
- Says holds quotes and Does holds behavior. Thinks and Feels add something rather than restating Says.
- Every note has a tag and a source. No simulated note is tagged `evidence`.
- Feels names the emotion *and* its cause.
- Clusters have titles, and at least one tension across quadrants is called out.
- The simulated personas sound like different people. If they all agree, rerun them with more friction.
- If most notes are simulated or assumed, the Playback says so plainly and names the one real-user check that would matter most.
- The map holds no features or solutions.

## Next
- `/edt-synthesize:as-is-scenario-map`: lay out this user's current experience step by step.
- `/edt-synthesize:needs-statements`: turn the clusters and tensions into needs.
- `/edt-plan:assumptions-and-questions`: prioritize the assumptions and simulated claims.
- `/edt-gather:interviews`: run more interviews, simulated or real, to fill thin quadrants.
- `/edt-core:sponsor-users`: find real users to validate the map.

## Source
[IBM Enterprise Design Thinking Toolkit: Empathy Map](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac17)
