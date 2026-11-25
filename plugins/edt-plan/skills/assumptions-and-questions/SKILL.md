---
name: assumptions-and-questions
description: Surface a team's assumptions and open questions, plot them by risk and certainty, and build an action plan to validate or invalidate the riskiest ones. Use when someone asks "what are we assuming", "what could prove us wrong", "how do we de-risk this", "what do we still need to learn", or before committing to Hills, a roadmap or a build. Also use to collect all the Assumption and Question tags across the design-thinking workspace.
argument-hint: "[project, Hill or idea] [facilitate]"
---

# Assumptions and Questions

> IBM Enterprise Design Thinking · Plan your work · Reflect · ~30 min

Every plan rests on guesses, and that's fine. Guessing is how the scientific method works: you form a hypothesis, then test whether it's right. The danger is guesses that nobody has said out loud. In this activity the team reflects on what it knows and what it still needs to understand. It then finds the assumptions that are both risky and uncertain and works out cheap, fast ways to test them. Guess early, test early, learn early. Failing fast and cheaply beats being wrong late and expensively.

## When to use it
- Early and often. The sooner assumptions surface, the sooner the team can reduce the risk they carry.
- Right after writing Hills, a roadmap or big ideas. Each of these is full of beliefs.
- When a debate keeps going in circles because people hold different unstated beliefs.
- Before a research plan, to decide what the research has to answer.

## Inputs
- Upstream artifacts in `design-thinking/`: anything. Every artifact in this toolkit tags items as Assumption or Question, so search the whole folder for those tags. The most likely sources are `hills-*`, `needs-statements-*`, `empathy-map-*`, `to-be-scenario-map-*`, `big-idea-vignettes-*`, `experience-based-roadmap-*` and `prioritization-grid-*`.
- What to ask the user for if missing: the scope (which project, Hill or idea to de-risk), any decision deadline, and the team's beliefs about users, value, feasibility and the business.

## Co-create with Claude
1. **Scope.** Agree on what you're de-risking, for example "Hill 2" or "the self-serve onboarding idea", and the decision it feeds.
2. **Collect without judging.** List `design-thinking/`, search for items tagged **Assumption** and **Question** with something like `grep -rn "Assumption\|Question" design-thinking/`, and pull each one in with its source file. Then ask the user to brain-dump more.
   - Prompt across these lenses: users and their problem, value (will they care?), solution (will it work for them?), feasibility (can we build it?), business (will it pay and fit the strategy?), adoption (will they switch?).
   - Add your own candidates and label them as Claude-proposed.
   - Keep one idea per item. Write assumptions as a testable belief, "We believe …", and questions as open questions.
   - Don't evaluate yet.
3. **Set up the grid.** The vertical axis runs from Low risk (bottom) to High risk (top). The horizontal axis runs from Certain (left) to Uncertain (right).
   - **Risk:** if this turns out to be wrong, how badly does it damage the plan or the users?
   - **Certainty:** how much evidence do we already have? Items backed by Evidence belong on the left.
4. **Plot quickly, then refine.** Give each item a rough placement with a one-line reason for each axis. Ask the user to challenge the placements, and reposition items relative to each other. Ask questions like "Is this riskier than that one?"
5. **Build an action plan for the upper right.** Pull the high-risk, uncertain items into their own list. For each one, come up with at least two ways to validate or invalidate it:
   - **Ask:** is there someone, such as a sponsor user or an expert, who can answer this directly?
   - **Observe:** can you see it happen, through contextual inquiry, analytics or support tickets?
   - **Make:** can you build a quick prototype to test the hypothesis?

   Then choose the cheapest test that would be convincing. Define the signal in advance ("we're wrong if …"), and record an owner and a date.
6. **Note the other quadrants.**
   - High risk and certain: plan around these, but there's no need to research them.
   - Low risk and uncertain: learn about these as you go.
   - Low risk and certain: proceed.
7. **Play back.** Write the Playback section. Recommend that one person presents the assumptions and someone else presents the plan to resolve them.

## Facilitate a live session
**Agenda (30 min)**
| Time | Step | What happens |
| --- | --- | --- |
| 0:00 | Intro | Why: guess early, test early. Set the scope |
| 0:03 | Collect | Silent writing, one assumption or question per sticky. No discussion yet |
| 0:10 | Set up | Draw the 2×2: High risk at the top, Low risk at the bottom, Certain on the left, Uncertain on the right |
| 0:12 | Identify | Everyone places their own stickies quickly, then the group discusses and repositions |
| 0:20 | Build | Move the upper-right stickies to an action board and come up with tests for each |
| 0:27 | Playback | One person plays back the assumptions, another plays back the plan |

**Prompts to read aloud**
- "What has to be true for this to work? Write it down, even if it feels obvious."
- "If this one turned out to be wrong, would we change the plan? Then it's high risk."
- "What evidence do we have? Have we seen it ourselves, or do we just believe it?"
- "Who could we ask, what could we watch, or what could we make to find out this week?"

**Materials:** sticky notes, markers, a timer, and tape or a Mural frame for the grid.

**Board layout:** on the left, a collection area. In the center, the 2×2 grid with its axis labels. On the right, an action board with the columns Item | Ask / Observe / Make | "We're wrong if…" | Owner | By when.

**After the session:** digitize the grid and the action board into the Output template, keeping track of who raised each item.

## Output
Save to `design-thinking/assumptions-and-questions-<topic>.md` using this template:

```markdown
# Assumptions and Questions: <scope>
Decision this informs: <decision> · by <date>

## Inventory
| # | Item | Type | Source | Risk | Certainty | Why placed here |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | We believe … | Assumption | hills-x.md / team / Claude-proposed | High | Uncertain | … |
| Q1 | How many …? | Question | … | High | Uncertain | … |

## Grid
- **High risk · Uncertain (test first):** A1, Q1, …
- **High risk · Certain (plan around):** …
- **Low risk · Uncertain (learn as you go):** …
- **Low risk · Certain (proceed):** …

## Action plan
| # | Item | Test (ask / observe / make) | We're wrong if… | Owner | By when |
| --- | --- | --- | --- | --- | --- |

## Playback
- Key takeaways: <3–5 bullets>
- Assumptions and questions to validate: <the test-first list>
- Next activity: …
```

## Quality checks
- **Each item holds one idea and can be tested.** "Users want it to be better" fails. "We believe adjusters re-key claim data at least daily" passes.
- **Risk and certainty are scored separately.** A frightening item can still be certain, and a trivial one can be uncertain.
- **Nothing is called certain without Evidence and a source.** Team agreement doesn't count as evidence.
- **Every test-first item has a test, an owner, a date, and a "we're wrong if" signal set in advance.** Without a signal set in advance, any result can be read as confirmation.
- **Tests are cheap and fast,** measured in hours or days, not a quarter. Questions about users go to real users, not to internal proxies.
- **At least one test could kill the idea.** If every test can only confirm, the plan is validation theater.
- **Re-run the activity each iteration.** Resolved items become Evidence in the source artifacts, so update those files.

## Next
- `/edt-plan:research-plan`: turn the test-first items into research questions with methods, participants and a schedule.
- `/edt-gather:interviews` or `/edt-gather:contextual-inquiry`: answer the "ask" and "observe" tests.
- `/edt-test:paper-prototypes`: answer the "make" tests cheaply.
- `/edt-plan:prioritization-grid`: rank ideas once the biggest unknowns are resolved.

## Source
[IBM Enterprise Design Thinking Toolkit: Assumptions and Questions](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac2f)
