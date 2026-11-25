---
name: hopes-and-fears
description: Gathers and clusters a team's hopes and fears for upcoming work into shared themes, risks to watch and working agreements. Use at a kickoff or onboarding, or at the start of a project, sprint, quarter or initiative. Triggers include "hopes and fears", "kickoff activity", "icebreaker for the new team", "what is everyone worried about?", "align expectations", "onboarding a new teammate", or setting team norms.
argument-hint: "[project, sprint or initiative] [facilitate]"
---

# Hopes and Fears

> IBM Enterprise Design Thinking · Align your team · Reflect · ~30 min

Before a big commitment of work, a team rarely says out loud what it hopes for or what keeps it up at night. Hopes and Fears makes both visible. Hopes show the team's shared picture of success. Fears show the risks while they are still cheap to address. It is a fast way to get to know each other and align on intent, which is the Reflect part of the Loop. It also puts the diverse empowered teams principle into practice: everyone writes, so every voice is on the wall, not only the loudest or most senior.

## When to use it
- Anything that feels like a beginning: a project, initiative, sprint, quarter, iteration, release cycle, or any other large commitment of work.
- A new teammate, stakeholder or Sponsor User joins.
- The team is forming. Use it as the opening activity of a kickoff workshop.

## Inputs
- Upstream artifacts in `design-thinking/`:
  - **Context:** `hills*`, `stakeholder-map*`, `workshop-planner*`, `assumptions-and-questions*`
  - **History:** earlier `hopes-and-fears*` and `retrospectives*` files, to see which past fears came true
- Ask the user for anything still missing:
  - What is beginning, and the time horizon
  - Who is on the team, by role or discipline
  - The hopes and fears themselves: pasted notes, survey or chat replies, a Mural or whiteboard export, or a photo of the wall. Claude can read images.
- Never invent teammates' hopes or fears. If only the user's own input is available, say so and offer to collect the rest asynchronously (step 2).

## Co-create with Claude
1. **Set the frame.** Name the work you're about to begin and its horizon. Ask whether input should be anonymous. Fears come out more honestly when names are not attached.
2. **Collect silently.** Claude drafts a short async ask that the user can post in chat or a form. It includes the starter phrases and the rule of one idea per note:
   - **Hopes:** "I hope…", "It would be great if…"
   - **Fears:** "I'm concerned that…", "This would be great, but…"

   Suggest prompting for three kinds of hopes and fears: about **user outcomes** (did we keep users at the center?), about **how we'll work together**, and about **delivery**. The user contributes their own as well.
3. **Digitize.** Turn every input into one line, keeping the author's wording. Split notes that hold several ideas. Merge only exact duplicates, and count them, because several people writing the same thing is a signal. Tag each item:
   - **Assumption:** the default, because these are beliefs about the future.
   - **Evidence:** the item rests on something observed, with its source, for example "the last two releases slipped (Q2 retro)".
   - **Question:** an open unknown, for example "Will we get Sponsor User access?"
4. **Cluster.** Group the hopes into themes and the fears into themes, and give each theme a short title, such as *Workflow*, *Alignment*, *Constraints* or *User value*. Look for **mirrored themes**: the same topic on both sides, for example hoping for smooth sprint planning while fearing too many meetings. Mirrored themes are where the team most needs an agreement.
5. **Hang it up: decide how you'll work.** For each major theme, draft:
   - **From hopes:** a working agreement that makes the hope more likely.
   - **From fears:** a risk entry with an early-warning sign, a mitigation and an owner. Fears that are really unknowns become questions to validate.

   Have the team review the drafts. Claude proposes them, and the team decides.
6. **Playback.** Draft two short summaries, one for the hopes and one for the fears, so that two different people can present them. Save the artifact somewhere the team will see it again, and schedule a revisit at the next retrospective.

## Facilitate a live session
**Agenda (30 min)**
- **0–3:** Intro. Explain why you're doing this and the ground rules: write before you talk, one idea per note, there are no bad ideas.
- **3–10:** Silent ideation. Everyone writes hopes and fears and posts them on the wall.
- **10–20:** Discuss and cluster. Circle and title the themes, and draw links between mirrored themes.
- **20–25:** Hang it up. Agree on 2–4 working agreements and the top risks.
- **25–30:** Playback. One person presents the Hopes, another presents the Fears.

**Prompts to read aloud**
- "For the next seven minutes, silently write your hopes and fears about <work>. One idea per sticky note."
- "Starters: I hope… · It would be great if… · I'm concerned that… · This would be great, but…"
- "Include at least one hope or fear about our users, not only about us."
- "Which fear would hurt most if it came true? What would we notice first?"

**Materials:** a marker and a sticky-note pad for everyone, a large sheet or whiteboard, a timer, and dot stickers if you want to vote on the top fears.

**Board layout (wall or Mural):** a vertical line down the center, with **Hopes** on the left and **Fears** on the right. Leave space to circle and title clusters, and add a parking lot in the corner. On Mural, turn on anonymous stickies if the team wants them.

**Tips**
- Leaders write fears too. It makes candor normal for everyone else.
- Use "yes, and…" to build on a note instead of debating it.
- Watch the clock.
- Park off-topic issues instead of solving them now.

**Afterwards:** give Claude the photo of the wall or the Mural export, and Claude digitizes it into the template below.

## Output
Save to `design-thinking/hopes-and-fears-<topic>.md` using this template:

```markdown
# Hopes and Fears: <project or sprint>

**Date:** … · **Horizon:** … · **Participants (roles):** … · **Anonymous:** yes/no

## Hopes
### <Theme> (<n> notes)
- <hope, in the author's words>. Assumption | Evidence: <source> | Question

## Fears
### <Theme> (<n> notes)
- <fear>. Assumption | Evidence: <source> | Question

## Mirrored themes
| Theme | Hope side | Fear side | Agreement needed |
|---|---|---|---|

## How we'll work (working agreements)
1. <agreement>, which supports the hope "<theme>"

## Risks to watch
| Fear | Early-warning sign | Mitigation | Owner |
|---|---|---|---|

## Parking lot
- …

## Playback
- **Key takeaways (3–5):** …
- **Assumptions and questions to validate:** …
- **Revisit at:** <date or retrospective>
- **Recommended next activity:** `/…`
```

## Quality checks
- Every note traces to a participant. Claude did not add hopes or fears of its own, and it says when the input is partial.
- Each note holds one idea, in the author's wording. Themes are titled and counted.
- At least one hope or fear concerns users or user outcomes. If none does, flag it to the team.
- Every major fear has an early-warning sign and an owner, not only a mitigation.
- The working agreements are concrete and checkable, for example "Design and engineering pair on every story before estimation". "Communicate better" is too vague.
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
