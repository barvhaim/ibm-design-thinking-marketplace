#!/usr/bin/env python3
"""Build the GitHub Pages site from the marketplace's skills.

Every page is generated from the SKILL.md files, the shared guides and the examples,
so the site can't drift from what the plugins install.

    pip install markdown-it-py==3.0.0
    python3 scripts/build-site.py              # writes _site/
    python3 -m http.server -d _site 8000       # preview at http://localhost:8000
"""
import html
import json
import os
import re
import shutil
import sys
from pathlib import Path

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "_site"
REPO = "https://github.com/barvhaim/ibm-design-thinking-marketplace"
BLOB = REPO + "/blob/master/"
REPO_SLUG = REPO.split("github.com/")[1]
MARKETPLACE = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
MKT = MARKETPLACE["name"]
FONTS = ("https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500"
         "&family=IBM+Plex+Sans+Condensed:wght@500;600&family=IBM+Plex+Sans:wght@300;400;600&display=swap")
PHASES = ("observe", "reflect", "make")
TAGS = {"evidence": "Evidence", "simulated": "Simulated", "assumption": "Assumption", "question": "Question"}
# Shown in the "Guides" group of the side navigation, in this order.
GUIDES = [
    ("plugins/edt-core/skills/guide/framework.md", "skills/edt-core/guide/framework.html", "The framework"),
    ("plugins/edt-core/skills/guide/activities.md", "skills/edt-core/guide/activities.html", "Activity catalog"),
    ("shared/simulated-users.md", "guides/simulated-users.html", "Simulated users protocol"),
    ("shared/artifacts.md", "guides/artifacts.html", "HTML artifact format"),
]

md = MarkdownIt("commonmark", {"html": False}).enable("table")


def esc(text):
    return html.escape(text, quote=True)


def rel(target, current):
    """URL of site path `target` relative to the page at site path `current`."""
    url = os.path.relpath(target, os.path.dirname(current) or ".")
    if url == "index.html" or url.endswith("/index.html"):
        url = url[: -len("index.html")] or "./"
    return url


# ---------------------------------------------------------------- load the marketplace

def readme_table():
    """Plugin labels and skill order, from the Plugins table in README.md."""
    labels, order = {}, {}
    for line in (ROOT / "README.md").read_text().splitlines():
        m = re.match(r"\| \*\*(edt-[a-z]+)\*\*: ([^|]+?) \| (.+) \|$", line)
        if m:
            name, label, skills = m.groups()
            labels[name] = label[0].upper() + label[1:]
            order[name] = re.findall(r"`([a-z-]+)`", skills)
    return labels, order


def split_description(desc):
    """(what it does, when to use it). Descriptions end with a 'Use when…' sentence."""
    parts = re.split(r"(?<=[.!?]) (?=Use\b)", desc, maxsplit=1)
    return parts[0], (parts[1] if len(parts) > 1 else "")


def card_summary(lede):
    text = re.sub(r",? (?:as|on|inside|in) an HTML artifact(?=[.,:])", "", lede)
    sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z])", text)
    return " ".join(sentences[:2])


def parse_skill(plugin, folder):
    text = (folder / "SKILL.md").read_text()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    front = {}
    for line in m.group(1).splitlines():
        key, _, value = line.partition(":")
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] == '"':
            value = value[1:-1]
        front[key.strip()] = value
    body = text[m.end():]
    h1 = re.search(r"^# (.+)\n", body, re.M)
    title = h1.group(1).strip()
    body = body[: h1.start()] + body[h1.end():]
    meta = re.search(r"^> (IBM Enterprise Design Thinking .+)\n", body, re.M)
    parts = []
    if meta:
        parts = [p.strip() for p in meta.group(1).split("·")]
        body = body[: meta.start()] + body[meta.end():]
    loop = parts[2] if len(parts) > 2 else ""
    phases = list(PHASES) if "all loop" in loop.lower() else [p for p in PHASES if p in loop.lower()]
    lede, when = split_description(front["description"])
    name = front["name"]
    return {
        "plugin": plugin, "name": name, "title": title, "hint": front.get("argument-hint", ""),
        "lede": lede, "when": when, "summary": card_summary(lede),
        "category": parts[1] if len(parts) > 1 else "", "loop": loop,
        "duration": parts[3] if len(parts) > 3 else "", "phases": phases,
        "body": body, "src": folder / "SKILL.md",
        "extras": sorted(f for f in folder.glob("*.md") if f.name != "SKILL.md"),
        "url": f"skills/{plugin}/{name}/index.html", "cmd": f"/{plugin}:{name}",
    }


