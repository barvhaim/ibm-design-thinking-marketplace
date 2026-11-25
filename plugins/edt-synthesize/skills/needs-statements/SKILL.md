---
name: needs-statements
description: Turns research into Needs Statements ("[user] needs a way to [need] so that they [benefit]") as an HTML artifact. It diverges on needs, converges on 3–5 statements traced to upstream notes, and can have simulated users react to and rank them. Use when the user says "needs statements", "user needs", "what does our user actually need?", "problem statements", "reframe these features as needs" or "turn research into needs", or after research and before ideation or Hills.
argument-hint: "[user] [facilitate]"
---

# Needs Statements

> IBM Enterprise Design Thinking · Synthesize research · Reflect, leading into Make · ~30 min

Teams jump to features. Needs Statements bring the conversation back to what users actually require to reach their goals, and why it matters to them. Once you've outlined what users need, ideation can focus on ideas that help them get there. The format keeps three things together: a specific **user**, a **need** stated as something they do or achieve (not a feature), and the **benefit** they get from it. Needs Statements are only as reliable as the research behind them, so every statement shows which notes it is built on and where those came from. This is Reflect, and it sets up Make: good needs make ideation and Hills much sharper.

## When to use it
- After research, when the team wants to reframe its thinking to be more user-centered. Ask: "What does our user actually need?"
- When a backlog or PRD is a list of features and nobody can say what they're for.
- Before ideation, or before writing Hills.
- When stakeholders are arguing about solutions. Step back to the need.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of:
  - synthesis: `empathy-map-*` (especially the Thinks and Feels clusters, the tensions and the implications), `as-is-scenario-map-*` (the lows, gaps and opportunities)
  - research: `interviews-*` (themes), `contextual-inquiry-*` (workarounds), `sponsor-users-*`
  - `simulated-users.html`
