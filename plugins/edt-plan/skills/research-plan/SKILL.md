---
name: research-plan
description: Write a research plan that defines what the team needs to learn and how to find out. It covers a title, stakeholders, background, objective, research questions, methods, participants, schedule and budget, sized to one sprint. Use when someone asks "plan our user research", "how do we test these assumptions", "who should we talk to and when", or "write a study plan", or after Assumptions and Questions or at project kickoff.
argument-hint: "[study topic or assumption] [facilitate]"
---

# Research Plan

> IBM Enterprise Design Thinking · Plan your work · Reflect, to plan the next Observe · ~60 min

Research without a plan collects anecdotes. Research with a plan answers the questions the team's next decision depends on. A research plan defines what you need to learn, how you'll find the answers, from whom, and by when. It also makes the time and cost of the research easy to justify to stakeholders. It turns a list of risky unknowns into concrete Observe activities, and it schedules them so the findings arrive before the team's next decision, not after.

## When to use it
- At the start of a project. A plan is essential before the first round of research.
- Right after `/edt-plan:assumptions-and-questions`, to turn the test-first items into a study.
- Before any interview, contextual inquiry or prototype test that involves real participants.
- When stakeholders ask "why are we spending time on research?"

## Inputs
- Upstream artifacts in `design-thinking/`: `assumptions-and-questions-*` (the main source of research questions), `empathy-map-*` (who to recruit), `sponsor-users-*`, `stakeholder-map-*`, `hills-*` and any earlier `research-plan-*`.
- What to ask the user for if missing: the decision this research must inform and when it's due, the target users, access constraints (NDAs, client approval, recruiting channels), the budget for incentives and tools, and who the stakeholders are.

## Co-create with Claude
1. **Ground.** List `design-thinking/` and read the upstream artifacts. Pull the high-risk, uncertain items from the assumptions file, with their IDs. Confirm the decision and the date the research has to beat.
2. **Title the plan.** A stranger should understand its purpose from the title alone. Combine what you'll study, the methods and the user group, for example "How claims adjusters triage new claims: contextual inquiry and interviews with mid-size insurers". Long titles are fine.
3. **Record authorship and stakeholders.** List the author and their contact details. Add each stakeholder as they buy in, so everyone can be kept up to date.
4. **Write the background.** In no more than a couple of sentences, say which project this supports and why the study matters to it.
5. **Write the objective.** In one sentence, starting "The objective of this study is to…", say what you want to learn. Make it about learning. "Prove users love X" is a conclusion looking for data.
6. **Draft the research questions.** Write 3–7 specific questions the study will answer, each tied to the objective and, where possible, to an assumption or question ID.
   - These questions are for the team. You don't ask them to participants directly. Turning them into neutral participant prompts happens in `/edt-gather:interviews`.
   - Suggest that the user brainstorm the questions with the team, stakeholders and clients before finalizing them.
7. **Choose methods.** Map each research question to the Observe method that answers it most effectively and efficiently:
   - Behavior in context: `/edt-gather:contextual-inquiry`.
   - Motivations and history: `/edt-gather:interviews`.
   - Reactions to a concept: `/edt-test:paper-prototypes` or `/edt-test:cognitive-walkthrough`.
   - What already happens at scale: existing data such as analytics or support tickets.

   Build a matrix of questions against methods. Each chosen method will need its own detailed planning.
8. **Define the participants.** Participants must represent the real users.
   - Start from empathy maps or personas, and from sponsor users, to define who embodies those users best.
   - Write inclusion and exclusion criteria, and leave out people with no stake in the problem.
   - Set the number per segment. 5–8 is typical for qualitative work.
   - Note recruiting sources and how consent will be collected.
9. **Schedule and budget.** Draft dates for recruiting, running each method, synthesis and the playback. Try to fit the plan into one sprint or iteration, timed so the findings inform the team's next decisions. Add costs if they're relevant, such as incentives, tools and people's time.
10. **Play back.** Share the plan with stakeholders for buy-in. Write the Playback section and save the artifact.