def load():
    labels, order = readme_table()
    plugins = []
    for entry in MARKETPLACE["plugins"]:
        name = entry["name"]
        folder = (ROOT / entry["source"]).resolve()
        icon = (ROOT / "assets" / "icons" / f"{name}.svg").read_text()
        ranked = order.get(name, [])
        dirs = sorted((d for d in (folder / "skills").iterdir() if (d / "SKILL.md").exists()),
                      key=lambda d: (ranked.index(d.name) if d.name in ranked else 999, d.name))
        plugins.append({
            "name": name, "label": labels.get(name, name), "description": entry["description"],
            "color": re.search(r'fill="(#[0-9a-fA-F]{6})"', icon).group(1),
            "skills": [parse_skill(name, d) for d in dirs],
        })
    return plugins


PLUGINS = load()
SKILLS = {(s["plugin"], s["name"]): s for p in PLUGINS for s in p["skills"]}
ORDERED = [s for p in PLUGINS for s in p["skills"]]
PLUGIN_BY_NAME = {p["name"]: p for p in PLUGINS}

# Repo Markdown file -> site page, so relative links between them keep working.
PAGE_MAP = {s["src"].resolve(): s["url"] for s in ORDERED}
for s in ORDERED:
    for extra in s["extras"]:
        PAGE_MAP[extra.resolve()] = f"skills/{s['plugin']}/{s['name']}/{extra.stem}.html"
for src, url, _ in GUIDES:
    PAGE_MAP[(ROOT / src).resolve()] = url


# ---------------------------------------------------------------- Markdown

def rewrite_href(href, src, current):
    if not href or href.startswith("#") or re.match(r"^[a-z][a-z0-9+.-]*:", href):
        return href
    path, _, frag = href.partition("#")
    frag = "#" + frag if frag else ""
    target = (src.parent / path).resolve()
    if target in PAGE_MAP:
        return rel(PAGE_MAP[target], current) + frag
    try:
        return BLOB + target.relative_to(ROOT).as_posix() + frag
    except ValueError:
        return href


def render_md(text, src, current):
    """Render Markdown to HTML. Returns (html, [(id, h2 text)])."""
    tokens = md.parse(text)
    seen, toc = {}, []
    for i, token in enumerate(tokens):
        if token.type == "heading_open":
            plain = re.sub(r"[`*_]", "", tokens[i + 1].content)
            slug = re.sub(r"[^a-z0-9]+", "-", plain.lower()).strip("-") or "section"
            count = seen.get(slug, 0)
            seen[slug] = count + 1
            slug = f"{slug}-{count}" if count else slug
            token.attrSet("id", slug)
            if token.tag == "h2":
                toc.append((slug, plain))
        for child in token.children or []:
            if child.type == "link_open":
                child.attrSet("href", rewrite_href(child.attrGet("href"), src, current))
    out = md.renderer.render(tokens, md.options, {})
    out = out.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")

    def link_command(m):
        skill = SKILLS.get((m.group(1), m.group(2)))
        if not skill:
            return m.group(0)
        return f'<a class="cmd-link" href="{rel(skill["url"], current)}">{m.group(0)}</a>'

    out = re.sub(r"(?<!<pre>)<code>/(edt-[a-z]+):([a-z-]+)[^<]*</code>", link_command, out)

    def link_shared(m):
        target = (ROOT / "shared" / m.group(1)).resolve()
        href = rel(PAGE_MAP[target], current) if target in PAGE_MAP else BLOB + "shared/" + m.group(1)
        return f'<a href="{href}">{m.group(0)}</a>'

    out = re.sub(r"<code>\$\{CLAUDE_PLUGIN_ROOT\}/shared/([a-z-]+\.(?:md|html))</code>", link_shared, out)
    return out, toc


