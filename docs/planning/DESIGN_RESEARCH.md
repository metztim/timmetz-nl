# Design Research & Discussion Notes

> Captured from initial planning session (2026-02-14). Preserves all nuance from reference site review and design discussions.

## Tim's design brief (from voice memos)

- "Famous engineers have these really minimal blogs that are sometimes purely text based"
- "Often black and white. We don't necessarily have to do black and white"
- "When they're well done, they look really good"
- Information architecture is critical — lots of content needs clear organization
- Site managed entirely by Claude Code — Tim is non-technical product manager

## Design direction evolution

### Round 1: Old-school minimal (rejected)

Initial references: gwern.net, danluu.com, patrickcollison.com, paulgraham.com, sive.rs

Tim's reaction: "I don't like any of these! These are all minimalistic but also ugly and old fashioned. I meant minimalistic and simple but in a 2026 way, not a 1990s or 2000s style kind of way. A simple, minimalistic site designed by someone with taste. E.g., these all look like how Bill Gates would design his personal minimalistic site. I want how Steve Jobs or the founders of Notion would design their personal minimalistic, simple sites."

### Round 2: Modern refined minimal

Explored: brianlovin.com, rauno.me, paco.me, leerob.com, rsms.me, macwright.com, stephango.com, carlbarenbrug.com, manuelmoreale.com, zenorocha.com, tonsky.me, linusrogge.com, kentcdodds.com

### Round 3: Tim's detailed feedback on each site

**tonsky.me** — "Actually quite like this. The blue is a bit much though I'm not against some color and the text and nav are simple and clear, but not boring. At the same time, I don't necessarily like the information architecture of this one, but overall feel is better than most others to me."
- Likes: Simple clear text, nav is simple but not boring, year-grouped content
- Dislikes: Too much blue, IA not suitable for Tim's diverse content

**stephango.com** — "I quite like this. Minimalistic but easy to understand and read and with some nice color touches. Doesn't feel 1990s even though it's simple."
- Likes: Easy to understand, nice color touches, modern feel despite simplicity

**macwright.com** — "I like this navigation and information architecture the best of all probably. Somehow a nav on the left still feels most logical (at least on desktop), and I like how the index is not overwhelming but gives space to all different types of projects and media (writing, photos, reading) without being overwhelming."
- **Winner for navigation and IA pattern**
- Key insight: left sidebar nav on desktop, diverse content types organized well

**brianlovin.com** — "This is well done too. Simple and not overwhelming while still looking modern and housing a lot of info in a non-confusing way."
- Likes: Simple, modern, lots of info without confusion

**zenorocha.com** — "Doesn't really make sense to me. Layout is a bit confusing, too much 'let's try to be different while also being minimalistic'. Do kinda like the bright color headers on black background."
- Dislikes: Confusing layout, trying too hard
- Likes: Bright mint green "Work. Hobby. Open Source." headers on dark background

**carlbarenbrug.com** — "Also too much let's try to be different (on the homepage) in terms of UX/nav. Some of the project pages are really nice though."
- Dislikes: Homepage UX/nav too experimental
- Likes: Some project pages, minimalism.com (though too dark), formfeelingfunction.com ("really cool, love the squares and the simple black and white style")

**manuelmoreale.com** — "A bit too soft and pastel. Also the site confuses me."
- Dislikes: Too soft/pastel, confusing navigation

**paco.me** — "This is a little bit again to me trying to be too different. The three column idea is kinda cool but not friendly for the visitor/reader."
- Dislikes: Three columns, not reader-friendly

**rauno.me** — "This is a bit too confusing and also too lets try to be different with the horizontal scroll, but I do like the boldness and brightness of the colors versus very dark and monotone sites."
- Dislikes: Confusing, horizontal scroll
- Likes: Bold bright colors vs dark/monotone

**kentcdodds.com** — "Looks more like a SaaS website than a personal blog."
- Reject: Too SaaS-like