## Facilitate a live session
**Agenda (60 min)**
| Time | Step | What happens |
| --- | --- | --- |
| 0:00 | Intro | Why plan, and the decision this research must inform |
| 0:05 | Set up | Agree on a draft title, the authors, the stakeholders and a two-sentence background |
| 0:15 | Define goals | Write a one-sentence objective, then brainstorm research questions in silence, cluster them and pick 3–7 |
| 0:30 | Methods | Map questions to Observe methods on a matrix |
| 0:40 | People | Write participant criteria from the empathy maps. Name sponsor users and recruiting sources |
| 0:50 | Schedule | Lay out recruiting, sessions, synthesis and the playback on a one-sprint timeline. Assign owners |

**Prompts to read aloud**
- "What decision will we make differently depending on what we learn?"
- "Is this a question for us to answer, or a question to ask a participant? Keep ours here."
- "Which method gets us a trustworthy answer fastest?"
- "Who would we be wrong to leave out, and who has no reason to be in the study?"

**Materials:** the assumptions board or file, the empathy maps, sticky notes, markers and a timer.

**Board layout:** a header band for the title, authors and background. A large "Research questions" area. A questions-by-methods matrix. A "Participants" panel with include and exclude columns. A one-sprint timeline along the bottom.

**After the session:** digitize everything into the Output template and circulate it to stakeholders.

## Output
Save to `design-thinking/research-plan-<topic>.md` using this template:

```markdown
# Research Plan: <descriptive title: what, methods, user group>

## Authors and stakeholders
| Name | Role | Contact | Bought in? |
| --- | --- | --- | --- |

## Background
<one or two sentences: project, and why this study matters>

## Objective
The objective of this study is to …
Decision it informs: <decision> · needed by <date>

## Research questions
| # | Research question (for the team, not participants) | From (assumption or question ID) |
| --- | --- | --- |
| RQ1 | … | A1 in assumptions-and-questions-x.md |

## Methods
| Method | Answers | Why this method | Detailed plan |
| --- | --- | --- | --- |
| Contextual inquiry | RQ1, RQ3 | … | `/edt-gather:contextual-inquiry` |

## Participants
- Represents: <persona or user group, with source>
- Include: … · Exclude: …
- Number per segment: … · Sponsor users: …
- Recruiting sources: … · Consent and data handling: …

## Schedule
| Step | Owner | Start | End |
| --- | --- | --- | --- |
| Recruit | | | |
| Run <method> | | | |
| Synthesize | | | |
| Play back findings | | | |

## Budget (optional)
| Item | Cost | Justification |
| --- | --- | --- |

## Playback
- Key takeaways: <3–5 bullets>
- Assumptions and questions to validate: <the RQs and the assumptions they test>
- Next activity: …
```

## Quality checks
- **The title passes the stranger test.** It names what's being studied, the methods and the user group.
- **The objective is one sentence about learning, not about confirming a solution.**
- **Research questions aren't interview questions.** They're neutral, they don't lead, and they don't presume an answer.
- **Every research question has at least one method, and every method answers at least one question.** Drop any method that answers nothing.
- **Participants are real, representative users.** Colleagues standing in for users are labelled as proxies, and their findings are labelled as weaker evidence.
- **The plan fits in one sprint or iteration, and its findings land before the decision date.**
- **No findings are pre-written.** Expected results are written as Assumptions, never as Evidence.

## Next
- `/edt-gather:interviews` and `/edt-gather:contextual-inquiry`: plan and run the sessions.
- `/edt-core:sponsor-users`: recruit participants who'll stay involved.
- `/edt-synthesize:empathy-map`: synthesize what you learn.
- `/edt-align:playbacks`: play the findings back to stakeholders.

## Source
[IBM Enterprise Design Thinking Toolkit: Research Plan](https://www.ibm.com/downloads/documents/us-en/137a1e253e5bac03)
