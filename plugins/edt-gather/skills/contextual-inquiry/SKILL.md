---
name: contextual-inquiry
description: Plans a Contextual Inquiry (scope, outreach, observation guide, consent) and turns field notes from watching users in their own setting into tagged findings. Use when the user says "contextual inquiry", "shadow a user", "site visit", "field study", "ride-along", "observe users at work", "watch how they actually do it", "debrief my field notes", or wants the how and why behind real behavior.
argument-hint: "[user and task] [plan | debrief] [facilitate]"
---

# Contextual Inquiry

> IBM Enterprise Design Thinking · Gather user data · Observe, then Reflect · ~60 min

People are often poor reporters of their own work. They do it, they don't describe it. Contextual Inquiry puts you inside the user's environment, at their desk, on the warehouse floor or at the kitchen table, so you can watch a real task as it happens. You see the tools, the people, the workarounds and the vocabulary around it, and you learn the mental model behind it: the how and the why of their behavior. This is Observe in its purest form, immersing yourself in the real world. Some observation can be done remotely, but nothing replaces seeing the user's world in person. Claude can't go on the visit for you. It helps you plan a good one and make sense of what you bring back.

## When to use it
- Any time. Use it to find new problems worth solving, or to judge how well an existing solution holds up in real conditions.
- What users say and what they do may differ. Look for spreadsheets beside the "official" tool, sticky notes on monitors and printouts.
- Interviews keep producing "it depends" answers. Go and watch.
- The team is about to build an empathy map or an as-is scenario map with no first-hand observation behind it.

## Inputs
- Upstream artifacts in `design-thinking/`:
  - **Plan:** `research-plan*` (objectives, screening criteria), `assumptions-and-questions*` (what to watch for)
  - **People:** `sponsor-users*` (who to visit), `stakeholder-map*` (who grants access)
  - **History:** earlier `contextual-inquiry*` and `interviews*` files
- Ask the user for anything still missing:
  - The user, the task and the moment: who, doing what, and when
  - The decision this research will inform
  - Access constraints: site rules, safety gear, NDAs, recording policy
  - For a debrief: the raw field notes, photos (Claude can read images), audio transcripts and each observer's reflections
- Never invent observations. If the visit hasn't happened yet, work in plan mode only.

## Co-create with Claude
**A. Plan the visit** (`plan`)
1. **Define the scope.** Agree as a team on the experience to investigate: who the user is, what they're doing, and when. Push for a specific scope. "How night-shift nurses hand over patients at shift change" is a scope. "Nurses" is not. Write 3–5 learning objectives, and link each one to an assumption or question in the workspace.
2. **Reach out.** Draft a message to the users or Sponsor Users you want to observe. Explain the purpose, what you'll do while you're there, how long you'll stay, what you'll record and how the data will be used. More detail builds more trust. Finding the right opportunity and the right level of access can take time. Suggest fallbacks: another site, a shorter visit, or a remote screen-share labeled as lower fidelity.
3. **Nail down the details.** Schedule the visit in the real environment, at the moment the task actually happens. Get permission to record audio or video where you can. Send no more than two observers: a **lead** who asks questions and a **documenter** who captures. Draft a logistics checklist covering badges, safety gear, consent forms and the NDA.
4. **Write the observation guide.** This is a guide, not a questionnaire. It contains an opening script, the "teach me your job" request, what to watch for, and probes. What to watch for:
   - The activities and their sequence
   - The environment
   - Interactions with people and with things
   - Tools and artifacts
   - Interruptions
   - Workarounds
   - The words the user uses for things
5. **List your expectations.** Before you go, write down what you expect to see, as Assumptions, so you notice when reality contradicts them.

