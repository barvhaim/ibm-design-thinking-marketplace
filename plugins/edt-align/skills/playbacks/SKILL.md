---
name: playbacks
description: Builds a Playback story from the design-thinking/ artifacts (user, as-is problem, Hills, to-be concept, what's next) plus a plan for capturing feedback and spotting misalignment. Use when the user says "prep a playback", "Hills Playback", "Playback Zero", "delivery playback", "client playback", "present our research to stakeholders", "share our progress", or needs to align stakeholders and gather feedback on work in progress.
argument-hint: "[hills | zero | delivery | client | informal] [audience] [facilitate]"
---

# Playbacks

> IBM Enterprise Design Thinking · Align your team · Reflect · ~30 min

A Playback brings stakeholders into the Loop. It gives them a safe space to hear the team's story and trade feedback. Instead of a status report, the team tells a story about its users: what it observed, what it learned, and what it made. A story makes people care, so stakeholders see the value and can say early where they disagree. Playbacks with a capital P are formal milestones at key moments. Playbacks with a lowercase p are informal and can happen any time you have something new to share.

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
- Upstream artifacts in `design-thinking/`:
  - **User:** `sponsor-users*`, `empathy-map*`, `interviews*`, `contextual-inquiry*`
  - **As-is:** `as-is-scenario-map*`, `needs-statements*`
  - **Hills:** `hills*`
  - **To-be:** `big-idea-vignettes*`, `to-be-scenario-map*`, `storyboards*`, `wireframes*`, `paper-prototypes*`, `feedback-grid*`, `cognitive-walkthrough*`
  - **Next:** `assumptions-and-questions*`, `experience-based-roadmap*`, `research-plan*`
  - **Audience:** `stakeholder-map*`
  - Earlier `playbacks-*` files, to see what changed since last time
- Ask the user for anything still missing:
  - The milestone type, the audience, the date and length
  - The ask: the decision, feedback or support you need from this audience
  - Any demo or prototype link
  - For Client Playbacks, whether an NDA is in place

## Co-create with Claude
1. **Frame it.** Agree on the milestone, the audience and the ask. Match the polish to the audience. A team playback can be sketches on a wall. An executive Playback needs a tight story with a clear ask up front.
2. **Take inventory.** List `design-thinking/` and read the upstream artifacts. Map each story beat (user → as-is → Hills → to-be → next) to its sources. When a beat has no evidence behind it, write it down as a gap. Do not paper over it. Point to the activity that fills the gap: no user evidence → `/edt-gather:interviews`, no Hills → `/edt-plan:hills`, no concept → `/edt-ideate:storyboards`.
3. **Invite.** Draft the invite list across silos and levels of hierarchy, using the stakeholder map if there is one. Ask "Who would benefit from knowing what we're working on?" and "Whose perspective is missing?" Include Sponsor Users where it's appropriate. For a Client Playback, confirm the NDA and remove internal-only content.
4. **Make it about users.** Draft the story in five beats, each with 1–3 points, and tag every point.
   - Open with a real user, or a Sponsor User who has agreed to be named, and a quote. Do not open with the team or the technology.
   - Show today's pain with evidence.
   - State the Hills exactly as written.
   - Walk through the to-be moment where the Wow happens.
   - Close with what's next and the ask, repeated.

   Plan for about 2/3 of the time on the story and at least 1/3 on listening.
5. **Rehearse.** Claude plays the audience. It asks the hard questions each stakeholder is likely to raise, flags jargon and claims that have no source, and checks that the story still holds if the demo fails. Revise. For milestone Playbacks, suggest a Playback −1 with friendly reviewers first.
6. **Plan the listening.** Assign a presenter, a note-taker and a timekeeper. Choose a capture format: a feedback grid with *what worked*, *what to change*, *questions* and *ideas*. Write 3–5 open questions for the room. List the misalignment signals to watch for:
   - Disagreement about who the user is
   - "Why aren't we doing X?"
   - Scope surprises
   - Silence from a key decision-maker
   - Conflicting priorities between silos
7. **After the Playback, close the loop.**
   - Log the feedback verbatim, with who said it, and tag each item.
   - Decide for each item: act, park or discuss.
   - Update the affected artifacts, for example revise the Hills. Everything is a prototype.
   - Draft a follow-up message to attendees: what we heard and what we'll change.

## Facilitate a live session
**Agenda (30 min)**
- **0–2:** Welcome. State the purpose and the ask, and explain how to give feedback.
- **2–22:** The story in five beats (about 3 / 5 / 3 / 7 / 2 min), with demo or artifacts.
- **22–26:** Silent feedback. Everyone writes one thought per sticky note.
- **26–30:** Share and cluster the feedback, then recap what you heard and the next steps.

**Prompts to read aloud**
- "This is work in progress. Everything here is a prototype, so honest reactions help us most."
- "While we talk, write one thought per sticky note: what works, what you'd change, your questions, your ideas."
- "What surprised you? Where do you see this differently?"
- "Here's what we heard. Here's what we'll do next."

**Materials:** printed or on-screen artifacts for each beat, sticky notes and markers for everyone, a timer, and an agreed way to record the session if needed.

**Board layout (wall or Mural):** a left-to-right story wall with five frames (User · As-is · Hills · To-be · Next). Beside it, a 2×2 feedback grid (Worked · Change · Questions · Ideas), and a parking lot in the corner.

**Afterwards:** give Claude the photo of the wall or the Mural export. Claude digitizes it into the feedback log below.

## Output
Save to `design-thinking/playbacks-<milestone>-<topic>.md` using this template:

```markdown
# Playback: <milestone>, <project>

**Type:** Hills Playback | Playback −1 | Playback Zero | Delivery Playback | Client Playback (NDA: yes/no) | informal
**Date / length:** … · **Presenter:** … · **Note-taker:** … · **Timekeeper:** …
**Our ask:** <decision, feedback or support needed>

## Audience
| Who | Role / silo | What they care about | What we need from them |
|---|---|---|---|

## Story
### 1. Meet the user (~3 min)
- <point>. Evidence: <quote or finding, source file>
### 2. Their world today (~5 min)
- <pain point>. Evidence: <source> | Assumption: …
### 3. Our Hills (~3 min)
- Who / What / Wow, verbatim from `hills-*.md`
### 4. The new experience (~7 min)
- <storyboard frame or demo step>. Evidence: tested with <n> users | Assumption: untested
### 5. What's next and our ask (~2 min)
- Next activities, open questions, the ask restated

## Source map and gaps
| Beat | Artifacts used | Gap → activity that would fill it |
|---|---|---|

## Feedback capture plan
- **Format:** Worked · Change · Questions · Ideas
- **Questions for the room:** …
- **Misalignment signals to watch for:** …

## Feedback log
| # | Feedback (verbatim) | From | Quadrant | Tag | Act / Park / Discuss | Owner |
|---|---|---|---|---|---|---|

## Playback
- **Key takeaways (3–5):** …
- **Where we're aligned / misaligned:** …
- **Assumptions and questions to validate:** …
- **Recommended next activity:** `/…`
```

## Quality checks
- The story starts with a user, not with the team, the org chart or the architecture.
- Every claim is tagged. User facts trace to a source file or quote, and nothing about users is invented.
- The Hills appear verbatim, and the to-be section shows how it delivers each Wow.
- The ask is explicit and appears at the start and at the end.
- At least a third of the time goes to listening. The presenters capture feedback without defending the work.
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
- `/edt-plan:assumptions-and-questions`: turn new doubts into assumptions to test.
- `/edt-synthesize:stakeholder-map`: map who else needs to be brought into the Loop.
- `/edt-align:retrospectives`: reflect on how the Playback, and the iteration behind it, went.

## Source
[IBM Enterprise Design Thinking Toolkit: Playbacks](https://www.ibm.com/downloads/documents/us-en/137a1e253e5bac07)
