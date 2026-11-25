---
name: retrospectives
description: Runs a retrospective after an iteration. The team captures what went well, what didn't and what to try, clusters it, plays it back, and leaves with a few owned experiments. Use when the user says "retro", "retrospective", "sprint retro", "post-mortem", "lessons learned", "what went well / what didn't", "how can we work better as a team?", or a sprint, iteration, release or project phase has just ended.
argument-hint: "[sprint, iteration or phase] [facilitate]"
---

# Retrospectives

> IBM Enterprise Design Thinking · Align your team · Reflect · ~60 min

A retrospective is the team reflecting together at the end of a stretch of work. It looks at how the team worked, not only what it shipped, and turns that into concrete ways to improve its workflows and dynamics. It is restless reinvention applied to the team itself: the way you work is a prototype too. A good retro is safe, inclusive and specific. It uses disagreement productively, and it ends with a few owned changes instead of a long list of complaints.

## When to use it
- At the end of a sprint, iteration, release or project phase.
- After a Playback, a launch or an incident, when the team wants to learn from it.
- When friction keeps coming back: missed handoffs, recurring blockers, unclear ownership.

## Inputs
- Upstream artifacts in `design-thinking/`:
  - **Last retro:** earlier `retrospectives*` files. What did we agree to try, and did it work?
  - **Kickoff:** `hopes-and-fears*`. Which hopes came true, and which fears?
  - **Daily syncs:** `daily-syncs*`. Recurring blockers and the after-sync topics.
  - **Playbacks:** `playbacks*`. Stakeholder feedback and misalignment.
  - **Plans:** `hills*`, `experience-based-roadmap*`. Did we move toward the user outcomes we committed to?
- Optional evidence from the repo, read-only: `git log --since="<iteration start>" --no-merges --oneline | wc -l`, plus reverts, hotfixes and the PR cycle time from `gh pr list --state merged`. Treat these numbers as prompts for discussion, never as a scorecard.
- Ask the user for anything still missing:
  - The iteration's dates and its goal or Hill
  - Who participated, by role
  - The captured notes: a chat thread, a form, a Mural export, or a photo of the wall

## Co-create with Claude
1. **Schedule and scope.** Confirm the iteration window, the goal, and that everyone who did the work can attend or contribute asynchronously. Pull in the inputs above. Then draft a one-paragraph **look back**: the goal, what was delivered, the status of the last retro's experiments, and kickoff fears that came true. Tag each item.
2. **Set up the prompts.** The default is three columns: **What went well? · What didn't go well? · What might we try next?** Offer the four-quadrant variant for a deeper retro: **Worked well · Needs to change · Unanswered questions · New ideas to try**. Keep the prompts about how we work and what users got, not about who to blame.
3. **Capture.** Each person writes one idea per note, silently. Write before you talk. Claude drafts an async form for the user to send, and helps the user add their own notes. Claude never makes up teammates' input. Tag each note:
   - **Evidence:** the note cites something that happened, with a date, ticket or log.
   - **Assumption:** a belief about a cause.
   - **Question:** an open unknown.
4. **Cluster.** Group similar notes into titled themes, and count the notes in each. Then flag:
   - Themes that appear in both *went well* and *didn't go well*
   - Repeats from the last retro, which mean an earlier fix didn't stick
5. **Playback.** One person plays back the positive and the negative clusters. Mark notes the whole team doesn't understand, and have the author clarify them. Claude drafts this playback script.
6. **Ideate and choose.** For each *didn't go well* cluster, generate several ways to address it. Build on each other's ideas with "yes, and…". Pick **2–3 experiments** by collective input, such as dot voting or impact against effort. Each experiment gets:
   - An owner
   - A signal that shows it worked
   - A date to check in, usually the next retro

   Fewer, owned experiments beat many wishes.

## Facilitate a live session
**Agenda (60 min)**
- **0–5:** Welcome, purpose and ground rules. Review the experiments from the last retro.
- **5–15:** Silent capture across all columns.
- **15–25:** Post the notes and cluster them, then title the themes.
- **25–35:** Playback of the positive and negative clusters, with clarifying questions.
- **35–50:** Ideate fixes for each *didn't go well* cluster, then dot-vote.
- **50–60:** Commit to 2–3 experiments with owners and signals. Close with a one-word check-out.

**Prompts to read aloud**
- "We're here to improve how we work, not to judge anyone. Assume everyone did their best with what they knew."
- "Silently, for ten minutes: what went well, what didn't, what might we try? One idea per note."
- "Which of these would make the biggest difference to our users or to our team next iteration?"
- "Who owns this, and how will we know it worked?"

**Materials:** sticky notes in three or four colors (one per column), markers for everyone, dot stickers, a timer, and the list of the last retro's experiments.

**Board layout (wall or Mural):** three columns, *Went well · Didn't go well · Try next*, with arrows from each *didn't go well* cluster to the ideas that address it. Or use four quadrants: *Worked well · Needs to change · Questions · New ideas*. Add a parking lot along the bottom.

**Tips**
- Everyone participates. The facilitator should stay neutral, or rotate the role.
- Park off-topic issues.
- Start on time and stay on time.

**Afterwards:** give Claude the photo of the wall or the Mural export, and Claude digitizes it into the template below.

## Output
Save to `design-thinking/retrospectives-<iteration>.md` using this template:

```markdown
# Retrospective: <sprint, iteration or phase>

**Dates:** … · **Goal / Hill:** … · **Participants (roles):** … · **Format:** 3-column | 4-quadrant

## Look back
- **Last retro's experiments:** <experiment>: kept | dropped | didn't try. Evidence: …
- **Kickoff hopes and fears:** <which came true>
- **Signals:** <delivery notes, recurring blockers>. Evidence: <source>

## What went well
### <Theme> (<n> notes)
- <note>. Evidence | Assumption | Question

## What didn't go well
### <Theme> (<n> notes)
- <note>. Evidence | Assumption | Question

## Unanswered questions (4-quadrant only)
- …

## Experiments to try next
| Experiment | Addresses | Owner | Signal it worked | Check-in |
|---|---|---|---|---|

## Parking lot
- …

## Playback
- **Key takeaways (3–5):** …
- **Assumptions and questions to validate:** …
- **Recommended next activity:** `/…`
```

## Quality checks
- Every note comes from a participant. Claude only adds context drawn from artifacts, and labels it with its source.
- Notes are specific and observable. "Design specs landed after sprint planning twice" is better than "communication was bad".
- The retro reviewed the last retro's experiments before generating new ones.
- The team commits to 2–3 experiments at most. Each has an owner, a signal and a check-in date.
- At least one theme considers the user. Did our way of working help or hurt what users got?
- Metrics and git stats start conversations. They never rank individuals.
- Pitfalls:
  - Blaming people instead of processes
  - The same complaints every sprint with no follow-through
  - The loudest voice setting the agenda
  - Skipping the retro when the team is busy

## Next
- `/edt-align:hopes-and-fears`: kick off the next iteration and refresh the team's expectations.
- `/edt-align:daily-syncs`: build the chosen experiments into the daily cadence.
- `/edt-align:playbacks`: if the retro surfaced misalignment with stakeholders, plan a Playback.
- `/edt-core:practice-check`: check how well the team is applying EDT principles overall.

## Source
[IBM Enterprise Design Thinking Toolkit: Retrospectives](https://www.ibm.com/downloads/documents/us-en/137a3e3494bed9b0)
