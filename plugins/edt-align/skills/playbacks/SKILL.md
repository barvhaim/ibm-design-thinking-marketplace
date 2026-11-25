---
name: playbacks
description: Builds a Playback story as an HTML artifact from the upstream design-thinking/ pages (user, as-is, Hills, to-be, next and the ask), showing per beat how much rests on simulated users. Claude rehearses it with a simulated audience of stakeholders and users, then logs the real feedback. Use when the user says "prep a playback", "Hills Playback", "Playback Zero", "delivery playback", "client playback", "present our research to stakeholders" or "share our progress".
argument-hint: "[hills | zero | delivery | client | informal] [audience] [facilitate]"
---

# Playbacks

> IBM Enterprise Design Thinking · Align your team · Reflect · ~30 min

A Playback brings stakeholders into the Loop. It gives them a safe space to hear the team's story and trade feedback. Instead of a status report, the team tells a story about its users: what it observed, what it learned, and what it made. A story makes people care, so stakeholders see the value and can say early where they disagree. Playbacks with a capital P are formal milestones at key moments. Playbacks with a lowercase p are informal and can happen any time you have something new to share.

**Simulated users here.** A Playback is a team activity with real stakeholders, so simulation has two narrow jobs. First, the story carries the provenance of everything upstream: when the user or to-be beats rest on simulated users, the page and the presenter say so plainly. Second, Claude simulates the audience for a rehearsal, so the team hears the hard questions before the room asks them. The Playback itself, and every word in the feedback log, comes from real people.

## When to use it
- Your team, stakeholders or clients need to be on the same page about a future user experience.
- You hit a milestone (see the table below), or learned or made something others should see.
- You suspect misalignment and want to bring it out while the work is still cheap to change.

| Milestone | When | Emphasis | Typical ask |
|---|---|---|---|
| **Hills Playback** | Hills are drafted, before heavy Make work | User, as-is pain, Who/What/Wow | Agree on the Hills and the scope |
| **Playback −2, −1** | Draft rehearsals before Playback Zero | The whole story, rough | Poke holes, sharpen the story |
| **Playback Zero** | The team has an end-to-end concept for its Hills | To-be experience | Commit to the experience we will deliver |
| **Delivery Playbacks** | Throughout delivery | Working results against the Hills, what changed | Feedback, unblocking, resources |
| **Client Playbacks** | Sharing with clients or Sponsor Users, under NDA | Their users, their outcomes | Validate the direction |
| *playback* (informal) | Any time | Whatever is new | Quick reactions |

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks, especially `items` with their tags and sources, of:
  - **User:** `sponsor-users-*`, `empathy-map-*`, `interviews-*`, `contextual-inquiry-*`
  - **As-is:** `as-is-scenario-map-*`, `needs-statements-*`
  - **Hills:** `hills-*`
  - **To-be:** `big-idea-vignettes-*`, `to-be-scenario-map-*`, `storyboards-*`, `wireframes-*`, `paper-prototypes-*`, `feedback-grid-*`, `cognitive-walkthrough-*`
  - **Next:** `assumptions-and-questions-*`, `experience-based-roadmap-*`, `research-plan-*`
  - **Audience:** `stakeholder-map-*`
  - Earlier `playbacks-*` pages, to see what changed since last time
- **The simulated user panel,** `design-thinking/simulated-users.html`, for the rehearsal audience. Create it if it's missing (see `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`).
- **Ask the user only for:** the milestone type, the audience, the date and length, the ask (the decision, feedback or support you need), any demo or prototype link, and, for Client Playbacks, whether an NDA is in place.

## Co-create with Claude
1. **Frame it.** Agree on the milestone, the audience and the ask. Match the polish to the audience. A team playback can be sketches on a wall. An executive Playback needs a tight story with a clear ask up front.
2. **Take inventory.** List `design-thinking/` and read the upstream pages. Map each story beat (user → as-is → Hills → to-be → next and ask) to the pages and items behind it, and count those items by tag. That count is the beat's provenance summary. When a beat has nothing behind it, record a gap rather than papering over it, and name the activity that fills it: no user → `/edt-gather:interviews`, no Hills → `/edt-plan:hills`, no concept → `/edt-ideate:storyboards`, an untested to-be → `/edt-test:cognitive-walkthrough`.
3. **Invite.** Draft the invite list across silos and levels of hierarchy, using the stakeholder map if there is one. Ask "Who would benefit from knowing what we're working on?" and "Whose perspective is missing?" Include Sponsor Users where it's appropriate. For a Client Playback, confirm the NDA and remove internal-only content.
4. **Make it about users.** Draft the story in five beats, each with 1–3 points. Every point is an upstream item that keeps its tag and source: a simulated quote stays simulated on the Playback page.
   - Open with a real user, or a Sponsor User who has agreed to be named, and a quote. Do not open with the team or the technology. If the only user material is simulated, open with the persona, but say so on the frame and out loud: "Rafa is a simulated persona. We haven't met a real release engineer yet." Never present a simulated persona as a real person or a Sponsor User.
   - Show today's pain, with its sources.
   - State the Hills exactly as written.
   - Walk through the to-be moment where the Wow happens.
   - Close with what's next and the ask, repeated. When a beat rests mostly on simulated or assumed items, the ask includes the real-user check that would firm it up.

   Plan for about 2/3 of the time on the story and at least 1/3 on listening.
