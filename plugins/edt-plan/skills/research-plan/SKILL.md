---
name: research-plan
description: Writes a one-sprint research plan as an HTML artifact with two tracks (simulated pilot rounds Claude runs first to sharpen the questions, then real research to validate the simulated claims that matter most). Covers title, stakeholders, objective, research questions, methods, participants, schedule and budget. Use when someone asks "plan our user research", "how do we test these assumptions", "who should we talk to and when" or "write a study plan", or after Assumptions and Questions.
argument-hint: "[study topic or assumption] [facilitate]"
---

# Research Plan

> IBM Enterprise Design Thinking · Plan your work · Reflect, to plan the next Observe · ~60 min

Research without a plan collects anecdotes. Research with a plan answers the questions the team's next decision depends on. A research plan defines what you need to learn, how you'll find the answers, from whom, and by when, and it makes the time and cost easy to justify to stakeholders. It turns a list of risky unknowns into concrete Observe activities, scheduled so the findings arrive before the team's next decision, not after. With simulated users the plan runs on two tracks. Simulated pilot rounds come first and cost hours: they rehearse the guide and expose weak questions. Real research follows, and it is the only track that can answer a research question.

## When to use it
- At the start of a project. A plan is essential before the first round of research.
- Right after `/edt-plan:assumptions-and-questions`, to turn the test-first items into a study.
- When earlier activities leaned on simulated users and the team needs a plan to check those claims with real people.
- Before any interview, contextual inquiry or prototype test that involves real participants.
- When stakeholders ask "why are we spending time on research?"

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of `assumptions-and-questions-*` (the main source of research questions), `empathy-map-*` (who to recruit), `sponsor-users-*`, `stakeholder-map-*`, `hills-*` and any earlier `research-plan-*`. Also read every page's `playback.validate` list: those are the simulated and assumed claims the team leans on most.
- **The simulated user panel,** `design-thinking/simulated-users.html`. Create it if it's missing (see `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`).
- **Ask the user only for:** the decision this research must inform and when it's due, access constraints (NDAs, client approval, recruiting channels), the budget for incentives and tools, and who the stakeholders are. None of these can be simulated.

## Co-create with Claude
1. **Ground.** List `design-thinking/` and read the upstream data. Pull the test-first items from the assumptions page with their IDs, and the simulated claims from every page's "Validate next". Confirm the decision and the date the research has to beat.
2. **Title the plan.** A stranger should understand its purpose from the title alone. Combine what you'll study, the methods and the user group, for example "How claims adjusters triage new claims: contextual inquiry and interviews with mid-size insurers". Long titles are fine here; the page's short `<title>` is separate.
3. **Record authorship and stakeholders.** List the author and their contact details. Add each stakeholder as they buy in, so everyone can be kept up to date.
4. **Write the background.** In no more than a couple of sentences, say which project this supports and why the study matters to it.
5. **Write the objective.** In one sentence, starting "The objective of this study is to…", say what you want to learn. Make it about learning. "Prove users love X" is a conclusion looking for data.
6. **Draft the research questions.** Write 3–7 specific questions the study will answer, each tied to the objective and, where possible, to an item ID, keeping that item's tag (`simulated`, `assumption` or `question`).
   - These questions are for the team. You don't ask them to participants directly. Turning them into neutral participant prompts happens in `/edt-gather:interviews`.
   - Suggest that the user brainstorm the questions with the team, stakeholders and clients before finalizing them.
7. **Choose methods.** Map each research question to the Observe method that answers it most effectively and efficiently, and build a matrix of questions against methods. Each chosen method will need its own detailed planning.
   - Behavior in context: `/edt-gather:contextual-inquiry`.
   - Motivations and history: `/edt-gather:interviews`.
   - Reactions to a concept: `/edt-test:paper-prototypes` or `/edt-test:cognitive-walkthrough`.
   - What already happens at scale: existing data such as analytics or support tickets.
8. **Plan Track A: simulated pilot rounds.** Say what Claude will simulate first, before any real session, to sharpen the questions. For each round, record the method, the research questions it rehearses, the personas (2–3, including the skeptic and the edge case, one session each) and what you want out of it:
   - prompts that confuse, lead or land flat
   - branches and follow-ups the guide is missing
   - research questions to split, reword or drop
   - sharper hypotheses and "we're wrong if" signals for the real track

   Pilot output is `simulated`. It sharpens the guide and the hypotheses; it never answers a research question. Offer to run Track A right away through the method's skill, such as `/edt-gather:interviews`, and then update the plan with what changed.
9. **Plan Track B: real research.** Plan sessions with real participants to validate the simulated claims that matter most, and the riskiest assumptions. Order the work by what the next decision depends on. Give every simulated claim the plan relies on at least one real check with a "we're wrong if" signal.
10. **Define the participants.** Real participants must represent the real users.
    - Start from empathy maps, the simulated panel and sponsor users to define who embodies those users best. The personas are hypotheses about segments, so recruit real people who fit them, especially the skeptic and the edge case.
    - Write inclusion and exclusion criteria, and leave out people with no stake in the problem.
    - Set the number per segment. 5–8 is typical for qualitative work.
    - Note recruiting sources and how consent will be collected.
    - If Track A needs a persona the panel lacks, add one with `/edt-core:simulated-users`.
11. **Schedule and budget.** Put Track A in the first day or two, so the real sessions use the sharpened guide. Draft dates for recruiting, each real method, synthesis and the playback. Fit the plan into one sprint or iteration, timed so the findings land before the decision. Add costs if they're relevant, such as incentives, tools and people's time.
12. **Play back.** Share the plan with stakeholders for buy-in. Put the simulated claims Track B will check at the top of "Validate next". Then publish the page.

