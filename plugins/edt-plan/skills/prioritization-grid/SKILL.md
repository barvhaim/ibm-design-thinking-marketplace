---
name: prioritization-grid
description: Plots ideas, stories or features on importance to the user against feasibility for the team (or business value) as an HTML artifact, sorting them into No-brainers, Big bets, Utilities and Unwise. Simulated users rate importance one persona at a time; the team rates feasibility. Use when a team asks "what should we build first", "help us prioritize", "which ideas are worth it" or "we have too many ideas", or after ideation or backlog grooming.
argument-hint: "[set of ideas or backlog] [facilitate]"
---

# Prioritization Grid

> IBM Enterprise Design Thinking · Plan your work · Reflect · ~30 min

Most teams judge ideas too early and too often, so they come up with fewer of them. The brain can barely create and evaluate at the same time. So create first. Then use the Prioritization Grid to reflect on the ideas together, through the lens of user value against feasibility, or against business value. The goal isn't a perfect ranking. It's a shared view of which ideas are obvious wins, which are worth a serious bet, and which to let go, so the team can decide what to do next. The two axes have different judges: importance belongs to users, and feasibility belongs to the people who'll build it.

## When to use it
- After an idea-generating activity, such as big idea vignettes, a to-be scenario map or storyboards, when the team must converge.
- When grooming a backlog of user stories before a sprint or release.
- When stakeholders disagree about what comes first and need to see the tradeoffs.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of:
  - the ideas: `big-idea-vignettes-*`, `user-stories-*`, `to-be-scenario-map-*`, `storyboards-*`
  - importance: `hills-*`, `needs-statements-*`, `empathy-map-*`
  - risk: `assumptions-and-questions-*`
- **The simulated user panel,** `design-thinking/simulated-users.html`. Create it if it's missing (see `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`).
- **Ask the user only for:** the list of ideas, if none exists upstream; the team's capacity and constraints (skills, stack, deadlines, dependencies), which simulation can't supply; and whether to use business value instead of feasibility.
- A grid is only as good as the ideas on it. If there are only a handful, or they're all variations of one, suggest `/edt-ideate:big-idea-vignettes` first.

## Co-create with Claude
1. **Bring the ideas.** List `design-thinking/` and collect the candidate ideas with their sources. Rewrite each as a one-line card that says what the user gets, merge duplicates, and number them. Aim for roughly 8–25 distinct ideas.
2. **Set up the axes.** Agree on the definitions before scoring anything.
   - **Importance to the user**, from low to high: how much value the idea delivers to the target user. Anchor it to Hills and needs statements, not to how loudly a stakeholder asks.
   - **Feasibility for the team**, from difficult to easy: effort, skills, dependencies and technical risk.
   - Or **Business value** in place of feasibility, if the team chooses it. The team rates that axis too.
3. **Rate importance with simulated users, one persona at a time.** Pick 3–5 personas from the panel who represent the target user, including the skeptic and the edge case. Run each one separately, in character, and never show one persona another's ratings.
   - Read the cards in the persona's words, not product vocabulary, and shuffle the order for each persona.
   - Ask them first to sort the cards into "would change my week", "nice to have" and "don't care", then to rate each 1–5 with a one-line reason drawn from something they actually did recently.
   - Let them say "I don't get this one." That's a finding about the card.

   Record each persona's ratings separately. An idea's importance is the median of its ratings, shown with the spread (lowest to highest) and a count such as "3 of 4 simulated users rated it 4 or 5". Never turn it into a percentage or a decimal average. A wide spread usually means two kinds of user, so flag it rather than averaging it away. Where real evidence exists, such as a needs statement backed by evidence or a support-ticket count, it leads, and the simulated rating sits beside it.
4. **Rate feasibility as the team.** After every idea has an importance rating, score every idea on feasibility from 1–5 with a one-line reason, so a high score on one axis doesn't color the other. Simulated users never rate feasibility. If the product's code is in the working directory, you can look at it to inform the estimate. Tag Claude's estimates `assumption` until the builders confirm them.
5. **Plot and reposition.** Convert the 1–5 scores to 0–100 (`(score − 1) × 25`), with feasibility on x and importance on y. Show the plot and invite the user to challenge it with pairwise questions: "Is A really more valuable to the user than B?" If everything sits in the middle, force a spread. Relative position matters more than the numbers.
6. **Draw the focus areas.** Name the four zones by importance and feasibility:
   | Zone | Importance | Feasibility | What to do |
   | --- | --- | --- | --- |
   | **No-brainers** | High | Easy | Do them next |
   | **Big bets** | High | Mid to difficult | Big investments with potentially big payoffs, so discuss them |
   | **Utilities** | Low | Easy | Bundle them or do them when there's slack |
   | **Unwise** | Low | Difficult | Drop them, and say so |

   The deck draws these as rough bands, not strict quadrants, so discuss the dots near a border instead of letting the midline decide.
7. **Focus the conversation on Big bets.** For each one, ask why it's worth it, what makes it hard, what its riskiest assumption is, and what the smallest step to de-risk it would be. Note how much its importance rests on simulated ratings.
8. **Decide and play back.** Record what happens next, what you'll invest in, what you'll bundle, and what you won't do. Put the ideas whose zone depends only on simulated ratings at the top of "Validate next". Then publish the page.