# ---------------------------------------------------------------- page parts

def copy_line(label, command, shown=None):
    k = f'<span class="run-k">{esc(label)}</span>' if label else ""
    return (f'<div class="run">{k}<code>{shown if shown is not None else esc(command)}</code>'
            f'<button class="copy" type="button" data-copy="{esc(command)}">Copy</button></div>')


def shell(current, title, description, main, nav=""):
    r = lambda target: rel(target, current)  # noqa: E731
    links = [("index.html#skills", "Skills"), ("guides/simulated-users.html", "Simulated users"),
             ("guides/artifacts.html", "HTML artifacts"), ("index.html#example", "Example")]
    here = ' aria-current="page"'
    top = "".join(f'<a href="{r(href)}"{here if href == current else ""}>{label}</a>' for href, label in links)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="icon" href="{r('icons/edt-core.svg')}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{r('style.css')}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap top-in">
  <a class="brand" href="{r('index.html')}"><img src="{r('icons/edt-core.svg')}" alt="" width="28" height="28"><span>EDT skills <small>for Claude Code</small></span></a>
  <nav class="top-nav" aria-label="Site">{top}<a href="{REPO}">GitHub</a></nav>
</div></header>
{main}
<footer class="foot"><div class="wrap foot-in">
  <p>Enterprise Design Thinking, its framework and its toolkit are © IBM Corporation. These skills paraphrase IBM's public materials and link to the original toolkit decks. The skill files are licensed under <a href="{BLOB}LICENSE">Apache-2.0</a>, which doesn't cover IBM's materials.</p>
  <p>Generated from the skills in <a href="{REPO}">{REPO_SLUG}</a>.</p>
</div></footer>
<script src="{r('site.js')}"></script>
</body>
</html>
"""


def side_nav(current):
    def item(url, label):
        here = ' aria-current="page"' if url == current else ""
        return f'<li><a href="{rel(url, current)}"{here}>{esc(label)}</a></li>'

    groups = ['<div class="nav-g"><p>Guides</p><ul>'
              + "".join(item(url, label) for _, url, label in GUIDES) + "</ul></div>"]
    for p in PLUGINS:
        icon = f'<img src="{rel("icons/" + p["name"] + ".svg", current)}" alt="" width="16" height="16">'
        groups.append(f'<div class="nav-g"><p>{icon}{esc(p["label"])}</p><ul>'
                      + "".join(item(s["url"], s["title"]) for s in p["skills"]) + "</ul></div>")
    inner = "".join(groups)
    return (f'<details class="nav-mobile"><summary>All {len(ORDERED)} skills and guides</summary><div>{inner}</div></details>'
            f'<nav class="side" aria-label="Skills">{inner}</nav>')


def toc_html(toc):
    if len(toc) < 3:
        return ""
    links = "".join(f'<a href="#{slug}">{esc(text)}</a>' for slug, text in toc)
    return f'<nav class="toc" aria-label="On this page"><b>On this page</b>{links}</nav>'


def doc_page(current, title, description, header, body, footer="", color=None):
    style = f' style="--p:{color}"' if color else ""
    main = (f'<div class="wrap doc">{side_nav(current)}'
            f'<main id="main" class="article"{style}>{header}<div class="prose">{body}</div>{footer}</main></div>')
    return shell(current, title, description, main)


# ---------------------------------------------------------------- pages

def skill_page(s):
    current = s["url"]
    p = PLUGIN_BY_NAME[s["plugin"]]
    body, toc = render_md(s["body"], s["src"], current)
    facts = [f for f in (s["loop"], s["duration"]) if f]
    hint = f' <span class="hint">{esc(s["hint"])}</span>' if s["hint"] else ""
    when = f'<p class="when"><b>When Claude uses it</b>{esc(s["when"])}</p>' if s["when"] else ""
    header = f"""<nav class="crumbs" aria-label="Breadcrumb"><a href="{rel('index.html', current)}#skills">All skills</a><span>/</span><a href="{rel('index.html', current)}#{p['name']}">{esc(p['label'])}</a></nav>
