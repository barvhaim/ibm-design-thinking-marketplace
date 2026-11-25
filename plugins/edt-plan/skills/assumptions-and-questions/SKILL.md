---
name: assumptions-and-questions
description: Harvests every assumption, open question and simulated claim across design-thinking/, plots them by risk and certainty, and builds a test plan for the riskiest, as an HTML artifact. Simulated claims can get a cheap first pass with simulated users before the real test. Use when someone asks "what are we assuming", "what could prove us wrong", "how do we de-risk this" or "what do we still need to learn", or before committing to Hills, a roadmap or a build.
argument-hint: "[project, Hill or idea] [facilitate]"
---

# Assumptions and Questions

> IBM Enterprise Design Thinking · Plan your work · Reflect · ~30 min

Every plan rests on guesses, and that's fine. Guessing is how the scientific method works: you form a hypothesis, then test whether it's right. The danger is guesses nobody has said out loud. In this activity the team reflects on what it knows and what it still needs to understand, finds the assumptions that are both risky and uncertain, and works out cheap, fast ways to test them. Guess early, test early, learn early. Failing fast and cheaply beats being wrong late and expensively. When much of the team's knowledge came from simulated users, those claims are guesses too, just better-dressed ones, so they get tested first.

## When to use it
- Early and often. The sooner assumptions surface, the sooner the team can reduce the risk they carry.
- Right after writing Hills, a roadmap or big ideas. Each of these is full of beliefs.
- When earlier activities leaned on simulated users and the team needs to know which of those claims to check with real people.
- When a debate keeps going in circles because people hold different unstated beliefs.
- Before a research plan, to decide what the research has to answer.

## Inputs
- **From `design-thinking/`: every page.** Read each page's `#edt-data` and collect its `items` tagged `assumption`, `question` or `simulated`, plus its `playback.validate` list. The richest sources are usually `hills-*`, `needs-statements-*`, `empathy-map-*`, `to-be-scenario-map-*`, `big-idea-vignettes-*`, `experience-based-roadmap-*` and `prioritization-grid-*`. Older `*.md` artifacts: search their text for Assumption and Question tags.
- **The simulated user panel,** `design-thinking/simulated-users.html`. Create it if it's missing (see `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`).
- **Ask the user only for:** the scope (which project, Hill or idea to de-risk), the decision it feeds and its deadline, and the team's beliefs that aren't written down anywhere.

## Co-create with Claude
1. **Scope.** Agree on what you're de-risking, for example "Hill 2" or "the self-serve onboarding idea", and the decision it feeds.
2. **Harvest without judging.** Pull every tagged item into one inventory, with the page and item ID it came from:
   ```bash
   python3 - <<'EOF'
   import re, json, glob
   for f in sorted(glob.glob("design-thinking/*.html")):
       m = re.search(r'id="edt-data">(.*?)</script>', open(f).read(), re.S)
       if not m: continue
       d = json.loads(m.group(1))
       for i in d.get("items", []):
           if i.get("tag") in ("assumption", "question", "simulated"):
               print(f, i.get("id"), i["tag"], i.get("source", ""), i["text"], sep=" | ")
       for v in d.get("playback", {}).get("validate", []):
           print(f, "validate", v.get("tag"), "", v.get("text"), sep=" | ")
   EOF
   ```
   Sort what you find into three classes, and keep each item's tag:
   - **Assumptions** (`assumption`), written as a testable belief: "We believe adjusters re-key claim data at least daily."
   - **Questions** (`question`), written as open questions.
   - **Simulated claims** (`simulated`): things a persona said or did that a later page leans on, such as a need, a Hill's Wow or a roadmap stage. Rewrite each as a belief about *real* users ("We believe real release engineers, like SU-2, check the design channel before every sprint"). Keep the persona ID as its source. If several personas said the same thing, it's one claim with several sources. Repetition across a simulated panel isn't extra certainty.

   Then ask the user to brain-dump more across these lenses: users and their problem, value (will they care?), solution (will it work for them?), feasibility (can we build it?), business (will it pay and fit the strategy?) and adoption (will they switch?). Add your own candidates as `assumption` with the source "Claude-proposed". Keep one idea per item, and don't evaluate yet.