## Facilitate a live session
Produce `design-thinking/prioritization-grid-<topic>-kit.html`. It needs:
- **Agenda table (30 min):**
  - 0:00–0:03 Intro: create first, evaluate second. Confirm the axis definitions
  - 0:03–0:08 Bring ideas: post the idea stickies, merge duplicates, read each one aloud once
  - 0:08–0:10 Set up: draw the axes, Importance to the user (low to high) and Feasibility (difficult to easy)
  - 0:10–0:20 Evaluate: each person quickly places a share of the stickies, then the group discusses and repositions
  - 0:20–0:23 Focus: sketch the four zones on the grid and label them
  - 0:23–0:30 Playback: spend most of the time on Big bets, then confirm the No-brainers and the drops
- **Prompts to read aloud:**
  - "Importance means value to the user, not to us. Which need does this serve?"
  - "Feasibility is for the people who'll build it to judge. Builders, does this placement look right?"
  - "Which of these would we regret not doing in a year?"
  - "What's the smallest thing we could do this sprint to find out if this Big bet pays off?"
- **Materials:** the idea stickies, a large sheet or a Mural canvas, markers in two colors (one for axes, one for zones) and a timer.
- **An empty board:** an empty `.plot` with Feasibility on x (difficult left, easy right), Importance on y, and the four zone labels, plus the numbered idea list in an empty `.key`. Optionally add a table of the simulated users' importance ratings as a reference for the room, labeled simulated.

After the session, read the photos or the board export and build the results page, recording each sticky's approximate position and zone and who placed it.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/prioritization-grid-<topic>.html`.
- **Title:** `<Scope> Prioritization Grid`, for example "Release Tools Prioritization Grid".
- **Sections:**
  1. **The grid:** `.plot-wrap` with a `.plot`. Zones: `z-tl` "Big bets", `z-tr` "No-brainers", `z-bl` "Unwise", `z-br` "Utilities". Labels: `.axis.x` "Feasibility →" and `.axis.y` "Importance to <user> →". Each idea is a numbered `.dot` whose `data-tag` is the basis of its importance rating (`evidence`, `simulated` or `assumption`). The `.key` lists each number with the idea, a pill for its importance basis (such as "rated by SU-1–SU-4 · 2–5") and a pill for its feasibility basis.
  2. **Ideas:** a table of number, idea, source, importance (median, spread and basis pill), feasibility (score, reason and basis pill), and zone.
  3. **Simulated ratings:** a table with one row per idea and one column per persona, so the spread shows. Then a `simulated` note for each telling reason, and a `details.transcript` per persona.
  4. **Big bets:** a table of bet, why it's worth it, what makes it hard, riskiest assumption, and smallest de-risking step.
  5. **Decisions:** `.cols` with Do next, Invest in, Bundle, and Not doing.
  6. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "scope": "", "user": "", "axes": { "x": "feasibility", "y": "importance" },
    "ideas": [{ "n": 1, "id": "I1", "text": "", "from": "design-thinking/big-idea-vignettes-x.html",
      "importance": { "ratings": { "SU-1": 4, "SU-2": 2, "SU-3": 5 }, "median": 4, "spread": [2, 5], "evidence": [], "tag": "simulated" },
      "feasibility": { "score": 2, "why": "", "tag": "assumption", "confirmed_by": "" },
      "x": 25, "y": 75, "zone": "big-bet" }],
    "big_bets": [{ "idea": "I1", "worth": "", "hard": "", "riskiest_assumption": "", "next_step": "" }],
    "decisions": { "do_next": [], "invest": ["I1"], "bundle": [], "not_doing": [] } }
  ```
  `zone` is one of `no-brainer`, `big-bet`, `utility`, `unwise`. `items` holds every dot and note.

## Quality checks
- **Ideas were generated before evaluation.** Don't prune while you collect.
- **Importance reflects user value and cites a need or Hill.** Stakeholder volume, team excitement and "the competitor has it" don't count unless they're tied to a user need.
- **Each persona rated alone,** in character, with the cards shuffled. The grid shows the spread and counts of simulated users, never percentages or averages.
- **The personas disagree somewhere.** If every persona rates every idea 4 or 5, the simulation is flattering the team, so rerun it with more friction. If two personas give the same ratings for the same reasons, they aren't distinct enough; fix the panel with `/edt-core:simulated-users`.
- **Simulated ratings stay simulated.** A dot placed on simulated ratings is tagged `simulated`, never `evidence`, however many personas agreed.
- **Feasibility is judged or confirmed by the people who'll build the idea.** Simulated users never rate it, and Claude's estimates stay tagged `assumption`.
- **The ideas are spread out.** If everything ends up "medium-medium", the team has avoided choosing.
- **Every Big bet has a riskiest assumption and a de-risking step.** A bet without a test is a gamble.
- **The Unwise list is written down and agreed.** Saying no out loud is half the value.
- **Each idea is one card about what the user gets,** not a bundle of features.

## Next
- `/edt-plan:experience-based-roadmap`: sequence the No-brainers and Big bets into stages.
- `/edt-plan:assumptions-and-questions`: dig into the riskiest assumptions and simulated ratings behind the Big bets.
- `/edt-plan:user-stories`: break the chosen ideas into user tasks with acceptance criteria.
- `/edt-test:paper-prototypes`: test a Big bet cheaply before investing.
- `/edt-align:playbacks`: share the decisions with stakeholders.

## Source
[IBM Enterprise Design Thinking Toolkit: Prioritization Grid](https://www.ibm.com/downloads/documents/us-en/137a1e253e5bac05)