<header class="article-h">
  <p class="eyebrow"><img src="{rel("icons/" + p["name"] + ".svg", current)}" alt="" width="20" height="20">{esc(p['name'])} · {esc(s['category'])}</p>
  <h1>{esc(s['title'])}</h1>
  <p class="lede">{esc(s['lede'])}</p>
  {when}
  <div class="runbox">{copy_line("Run", s["cmd"], esc(s["cmd"]) + hint)}{copy_line("Install", f"claude plugin install {p['name']}@{MKT}")}</div>
  <ul class="facts">{"".join(f"<li>{esc(f)}</li>" for f in facts)}</ul>
  {toc_html(toc)}
</header>"""
    more = ""
    if s["extras"]:
        items = "".join(
            f'<li><a href="{rel(PAGE_MAP[e.resolve()], current)}">{esc(md_title(e))}</a></li>' for e in s["extras"])
        more = f'<section class="more"><h2>More for this skill</h2><ul>{items}</ul></section>'
    i = ORDERED.index(s)
    pager = ""
    if i > 0:
        prev = ORDERED[i - 1]
        pager += f'<a class="prev" href="{rel(prev["url"], current)}"><small>Previous</small>{esc(prev["title"])}</a>'
    if i < len(ORDERED) - 1:
        nxt = ORDERED[i + 1]
        pager += f'<a class="next" href="{rel(nxt["url"], current)}"><small>Next</small>{esc(nxt["title"])}</a>'
    src = s["src"].relative_to(ROOT).as_posix()
    footer = (f'{more}<p class="src"><a href="{BLOB}{src}">View SKILL.md on GitHub</a></p>'
              f'<nav class="pager" aria-label="More skills">{pager}</nav>')
    return doc_page(current, f"{s['title']} · EDT skills", s["lede"], header, body, footer, p["color"])


def md_title(path):
    m = re.search(r"^# (.+)$", path.read_text(), re.M)
    return m.group(1).strip() if m else path.stem.replace("-", " ").capitalize()


def markdown_page(src, current, crumb_url, crumb_label, color=None):
    text = src.read_text()
    title = md_title(src)
    text = re.sub(r"^# .+\n", "", text, count=1, flags=re.M)
    body, toc = render_md(text, src, current)
    header = f"""<nav class="crumbs" aria-label="Breadcrumb"><a href="{rel(crumb_url, current)}">{esc(crumb_label)}</a></nav>