3. **Set up the grid.** The vertical axis runs from Low risk (bottom) to High risk (top). The horizontal axis runs from Certain (left) to Uncertain (right).
   - **Risk:** if this turns out to be wrong, how badly does it damage the plan or the users?
   - **Certainty:** how much real evidence do we already have? Only items backed by `evidence` belong left of center. Simulated claims always sit right of center, however many personas agreed.
4. **Plot quickly, then refine.** Place each item with a one-line reason for each axis. Treat simulated claims as a high-priority class: one that a Hill, a roadmap stage or a build decision depends on starts high on risk. Ask the user to challenge placements, and reposition items relative to each other: "Is this riskier than that one?"
5. **Optional: a cheap first pass with simulated users.** For test-first items about user behavior or reaction, you can probe them in minutes before spending on real research. Don't use this for market size, feasibility or how a specific organization works; simulation is weak there.
   - Pick 2–3 personas who did *not* produce the claim, and include the skeptic and the edge case. Run each one separately, in character.
   - Ask open questions about past behavior ("Tell me about the last time you…"), never "Would you…?" or a question that hands them the answer.
   - Record each session as a transcript, and give the item a result: held up, mixed, or fell apart in simulation.

   A claim that falls apart is worth rethinking cheaply now. A claim that holds up stays `simulated` and stays in the test-first list. Neither result moves an item toward Certain, and neither replaces the real test in step 6.
6. **Build an action plan for the upper right.** For each high-risk, uncertain item, come up with at least two ways to validate or invalidate it with real people or real data:
   - **Ask:** is there someone, such as a sponsor user or an expert, who can answer this directly?
   - **Observe:** can you see it happen, through contextual inquiry, analytics or support tickets?
   - **Make:** can you build a quick prototype to test the hypothesis?

   Choose the cheapest test that would be convincing. Define the signal in advance ("we're wrong if …"), and record an owner and a date. Use the first-pass result to sharpen the test, for example by asking about the part that wobbled.
7. **Note the other quadrants.** High risk and certain: plan around these, with no need to research them. Low risk and uncertain: learn as you go. Low risk and certain: proceed.
8. **Play back.** Recommend that one person presents the assumptions and someone else presents the plan. Put the simulated claims the plan depends on most at the top of "Validate next". Then publish the page.

## Facilitate a live session
Produce `design-thinking/assumptions-and-questions-<topic>-kit.html`. It needs:
- **Agenda table (30 min):**
  - 0:00–0:03 Intro: guess early, test early. Set the scope
  - 0:03–0:10 Collect: silent writing, one assumption or question per sticky, no discussion yet
  - 0:10–0:12 Set up: draw the 2×2 with High risk at the top, Low risk at the bottom, Certain on the left and Uncertain on the right
  - 0:12–0:20 Identify: everyone places their own stickies quickly, then the group discusses and repositions
  - 0:20–0:27 Build: move the upper-right stickies to an action board and come up with tests for each
  - 0:27–0:30 Playback: one person plays back the assumptions, another plays back the plan
- **Prompts to read aloud:**
  - "What has to be true for this to work? Write it down, even if it feels obvious."
  - "If this one turned out to be wrong, would we change the plan? Then it's high risk."
  - "What evidence do we have? Have we seen it ourselves, heard it from a simulated user, or do we just believe it?"
  - "Who could we ask, what could we watch, or what could we make to find out this week?"
