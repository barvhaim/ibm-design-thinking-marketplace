---
name: interviews
description: Plans user or stakeholder interviews (scope, recruiting note, a discussion guide of open, non-leading questions) and turns transcripts or notes into tagged findings. Use when the user says "user interviews", "interview guide", "discussion guide", "talk to customers", "stakeholder interviews", "what should I ask?", "review my interview questions", "synthesize these transcripts", or wants to validate a hypothesis about users.
argument-hint: "[user or topic] [plan | review | debrief] [facilitate]"
---

# Interviews

> IBM Enterprise Design Thinking · Gather user data · Observe, then Reflect · ~60 min

There is no substitute for talking with the people you're designing for. A good interview shows you the world as the other person sees it: their goals, their frustrations, their words for things and the reasons behind what they do. It builds empathy, and it turns up questions the team didn't know to ask. The conversation is Observe. Reflecting right afterwards turns what you heard into something the team can use. Claude can't sit in the room. It helps you write a guide that doesn't lead, rehearse it, and synthesize the results without losing the participants' voices.

## When to use it
- To validate a hypothesis or assumption about your users.
- To understand how an idea might affect users before you invest in it.
- In early discovery, when the team doesn't yet know the user's world.
- To learn stakeholders' goals, constraints and definitions of success.
- Pair it with `/edt-gather:contextual-inquiry` when you need to see behavior, not only hear about it. What people say they do is not always what they do.

