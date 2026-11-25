---
name: contextual-inquiry
description: Produces a Contextual Inquiry as an HTML artifact. Claude writes a simulated observer's log of a panel persona doing a real task in their own setting (actions, think-aloud, workarounds, the artifacts on their desk), draws out patterns and plans the real visit. It also builds a field kit and debriefs real field notes. Use when the user says "contextual inquiry", "shadow a user", "site visit", "field study", "observe users at work", "watch how they actually do it" or "debrief my field notes".
argument-hint: "[user and task] [facilitate]"
---

# Contextual Inquiry

> IBM Enterprise Design Thinking · Gather user data · Observe, then Reflect · ~60 min

People are often poor reporters of their own work. They do it, they don't describe it. Contextual Inquiry puts you inside the user's environment, at their desk, on the warehouse floor or at the kitchen table, so you can watch a real task as it happens. You see the tools, the people, the workarounds and the vocabulary around it, and you learn the mental model behind it: the how and the why of their behavior. This is Observe in its purest form. Claude can't go on the visit, so it does two things. It simulates what an observer would likely see and hear, so the team arrives with sharper expectations and knows what to look for. And it plans the real visit and debriefs what you bring back, because only a real visit shows the tacit workarounds and local habits a simulation can't imagine.

## When to use it
- Any time. Use it to find new problems worth solving, or to judge how well an existing solution holds up in real conditions.
- What users say and what they do may differ. Look for spreadsheets beside the "official" tool, sticky notes on monitors and printouts.
- Interviews keep producing "it depends" answers. Go and watch.
- The team is about to build an empathy map or an as-is scenario map with no observation behind it.
- Before a real visit, to rehearse what to watch for and write down the expectations it should test.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of:
  - plan: `research-plan-*` (objectives, screening criteria), `assumptions-and-questions-*` (what to watch for)
  - people: `simulated-users.html`, `sponsor-users-*` (who to visit), `stakeholder-map-*` (who grants access)
  - history: earlier `contextual-inquiry-*` pages, and `interviews-*`, especially their says-vs-does flags
- **Files the user points to,** such as field notes, photos (Claude can read images), audio transcripts and each observer's reflections. These are real evidence and come first.
- **The simulated user panel.** If `design-thinking/simulated-users.html` doesn't exist, or has nobody who does this task, create or extend it first, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`.
- **Ask the user only for:** the user, task and moment, if they aren't clear, and the decision this research informs. For the real visit, access constraints such as site rules, safety gear, NDAs and recording policy can stay as open questions on the plan.

## Co-create with Claude
1. **Define the scope.** Agree on who the user is, what they're doing, and when. Push for a specific scope. "How night-shift nurses hand over patients at shift change" is a scope. "Nurses" is not. Write 3–5 learning objectives (`O1…`), and link each one to an assumption or question in the workspace.
2. **List your expectations.** Before observing anything, write down what the team expects to see, tagged `assumption`, so you notice when the observation contradicts it.
3. **Pick who to observe.** Choose 1–3 personas from the panel who really do this task, preferring contrasts such as an expert and a novice, or the panel's edge case. Fix each one's setting: the place, the time of day, the tools at hand, who sits nearby, and what else is going on that day.
4. **Simulate the observation, one persona at a time.** Write the documenter's log of a 40-minute session, at the moment the task really happens. Claude plays the lead, who acts as an apprentice ("Imagine you're teaching me to do your job." "I noticed you just ___. Can you tell me about that?"). The persona keeps working. Log only what an observer could see or hear:
   - timestamped actions in sequence, including waiting, mistakes and redoing
   - think-aloud fragments in the persona's own words, often half-sentences
   - interactions with people, such as a colleague's question or a phone call, and with things
   - interruptions, and what the persona does when they come back
   - workarounds: the spreadsheet beside the official tool, the re-typed number, the sticky note on the monitor
   - the artifacts on the desk or screen, and what each one is for
   - the words the persona uses for things
   - the environment: noise, space, light, devices

   The persona works the way they actually do, not the way the official process says. They don't perform for the observer, they skip steps they find obvious, and they may be mildly annoyed at being watched. Include one bad-day moment. Never narrate thoughts the persona didn't say aloud, because those are the team's inferences. Close with the wrap-up: what they'd normally do next, and what we should have seen today but didn't. Optionally sketch the workspace.
