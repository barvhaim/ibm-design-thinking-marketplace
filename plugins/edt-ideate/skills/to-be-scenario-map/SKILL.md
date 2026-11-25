---
name: to-be-scenario-map
description: Map a future experience in which your ideas already exist, covering what the user does, thinks and feels in each phase, and compare it with the as-is map to show which pain points and needs it resolves. Use when someone says "to-be map", "future-state journey", "what would the future look like", "how would our idea change their day", or after ideating, to align stakeholders and users on intent.
argument-hint: "[user, scenario or idea] [facilitate]"
---

# To-be Scenario Map

> IBM Enterprise Design Thinking · Generate new ideas · Reflect / Make · ~60 min

An as-is scenario map shows what users struggle with today. A to-be map imagines your ideas already exist and walks the same user through the same goal again, phase by phase: what they do, think and feel. The team can then reflect honestly on whether its ideas address current needs, or whether they only look good on a sticky note. The result is a coherent story to put in front of stakeholders and Sponsor Users so everyone aligns on intent before anything is built.

## When to use it
- After Big Idea Vignettes or any ideation, to see how the chosen ideas fit together end to end.
- To check that the ideas resolve the as-is pain points and needs statements.
- To prepare a Playback, because a to-be map is a strong artifact for aligning stakeholders and users.
- To compare competing directions: sketch two or three rough alternative futures instead of debating in the abstract.

## Inputs
- Upstream artifacts in `design-thinking/`: `as-is-scenario-map-*` (the essential baseline), `needs-statements-*`, `hills-*`, `big-idea-vignettes-*` (the ideas in scope) and `empathy-map-*`.
- If there's no as-is map, recommend `/edt-synthesize:as-is-scenario-map` first. If the user wants to continue anyway, ask them to describe today's experience briefly and tag it as an Assumption.
- If there are no ideas yet, ask which ideas this future contains, or suggest `/edt-ideate:big-idea-vignettes`.

## Co-create with Claude
1. **Anchor.** Create `design-thinking/` if missing, list it, and read the upstream artifacts. Restate the user, the goal and the ideas in scope. Use the same user and goal as the as-is map, for example "assign a workstation to a new employee". List the as-is pain points and needs statements this map must answer, with their tags and sources.
2. **Set up the rows:** Phases, Doing, Thinking and Feeling. Leave Phases blank for now, because they emerge from clustering.
3. **Brainstorm.** Imagine the ideas are real today, and walk the user's journey from trigger to goal. At each moment, what does the user do, think and feel? Ask the user to go first, then add your own. Write one item per bullet, the way you would on a sticky note, and write Thinking and Feeling in the user's voice. Revisit each as-is pain point and ask what happens at that moment now. Some steps should disappear, and that's often the biggest win.
4. **Cluster into phases.** Group similar items, refine their order and name each phase from the user's point of view ("Getting set up", not "Provisioning"). Phases don't have to match the as-is map.
5. **Identify highs and lows.** Mark ▲ highs and ▼ lows. Be honest: a credible future still has lows, such as waiting, learning something new, deciding whether to trust it, and new failure modes the idea introduces. Compare each as-is pain point with the to-be moment and mark it resolved, improved, unchanged or worse.
6. **Find the gaps.** Which needs are still unaddressed? Which lows need new ideas? For those, loop back to `/edt-ideate:big-idea-vignettes`. What must be true for this future to work?
7. **Tag.** A to-be map is envisioned, so its Doing, Thinking and Feeling items are Assumptions until you test them with users. Pain points carried over from the as-is map keep their Evidence tags and sources. Open unknowns are Questions.
8. **Save and play back** using the template below.

Describe the user's experience, not the system's: "Sam sees her desk on her phone", not "the API syncs records". Keep UI detail out, because that comes later in `/edt-test:wireframes`.

## Facilitate a live session
**Agenda (60 min)**