## Inputs
- Upstream artifacts in `design-thinking/`:
  - **Plan:** `research-plan*`, `assumptions-and-questions*` (the hypotheses to probe), `hills*` (if you're testing ideas against intent)
  - **People:** `sponsor-users*`, `stakeholder-map*`
  - **History:** earlier `interviews*` and `empathy-map*` files
- Ask the user for anything still missing:
  - Who to talk to (role, segment, how many) and the decision the research informs
  - The format (phone, video or in person) and the recording rules
  - For a debrief: transcripts, notes or recordings, plus each interviewer's reflections
- Never invent participants or quotes. Rehearsal answers from Claude are practice, not data.

## Co-create with Claude
**A. Plan** (`plan`)
1. **Define the scope.** Agree on who the user is, what they're doing and when. An example: "IT admins provisioning accounts for new hires in their first week." Write 3–5 learning objectives, and link each one to an assumption or question.
2. **Recruit.** Draft a note to the users or Sponsor Users you want to talk to. It explains the purpose, the length, the format, what will be recorded and how their data will be used. Start with a handful of people per user type, and keep going until you stop hearing new things.
3. **Prepare.** Get permission to record. Line up a second person to take notes. Schedule the call or visit.
4. **Write the discussion guide.**
   - **Warm-up:** general questions about their role, background and experience.
   - **Core:** specific questions tied to the objectives. Move from broad to specific. Anchor questions in real past events, for example "Tell me about the last time you…".
   - **Wrap-up:** a closing set of questions.

   Write about 8–12 core questions for 45 minutes, each with 1–2 probes.

**B. Review the guide** (`review`)
1. **Check every question against the rubric:**
   - **Open:** it can't be answered yes or no.
   - **Neutral:** it doesn't suggest an answer.
   - **Single:** it asks one thing at a time.
   - **Past behavior:** it asks what happened, not what they'd hypothetically do.
   - **No pitch:** it doesn't introduce your solution.
   - **Their words:** it uses the user's vocabulary.

   Return a before-and-after table:

   | Before | Problem | After |
   |---|---|---|
   | "Would a dashboard help you track orders?" | Pitches a feature; yes/no | "How do you keep track of orders today?" |
   | "Don't you find approvals frustrating?" | Leading | "Walk me through the last approval you needed." |
   | "How often do you export reports, and why?" | Two questions | "When did you last export a report?" then "What was it for?" |
   | "Would you use this every day?" | Hypothetical | "When did you last need to do this? What did you do?" |

2. **Rehearse.** Claude can play a participant so you can time the guide and spot awkward questions. Label this clearly as a rehearsal, and never carry its answers into findings.

**C. Debrief** (`debrief`)
1. **Capture.** From the transcripts or notes, record what you heard without judgement. Keep quotes verbatim with the participant ID and a timestamp, and mark any paraphrase as a paraphrase. Keep what was said (Evidence) apart from what you conclude (Assumption).
2. **Reflect.** Directly after each interview, each interviewer writes their own takeaways and "aha" moments, then shares them. Claude compares across interviews to find themes, contradictions and counts ("4 of 6"). It flags any gap between what people say and what they do as a candidate for observation.
3. **Playback.** Summarize what you learned, what changed in your assumptions, and what it means for the team.

## Facilitate a live session
In this activity, the session is the interview itself. Claude prepares a kit for the interviewer and the note-taker.

**Agenda (60 min)**
- **0–5:** Intro. Thank them, explain the purpose and how their data will be used, and confirm consent to record. "There are no right answers. You're the expert."
- **5–10:** Warm-up questions about their role, background and a typical day.
- **10–45:** Core questions, one at a time. Follow interesting threads, then return to the guide.
- **45–55:** Wrap-up. "What didn't we ask that we should have?" "Who else should we talk to?"
- **55–60:** Thanks and next steps.
- **Right after:** 10 min of individual reflection, then 10 min comparing notes.

**Probes to keep at hand**
- "Tell me more about that."
- "Can you give me an example?"
- "What happened next?"
- "Why was that important to you?"
- "You said ___. What do you mean by ___?"
- "How did that feel?"

Let silence sit for a few seconds before you fill it. React neutrally, for example "Thanks, that's helpful." Saying "Great!" signals a right answer.

**Roles:** The interviewer asks one question at a time. They stay engaged without feeling they must respond to everything, and they keep the conversation on time and on topic while leaving room to probe. The note-taker captures quotes verbatim, flags timestamps and notes body language.

**Debrief board (wall or Mural):** one column per participant, with rows for *Quotes*, *Goals*, *Pain points*, *Behaviors described*, *Surprises* and *Questions*. Use one sticky per note.

**Afterwards:** give Claude the transcripts or notes, and Claude digitizes them into the template below.

## Output
Save to `design-thinking/interviews-<topic>.md` using this template:

```markdown
# Interviews: <user or topic>

**Scope:** <who> doing <what> when <when> · **Dates:** … · **Format:** … · **Interviewers:** … · **Participants:** <n>

## Learning objectives
| # | Objective | Linked assumption or question | What we learned | Status (confirmed / contradicted / open) |
|---|---|---|---|---|

## Discussion guide
- **Intro (5 min):** purpose, consent, data use
- **Warm-up (5 min):** 1. …
- **Core (35 min):** 1. <question>. Probes: …
- **Wrap-up (10 min):** …

## Participants
| ID | Role or segment | Date | Length | Sponsor User? |
|---|---|---|---|---|
<!-- Use IDs, not names, unless the participant agreed to be named. -->

## Findings by participant
### <ID>: <role>
- "<verbatim quote>". Evidence: <ID, timestamp>
- <behavior or event they described>. Evidence: <ID, notes>
- <our interpretation>. Assumption

## Themes across interviews
| Theme | Supporting evidence (IDs, count) | Counter-evidence | Tag |
|---|---|---|---|

## Aha moments
- …

## Says vs. does (to observe)
- …. Question

## Playback
- **Key takeaways (3–5):** …
- **Assumptions that changed:** …
- **Assumptions and questions to validate:** …
- **Recommended next activity:** `/edt-synthesize:empathy-map`
```

## Quality checks
- Every question in the guide passes the rubric: open, neutral, single, about past behavior, with no pitch, in the user's words.
- Each objective has at least one question, and the guide fits the time.
- Quotes are verbatim, with an ID and a timestamp. Paraphrases are marked.
- Findings keep what was said (Evidence) apart from conclusions (Assumption), and themes show counts.
- Counter-evidence is reported. A theme seen in one participant is labeled as such.
- Consent was obtained, participants are anonymized, and rehearsal answers never appear as findings.
- Pitfalls:
  - Pitching your solution, or asking users to design the feature
  - Asking "Would you…?" instead of "When did you last…?"
  - Answering your own question, or rushing to fill a silence
  - One person both asking questions and taking notes
  - Synthesizing days later from memory

## Next
- `/edt-synthesize:empathy-map`: reflect as a team on what you heard.
- `/edt-synthesize:needs-statements`: state what users need once patterns are clear.
- `/edt-gather:contextual-inquiry`: go and observe the behaviors people described.
- `/edt-plan:assumptions-and-questions`: update which assumptions held.
- `/edt-synthesize:stakeholder-map`: for stakeholder interviews, map what you learned about expectations and relationships.

## Source
[IBM Enterprise Design Thinking Toolkit: Interviews](https://www.ibm.com/downloads/documents/us-en/137a1e253e5bac0d)
