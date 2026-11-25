# Simulated users

These skills don't wait for research access. When an activity needs users, Claude simulates them: it builds a panel of distinct personas, keeps them consistent across activities, and role-plays them in interviews, observations, walkthroughs and feedback sessions. Simulation is fast and lets the team rehearse. But a simulated user is Claude's model of a person, not the person. It can only reflect what Claude already knows about people like them, so every simulated item stays labeled `simulated` all the way through the Loop.

## The panel

The panel lives at `design-thinking/simulated-users.html`. Every activity reuses it, so the same people show up from the first interview to the last test.

1. **Check for a panel.** If `design-thinking/simulated-users.html` exists, read its `#edt-data` and use those personas. If it covers the wrong users, add personas to it rather than starting a separate panel.
2. **Ground it.** Before inventing anything, collect what is real:
   - the product and domain, from the README, docs, PRD and the code's user-facing parts
   - any real research the user provides
   - the target roles the user names

   Ask the user one short question if the target users are unclear. Otherwise proceed.
3. **Build 3 to 5 personas per target role.** Make them meaningfully different, not variations of one person. Spread them across:
   - experience: a novice and an expert
   - context: team size, constraints, tools, environment
   - attitude: a champion, a pragmatist, and at least one skeptic or non-adopter
   - at least one edge case: accessibility needs, a non-native language, low bandwidth, an unusual workflow, regulation

   For each persona, record:
   - `id` (`SU-1`, `SU-2` and so on)
   - an obviously fictional name
   - role and context
   - goals and pains
   - tools and habits
   - how they talk: vocabulary, patience, directness
   - what they'd never say
   - `grounded_in`: which traits come from real sources (cite `S…`) and which are invented
4. **Voice check.** Write two short in-character answers per persona: "Walk me through the last time you did <core task>" and "What would make you stop using a tool like this?" If two personas sound alike, rewrite one.
5. **Save the panel** as `design-thinking/simulated-users.html`, an HTML artifact following [artifacts.md](artifacts.md). The `/edt-core:simulated-users` skill defines the full page; when you build the panel from another skill, include at least:
   - **Title:** "<Product> Simulated Users"
   - **Board:** one `.persona` card per person, under the simulated banner
   - **Coverage:** a table of each persona against experience, context, attitude and edge case
   - **Voice check:** the answers as `.note[data-tag="simulated"]`
   - **Data:** `content.personas` holds the full records
   - **Publish:** publish it like any other artifact

## Role-playing a simulated user

- **One persona at a time.** Run each session separately, in the first person, staying in character. Don't blend personas.
- **Be a realistic person, not a helpful assistant.**
  - Know only what the persona would know.
  - Use their words, not product vocabulary.
  - Wander, forget, contradict yourself a little, and describe what you actually did last time rather than what you'd ideally do.
  - Get irritated where they would. Say "I don't know" when they wouldn't know.
- **Don't flatter the team's idea.** Skeptics push back. Pragmatists ask what it costs them. Most people are indifferent to most features. If every simulated user loves a concept, the simulation is broken, so run it again with more friction.
- **Keep the interviewer honest.** Ask open questions about real past behavior. Never lead the persona to the answer you want.
- **Record everything.** Each session goes into the artifact as a `.transcript` with `turn sim` lines. Every insight drawn from it is a `data-tag="simulated"` note whose `src` is the persona ID.

## Mixing real and simulated

- **Real data comes first.** If the user gives you real research, use it and tag it `evidence`. Use simulated users only to fill gaps, to rehearse an interview guide, or to stress-test an idea. Show both side by side, never merged into one note.
- **Simulated items never change tag.** A simulated insight never becomes `evidence` because it sounds plausible or because several personas repeated it. It becomes evidence only when a real person confirms it, and then it gets a new note with the real source.
- **Make the balance visible.** Every Playback's "Validate next" list names the simulated claims the team is leaning on most, and suggests how to check each one with a real user. For recruiting real users, see `/edt-core:sponsor-users`.

## Limits

Say these plainly when they matter:
- Simulation finds the needs Claude can already imagine. It is weak at genuine surprises, tacit workarounds, and how a specific organization works.
- Personas drift toward stereotypes. Check the panel for clichés and fix them.
- Numbers from a simulated panel, such as "4 of 5 preferred A", are not statistics. Report them as counts of simulated users, never as percentages of users.
