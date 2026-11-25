---
name: cognitive-walkthrough
description: Plan, run and debrief a Cognitive Walkthrough, where real users try to reach a goal on your prototype while you watch silently, to judge whether it works. Produces the goal, tasks, scenario, think-aloud script, note sheets and results. Can also run an expert pre-walkthrough of a UI in the repo or a running app. Use when someone says "test this prototype with users", "usability test", "will users get this flow" or "walk through the app before we show users".
argument-hint: "[prototype, URL or path] [facilitate | expert]"
---

# Cognitive Walkthrough

> IBM Enterprise Design Thinking · Test your ideas · Observe and Reflect · ~60 min

A prototype only proves something when a real user tries it without help. In a Cognitive Walkthrough, a user works through a realistic scenario on your prototype while the team watches in silence and takes notes. The team sees, in real time, where the user succeeds, hesitates or gets lost, and how they feel about each part. Use it early and often. Everything is a prototype, and each round tells you what to change next.

## When to use it
- As soon as a paper prototype, wireframe or build can support one goal from start to finish, and again after every significant change.
- When the team disagrees about whether a flow is "intuitive". Watch someone use it instead of debating.
- Before a Playback, so you can show evidence of how the flow performs instead of opinions about it.
- **Expert pre-walkthrough** (`expert` argument): when you want Claude to find obvious blockers in a UI in the repo or a running app before you spend users' time.

## Inputs
- From `design-thinking/`: the prototype (`paper-prototypes-*`, `wireframes-*` or a link to a build), plus `hills-*`, `to-be-scenario-map-*`, `assumptions-and-questions-*` and `sponsor-users-*`.
- Ask the user for:
  - the prototype itself: a path, a URL, screenshots or photos
  - the Hill or assumptions this round should test
  - who the participants are. Real target users, ideally sponsor users, not teammates standing in for them. If there are none, use `/edt-core:sponsor-users`.

## Co-create with Claude
1. **Identify the goal.** Pick one high-level outcome the user should reach with the prototype, framed in their terms and tied to a Hill. Example: "Get reimbursed for a client trip."
2. **Identify the tasks.** List the tasks a user would have to complete to reach the goal, such as find the trip, attach the receipts and submit for approval. For each task, write down what success looks like. These tasks are for the team's eyes. Participants never see this list.
3. **Identify the scenario.** Write a short, realistic situation that gives the user the goal without naming any UI elements. For example: "You just got back from a client visit in Austin and want your $412 back before the month closes." Use the user's words, not the screen labels. Wording like "click Submit expense" gives the answer away.
4. **Prepare the prototype.** Walk the task list against the prototype and confirm that every screen, state and piece of content the user needs exists. That includes error and empty states the scenario might trigger. Fill the gaps or cut the task.
5. **Write the session script:**
   - **Welcome (read aloud):** "We're testing the design, not you. You can't do anything wrong. It's an early version, so parts may not work. I'll stay quiet, because seeing how it works without us is what helps most."
   - **Consent:** ask permission to take notes or record.
   - **Warm-up:** 2–3 questions about how they do this work today.
   - **Think-aloud:** "As you go, please say what you're looking at, what you're trying to do, and what you expect to happen."
   - **Scenario:** read it aloud, then hand it over on a card.
   - **Neutral prompts:** "What are you thinking?", "What do you expect that will do?", "What would you do if I weren't here?", "Tell me more about that."
   - **Never ask** "Was that easy?" or "Did you see the button?", and never point at anything.
   - **Questions back:** answer their questions with a question: "What do you think it does?"
   - **When stuck:** wait. If they would give up, mark the task as failed and move on. Only afterward, ask what would have helped.
   - **Wrap-up:** "What worked for you? What would you change? What was confusing?"
6. **Plan roles and numbers.** A facilitator runs the script and a note-taker captures everything. Other observers stay silent. Three to five users per round usually surface the main problems. Fix them, then run another round.
7. **Test.** Never demonstrate the prototype. The note-taker writes down what the user **did**, what they **said** (verbatim), where they **hesitated or erred**, and how they **seemed to feel**, with timestamps. Keep observation (Evidence) separate from interpretation (Assumption).
8. **Review and reflect.** After the sessions, read the notes together and answer:
   - What went well?
   - Did they reach the intended outcome?
   - Where did they struggle?
   - Did they understand how the prototype is structured?
   - What has to change?
   Record each task's outcome as Success, Assisted or Failed.
9. **Organize the observations** into a Feedback Grid with `/edt-test:feedback-grid`. Mark each assumption Validated, Invalidated or Inconclusive, and list the changes for the next iteration.