5. **Reflect, then find patterns.** Right after each log, write the observer's own takeaways and "aha" moments. Then turn the logs into one note per observation, and tag each one:
   - `simulated`: what a persona did or said, with the `SU-…` ID and the log time. "Re-typed the order number from a printout" is an observation.
   - `assumption`: an interpretation. "Doesn't trust the system" is an assumption.
   - `question`: what you couldn't see.
   - `evidence`: anything from real field notes, with the participant ID and a time or photo.

   Group the notes on the debrief board: Observations, Quotes, Workarounds and breakdowns, Tools and environment, Aha moments, and Questions. Note where each objective and expectation was supported or contradicted.
6. **Plan the real visit.** Draft:
   - **The outreach message:** the purpose, what you'll do while you're there, how long you'll stay, what you'll record and how the data will be used. More detail builds more trust, and finding the right access can take time.
   - **Logistics:** the real environment at the moment the task happens, permission to record, no more than two observers (a **lead** who asks and a **documenter** who captures), badges, safety gear, consent forms and the NDA.
   - **Fallbacks:** another site, a shorter visit, or a remote screen-share labeled as lower fidelity.
   - **Check on site:** the simulated observations and expectations that matter most, phrased as things to watch for rather than questions to ask.
7. **Playback.** Ask what the findings imply for the wider team, and what you could make to show the insight: a quote wall, a sketch of the workspace, a short story. Put the simulated claims at the top of "Validate next", offer the field kit (`facilitate`), and publish the page.

If the user brings real field notes, debrief those first through steps 5 and 7 as `evidence`. Simulate only to fill gaps, and show simulated observations beside the real ones, never merged.

## Facilitate a live session
Here, the session is the real visit plus a same-day debrief. Produce `design-thinking/contextual-inquiry-<topic>-kit.html` for the observer pair. It needs:
- **Agenda table (60 min on site, then a 25 min debrief):**
  - 0–5 Intro and consent. Say who you are and why you came, and confirm recording. "You're the expert, we're here to learn."
  - 5–45 Observe. The user does their real work while the lead asks to be taught and the documenter captures.
  - 45–55 Wrap up. Clarify the moments you flagged, ask what you missed, thank them and explain next steps.
  - Right after: 10 min of individual reflection in silence, then 15 min sharing reflections.
- **Prompts to read aloud:** "Please work the way you normally would. Imagine you're teaching me to do your job." "Talk me through what you're doing as you go." "I noticed you just ___. Can you tell me about that?" "What would you normally do next? What happens on a bad day?" "What's that note, spreadsheet or printout for?" "Is there anything we should have seen today but didn't?"
- **Roles and materials:** the lead acts as an apprentice, stays curious, follows the user's lead and never suggests solutions. The documenter captures verbatim quotes, actions with timestamps, photos (with permission) and a sketch of the space. Bring a notebook, a recorder, a consent form, the observation guide and a camera.
- **The observation guide:** the opening script, the "teach me your job" request, what to watch for (activities and sequence, environment, interactions with people and things, tools and artifacts, interruptions, workarounds, vocabulary) and the probes.
- **The expectations and the check-on-site list,** as `assumption` and `simulated` notes, plus the logistics checklist and the outreach message.
- **An empty debrief board:** `.cols` with the six columns above. On the wall, use one sticky per observation and one color per participant.

