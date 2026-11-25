---
name: stakeholder-map
description: Maps everyone involved with or affected by the work as an HTML artifact, with labeled groups, decision-makers, an influence and interest plot, relationship lines and open unknowns. Simulated stakeholder personas voice the expectations the team can't ask about yet. Use when the user says "stakeholder map", "who are our stakeholders?", "who decides?", "who should we invite?" or "map the org", or at a kickoff, when onboarding, or before interviews, Playbacks or Sponsor User recruiting.
argument-hint: "[project or initiative] [facilitate]"
---

# Stakeholder Map

> IBM Enterprise Design Thinking · Synthesize research · Reflect · ~30 min

Work succeeds or stalls on people. A stakeholder map is the team reflecting together on who is involved with and affected by the project, what each of them expects, and how they relate to one another, so the team can communicate with them more effectively. It shows who decides, who influences, which relationships are strained, and who nobody thought to include. Often that last group is the end users and the people who support them. Done early, it gives the whole team a clear picture of who matters to this work. Where the team can't yet ask a stakeholder what they expect, a simulated persona for that role can give a first answer, clearly labeled, so the map shows what to go and ask.

## When to use it
- As early as possible on any new piece of work.
- At kickoff, or when a new teammate or sponsor joins.
- Before deciding who to interview, who to invite to Playbacks, or where to recruit Sponsor Users.
- When an initiative stalls and you suspect a missing, unheard or unhappy stakeholder.

## Inputs
- **From `design-thinking/`.** Read the `#edt-data` blocks of:
  - people: `simulated-users.html`, `sponsor-users-*`, `interviews-*` (especially stakeholder interviews)
  - context: `hopes-and-fears-*`, `research-plan-*`, `playbacks-*`
  - history: earlier `stakeholder-map-*` pages
- **Files the user points to,** such as org charts, RACI tables, project docs or meeting attendee lists. These are real sources.
- **The simulated user panel.** If you'll simulate stakeholders and `design-thinking/simulated-users.html` doesn't exist, create it first, following `${CLAUDE_PLUGIN_ROOT}/shared/simulated-users.md`. Add stakeholder personas to the same panel.
- **Ask the user only for:** the project and its boundary, if you can't infer them, and what they know about who decides and how people relate. Relationships are rarely written down.

## Co-create with Claude
1. **Set up.** Name the project and its boundary. Decide on scope: internal teams, the client, users, and outside parties such as vendors, partners and regulators.
2. **Identify.** List everyone involved with or affected by the project, with their title if you know it. Prompt by category: Who funds it? Who decides? Who builds it? Who uses it? Who supports or operates it? Who is affected downstream? Who can block it (legal, security, procurement)? Who is outside the organization? Record where each one came from. A stakeholder from an org chart, a RACI or an attendee list cites its `S…`. One that the team or Claude believes should be there is tagged `assumption`. Where names aren't known, use roles, and never invent a named real person.
3. **Cluster.** As groups surface, cluster them and label each one, for example *Finance*, *Platform team*, *Client IT* or *Patients and families*.
4. **Connect.** Draw the relationships. Ask how they depend on each other and how they interact. For every line, record:
   - **The direction and the verb,** for example *approves*, *funds*, *hands off to*, *is first contact for*.
   - **Whether it's formal** (a reporting line or sign-off) or informal influence.
   - **The quality:** good (+), strained (−) or unknown (?).

   Mark decision-makers and influencers with ★. Place each key stakeholder by influence over the work and interest in it. Base influence on who actually decides or can block, not on seniority.
5. **Simulate the stakeholders you can't ask yet.** For each key stakeholder role with no real input, add a stakeholder persona to the panel, with an `SU-…` ID, an obviously fictional name, the role and its context, what they answer to, and what would make them block the work. A simulated stakeholder stands for a role, such as "a procurement lead at a regional bank". Never role-play a real, named colleague. A named person's expectations stay `assumption` until someone asks them. Interview each persona briefly, one at a time, in character: "What would success look like for you? What worries you about this? Who do you listen to on this? What would make you say no? Who else should we have talked to?" Include at least one who is indifferent or resistant. Keep the transcripts. Record their expectations as `simulated` notes, and add anyone a persona names who isn't on the map yet as a `question` note.
6. **Playback.** Describe the stakeholders' goals and relationships as a short story, then list the unknowns that remain. Suggest concrete engagement actions: who to talk to, who to invite, and who to keep informed. Put the simulated expectations the plan depends on at the top of "Validate next", each with the real person or role to ask.
7. **Check privacy, then publish.** Relationship ratings are about real colleagues. Keep the wording factual and respectful. Before publishing, ask whether the page may name real people. If it may not, or if a named person is on a strained (−) line, describe people by role on the page you publish. Record the choice in the header's `.meta` as *Sharing: team only* or *Sharing: shareable*.

## Facilitate a live session
Produce `design-thinking/stakeholder-map-<topic>-kit.html`. It needs:
- **Agenda table (30 min):**
  - 0–3 Intro: why you're doing this, and the norms (write before you talk, everyone participates, use a parking lot)
  - 3–5 Setup: write the project name in the middle of a blank wall or canvas
  - 5–13 Identify: everyone writes silently, one stakeholder per sticky note, with a name or role and a title
  - 13–18 Cluster: group the notes and label the groups as they surface
  - 18–26 Connect: draw lines and arrows, label them with verbs, and add the legend symbols
  - 26–30 Playback: one person walks through goals and relationships, and the team lists the unknowns