<header class="article-h"><h1>{esc(title)}</h1>{toc_html(toc)}
  <p class="src"><a href="{BLOB}{src.relative_to(ROOT).as_posix()}">View source on GitHub</a></p></header>"""
    return doc_page(current, f"{title} · EDT skills", title, header, body, color=color)


def example_notes():
    """One note per provenance tag, taken from the example empathy map's data block."""
    page = ROOT / "examples" / "shipnote" / "design-thinking" / "empathy-map-release-engineer.html"
    if not page.exists():
        return ""
    m = re.search(r'id="edt-data">(.*?)</script>', page.read_text(), re.S)
    items = json.loads(m.group(1)).get("items", []) if m else []
    picked = []
    for tag in TAGS:
        found = next((i for i in items if i.get("tag") == tag), None)
        if found:
            picked.append(found)
    notes = "".join(
        f'<div class="note" data-tag="{esc(i["tag"])}"><span class="note-k">{TAGS[i["tag"]]}</span>'
        f'<span>{esc(i["text"])}</span><span class="note-s">{esc(i["id"])} · {esc(str(i.get("source", "")))}</span></div>'
        for i in picked)
    return f"""<figure class="wall" aria-label="Sticky notes from the example empathy map">
  <div class="wall-notes">{notes}</div>
  <figcaption class="wall-cap">Four notes from the <a href="examples/shipnote/empathy-map-release-engineer.html">example empathy map</a>. Every note says where it came from: a real source (<code>S…</code>), a simulated user (<code>SU-…</code>), or the team.</figcaption>
</figure>"""