After the visit, read the notes, photos and transcripts, and build the results page with real observations tagged `evidence`. Keep any simulated observations beside them, and say which ones the visit confirmed or contradicted.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/contextual-inquiry-<topic>.html`. `${CLAUDE_PLUGIN_ROOT}/shared/example-empathy-map.html` shows a finished page.
- **Title:** `<User or task> Contextual Inquiry`, for example "Shift Handover Contextual Inquiry".
- **Sections:**
  1. **Scope and objectives:** the scope in the lede, then a table of objective, linked assumption or question, what we saw, and a status pill (`data-tone="good"` confirmed, `data-tone="bad"` contradicted, both on evidence only; `data-tag="simulated"` for simulated support or contradiction; `data-tag="question"` for open).
  2. **Who we observed:** `.personas` cards for the simulated users, each with its setting, and a table of real participants by ID, with role and context, site, length, in person or remote, and whether they're a Sponsor User.
  3. **Observation log:** one `details.transcript` per session. `.who` holds the log time and the speaker, such as "09:14 SU-3" or "09:15 Lead". Mark the persona's actions and words as `turn sim`. End with the observer's reflection. Optionally add a workspace sketch as a `.frames` frame.
  4. **Debrief board:** `.cols` with the six columns, each holding tagged `.note`s.
  5. **Expected vs. observed:** a table of what we expected, what we observed, and a tag pill.
  6. **Plan for a real visit:** the outreach message, a logistics table with owners, and the check-on-site list as notes. Leave it out of a results page from a real visit.
  7. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "scope": { "who": "", "task": "", "when": "", "decision": "" },
    "objectives": [{ "id": "O1", "text": "", "links": ["A2"], "saw": "", "status": "simulated-support" }],
    "sessions": [{ "participant": "SU-3", "kind": "simulated", "setting": "", "remote": false,
                   "log": [{ "t": "09:14", "who": "SU-3", "kind": "action", "text": "" }], "reflection": "" }],
    "board": { "observations": ["N1"], "quotes": [], "workarounds": [], "tools": [], "aha": [], "questions": [] },
    "expected_vs_observed": [{ "expected": "", "observed": "", "tag": "simulated" }],
    "real_visit": { "outreach": "", "observers": { "lead": "", "documenter": "" }, "logistics": [""],
                    "fallbacks": [""], "check_on_site": ["N4"] } }
  ```
  `log[].kind` is `action`, `quote`, `prompt`, `interruption` or `environment`. `items` holds every note, with `group` set to its board column.

## Quality checks
- The observation is set in the user's own environment, during real work. A demo or a conference-room re-enactment doesn't count, and any remote observation is labeled remote.
- Observations record behavior and quotes. Interpretations are tagged `assumption`, never written as fact.
- Every `evidence` note carries a participant ID and a time or artifact reference. Every `simulated` note carries an `SU-…` ID and a log time. No simulated note is tagged `evidence`.
- The user's own vocabulary is kept, not translated into product or team terms.
- Workarounds and homemade artifacts are captured. They are often the richest signal.
- Findings that contradict expectations are reported, not smoothed over.
- One user's behavior is not generalized. Patterns state how many participants showed them, with real and simulated counts kept apart and never given as percentages.
- No more than two observers went, one of them owned capture, and reflection happened right after the visit, individually first.
- Simulation pitfalls:
  - A log that reads like the official process or a tidy tutorial. Real work has waiting, interruptions and shortcuts, so rewrite it messier.
  - Narrating the persona's inner thoughts. An observer only hears what's said aloud.
  - Personas who all work the same way. Different setups should produce different workarounds.
  - A persona who praises your product or volunteers feature ideas. The observation is about their work, not your idea.
  - Treating the simulated log as the visit. It's a rehearsal and a list of things to check.
- Pitfalls:
  - Turning the visit into an interview or a demo of your product
  - Leading the user, for example "Wouldn't it be easier if…?"
  - Recording without consent, or naming participants without permission
  - Debriefing days later from memory

## Next
- `/edt-synthesize:empathy-map`: reflect as a team on what you observed while it's fresh.
- `/edt-synthesize:as-is-scenario-map`: lay out the workflow you watched, phase by phase.
- `/edt-gather:interviews`: follow up on the why behind behaviors you saw.
- `/edt-plan:assumptions-and-questions`: update which assumptions held and which didn't.
- `/edt-plan:research-plan`: plan the next round if gaps remain.
- `/edt-align:playbacks`: share what you learned with stakeholders.

## Source
[IBM Enterprise Design Thinking Toolkit: Contextual Inquiry](https://www.ibm.com/downloads/documents/us-en/137a1e2551dbac1b)