**linusrogge.com** — "Looks nice but indeed too visual heavy for what I want."
- Reject: Too image-heavy

## Synthesized design principles

From all feedback, Tim's ideal site is:

1. **Simple and logical** — don't try to be different for different's sake
2. **Modern but not dated** — stephango/brianlovin quality level, not 1990s sparse
3. **Left sidebar nav on desktop** — macwright pattern, most logical for diverse content
4. **Not boring** — some color personality (tonsky, stephango, zenorocha headers)
5. **Text-heavy is fine** — when readable and well-organized
6. **Good IA** — multiple content types need clear, non-overwhelming organization
7. **Not overwhelming** — brianlovin's "housing a lot of info without confusion"
8. **Not SaaS** — personal, authentic, not corporate
9. **Not pastel/soft** — clear contrast, readable
10. **Year-grouped content** — tonsky-style for blog/writing sections

## Open questions from Tim (to address in next session)

1. **Homepage mockup review needed** — Tim wants to review a visual prototype before building the full site. Phase 0 in the plan covers this.

2. **"Writing" vs "Blog" naming** — The plan uses both terms inconsistently. Need to decide:
   - Nav item is "Writing" (broader, includes essays, columns, articles)
   - Content collection could still be called `blog/` internally (technical name)
   - Or rename everything consistently to "writing"
   - Recommendation: Nav says "Writing", URL is `/writing/`, internal collection is `writing/` too

3. **Tech stack re-evaluation** — With left sidebar layout (not centered single column), is Astro 5 + Tailwind still the right choice? Yes — the layout change doesn't affect the framework choice. Astro handles any layout. Sidebar is just CSS/HTML structure. The stack was chosen for content management (Markdown collections), build performance, and zero-JS output — all still apply.

## Project references explored

- `/Users/timmetz/Developer/Projects/SaentLifeline` — Swift macOS app, 4.8★, MVVM, feature-locked for App Store
- `/Users/timmetz/Developer/Projects/system/my-os` — Personal OS, Node/TS, Notion+Logseq integration
- `/Users/timmetz/Developer/Projects/Animalz/animalz-intelligence-os` — AI content ops, Node/TS/Express, Claude+OpenAI
- `/Users/timmetz/Developer/Projects/Personal/` — 20 subdirectories of personal projects
- `saent.com` — Current Webflow site with Lifeline landing page + ~228 blog posts

## Phase 0 outcomes (2026-02-14)

Prototype approved. Prototype file: `prototype/index.html`

**Decisions confirmed:**
- Left sidebar layout works well — proportions feel right
- Terracotta accent approved (both light #c05030 and dark #e07050)
- Inter + JetBrains Mono pairing approved
- Dark mode looks good, keep as-is
- Stars removed from writing list — cleaner without them
- Date format: zero-padded dot notation (02.10, 11.22) with year as group heading
- "Writing" used consistently (not "Blog")

**Refinements to revisit during Phase 1 build:**
1. **Writing entry title weight** — Consider bumping to font-weight 450 or 500. Currently same weight as body text, which makes them scan slightly flat in list view. A small bump would give more presence without heaviness.
2. **"→ all projects" link visibility** — Very understated in prototype. Revisit once real content is in place and actual navigation is happening. May need a nudge of visibility.
3. **Font alternatives to keep in mind** — Inter works well, but if Tim wants to experiment later, Instrument Sans or Geist would give a slightly more distinctive feel while staying in the same clean territory. Not urgent — Inter's readability and familiarity is a strength for a Claude Code-maintained site.

## Briefing source files

Voice memos transcribed at:
- `materials/briefing/Timmetz.nl part 1.txt` — Purpose, vision, tone, maintenance model
- `materials/briefing/Timmetz.nl part 2.txt` — Content structure, IA challenges, content inventory
- `materials/briefing/Timmetz.nl part 3.txt` — Domain migration, saent.com, MyOS integration, SEO