- **Files the user points to,** such as PRDs, backlogs and tickets. Feature requests in them are raw material to reframe, not needs.
- **The simulated user panel.** If you'll run the reaction round and `design-thinking/simulated-users.html` doesn't exist, create it first, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`.
- **Ask the user only for:** which user the statements are for, if it isn't clear. Use the same user as the empathy map.
- If there's no upstream research at all, say so. Offer to run `/edt-gather:interviews` or `/edt-synthesize:empathy-map` first, or draft statements that rest openly on assumptions and simulated users.

## Co-create with Claude
1. **Gather.** List `design-thinking/` and read the upstream `items`. Pull out the raw material: quotes about goals, workarounds, the lows and gaps on the as-is map, and the tensions on the empathy map. Keep each item's ID, tag and source, so every statement can trace back. Invite the user to bring in a Sponsor User if possible.
2. **Set up.** Write the frame, with the user filled in as specifically as you can, by role and context:
   **[Our user] needs a way to [address this need] so that they [benefit in this way].**
3. **Diverge.** Ask the user to write their own candidates first (write before you talk). Then Claude adds more, aiming for 15–30 in total. Each candidate is one note that pairs a need with a benefit and cites the upstream items behind it. Tag it by what backs it: `evidence` when a real source shows it (cite the `S…`), `simulated` when only simulated users do (cite the `SU-…`), and `assumption` when nothing upstream does. Then screen out features:
   - **Spot them.** If a note talks about the machine (a dashboard, a button, a click, an app, an alert, "AI"), it's a feature.
   - **Ladder it.** Ask "What would that let them do?" and then "Why does that matter to them?" Keep the answer and drop the feature.
   - **Cover the levels.** Include task needs, relationship and social needs (trust, belonging, looking competent), and emotional needs, wherever the research supports them.
4. **Converge.** Cluster similar candidates and title the clusters, for example *Work to be done*, *Big pain points* or *Key goals*. For each important cluster, write one statement in exactly the frame's format. Aim for **3–5 strong statements**. Run each one through the quality checks, and record its confidence:
   - **High:** backed by several real sources.
   - **Medium:** one real source, or real and simulated together.
   - **Low:** simulated or assumed only. Add how to validate it.
5. **Ask simulated users to react (optional, offer it).** Show the converged statements to 2–4 personas who are this user, one at a time, in character. Ask: "Which of these sounds like your week? Which is wrong, or not your problem? How would you say the 'so that' part?" Then ask each to rank the statements by what matters most to them. They react to needs, not features, so never ask "Would you use…?". Expect at least one persona to reject a statement or say it misses the point. Keep each transcript, and record each ranking and objection as `simulated` notes. Reword a statement in a persona's words only if it keeps the format, and say so. Reactions never raise a statement's confidence.
6. **Playback.** Read the converged statements back. Ask what new questions this exercise raised. Put the low-confidence statements the team leans on most at the top of "Validate next". Recommend going straight into ideation while the needs are fresh, then publish the page.

**Reframing features as needs.** These examples are hypothetical illustrations, not research.

| Feature-shaped | Needs Statement |
|---|---|
| "Managers need an approvals dashboard." | "Finance managers need a way to see which approvals are stuck before month-end so that they can close the books on time without chasing people." |
| "New developers need a Slack bot." | "Developers new to the codebase need a way to find who owns a service so that they can get unblocked the same day." |

## Facilitate a live session
Produce `design-thinking/needs-statements-<user>-kit.html`. It needs:
- **Agenda table (30 min):**
  - 0–3 Intro: why you're doing this, and the norms (write before you talk, there are no bad ideas, everyone participates, build with "yes, and…")
  - 3–5 Gather: post the empathy map, the as-is map and the key research where everyone can see them. Sponsor Users join if possible.
  - 5–7 Setup: write the frame large across the top of the wall, with the user filled in
  - 7–17 Diverge: everyone writes silently, the need on one sticky note and the benefit on another beside it. The facilitator calls out features as they appear.
  - 17–27 Converge: cluster the notes, label the clusters, and write a few Needs Statements in the exact format
  - 27–30 Playback: one person reads the converged statements. Capture new questions, and book the ideation session.
- **Prompts to read aloud:** "What does our user actually need? Not what should we build." "Need on the left sticky, benefit on the right: 'so that they…'" "If your note names a screen, a button or a technology, ask: what would that let them do?" "Which research note backs this up? If none, mark it 'Assumption?'" "Is this a benefit to the user, or to us?"
- **Materials:** markers and sticky notes in two colors, one for needs and one for benefits, plus dots for marking assumptions.
- **The board:** the frame across the top, a diverge area that becomes cluster circles, a strip of empty `.stmt` cards for the converged statements, an "Assumption?" corner for notes with no evidence behind them, and a parking lot. Optionally seed the diverge area with upstream notes, keeping their tags.

After the session, read the photo of the wall or the Mural export and build the results page, keeping each note's tag.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/needs-statements-<user>.html`. `${CLAUDE_PLUGIN_ROOT}/shared/example-empathy-map.html` shows a finished page.
- **Title:** `<User> Needs Statements`, for example "Release Engineer Needs Statements".
- **Sections:**
  1. **Needs Statements:** `.stmts`, one `.stmt` per statement. In `.say`, label the parts `User`, `Need` and `Goal` (the benefit). In `.why`, show one pill per provenance tag with its sources, a confidence pill (`data-tone="good"` high, `"warn"` medium, `"bad"` low), and "Built on:" with the upstream items and their groups.
  2. **Clusters:** titled `.cluster`s of candidate `.note`s, each reading "Need · Benefit", tagged and sourced.
  3. **Features we reframed:** a table of the original feature, the underlying need, and the statement or cluster it went to.
  4. **Simulated reactions:** a table with one row per statement and one column per persona, showing their rank and their objection, followed by a `details.transcript` per persona. Include this only when you ran the round.
  5. **Parking lot,** if anything landed there, then the **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "user": { "role": "", "context": "", "empathy_map": "design-thinking/empathy-map-<user>.html" },
    "statements": [{ "id": "NS1", "user": "", "need": "", "goal": "", "cluster": "", "built_on": ["N3", "N8"],
                     "tags": ["simulated", "evidence"], "sources": ["SU-2", "S1"], "confidence": "medium", "validate_by": "" }],
    "clusters": [{ "title": "", "candidates": ["C1", "C2"] }],
    "reframed": [{ "feature": "", "need": "", "went_to": "NS2" }],
    "reactions": [{ "persona": "SU-2", "ranking": ["NS2", "NS1", "NS3"], "notes": ["N21"] }],
    "parking_lot": [""] }
  ```
  `built_on` holds upstream item IDs, and `upstream` in the envelope names the pages they come from. `items` holds every candidate and reaction note, with `group` set to its cluster or `"Reactions"`.

## Quality checks
- Every statement follows the format exactly: "<user> needs a way to <need> so that they <benefit>."
- The user is specific, a role in a context, and matches the empathy map. "Users" or "customers" is too vague.
- The need is solution-agnostic. It names no UI, technology or product, and it is led by a verb such as know, decide, prove or hand off.
- The benefit is the user's outcome. "So that we increase retention" is a business goal, so reframe it or carry it to the Hills discussion.
- The need and benefit aren't the same thing restated. "A way to save time so that they save time" fails.
- Each statement traces to upstream items. A statement resting only on simulated or assumed items says so, has low confidence and names how to validate it. No simulated note is tagged `evidence`.
- There are 3–5 statements, not 30, and they cover different clusters rather than variations of one.
- In the reaction round, personas disagree with each other and reject something. If every persona ranks the same way or loves every statement, rerun them with more friction. Rankings are counts of simulated users ("2 of 4 ranked NS2 first"), never percentages or votes that settle priority.
- Pitfalls:
  - Writing features in disguise, for example "needs a way to get alerts"
  - Needs too broad to act on, for example "needs a way to be productive"
  - Inventing needs the research never showed, or letting a persona invent one

## Next
- `/edt-ideate:big-idea-vignettes`: ideate right away against the strongest needs.
- `/edt-plan:hills`: turn the most important needs into statements of intent (Who / What / Wow).
- `/edt-ideate:to-be-scenario-map`: imagine the future experience that meets these needs.
- `/edt-plan:prioritization-grid`: rank the needs or ideas by importance and feasibility.
- `/edt-plan:assumptions-and-questions`: plan how to validate the low-confidence statements.

## Source
[IBM Enterprise Design Thinking Toolkit: Needs Statements](https://www.ibm.com/downloads/documents/us-en/137a1e253e5bac0b)