## Facilitate a live session
Produce `design-thinking/research-plan-<topic>-kit.html`. It needs:
- **Agenda table (60 min):**
  - 0:00–0:05 Intro: why plan, and the decision this research must inform
  - 0:05–0:15 Set up: agree on a draft title, the authors, the stakeholders and a two-sentence background
  - 0:15–0:30 Define goals: write a one-sentence objective, then brainstorm research questions in silence, cluster them and pick 3–7
  - 0:30–0:40 Methods: map questions to Observe methods on a matrix, and mark which to pilot with simulated users first
  - 0:40–0:50 People: write participant criteria from the empathy maps and the panel. Name sponsor users and recruiting sources
  - 0:50–1:00 Schedule: lay out the pilots, recruiting, real sessions, synthesis and the playback on a one-sprint timeline. Assign owners
- **Prompts to read aloud:**
  - "What decision will we make differently depending on what we learn?"
  - "Is this a question for us to answer, or a question to ask a participant? Keep ours here."
  - "Which method gets us a trustworthy answer fastest?"
  - "Which of our beliefs came from simulated users? Who's the real person who can confirm it?"
  - "Who would we be wrong to leave out, and who has no reason to be in the study?"
- **Materials:** the assumptions page, the empathy maps, the simulated panel, sticky notes, markers and a timer.
- **An empty board:** a header band for the title, authors and background; an empty research questions table; an empty questions-by-methods matrix; two empty `.cols` for Track A and Track B; an include and exclude participants table; and a one-sprint schedule table.

After the session, read the photos or the board export, build the results page, and offer to run Track A.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/research-plan-<topic>.html`.
- **Title:** `<Topic> Research Plan`, for example "Claims Triage Research Plan". The descriptive study title goes in the first section.
- **Sections:**
  1. **The study:** the descriptive title, background, objective, and the decision with its date, followed by a table of authors and stakeholders (name, role, contact, and a bought-in pill with `data-tone`).
  2. **Research questions:** a table of ID, question, where it came from (item ID with its tag pill), and which tracks cover it.
  3. **Two tracks:** `.cols` with "Track A: simulated pilots" and "Track B: real research". Each round or method is a `.cluster` titled with the method, who and when. Its notes are the items it targets, keeping their tags: `question` notes for what a pilot should sharpen, and `simulated` or `assumption` notes for the claims a real session validates.
  4. **Methods:** a questions-by-methods table, with a track column.
  5. **Participants:** a table of segment, include, exclude, number, recruiting source and consent for Track B, and the personas used in Track A as `simulated` pills.
  6. **Schedule and budget:** a table of step, track, owner, start and end, and an optional budget table.
  7. **Pilot results:** what changed in the guide, as tagged notes, and a `details.transcript` per pilot session. Include this only when you ran Track A.
  8. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "title": "", "background": "", "objective": "", "decision": "", "decision_date": "",
    "people": [{ "name": "", "role": "", "contact": "", "bought_in": false }],
    "questions": [{ "id": "RQ1", "text": "", "from": [{ "id": "SC2", "page": "design-thinking/assumptions-and-questions-x.html", "tag": "simulated" }] }],
    "tracks": {
      "simulated": [{ "id": "P1", "method": "interviews", "rehearses": ["RQ1"], "personas": ["SU-2", "SU-4"], "aims": [""], "when": "", "status": "planned|run" }],
      "real": [{ "id": "R1", "method": "contextual-inquiry", "answers": ["RQ1"], "validates": ["SC2"], "wrong_if": "",
        "participants": { "segment": "", "include": "", "exclude": "", "n": 6, "sources": "", "consent": "" },
        "owner": "", "start": "", "end": "" }] },
    "budget": [{ "item": "", "cost": "", "why": "" }] }
  ```
  `items` holds every tagged note on the page.

## Quality checks
- **The title passes the stranger test.** It names what's being studied, the methods and the user group.
- **The objective is one sentence about learning, not about confirming a solution.**
- **Research questions aren't interview questions.** They're neutral, they don't lead, and they don't presume an answer.
- **Every research question has at least one method, and every method answers at least one question.** Drop any method that answers nothing.
- **Track A sharpens; it never answers.** No research question is marked answered from a pilot, and pilot notes stay tagged `simulated`.
- **The pilots have friction.** They include a skeptic and an edge case, and the personas sound like different people. If the guide sails through with no confusion at all, the pilot was too polite, so rerun it.
- **The simulated claims the team leans on most each have a real check in Track B.** Counts from pilots read "2 of 3 simulated users", never as percentages.
- **Participants are real, representative users.** Simulated personas are never participants. Colleagues standing in for users are labeled as proxies, and their findings as weaker evidence.
- **The plan fits in one sprint or iteration, and its findings land before the decision date.**
- **No findings are pre-written.** Expected results are tagged `assumption`, never `evidence`.

## Next
- `/edt-gather:interviews` and `/edt-gather:contextual-inquiry`: run the pilot rounds, then plan and run the real sessions.
- `/edt-core:sponsor-users`: recruit real participants who'll stay involved.
- `/edt-core:simulated-users`: add the personas Track A needs.
- `/edt-synthesize:empathy-map`: synthesize what you learn.
- `/edt-align:playbacks`: play the findings back to stakeholders.

## Source
[IBM Enterprise Design Thinking Toolkit: Research Plan](https://www.ibm.com/downloads/documents/us-en/137a1e253e5bac03)
