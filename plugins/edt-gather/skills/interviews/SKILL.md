---
name: interviews
description: Runs user or stakeholder interviews as an HTML artifact. Claude writes a non-leading discussion guide, interviews simulated users from the shared panel one at a time in character, and turns the transcripts into tagged findings. It also builds a field kit for real interviews and synthesizes real transcripts. Use when the user says "user interviews", "interview guide", "what should I ask?", "review my interview questions", "stakeholder interviews" or "synthesize these transcripts".
argument-hint: "[user or topic] [review] [facilitate]"
---

# Interviews

> IBM Enterprise Design Thinking · Gather user data · Observe, then Reflect · ~60 min

There is no substitute for talking with the people you're designing for. A good interview shows you the world as the other person sees it: their goals, their frustrations, their words for things and the reasons behind what they do. It builds empathy, and it turns up questions the team didn't know to ask. The conversation is Observe. Reflecting right afterwards turns what you heard into something the team can use. Claude can't sit in the room with your users, so it does two things. It interviews simulated users from the panel, which gives the team a fast first read and a guide that has already met some pushback. And it prepares and synthesizes the real interviews that confirm or overturn that first read.

## When to use it
- To validate a hypothesis or assumption about your users.
- To understand how an idea might affect users before you invest in it.
- In early discovery, when the team doesn't yet know the user's world.
- To learn stakeholders' goals, constraints and definitions of success.
- To test and tighten a discussion guide before the real interviews.
- Pair it with `/edt-gather:contextual-inquiry` when you need to see behavior, not only hear about it. What people say they do is not always what they do.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of:
  - plan: `research-plan-*`, `assumptions-and-questions-*` (the hypotheses to probe), `hills-*` (if you're testing ideas against intent)
  - people: `simulated-users.html`, `sponsor-users-*`, `stakeholder-map-*`
  - history: earlier `interviews-*` and `empathy-map-*` pages
- **Files the user points to,** such as real transcripts, notes, recordings and each interviewer's reflections. These are real evidence and come first.
- **The simulated user panel.** If `design-thinking/simulated-users.html` doesn't exist, or has no personas for this user, create or extend it first, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`. For stakeholder interviews, add stakeholder personas by role.
- **Ask the user only for:** who the interviews are about and the decision they inform, if neither is clear, and whether there are real transcripts you haven't seen.

## Co-create with Claude
1. **Define the scope.** Agree on who the user is, what they're doing and when, for example "IT admins provisioning accounts for new hires in their first week". Write 3–5 learning objectives (`O1…`), and link each one to an assumption or question in the workspace.
2. **Pick the interviewees.** Choose 3–5 personas from the panel who fit the scope. Spread them across experience and attitude, with at least one skeptic and the panel's edge case. If the user gave you real transcripts, synthesize those first (steps 6–7), then simulate only the voices or objectives they leave thin.
3. **Write the discussion guide.**
   - **Intro (5 min):** the purpose, consent, and how their data will be used. "There are no right answers. You're the expert."
   - **Warm-up (5 min):** their role, background and a typical day.
   - **Core (35 min):** 8–12 questions tied to the objectives, moving from broad to specific, each with 1–2 probes. Anchor them in real past events: "Tell me about the last time you…".
   - **Wrap-up (10 min):** "What didn't we ask that we should have?" "Who else should we talk to?"
4. **Critique the guide,** or the user's own guide with `review`. Check every question against the rubric:
   - **Open:** it can't be answered yes or no.
   - **Neutral:** it doesn't suggest an answer.
   - **Single:** it asks one thing at a time.
   - **Past behavior:** it asks what happened, not what they'd hypothetically do.
   - **No pitch:** it doesn't introduce your solution.
   - **Their words:** it uses the user's vocabulary.

   Record every rewrite as before, problem and after. For example, "Would a dashboard help you track orders?" pitches a feature and invites a yes, so it becomes "How do you keep track of orders today?". "How often do you export reports, and why?" asks two things, so it becomes "When did you last export a report?" and then "What was it for?". With `review`, stop here and build the page with the guide sections only.
5. **Interview each persona separately.** Run the whole guide with one persona at a time. Claude is a neutral interviewer, and the persona answers in the first person, in character, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`.
   - **The interviewer** asks one question at a time and follows threads with probes ("Can you give me an example?" "What happened next?"). It lets silences sit, reacts neutrally, and never feeds the persona an answer.
   - **The persona** answers from their own last real week, in their own words. Each one tells at least one concrete story, wanders a little, forgets something, and pushes back where they would. They don't know what earlier personas said.
   - **Right after each interview,** write the interviewer's reflection: takeaways and "aha" moments. Do this before moving on to the next persona. Keep every transcript for the page.
   - **When a question flops,** such as a bare yes or no, confusion, or an answer to a different question, add a fix to the guide.
6. **Capture.** For each participant, write one note per finding, grouped as Quotes, Goals, Pain points, Behaviors described, Surprises and Questions. Tag every note:
   - `evidence`: a real participant's verbatim quote or reported event, with the participant ID and a timestamp. Mark paraphrases as paraphrases.
   - `simulated`: anything a persona said or described, with its `SU-…` ID. A simulated quote is a quote from a simulation, not from a user.
   - `assumption`: the team's interpretation of what was said.
   - `question`: what's still unknown.
7. **Reflect across interviews.** Find themes, contradictions and counter-evidence. Give counts such as "3 of 4 simulated users" or "2 of 6 participants", and keep real and simulated counts apart. Label any theme seen in one participant as such. Flag every gap between what someone says and what they describe doing as a candidate for observation. Then update each objective's status. Only real evidence can make it confirmed or contradicted. Simulated answers alone give simulated support or a simulated contradiction, and everything else stays open.
8. **Playback.** Summarize what you learned, which assumptions moved, and what it means for the team. Put the simulated claims the team leans on most at the top of "Validate next", and offer the facilitator kit so real interviews can check them. Then publish the page.

## Facilitate a live session
Here, the session is a real interview. Produce `design-thinking/interviews-<topic>-kit.html` for the interviewer and the note-taker. It needs:
- **Agenda table (60 min):**
  - 0–5 Intro: thank them, explain the purpose and how their data will be used, and confirm consent to record. "There are no right answers. You're the expert."
  - 5–10 Warm-up
  - 10–45 Core questions, one at a time. Follow interesting threads, then return to the guide.
  - 45–55 Wrap-up
  - 55–60 Thanks and next steps
  - Right after: 10 min of individual reflection, then 10 min comparing notes
- **The discussion guide,** already critiqued against the rubric.
- **Probes to keep at hand:** "Tell me more about that." "Can you give me an example?" "What happened next?" "Why was that important to you?" "You said ___. What do you mean by ___?" "How did that feel?" Let silence sit for a few seconds before you fill it. React neutrally, for example "Thanks, that's helpful." Saying "Great!" signals a right answer.
- **Roles:** the interviewer asks one question at a time, stays engaged without responding to everything, and keeps the conversation on time and on topic while leaving room to probe. The note-taker captures quotes verbatim, flags timestamps and notes body language. One person never does both.
- **Recruiting and logistics:** a draft note to the users or Sponsor Users (purpose, length, format, what will be recorded, how their data will be used), permission to record, a second person to take notes, and a schedule. Start with a handful of people per user type, and keep going until you stop hearing new things.
- **Rehearsal (offer it):** run the guide against one simulated persona, ideally the skeptic, to time it and catch awkward questions. Put that transcript on the kit page, labeled Rehearsal, and use it to fix the guide, not as findings.
- **An empty debrief board:** `.cols` with one column per participant, each holding clusters for Quotes, Goals, Pain points, Behaviors described, Surprises and Questions.

After the interviews, read the transcripts or notes and build the results page, with real findings tagged `evidence`. Keep any earlier simulated findings beside them, never merged, and say which ones the real interviews confirmed or contradicted.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/interviews-<topic>.html`. `${CLAUDE_PLUGIN_ROOT}/shared/example-empathy-map.html` shows a finished page.
- **Title:** `<User or topic> Interviews`, for example "Release Engineer Interviews".
- **Sections:**
  1. **Scope and objectives:** the scope in the lede, then a table of objective, linked assumption or question, what we learned, and a status pill. Use `data-tone="good"` for confirmed, `data-tone="bad"` for contradicted, `data-tag="simulated"` for simulated support or contradiction, and `data-tag="question"` for open.
  2. **Discussion guide:** a table of section, time, question, probes and objective, then a "Guide fixes" table of before, problem and after.
  3. **Who we talked to:** `.personas` cards for the simulated interviewees, copied from the panel, and a table of real participants by ID, with role or segment, date, length and whether they're a Sponsor User. Use names only with permission.
  4. **Findings by participant:** `.cols`, one `.col` per participant, holding titled `.cluster`s of tagged `.note`s.
  5. **Themes across interviews:** a table of theme, supporting notes with counts, counter-evidence, and a tag pill.
  6. **Says vs. does:** `question` notes to carry into `/edt-gather:contextual-inquiry`.
  7. **Transcripts:** one `details.transcript` per interview, with persona lines as `turn sim`, followed by the interviewer's reflection.
  8. **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "scope": { "who": "", "what": "", "when": "", "decision": "" },
    "objectives": [{ "id": "O1", "text": "", "links": ["A2"], "learned": "", "status": "simulated-support" }],
    "guide": { "intro": "", "warmup": [""], "core": [{ "q": "", "probes": [""], "objective": "O1" }], "wrapup": [""],
               "fixes": [{ "before": "", "problem": "", "after": "" }] },
    "participants": [{ "id": "SU-2", "kind": "simulated", "role": "" }],
    "transcripts": [{ "participant": "SU-2", "turns": [{ "who": "Interviewer", "text": "" }], "reflection": "" }],
    "themes": [{ "text": "", "notes": ["N3", "N7"], "count": "3 of 4 simulated", "counter": ["N9"], "tag": "simulated" }],
    "says_vs_does": ["N12"] }
  ```
  `status` is `confirmed`, `contradicted`, `simulated-support`, `simulated-contradiction` or `open`. `items` holds every note, with `group` set to `"<participant> / <cluster>"`.

## Quality checks
- Every question in the guide passes the rubric: open, neutral, single, about past behavior, with no pitch, in the user's words.
- Each objective has at least one question, and the guide fits the time.
- Real quotes are verbatim, with an ID and a timestamp, and paraphrases are marked. Simulated quotes carry their `SU-…` ID. No simulated note is tagged `evidence`, and no objective is confirmed on simulated answers alone.
- Findings keep what was said apart from conclusions. Themes show counts, counter-evidence is reported, and a theme seen in one participant is labeled as such.
- Simulated counts stay counts ("3 of 4 simulated users"), never percentages, and they're never added to real counts.
- Each persona sounds like a different person, with their own vocabulary and stories. If every persona likes the idea or answers in tidy lists, rerun them with more friction.
- Claude, as the interviewer, stayed neutral. Reread each transcript for leading follow-ups and hints at the solution before you synthesize.
- Real participants gave consent and are anonymized. Rehearsal transcripts stay on the kit page.
- Pitfalls:
  - Pitching your solution, or asking users to design the feature
  - Asking "Would you…?" instead of "When did you last…?"
  - Answering your own question, or rushing to fill a silence
  - One person both asking questions and taking notes
  - Synthesizing days later from memory
  - Treating a simulated round as the research, when it is a rehearsal and a list of things to check

## Next
- `/edt-synthesize:empathy-map`: reflect as a team on what you heard.
- `/edt-synthesize:needs-statements`: state what users need once patterns are clear.
- `/edt-gather:contextual-inquiry`: go and observe the behaviors people described.
- `/edt-plan:assumptions-and-questions`: update which assumptions held.
- `/edt-synthesize:stakeholder-map`: for stakeholder interviews, map what you learned about expectations and relationships.
- `/edt-core:sponsor-users`: find real users to check the simulated findings.

## Source
[IBM Enterprise Design Thinking Toolkit: Interviews](https://www.ibm.com/downloads/documents/us-en/137a1e253e5bac0d)