5. **Rehearse with a simulated audience.** Follow `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`.
   - **Cast** 2–4 stakeholder personas for this audience, built from the stakeholder map where there is one: for example, the sponsor who wants the number, the engineering lead who smells scope creep, someone from a silo nobody consulted, and the skeptic who has seen this fail before. If the panel has no stakeholders, add them to `design-thinking/simulated-users.html` with the next `SU-n` IDs and the role marked as stakeholder, so later rehearsals reuse them. Add 1–2 user personas from the panel.
   - **Run** the story, then let each persona react, one at a time and in character. They interrupt, ask "so what?", challenge the sourcing ("Did you talk to any real customers?"), and push on cost, timeline and risk. The user personas say where the story doesn't match their day. Some of it should be hostile. If everyone likes it, rerun with more friction.
   - **Check** the story yourself too: flag jargon and unsourced claims, and test whether it still holds if the demo fails.
   - **Capture** every reaction as a `simulated` note in the feedback grid, with the persona ID. Revise the story and record what changed. For milestone Playbacks, also suggest a Playback −1 with friendly real reviewers.

   Rehearsal predicts objections. It doesn't measure alignment, so never report a simulated stakeholder's view as a real stakeholder's position.
6. **Plan the listening.** Assign a presenter, a note-taker and a timekeeper. Capture feedback in a grid: *what worked*, *what to change*, *questions* and *ideas*. Write 3–5 open questions for the room. List the misalignment signals to watch for:
   - Disagreement about who the user is
   - "Why aren't we doing X?"
   - Scope surprises
   - Silence from a key decision-maker
   - Conflicting priorities between silos
7. **After the Playback, close the loop.** Update the same page and republish it.
   - Log the room's feedback verbatim, with who said it as an `S…` source, and tag it `evidence`, or `question` when it's a question. Put it in the grid beside the rehearsal notes, never merged with them. Note which rehearsal objections actually came up, and which real ones the rehearsal missed.
   - Decide for each item: act, park or discuss, with an owner.
   - Update the affected upstream pages, for example revise the Hills. Everything is a prototype.
   - Draft a follow-up message to attendees: what we heard and what we'll change.

## Facilitate a live session
Produce `design-thinking/playbacks-<milestone>-<topic>-kit.html`. It needs:
- **Agenda table (30 min):**
  - 0–2 Welcome. State the purpose and the ask, and explain how to give feedback.
  - 2–22 The story in five beats (about 3 / 5 / 3 / 7 / 2 min), with demo or artifacts.
  - 22–26 Silent feedback. Everyone writes one thought per sticky note.
  - 26–30 Share and cluster the feedback, then recap what you heard and the next steps.
- **Prompts to read aloud:**
  - "This is work in progress. Everything here is a prototype, so honest reactions help us most."
  - "While we talk, write one thought per sticky note: what works, what you'd change, your questions, your ideas."
  - "What surprised you? Where do you see this differently?"
  - "Here's what we heard. Here's what we'll do next."
- **Materials:** printed or on-screen artifacts for each beat, sticky notes and markers for everyone, a timer, and an agreed way to record the session if needed.
- **Board layout:** five empty story frames (User · As-is · Hills · To-be · Next), each with its provenance summary, an empty feedback grid (Worked · Change · Questions · Ideas), a parking lot, and an empty feedback log. Optionally list the rehearsal's sharpest objections, labeled simulated, as a presenter crib sheet.