def index_page():
    current = "index.html"
    total = len(ORDERED)
    counts = {ph: sum(ph in s["phases"] for s in ORDERED) for ph in PHASES}
    filters = (f'<button type="button" data-phase="all" aria-pressed="true">All<span class="n">{total}</span></button>'
               + "".join(f'<button type="button" data-phase="{ph}" aria-pressed="false">{ph.capitalize()}'
                         f'<span class="n">{counts[ph]}</span></button>' for ph in PHASES))
    groups = []
    for p in PLUGINS:
        cards = "".join(
            f'<a class="card" href="{rel(s["url"], current)}" data-phases="{" ".join(s["phases"])}">'
            f'<span class="card-cmd">{esc(s["cmd"])}</span><strong class="card-t">{esc(s["title"])}</strong>'
            f'<span class="card-d">{esc(s["summary"])}</span>'
            f'<span class="card-m">{esc(" · ".join(f for f in (s["loop"], s["duration"]) if f))}</span></a>'
            for s in p["skills"])
        n = len(p["skills"])
        groups.append(f"""<section class="plugin" id="{p['name']}" style="--p:{p['color']}">
  <div class="plugin-head">
    <img class="picon" src="icons/{p['name']}.svg" alt="" width="44" height="44">
    <div class="plugin-t"><h3>{esc(p['label'])}</h3><p><code>{p['name']}</code> · {n} skill{'s' if n != 1 else ''}</p></div>
    {copy_line("", f"claude plugin install {p['name']}@{MKT}")}
  </div>
  <div class="cards">{cards}</div>
</section>""")

    def chain(*names):
        links = []
        for ref in names:
            plugin, skill = ref.split(":")
            s = SKILLS[(plugin, skill)]
            links.append(f'<a href="{rel(s["url"], current)}">{esc(s["cmd"])}</a>')
        return '<span class="chain">' + "<span>→</span>".join(links) + "</span>"

    paths = [
        ("Start without users", chain("edt-core:simulated-users", "edt-gather:interviews", "edt-synthesize:empathy-map")),
        ("From research to intent", chain("edt-synthesize:empathy-map", "edt-synthesize:as-is-scenario-map",
                                          "edt-synthesize:needs-statements", "edt-plan:hills", "edt-align:playbacks")),
        ("From intent to concept", chain("edt-ideate:big-idea-vignettes", "edt-plan:prioritization-grid",
                                         "edt-ideate:to-be-scenario-map", "edt-ideate:storyboards")),
        ("Test", chain("edt-test:paper-prototypes", "edt-test:cognitive-walkthrough", "edt-test:feedback-grid")),
        ("Delivery", chain("edt-plan:experience-based-roadmap", "edt-plan:user-stories")),
        ("Define an AI strategy", chain("edt-ai:intent", "edt-ai:data", "edt-ai:understanding",
                                        "edt-ai:reasoning", "edt-ai:knowledge")),
    ]
    path_items = "".join(f"<li><strong>{esc(t)}</strong>{c}</li>" for t, c in paths)
    install = (f"claude plugin marketplace add {REPO_SLUG}\n"
               f"claude plugin install edt-core@{MKT}")
    install_all = ("for p in " + " ".join(p["name"][len("edt-"):] for p in PLUGINS)
                   + f'; do claude plugin install "edt-$p@{MKT}"; done')
    tag_swatches = "".join(f'<span><i class="swatch" data-tag="{t}"></i>{label}</span>' for t, label in TAGS.items())
    guide = SKILLS[("edt-core", "guide")]
    sim = SKILLS[("edt-core", "simulated-users")]
    em = SKILLS[("edt-synthesize", "empathy-map")]
    shots = ""
    if (ROOT / "assets" / "screenshots" / "empathy-map-light.png").exists():
        shots = ('<a class="shot" href="examples/shipnote/empathy-map-release-engineer.html"><picture>'
                 '<source srcset="img/empathy-map-dark.png" media="(prefers-color-scheme: dark)">'
                 '<img src="img/empathy-map-light.png" alt="The generated empathy map: a header with the date, mode, '
                 'sources and a simulated-users banner, a tag filter, and the Says, Thinks, Does and Feels quadrants '
                 'filled with color-coded sticky notes" width="1200" height="1300" loading="lazy"></picture></a>')
    main = f"""<main id="main">
<section class="hero"><div class="wrap hero-in">
  <div>
    <p class="eyebrow">Claude Code plugin marketplace</p>
    <h1>IBM Enterprise Design Thinking skills for Claude Code</h1>
    <p class="lede">{total} skills in {len(PLUGINS)} plugins cover the framework and all 29 toolkit activities, from empathy maps to Hills and playbacks. Claude runs each activity with you, simulates users when you don't have any yet, and saves the result as an HTML page that the next activity builds on.</p>
    {copy_line("", install)}
    <p class="hero-links"><a href="#skills">Browse the skills</a><a href="#example">See an example page</a><a href="{REPO}">Source on GitHub</a></p>
  </div>
  {example_notes()}
</div></section>

<section class="sec" id="how"><div class="wrap">
  <div class="sec-h"><h2>How it works</h2></div>
  <div class="how">
    <div class="how-i"><h3>Simulated users</h3>
      <p>You don't need research access to start. When an activity needs users, Claude builds a panel of distinct personas with <a class="cmd-link" href="{rel(sim['url'], current)}"><code>{sim['cmd']}</code></a>, skeptics and edge cases included, and interviews, observes and tests with them in character.</p>
      <p>Real research always comes first, and simulated input never counts as evidence. <a href="guides/simulated-users.html">Read the protocol</a>.</p></div>
    <div class="how-i"><h3>HTML artifacts</h3>
      <p>Every activity saves a page in <code>design-thinking/</code>, laid out like a workshop wall, and publishes it as an artifact when your session supports it. Each sticky note is tagged by where it came from:</p>
      <p class="tags">{tag_swatches}</p>
      <p>A JSON block in each page feeds the next activity. <a href="guides/artifacts.html">See the format</a>.</p></div>
    <div class="how-i"><h3>Co-create or facilitate</h3>
      <p><b>Co-create</b>, the default: Claude runs the activity with you in the session.</p>
      <p><b>Facilitate</b>: add <code>facilitate</code> to the command and Claude prepares a kit page for a live team session, with an agenda, prompts to read aloud and an empty board. Afterwards, Claude turns photos of the wall into the results page.</p></div>
  </div>
</div></section>

<section class="sec" id="skills"><div class="wrap">
  <div class="sec-h"><h2>Skills</h2>
    <p>Run a skill as <code>/&lt;plugin&gt;:&lt;skill&gt;</code>, or describe what you need and Claude picks the right one. Each page below covers what the skill does, its steps, the live-session kit, the page it produces and its quality checks.</p></div>
  <div class="filter" role="group" aria-label="Filter by Loop phase"><span class="filter-k">Loop phase</span>{filters}</div>
  <div class="plugins">{"".join(groups)}</div>
  <div class="sec-h" style="margin:2.5rem 0 0"><p>Install every plugin at once:</p>{copy_line("", install_all)}</div>
</div></section>

<section class="sec" id="example"><div class="wrap">
  <div class="sec-h"><h2>Example output</h2>
    <p><b>shipnote</b> is a fictional CLI whose repo has nothing but a README. One command produced both pages below, unedited: <code>{em['cmd']} release engineer using shipnote</code>.</p></div>
  <div class="example">
    <ol>
      <li><a href="examples/shipnote/empathy-map-release-engineer.html">Release engineer empathy map</a><span>39 tagged notes, 5 tensions, three simulated interview transcripts and a playback. Only 2 notes come from real sources, and the page says so.</span></li>
      <li><a href="examples/shipnote/simulated-users.html">Simulated users panel</a><span>Four personas the map drew on, with coverage, a voice check and the gaps in their grounding.</span></li>
      <li><a href="{BLOB}examples/shipnote/README.md">The input README</a><span>Everything Claude knew about shipnote.</span></li>
    </ol>
    {shots}
  </div>
</div></section>

<section class="sec" id="start"><div class="wrap">
  <div class="sec-h"><h2>Where to start</h2>
    <p>Not sure? Ask the guide: <a class="cmd-link" href="{rel(guide['url'], current)}"><code>{guide['cmd']}</code></a> reads your <code>design-thinking/</code> pages, works out where you are in the Loop, and recommends the next one to three activities. Common paths:</p></div>
  <ul class="paths">{path_items}</ul>
</div></section>
</main>"""
    return shell(current, "IBM Enterprise Design Thinking skills for Claude Code",
                 f"{total} Claude Code skills for IBM Enterprise Design Thinking that run with simulated users and produce HTML artifacts.",
                 main)


