---
name: empathy-map
description: Builds an empathy map of one user (Says, Does, Thinks, Feels) from research in the workspace or a live team session, with clustered notes, tensions and labeled assumptions. Use when the user says "empathy map", "who is our user?", "get on the same page about our user", "synthesize interview notes", "make sense of what we observed", "persona workshop", or right after observation sessions and before key decisions.
argument-hint: "[user] [facilitate]"
---

# Empathy Map

> IBM Enterprise Design Thinking · Synthesize research · Reflect · ~30 min

What a team knows about its users is usually scattered across interview notes, support tickets, a sales call and a few people's memories. An empathy map puts all of it on one wall. The group reflects on its collective knowledge of one user and builds a shared understanding of that person's goals and motivations. The four quadrants separate what you can observe (what the user **says** and **does**) from what you have to infer (what they **think** and **feel**). That split is what makes the gaps visible. You are not your user, so the map is only as good as the evidence behind each note.

## When to use it
- Right after an observation session, such as interviews or a contextual inquiry, while it's fresh.
- Before an important decision, to check the team agrees on who it's designing for.
- At kickoff, to surface what the team *believes* about users. Expect many assumptions, which is useful too.
- When onboarding someone new to the user.

## Inputs
- Upstream artifacts in `design-thinking/`:
  - **Research:** `interviews*`, `contextual-inquiry*`, `sponsor-users*`, `research-plan*`
  - **History:** earlier `empathy-map*` files
  - **Other files the user points to:** transcripts, support tickets, survey verbatims, analytics
- Ask the user for anything still missing:
  - Which *one* user the map is for, by role or segment. Use one map per user type.
  - What research exists, and when it was gathered
  - Whether real users or Sponsor Users can take part
- If there is no defensible data from real observation, say so. Offer to build a map that is clearly titled as assumption-based, and point to `/edt-gather:interviews` or `/edt-gather:contextual-inquiry` to replace it with evidence.

## Co-create with Claude
1. **Gather.** List `design-thinking/` and read the research. Build a source list with an ID, type and date for each source, so every note can cite one.
2. **Set up.** Pick one user. Write the center of the map: a name, the role, and a short description of who they are and what they do, in context. The name is a real participant's only with permission. Otherwise use an archetype name and label it as one.
3. **Capture.** Work source by source. Write one note per observation, placed in the right quadrant:
   - **Says:** direct quotes, verbatim, with their source.
   - **Does:** actions and behaviors. Mark whether each was observed or only reported.
   - **Thinks:** beliefs, worries and aspirations they may not voice. These are inferred, so tag them Assumption unless the user stated them.
   - **Feels:** emotional states, each with its cause, for example "anxious before month-end close because figures arrive late".

   Then ask the user what the team knows that isn't written down. Add it, tagged by source.
4. **Cluster.** Within each quadrant, group related notes and title each group. Look for tensions *across* quadrants: says one thing but does another, or thinks what they won't say. These are often the strongest insights. Then ask the imagination question: if you stood in their shoes, how would these parts of their life shape what they need?
5. **Playback.** Tell the map back as a short story about this user. Label everything that is an assumption or a question to validate later. Recommend the next activity.

## Facilitate a live session
**Agenda (30 min)**
- **0–3:** Intro. Explain why you're doing this and the norms:
  - Write before you talk.
  - Everyone participates.
  - One observation per sticky note.
  - Build with "yes, and…".
  - Use a parking lot for off-topic issues.

  Remind the room that you are not your user.
- **3–5:** Setup. Draw the grid, then sketch the user in the center with a name and a one-line description.
- **5–15:** Capture. Everyone writes silently, one observation per sticky note, and posts each note in its quadrant.
- **15–25:** Cluster. Group the notes within each quadrant, name the clusters, and discuss the tensions.
- **25–30:** Playback. One person plays back the map, and the team marks assumptions and questions.

**Prompts to read aloud**
- "Write only what you've seen or heard from real users. If it's a hunch, add a question mark."
- "Says: what have you heard them say, word for word?"
- "Does: what have you watched them do?"
- "Thinks: what's on their mind that they might not say out loud?"
- "Feels: what worries them, and what excites them?"
- "Where do Says and Does disagree?"
- "Can you imagine yourself in their shoes? What would you need?"

**Materials:** a large sheet or whiteboard, markers and sticky notes for everyone, and colored dots. Use one sticky color for observed notes and another for assumptions, or put a "?" on every hunch.

**Board layout (wall or Mural):**

```
┌───────────────┬───────────────┐
│     SAYS      │    THINKS     │
│          ( user: name,        │
├───────────── role, context ) ─┤
│     DOES      │     FEELS     │
└───────────────┴───────────────┘
legend: plain = Evidence · ? = Assumption / Question      parking lot →
```

**Afterwards:** give Claude a photo of the wall or the Mural export. Claude digitizes it and keeps the tags.

## Output
Save to `design-thinking/empathy-map-<user>.md` using this template:

```markdown
# Empathy Map: <user>

**User:** <name, or archetype label> · <role> · <who they are and what they do>
**Based on:** <source IDs, types and dates> · **Contributors:** … · **Date:** …

## Says
### <cluster title>
- "<verbatim quote>". Evidence: <source>

## Thinks
### <cluster title>
- <inferred thought>. Assumption | Evidence: <source, if they said it>

## Does
### <cluster title>
- <behavior> (observed or reported). Evidence: <source>

## Feels
### <cluster title>
- <emotion> because <cause>. Assumption | Evidence: <source>

## Tensions and insights
| Insight | Quadrants | Supporting notes | Tag |
|---|---|---|---|

## What this suggests they need
- <implication, to carry into Needs Statements>. Assumption

## Evidence balance
- Evidence: <n> · Assumption: <n> · Question: <n> · Quadrants with no evidence: …

## Parking lot
- …

## Playback
- **Key takeaways (3–5):** …
- **Assumptions and questions to validate:** …
- **Recommended next activity:** `/edt-synthesize:needs-statements`
```

## Quality checks
- The map covers one user. If the notes describe two different people, split them into two maps.
- The center describes a specific person in context, not a demographic.
- Says holds verbatim quotes, and Does holds observable behavior. Thinks and Feels add something, rather than restating Says.
- Every note is tagged. Inferences in Thinks and Feels are Assumptions unless the user voiced them.
- Feels names an emotion *and* its cause. "Frustrated" on its own doesn't help the team.
- Clusters are titled, and at least one tension across quadrants is called out.
- If most notes are assumptions, the Playback says so plainly and recommends research.
- There are no features or solutions on the map.
- Pitfalls:
  - Describing your product instead of the user's life
  - Generic notes like "busy, wants efficiency"
  - Averaging several users into one
  - Skipping clustering, so the map stays a pile of notes

## Next
- `/edt-synthesize:as-is-scenario-map`: lay out this user's current experience step by step.
- `/edt-synthesize:needs-statements`: turn the clusters and tensions into needs.
- `/edt-plan:assumptions-and-questions`: prioritize the assumptions this map surfaced.
- `/edt-gather:interviews` or `/edt-gather:contextual-inquiry`: fill the quadrants that have no evidence.
- `/edt-core:sponsor-users`: validate the map with real users.

## Source
[IBM Enterprise Design Thinking Toolkit: Empathy Map](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac17)