After the session, read the photos or the Mural export and fill in the feedback grid and log on the results page, keeping each note's tag.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/playbacks-<milestone>-<topic>.html`. Keep the simulated banner whenever any beat or the rehearsal holds simulated items.
- **Title:** `<Topic> <Milestone> Playback`, for example "Checkout Hills Playback".
- **Sections:**
  1. **The ask and the audience:** a lede with the milestone type, date and length, presenter, note-taker, timekeeper, NDA status, and the ask. Then a table of who, role or silo, what they care about, what we need from them, and the persona they were rehearsed as (`SU-n`), if any.
  2. **The story:** `.frames`, one frame per beat in order (User · As-is · Hills · To-be · Next and ask). `.frame-n` reads like "Beat 2 · Their world today · 5 min". The art is an ASCII sketch of the beat, or the Hill's text. The caption holds the 1–3 points, then one provenance pill per tag with its count, such as `<span class="pill" data-tag="simulated">5 simulated</span>`.
  3. **What the story rests on:** one headline sentence, such as "11 of 15 claims rest on simulated users, and the Wow has no real-user evidence". Then a table of beat, evidence, simulated, assumption and question counts, and the gap with the activity that fills it. Under it, one `.cluster` per beat holding its claims as tagged `.note`s with their original sources.
  4. **Feedback grid:** `.quad` with Worked, Change, Questions and Ideas. Each cell holds a `.cluster` titled "Rehearsal" (`simulated` notes, `SU-n` sources) and, after the Playback, one titled "In the room" (`evidence` and `question` notes, `S…` sources). Below it, list what changed after rehearsal, and put each rehearsal session in a `details.transcript` with `turn sim` lines.
  5. **Listening plan:** the questions for the room and the misalignment signals to watch for.
  6. **Feedback log:** a table of #, feedback (verbatim), from, quadrant, tag pill, act / park / discuss, and owner. It holds the room's feedback. A rehearsal item appears only if the team chose to act on it, with its `simulated` pill.
  7. **Playback:** the takeaways name where the room is aligned and misaligned. "Validate next" leads with the beats that rest most on simulated users.
- **`content` in `#edt-data`:**
  ```json
  { "milestone": "hills", "ask": "", "nda": false,
    "roles": { "presenter": "", "note_taker": "", "timekeeper": "" },
    "audience": [{ "who": "", "role": "", "cares": "", "need": "", "rehearsed_as": "SU-7" }],
    "beats": [{ "beat": "user", "minutes": 3, "points": ["N1", "N2"], "upstream": ["design-thinking/empathy-map-release-engineer.html"],
                "provenance": { "evidence": 1, "simulated": 4, "assumption": 0, "question": 0 },
                "gap": "", "fill": "/edt-gather:interviews" }],
    "rehearsal": { "personas": ["SU-6", "SU-7", "SU-2"], "notes": ["R1"], "changed": [""] },
    "listening": { "questions": [""], "signals": [""] },
    "feedback": [{ "id": "F1", "text": "", "from": "S3", "quadrant": "change", "tag": "evidence",
                   "decision": "act", "owner": "", "predicted_by": "R4" }],
    "alignment": { "aligned": [""], "misaligned": [""] } }
  ```
  `items` holds every claim, rehearsal note and feedback note, with `group` set to `"<Beat>"` or `"Feedback / <quadrant> / Rehearsal|In the room"`.

## Quality checks
- The story starts with a user, not with the team, the org chart or the architecture.
- Every claim keeps the tag and source from its upstream page. Claude never upgrades a simulated item to evidence and never invents user facts to fill a beat.
- Every beat shows its provenance count, and the headline matches `items`. If the user or to-be beat rests mostly on simulated users, the presenter says so aloud and the ask includes the real-user check.
- The Hills appear verbatim, and the to-be beat shows how it delivers each Wow.
- The ask is explicit and appears at the start and at the end.
- At least a third of the time goes to listening. The presenters capture feedback without defending the work.
- The rehearsal personas sound like different people, and at least one pushes back hard. If all of them approve, the simulation is broken.
- Rehearsal notes stay `simulated` and separate from the room's feedback. A simulated stakeholder never stands in for a real one, and Claude never writes what a real attendee "would have" said.
- Disagreement is treated as a finding to log, not a failure. The goal is clear communication, not a perfect deck.
- Polish fits the audience. Client Playbacks contain nothing confidential beyond what the NDA covers.
- Pitfalls:
  - A demo with no "why"
  - Too many slides, so there's no time for feedback
  - Inviting only people who will agree
  - Collecting feedback and never following up

## Next
- `/edt-test:feedback-grid`: sort the feedback you captured into themes and actions.
- `/edt-plan:hills`: revise the Hills if the Playback showed misalignment on Who, What or Wow.
- `/edt-plan:assumptions-and-questions`: turn new doubts, and the simulated beats, into assumptions to test.
- `/edt-core:sponsor-users`: recruit real users for the beats that rest on simulated ones.
- `/edt-synthesize:stakeholder-map`: map who else needs to be brought into the Loop.
- `/edt-align:retrospectives`: reflect on how the Playback, and the iteration behind it, went.

## Source
[IBM Enterprise Design Thinking Toolkit: Playbacks](https://www.ibm.com/downloads/documents/us-en/137a1e253e5bac07)