SKELETON = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px system-ui,-apple-system,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
"""


# ---------------------------------------------------------------- build

def write(path, text):
    target = OUT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text)


def main():
    if OUT == ROOT or OUT in ROOT.parents:
        sys.exit(f"refusing to replace {OUT}")
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    write("index.html", index_page())
    for s in ORDERED:
        write(s["url"], skill_page(s))
        for extra in s["extras"]:
            if extra.resolve() in {(ROOT / g[0]).resolve() for g in GUIDES}:
                continue
            write(PAGE_MAP[extra.resolve()],
                  markdown_page(extra, PAGE_MAP[extra.resolve()], s["url"], s["title"], PLUGIN_BY_NAME[s["plugin"]]["color"]))
    for src, url, _ in GUIDES:
        write(url, markdown_page(ROOT / src, url, "index.html#how", "How it works"))

    # Example pages are artifact bodies; give them the document skeleton the Artifact host adds.
    for page in sorted((ROOT / "examples").glob("*/design-thinking/*.html")):
        write(f"examples/{page.parent.parent.name}/{page.name}", SKELETON + page.read_text() + "\n</body>\n</html>\n")

    for name in ("style.css", "site.js"):
        shutil.copy(ROOT / "site" / name, OUT / name)
    (OUT / "icons").mkdir()
    for icon in (ROOT / "assets" / "icons").glob("*.svg"):
        shutil.copy(icon, OUT / "icons" / icon.name)
    shots = ROOT / "assets" / "screenshots"
    if shots.exists():
        (OUT / "img").mkdir()
        for img in shots.glob("*.png"):
            shutil.copy(img, OUT / "img" / img.name)
    (OUT / ".nojekyll").write_text("")
    pages = sum(1 for _ in OUT.rglob("*.html"))
    print(f"built {pages} pages ({len(ORDERED)} skills) in {OUT}")


if __name__ == "__main__":
    main()