| Time | Step | Notes |
|---|---|---|
| 0–5 | Intro & norms | Hang the as-is map above the new board and recap its pain points · write before you talk · yes, and · parking lot |
| 5–8 | Setup | Draw four rows labeled Phases, Doing, Thinking and Feeling. Read the scenario aloud |
| 8–25 | Brainstorm | Write silently, one sticky per answer with one color per row, then share |
| 25–37 | Cluster phases | Group, reorder, draw rough columns and name each phase |
| 37–50 | Highs & lows | Circle and label positives and negatives, compare with the as-is and list gaps |
| 50–60 | Playback | One or two people present the map, and the group discusses |

**Prompts to read aloud**
- "Imagine our ideas exist today. <User> is trying to <goal>. What's the first thing they do?"
- "What are they thinking at this moment? Write it as a quote."
- "How do they feel here, and is it better or worse than on the as-is map?"
- "Find that pain point on the as-is map above. What happens at that moment now?"
- Playback: "How does our idea change this user's experience? Where are there still gaps?"

**Materials:** the as-is map, sticky notes in three colors (Doing, Thinking, Feeling), markers, tape or a marker for the phase columns, and red and green markers for lows and highs.

**Board layout (physical wall or Mural)**
```
+-----------------------------------------------------------+
| AS-IS MAP (reference, directly above)                     |
+----------+-----------+-----------+-----------+------------+
| Phases   | <Phase 1> | <Phase 2> | <Phase 3> |  PARKING   |
| Doing    |           |           |           |  LOT       |
| Thinking |           |           |           |            |
| Feeling  |  (circle highs ▲ and lows ▼ in place)          |
+----------+-----------+-----------+-----------+------------+
```

**After the session:** ask for photos or a Mural export. Transcribe the phases and stickies word for word, record the circled highs and lows, then fill in the as-is vs. to-be comparison with the user.

## Output
Save to `design-thinking/to-be-scenario-map-<topic>.md` using this template:

```markdown
# To-be Scenario Map: <user>, <goal>
_Date · Participants · Mode: co-create | facilitated · Builds on: <as-is map file>, <ideas file>_

## Scenario
- **User:** … · **Goal:** … · **Ideas in this future:** …

## What this future must answer
| As-is pain point or need | Tag and source |
|--------------------------|----------------|
| | Evidence: <source> |

## Map
| | <Phase 1> | <Phase 2> | <Phase 3> |
|---|---|---|---|
| **Doing** | | | |
| **Thinking** | "…" | | |
| **Feeling** | | | |
| **High / Low** | ▲ … | ▼ … | |

All map items are Assumptions until tested with users.

## As-is vs. to-be
| Pain point or need | As-is moment | To-be moment | Status: resolved / improved / unchanged / worse |
|---|---|---|---|

## Gaps and new risks
- Question: …

## Playback
- **Key takeaways:** 3–5 bullets (biggest improvement, remaining lows, what surprised us)
- **Assumptions and questions to validate:** the riskiest few, and who could validate them (Sponsor Users)
- **Recommended next activity:** for example `/edt-ideate:storyboards` to tell this story visually
```

If the map has more than about five phases, replace the map table with one section per phase that contains Doing, Thinking, Feeling and High/Low.

## Quality checks
- **Relates back to the as-is map:** it has the same user and goal, and every key pain point is accounted for.
- **Resolves pain points or fulfills needs statements:** the traceability tables are complete, and an idea that addresses nothing is questioned.
- **Tells an engaging story** that someone outside the team can follow in a couple of minutes.
- The language is user-centric. Thinking items are quotes, and Feeling items name specific emotions like "relieved" or "uneasy" instead of "good".
- It has honest lows and named gaps. An all-highs map isn't credible.
- It isn't a feature spec and has no UI detail.
- Envisioned items are tagged as Assumptions, and nothing is presented as if it were observed.

## Next
- `/edt-ideate:storyboards`: turn this future into a visual story for stakeholders and users.
- `/edt-plan:hills`: capture the intended outcome as a Hill (Who, What, Wow).
- `/edt-plan:assumptions-and-questions`: plan how to validate the riskiest assumptions.
- `/edt-align:playbacks`: present the to-be map to stakeholders and Sponsor Users.
- `/edt-test:paper-prototypes`: make the highest-value phase testable.

## Source
[IBM Enterprise Design Thinking Toolkit: To-be Scenario Map](https://www.ibm.com/downloads/documents/us-en/137a3e34823ed9aa)