- **Prompts to read aloud:** "Who is involved in this work? Who is affected by it, even indirectly?" "Who can say yes? Who can say no? Who gets the blame if it fails?" "Who uses the result every day, and who supports them?" "How do these two depend on each other? How do they interact?" "Who is missing from this wall?"
- **Materials:** a blank wall or canvas, sticky notes, markers, and a legend drawn in one corner.
- **The board:** the project at the center, space around it for labeled cluster circles, solid arrows for formal dependencies and dashed lines for informal influence, each labeled with a verb, and a parking lot. The legend reads ★ decision-maker or influencer · + good relationship · − strained relationship · ? unknown. Add an empty relationships table for the digitized lines. Optionally seed the board with the stakeholder roles Claude expects, labeled Assumption.

After the session, read the photo of the wall or the Mural export and build the results page. Each line on the wall becomes a row in the relationships table, keeping its tag.

## Output
Build the page from `${CLAUDE_PLUGIN_ROOT}/shared/artifact-template.html`, following `${CLAUDE_PLUGIN_ROOT}/shared/artifacts.md`, and save it as `design-thinking/stakeholder-map-<topic>.html`. `${CLAUDE_PLUGIN_ROOT}/shared/example-empathy-map.html` shows a finished page. Add a *Sharing* item to the header's `.meta`.
- **Title:** `<Project> Stakeholder Map`, for example "Billing Migration Stakeholder Map".
- **Sections:**
  1. **Stakeholder groups:** `.cols`, one `.col` per labeled group. Each stakeholder is a `.note` giving the role or name, the title, ★ if they decide or influence, whether they're involved or impacted, and "Expects: …". Tag it by how we know the expectation: `evidence` if they said it, `simulated` if a stakeholder persona did, `assumption` otherwise. `.src` says where the stakeholder came from.
  2. **Influence and interest:** a `.plot-wrap`, with Interest on the x axis and Influence on the y axis. The zones are *Keep satisfied* (`z-tl`), *Manage closely* (`z-tr`), *Monitor* (`z-bl`) and *Keep informed* (`z-br`). Number one tagged `.dot` per key stakeholder, and list them in the `.key` with ★ and their group. Positions are the team's judgment, so they're tagged `assumption` unless a source shows them.
  3. **Relationships:** the legend in the lede, then a table of from, verb, to, formal or informal, quality and a tag pill. Show quality as a pill: `data-tone="good"` for +, `data-tone="bad"` for −, `data-tag="question"` for ?.
  4. **Unknowns:** `question` notes, each naming the engagement action that would resolve it.
  5. **Engagement plan:** a table of stakeholder, why they matter, next touchpoint (interview, Playback or update) and owner.
  6. **Simulated stakeholder sessions:** a `details.transcript` per persona. Include this only when you ran any.
  7. **Parking lot,** if anything landed there, then the **Playback.**
- **`content` in `#edt-data`:**
  ```json
  { "project": "", "boundary": "", "sharing": "team-only",
    "groups": [{ "label": "", "stakeholders": ["K1"] }],
    "stakeholders": [{ "id": "K1", "role": "", "title": "", "name": null, "persona": "SU-7", "key": true,
                       "involvement": "involved", "expects": "", "influence": 80, "interest": 40,
                       "tag": "simulated", "source": "S1" }],
    "relationships": [{ "from": "K1", "verb": "approves", "to": "K3", "formal": true, "quality": "+", "tag": "evidence", "source": "S1" }],
    "unknowns": [{ "text": "", "action": "" }],
    "engagement": [{ "stakeholder": "K1", "why": "", "touchpoint": "interview", "owner": "" }],
    "parking_lot": [""] }
  ```
  `involvement` is `involved` or `impacted`, `quality` is `+`, `-` or `?`, and `influence` and `interest` run from 0 to 100, matching the plot. Leave `name` null unless the user said the page may name people. `items` holds every note, with `group` set to the stakeholder group or `"Unknowns"`.

## Quality checks
- The map includes the people the work is *for* (end users and the people around them), not only senior names from the org chart.
- Every stakeholder has a role or title, and every group is labeled.
- Decision-makers and influencers are marked, and the approval path is visible. Influence is not assumed from seniority.
- Each relationship says *how* the two depend on or interact with each other, with a verb, not just a line.
- Key stakeholders have recorded expectations, each tagged by where it came from. Most stay `assumption` or `simulated` until someone asks the real stakeholder, and no simulated expectation is tagged `evidence`.
- Simulated stakeholders stand for roles, never for real, named people.
- Stakeholder personas have distinct incentives, and at least one is indifferent or resistant. If every persona champions the work, rerun them with more friction.
- Unknowns are listed, and each one leads to an engagement action.
- The page is fit to share: factual, respectful wording, and roles instead of names wherever the user hasn't agreed to names.
- Pitfalls:
  - Mapping only the immediate team
  - Treating "the client" as a single stakeholder
  - Drawing lines with no meaning
  - Never updating the map as people change

## Next
- `/edt-align:hopes-and-fears`: hear stakeholders' expectations directly at kickoff.
- `/edt-align:playbacks`: use the map to build the invite list and tailor the story.
- `/edt-core:sponsor-users`: recruit Sponsor Users from the user groups on the map.
- `/edt-gather:interviews`: interview key stakeholders to replace assumed and simulated expectations with evidence.
- `/edt-plan:research-plan`: decide who to research, and in what order.
- `/edt-core:workshop-planner`: plan who to bring to the next workshop.

## Source
[IBM Enterprise Design Thinking Toolkit: Stakeholder Map](https://www.ibm.com/downloads/documents/us-en/137a3e34823ed9ae)
