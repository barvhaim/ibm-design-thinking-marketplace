# shipnote

A CLI that drafts release notes from merged pull requests. Release engineers run `shipnote draft v2.4.0` at the end of a sprint; it groups PRs by label, flags PRs with no description, and writes a Markdown draft that the engineer edits before publishing to GitHub Releases.

Known issues from the support channel:
- "Half our PRs have no label, so everything lands in Other." (support thread, March)
- Teams in regulated industries need a sign-off trail before notes go out.