**B. Debrief the visit** (`debrief`)
1. **Capture.** Turn the notes into one line per observation, recording what was seen or heard with no judgement attached. Give each line its source: the participant ID plus a time or a photo. Keep observation and interpretation apart. "Re-typed the order number from a printout" is Evidence. "Doesn't trust the system" is an Assumption.
2. **Reflect individually first.** Ask each observer for their own takeaways and "aha" moments before Claude shares its reading, then compare. Good reflection happens directly after the visit, while memory is fresh.
3. **Find patterns.** Group the observations into workarounds, breakdowns, vocabulary, artifacts, people involved and the user's mental model. Note where the visit confirmed or contradicted each learning objective.
4. **Playback.** Ask what the findings imply for the wider team, and what you could make to show the insight: a quote wall, a sketch of the workspace, a short story. Recommend the next synthesis activity.

## Facilitate a live session
In this activity, the session is the visit itself plus a same-day debrief. Claude prepares a kit for the observer pair.

**Agenda (60 min on site, then a 25 min debrief)**
- **0–5:** Intro and consent. Say who you are and why you came, and confirm recording. Set the stance: "You're the expert, we're here to learn."
- **5–45:** Observe. The user does their real work while the lead asks to be taught and the documenter captures.
- **45–55:** Wrap up. Clarify moments you flagged, ask what you missed, thank them and explain next steps.
- **Right after:** 10 min of individual reflection in silence, then 15 min sharing reflections with each other.

**Prompts to read aloud**
- "Please work the way you normally would. Imagine you're teaching me to do your job."
- "Talk me through what you're doing as you go."
- "I noticed you just ___. Can you tell me about that?"
- "What would you normally do next? What happens on a bad day?"
- "What's that note, spreadsheet or printout for?"
- "Is there anything we should have seen today but didn't?"

**Roles and materials:** The lead acts as an apprentice. They stay curious, follow the user's lead and avoid suggesting solutions. The documenter captures verbatim quotes, actions with timestamps, photos (with permission) and a sketch of the space. Bring a notebook, a recorder, a consent form, the observation guide and a camera.

**Debrief board (wall or Mural):** six columns: *Observations*, *Quotes*, *Workarounds and breakdowns*, *Tools and environment*, *Aha moments* and *Questions*. Use one sticky per observation, and one color per participant.

**Afterwards:** give Claude the notes, photos and transcripts, and Claude digitizes them into the template below.

## Output
Save to `design-thinking/contextual-inquiry-<topic>.md` using this template:

```markdown
# Contextual Inquiry: <user> <task>

**Scope:** <who> doing <what> when <when> · **Dates:** … · **Sites:** … · **Observers:** lead …, documenter … · **Recorded:** yes/no · **In person / remote:** …

## Learning objectives
| # | Objective | Linked assumption or question | What we saw | Status (confirmed / contradicted / open) |
|---|---|---|---|---|

## Participants
| ID | Role and context | Site | Length | Sponsor User? |
|---|---|---|---|---|
<!-- Use IDs, not names, unless the participant agreed to be named. -->

## Observations
### <ID>: <task or moment>
- <what they did, without judgement>. Evidence: <ID, time or photo>
- "<verbatim quote>". Evidence: <ID, time>
- <what we think it means>. Assumption

## Patterns
| Pattern (workaround, breakdown, vocabulary, artifact, people, mental model) | What we saw | Seen in (IDs) | Tag |
|---|---|---|---|

## Expected vs. observed
| We expected | We observed | Tag |
|---|---|---|

## Aha moments
- …

## Open questions
- …. Question

## Playback
- **Key takeaways (3–5):** …
- **Implications for the team:** …
- **What we could make to show it:** …
- **Assumptions and questions to validate:** …
- **Recommended next activity:** `/edt-synthesize:empathy-map`
```

## Quality checks
- The observation happened in the user's own environment, during real work. A demo or a conference-room re-enactment doesn't count. Any remote observation is labeled as remote.
- Observations record behavior and quotes. Interpretations are tagged Assumption, never written as fact.
- Every Evidence item carries a participant ID and a time or artifact reference.
- The user's own vocabulary is kept, not translated into product or team terms.
- Workarounds and homemade artifacts are captured. They are often the richest signal.
- Findings that contradict expectations are reported, not smoothed over.
- One user's behavior is not generalized. Patterns state how many participants they were seen in.
- There were no more than two observers, and one of them owned capture. Reflection happened right after the visit, individually first.
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
