---
name: as-is-scenario-map
description: Maps a user's current end-to-end experience as named phases with Doing, Thinking and Feeling rows, then marks the highs, the lows and the gaps in team knowledge. Use when the user says "as-is scenario", "current-state journey", "journey map", "map the current experience", "where are the pain points?", "how does it work today?", or at the start of new work to surface what the team knows and doesn't.
argument-hint: "[user and scenario] [facilitate]"
---

# As-is Scenario Map

> IBM Enterprise Design Thinking · Synthesize research · Reflect · ~30 min

Before you can improve an experience, the team has to agree on what it is today. An as-is scenario map lays out a user's present experience phase by phase: what they're doing, thinking and feeling at each step. The team can then see where things work, where they break, and where nobody actually knows. It turns scattered research into one shared picture of current reality and points to opportunities for improvement. This is Reflect. The future experience belongs on a to-be map, where you Make.

## When to use it
- As the team starts a new body of work, to surface what it collectively knows and doesn't know.
- After research, to make sense of interview and observation data.
- When stakeholders disagree about where the real problem is.
- Before writing Hills or a to-be scenario.

## Inputs
- Upstream artifacts in `design-thinking/`:
  - **The user:** `empathy-map*` (use the same user)
  - **Research:** `interviews*`, `contextual-inquiry*`, `sponsor-users*`
  - **Context:** `stakeholder-map*`, for the other people involved in the experience
  - **History:** earlier `as-is-scenario-map*` files
- Ask the user for anything still missing:
  - Which one user the map is for
  - Which scenario, with a clear start and end. For example: "from noticing a billing error to seeing it corrected".
  - The research sources. If there are none, the map is a picture of team assumptions and must be labeled that way. Point to `/edt-gather:contextual-inquiry`.

## Co-create with Claude
1. **Set up.** Agree on the user and the scenario, including the trigger that starts it and the outcome that ends it. Create four rows: **Phases**, **Doing**, **Thinking** and **Feeling**. Add an optional row for tools or people involved only if the user wants it.
2. **Brainstorm.** Pull the steps from the research. Ask what the user is doing, thinking and feeling throughout the experience. Write one item per note, tag each one, and cite its source. Then ask the user what the team knows beyond the documents, and tag that as well. Include steps outside your product: other tools, other people, paper and waiting.
3. **Review and cluster.** Put the items in time order and group them into phases. Name each phase from the user's point of view with a verb, for example "Find a flight", not "Search module". Most scenarios have 4–8 phases. Mark empty cells explicitly instead of filling them with guesses.
4. **Identify highs, lows and gaps.** Mark the especially positive moments and the especially negative ones, and the areas where the team needs to learn more. Annotate each mark with why it matters, for example "Critical moment for trust", "Missed opportunity" or "Works well today, so protect it". Optionally score each phase's emotion from −2 to +2 to draw a curve.
5. **Playback.** Answer two questions. Which parts are we certain are true, and on what evidence? Where are the gaps in the team's knowledge? List the top lows as candidate opportunities, and recommend what comes next.

## Facilitate a live session
**Agenda (30 min)**
- **0–3:** Intro. Explain why you're doing this and the norms: write before you talk, there are no bad ideas, stay focused on users, use a parking lot.
- **3–5:** Setup. Write the scenario, with its start and end, across the top. Write the row labels down the left side.
- **5–15:** Brainstorm. Everyone writes silently, one note each, placing each note in its row.
- **15–22:** Review and cluster. Order the notes left to right, draw rough column lines, and name the phases.
- **22–27:** Identify. Circle and label the highs and lows, and put a "?" on blank areas.
- **27–30:** Playback. One or two people tell the story, then ask what we're certain of and where the gaps are.

**Prompts to read aloud**
- "What is our user doing, thinking and feeling throughout this experience? One idea per sticky."
- "What happens *before* they ever touch our product? What happens after?"
- "Where would they say 'this part is great'? Where would they give up?"
- "Which of these notes did we actually see or hear? Which are we guessing?"
- "Where on this map are we least sure what happens?"

**Materials:** a long wall or a wide Mural canvas, sticky notes in three colors (one each for Doing, Thinking and Feeling), markers, and symbols for highs (+), lows (−) and gaps (?).

**Board layout (wall or Mural):**

```
Scenario: <user> — from <start> to <end>
            │ Phase 1   │ Phase 2   │ Phase 3   │ Phase 4   │
 Phases     │ <verb…>   │ <verb…>   │ <verb…>   │ <verb…>   │
 Doing      │ ▢ ▢       │ ▢ ▢ ▢     │ ▢         │ ▢ ▢       │
 Thinking   │ ▢         │ ▢ ▢       │ ?         │ ▢         │
 Feeling    │ ▢         │ ▢ ▢       │ ▢         │ ▢         │
 Highs/lows │ +         │ − −       │ ?         │ +         │   parking lot →
```

**Afterwards:** give Claude a photo of the wall or the Mural export, and Claude digitizes it into the template below.

## Output
Save to `design-thinking/as-is-scenario-map-<topic>.md` using this template:

```markdown
# As-is Scenario Map: <user>, <scenario>

**User:** … (see `empathy-map-<user>.md`) · **Scenario:** from <start> to <end>
**Based on:** <source IDs> · **Contributors:** … · **Date:** …

## Overview
| | <Phase 1> | <Phase 2> | <Phase 3> | … |
|---|---|---|---|---|
| **Moment** | High / Low / Gap / — | … | … | … |
| **Emotion (−2…+2)** | … | … | … | … |

## Phases
### 1. <Phase name>
- **Doing:** <step>. Evidence: <source>
- **Thinking:** "<quote>" or <inferred thought>. Evidence: <source> | Assumption
- **Feeling:** <emotion> because <cause>. Assumption
- **Gaps:** <what we don't know>. Question

## Highs, lows and gaps
| Phase | High / Low / Gap | Why it matters | Tag |
|---|---|---|---|

## Opportunities
- <a low or gap worth designing for>. Linked phase: …

## Confidence
- **Certain (evidence-backed):** …
- **Gaps in team knowledge:** …

## Parking lot
- …

## Playback
- **Key takeaways (3–5):** …
- **Assumptions and questions to validate:** …
- **Recommended next activity:** `/edt-synthesize:needs-statements`
```

## Quality checks
- The map covers one user and one scenario, with an explicit start and end.
- Phases are named from the user's point of view, in their words. They are not system components or departments.
- It shows today's reality, including the workarounds, and not the official process or a fixed version. Solutions and features belong on the to-be map.
- Each phase has Doing, Thinking and Feeling filled in, or an explicit "?".
- Feeling names emotions with causes, and they vary across phases. If every phase says "frustrated", dig deeper.
- Highs are marked as well as lows, because what works today has to survive into the to-be.
- Every note is tagged, and gaps are named, not filled with guesses.
- Pitfalls:
  - Mapping only your product's screens instead of the whole experience
  - Going click-level detailed, or so coarse that there are only three phases
  - Blending several users into one journey

## Next
- `/edt-synthesize:needs-statements`: turn the lows and gaps into needs.
- `/edt-plan:hills`: write intent around the moments that matter most.
- `/edt-ideate:to-be-scenario-map`: reimagine the same scenario as it could be.
- `/edt-ideate:big-idea-vignettes`: generate ideas for the biggest lows.
- `/edt-gather:contextual-inquiry`: go and observe the phases marked as gaps.
- `/edt-plan:assumptions-and-questions`: prioritize what the map left uncertain.

## Source
[IBM Enterprise Design Thinking Toolkit: As-is Scenario Map](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac29)