- **Materials:** sticky notes in three colors (assumptions, questions, simulated claims), markers, a timer, and tape or a Mural frame for the grid.
- **An empty board:** a collection area, an empty `.plot` with the axis labels and the four zones, and an empty action table (item, ask / observe / make, we're wrong if…, owner, by when). Seed the collection area with the harvested items, keeping their tags, so the room starts from what the workspace already holds.

After the session, read the photos or the board export and build the results page, keeping who raised each item and each item's tag.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/assumptions-and-questions-<topic>.html`.
- **Title:** `<Scope> Assumptions and Questions`, for example "Onboarding Assumptions and Questions".
- **Sections:**
  1. **Grid:** `.plot-wrap` with a `.plot`. Zones: `z-tl` "Plan around", `z-tr` "Test first", `z-bl` "Proceed", `z-br` "Learn as you go". Labels: `.axis.x` "Uncertain →" and `.axis.y` "Risk →". Each item is a numbered `.dot` with its own `data-tag`, at `--x` = uncertainty and `--y` = risk (0–100). The `.key` lists each number with the item and a source pill.
  2. **Inventory:** a table of number, item, class (tag pill), where it came from (page and item ID), risk, certainty, and why it sits there.
  3. **Simulated first pass:** a table of item, personas probed, and the result as a pill with `data-tone` (good: held up, warn: mixed, bad: fell apart) next to a `simulated` pill. Then a `details.transcript` per session. Include this only when you ran any.
  4. **Action plan:** a table of item, test (ask, observe or make), we're wrong if…, real participants or data, owner and by when.
  5. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "scope": "", "decision": "", "decision_date": "",
    "axes": { "x": "uncertainty (certain → uncertain)", "y": "risk (low → high)" },
    "inventory": [{ "n": 1, "id": "SC1", "text": "We believe …", "class": "simulated", "source": "SU-2",
      "from": "design-thinking/empathy-map-x.html#N4", "risk": 80, "uncertainty": 85, "zone": "test-first", "why": "" }],
    "first_pass": [{ "item": "SC1", "personas": ["SU-3", "SU-4"], "result": "held-up|mixed|fell-apart", "notes": ["N12"] }],
    "actions": [{ "item": "SC1", "method": "ask|observe|make", "test": "", "wrong_if": "", "participants": "", "owner": "", "by": "" }] }
  ```
  Use IDs `A…` for assumptions, `Q…` for questions and `SC…` for simulated claims. `zone` is one of `test-first`, `plan-around`, `learn`, `proceed`. `items` holds every inventory item and every first-pass note.

## Quality checks
- **Each item holds one idea and can be tested.** "Users want it to be better" fails. "We believe adjusters re-key claim data at least daily" passes.
- **Risk and certainty are scored separately.** A frightening item can still be certain, and a trivial one can be uncertain.
- **Nothing is called certain without real evidence and a source.** Team agreement doesn't count, and neither do simulated users.
- **Simulated claims are their own class,** harvested from every page, never folded into assumptions or quietly dropped. None sits left of center.
- **A simulated first pass never changes a tag or moves an item toward Certain.** It only reshapes the real test. It uses personas who didn't produce the claim, including a skeptic. If every probed persona confirms the claim, the probe was too polite, so rerun it.
- **Counts from simulated users are counts.** Write "2 of 3 simulated users", never a percentage.
- **Every test-first item has a real test, an owner, a date, and a "we're wrong if" signal set in advance.** Without the signal, any result can be read as confirmation.
- **Tests are cheap and fast,** measured in hours or days, not a quarter. Questions about users go to real users, not to internal proxies or the simulated panel.
- **At least one test could kill the idea.** If every test can only confirm, the plan is validation theater.
- **Re-run the activity each iteration.** When a real test resolves an item, add a new `evidence` note with the real source to the page it came from and republish that page. Leave the original note in place with a Validated, Mixed or Invalidated pill.

## Next
- `/edt-plan:research-plan`: turn the test-first items into a study, with simulated pilot rounds and real research.
- `/edt-gather:interviews` or `/edt-gather:contextual-inquiry`: answer the "ask" and "observe" tests.
- `/edt-test:paper-prototypes`: answer the "make" tests cheaply.
- `/edt-core:sponsor-users`: recruit the real people the tests need.
- `/edt-plan:prioritization-grid`: rank ideas once the biggest unknowns are resolved.

## Source
[IBM Enterprise Design Thinking Toolkit: Assumptions and Questions](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac2f)