### Expert pre-walkthrough (Claude Code)
Claude can step through a UI before any user sees it: from source in the repo (routes, components, templates, copy), from a running app (with browser tools such as Chrome DevTools MCP, if they are available), or from screenshots and `wireframes-*.html`. For each task, Claude writes down the correct action sequence, then asks these questions at every step:
1. Will the user be trying to do this step at this point?
2. Will they notice that the right control is there?
3. Will they recognize it as the way to their goal? Does the label match their words?
4. After acting, will they see that they are making progress?

Name every "no" as a predicted issue, tag it **Assumption**, and cite where it happens (`file:line`, URL or screen). Put all findings under the heading **"Expert review (not user evidence)"**. These findings never validate an assumption. Use them to fix obvious blockers and to sharpen what to watch for with users. Use test accounts and test data, stop before any irreversible action (payments, emails, deletes), and don't edit code unless the user asks.

## Facilitate a live session
**Agenda (60 min, one or two participants):**
- 0:00–0:05 · **Intro.** Explain the Hill and the assumptions under test.
- 0:05–0:15 · **Identify.** Agree the goal, tasks, success criteria and the scenario card.
- 0:15–0:20 · **Prepare.** Do a dry run on the prototype, assign roles, and remind observers to stay silent.
- 0:20–0:45 · **Test.** The user works through the scenario while thinking aloud. The team notes, one observation per sticky note.
- 0:45–0:60 · **Review and reflect.** Answer the debrief questions, sort the notes on a Feedback Grid, and agree the changes.

**Materials:** the prototype, printed scenario cards (one task per card if you reveal them in sequence), the script, sticky notes in two colors (did and said), timers, and recording consent.

**Board layout:** a matrix with one column per task and one row per participant. In each cell, put the outcome (Success, Assisted or Failed) and the sticky notes. Put a Feedback Grid beside it. On Mural, use the same structure, with frames for each participant.

## Output
Save to `design-thinking/cognitive-walkthrough-<topic>.md`:

```markdown
# Cognitive Walkthrough: <prototype> (round <n>)

## Test plan
- Prototype: <path / URL, fidelity>
- Hill and assumptions under test:
- Goal:
- Tasks and success criteria: 1. … 2. … 3. …
- Scenario (read aloud):
- Participants: P1 <role, sponsor user?>, P2 …
- Facilitator / note-taker:

## Expert review (not user evidence)
| Task step | Q1 goal | Q2 visible | Q3 recognizable | Q4 progress | Predicted issue (Assumption) | Where |
| --- | --- | --- | --- | --- | --- | --- |

## Session notes
### P1
| Task | Outcome (Success / Assisted / Failed) | Did | Said (verbatim) | Struggled | Feelings |
| --- | --- | --- | --- | --- | --- |

## Results by task
| Task | P1 | P2 | P3 | Successes | Main blocker (Evidence) |
| --- | --- | --- | --- | --- | --- |

## Review and reflect
- What went well:
- Intended outcome reached?
- Where they struggled:
- Structure understood?
- What must change:

## Assumptions checked
| Assumption | Validated / Invalidated / Inconclusive | Evidence (P#, task) |
| --- | --- | --- |

## Changes for next iteration
| Change | Why (evidence) | Priority | Owner |
| --- | --- | --- | --- |

## Playback
- Key takeaways (3–5):
- Assumptions and questions to validate next:
- Recommended next activity:
```

## Quality checks
- Participants are real target users, not teammates. If anyone is a proxy, they are labeled as one.
- The scenario and prompts never name UI labels or hint at the path, and nobody demonstrated the prototype.
- Notes record behavior and quotes. Interpretations are tagged Assumption.
- Every task has a recorded outcome for every participant, failures included.
- Expert review findings sit in their own section and never count as user evidence.
- Each assumption ends with a verdict, and each blocker has a change and an owner.
- Common pitfalls:
  - rescuing users when they struggle
  - testing a prototype that can't support the whole goal
  - asking "would you use this?" instead of watching them use it

## Next
- `/edt-test:feedback-grid`: sort the observations and decide actions.
- `/edt-test:wireframes` or `/edt-test:paper-prototypes`: make the changes, then run another round.
- `/edt-plan:assumptions-and-questions`: record what was validated and invalidated.
- `/edt-align:playbacks`: play back the results with stakeholders and sponsor users.
- `/edt-plan:user-stories`: turn the validated flow into stories.

## Source
[IBM Enterprise Design Thinking Toolkit: Cognitive Walkthrough](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac1d)
