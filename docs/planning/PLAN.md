# timmetz.nl — Implementation Plan

> **Important:** On implementation start, copy this plan and appendices into `timmetz-nl/docs/planning/` and keep them up to date there as the source of truth.

## Context

Tim wants a personal website that serves as a hub for his non-linear career: projects, writing, work history, interviews, and media — all in one place. The site should feel like a well-organized personal archive, not a startup landing page. Claude Code is the sole builder and maintainer (no CMS). Tim acts as product manager.

The site also needs to absorb saent.com content (blog + Lifeline landing page), consolidate scattered writing and media, and be optimized for SEO and LLM discoverability.

### Site purposes (from briefing)
1. **Legacy artifact** — for Tim's children and family, capturing the full picture of his trajectory
2. **Professional hub** — consolidating scattered work across platforms into one place
3. **SEO/LLM discoverability** — a canonical home that search engines and AI systems can index
4. **Content repository** — collecting years of writing, interviews, videos, projects

### Key decisions made
- Lifeline integrates as a project page at `/projects/lifeline` (not a custom landing page)
- Full architecture planned first, MVP scope decided together
- Claude Code maintains everything — no CMS, no external editing tools
- Left sidebar nav on desktop (macwright-style)
- Simple, logical UX — no "trying to be different"

---

## 1. Information Architecture

### Navigation (left sidebar on desktop)

```
Desktop:                          Mobile:
┌──────────┬────────────────┐    ┌────────────────────┐
│ Tim Metz │                │    │ Tim Metz            │
│          │  Content       │    │ Projects Writing About│
│ Projects │  area          │    │                     │
│ Writing  │                │    │ Content area        │
│ About    │                │    │                     │
│          │                │    └────────────────────┘
│ ───      │                │
│ GitHub   │                │
│ LinkedIn │                │
│ RSS      │                │
└──────────┴────────────────┘
```

Three nav items. Everything else reachable from these hubs or homepage.

- **Projects** — Active projects, archived projects, contributions. Grouped by status.
- **Writing** — Blog posts, migrated saent.com articles, Africa columns, guest writing. Filterable by category.
- **About** — Bio, work history (CV view), media/press index, social links, /now section.

**Why left sidebar (Tim's feedback):** "Somehow a nav on the left still feels most logical (at least on desktop), and I like how the index is not overwhelming but gives space to all different types of projects and media without being overwhelming." (ref: macwright.com)

### Content model

Every content item is a Markdown file with typed frontmatter. Cross-references via slug strings. One source of truth per item, multiple views generated at build time.

**Collections:**
- `projects/` — title, description, status (active/on-ice/archived/completed), role, startDate, endDate, url, repo, tags, featured, sortOrder, relatedWork
- `blog/` — title, description, pubDate, updatedDate, category (productivity/ai/agile/startup/africa/general), tags, draft, originalUrl, originalSource
- `work/` — title, company, description, startDate, endDate, location, highlights, relatedProjects, relatedMedia
- `media/` — title, type (interview/podcast/video/article/press), date, url, publication, description, embedUrl

### Homepage

Hub page. Brief intro + concise sections for each content type:

```
[Brief intro — 2-3 sentences]

Projects
  Lifeline          macOS focus timer
  We Eat Robots     AI newsletter
  Claude Carbon     VS Code theme
  → all projects

Writing
  [3-4 recent posts with dates]
  → all writing

Work
  Animalz — AI Infrastructure (2023–)
  SAENT — Founder (2015–2022)
  → full history
```

### URL structure

```
/                           Homepage
/projects                   Project index (grouped by status)
/projects/lifeline          Individual project
/writing                    Writing index (filterable by category)
/writing/pomodoro-technique Individual post
/about                      Bio, work history, media, social, /now
```

### Content hierarchy

| Tier | What | Where |
|---|---|---|
| 1 (prominent) | Current focus, featured projects, recent writing | Homepage |
| 2 (one click) | All active projects, all writing, about/bio | Nav sections |
| 3 (two clicks) | Individual project/post detail pages, archived items | Within sections |
| 4 (ambient) | Social links, personal interests, specific press items | About page, sidebar |

### Cross-referencing

- **Parent-child:** project page shows its parent work entry; work entry lists its child projects
- **Related items:** articles reference projects and vice versa via `related` fields
- **Tag overlap:** items sharing tags appear in each other's "Related" sections
- **In-body links:** natural Markdown links within content for editorial connections

### Content inventory (known items to populate)

**Active projects:** Lifeline, Claude Carbon, ClaudeQuote, My-OS, We Eat Robots, Animalz Intelligence OS (link to separate site)

**On-ice/archived:** Little Lumi, Stock Scanner, SEO Traffic Calculator, Revive (contribution)

**Work history:** Animalz (AI infrastructure), Animalz (content marketing/marketing), KOS (awards, press), Africa documentary, others TBD via research

**Writing categories:** Productivity (saent.com blog), AI/tech (We Eat Robots, Animalz), Agile (~2 years), Africa columns (offline), guest writing (Parable, others)

**Media:** Interviews, KOS press coverage, other appearances — TBD via deep research

---

## 2. Tech Stack

### Framework: Astro 5

- Zero JavaScript shipped by default (perfect for text-heavy site)
- Content Collections with Zod schemas — type-safe Markdown with frontmatter
- Content Layer API with `glob()` loader for multiple content types
- Native Markdown/MDX support
- Fast builds, static HTML output
- Claude Code friendly: adding content = creating a `.md` file
- Version: pin to `astro@5.17.x` (latest stable)

### Styling: Tailwind CSS 4 + @tailwindcss/typography

- `prose` classes handle all Markdown rendering
- Dark mode with `class` strategy (toggleable)
- Utility classes self-documenting for Claude Code maintenance

### Hosting: Cloudflare Pages

- Unlimited bandwidth (free tier)
- Global edge network
- Built-in `_redirects` file
- Git-based deploys (push to main = deploy)
- Cloudflare DNS for saent.com bulk redirects

### OG images: satori + sharp at build time

- Generated from content metadata
- Matches the site aesthetic

---

## 3. Design Direction

### Design feedback summary (from reference review)

Tim reviewed ~15 reference sites. Key findings:

**Top references:**
- **macwright.com** — Best IA and nav. Left sidebar on desktop. Multiple content types without overwhelm. **Winner for navigation pattern.**
- **stephango.com** — Simple but not boring. Easy to read. Nice color touches. Modern despite simplicity.
- **brianlovin.com** — Simple, not overwhelming, modern. Houses lots of info without confusion.
- **tonsky.me** — Clear text, simple nav, not boring. Year-grouped content. (Blue too much, IA not ideal.)

**Specific elements Tim liked:**
- zenorocha's bright color headers on dark background
- formfeelingfunction.com's grid squares and simple B&W style
- macwright's left sidebar organizing diverse content types
- tonsky's clean year-grouped blog lists with star highlights
- stephango's color touches that prevent feeling dated

**Rejects:**
- "Trying to be different while being minimalistic" (paco, rauno, carlbarenbrug HP)
- SaaS-feeling sites (kentcdodds)
- Confusing layouts (zenorocha overall, manuelmoreale)
- Too soft/pastel
- Horizontal scrolling, three-column experiments

### Philosophy

**Simple, logical, don't-try-to-be-different.** The site should feel immediately understandable. Navigation obvious. Content easy to find.

**Modern through quality, not novelty.** Clean typography, some color personality, well-organized content. The macwright/stephango sweet spot.

**Not boring, not flashy.** The tonsky/stephango balance — enough design care to feel modern, no gimmicks.

### Layout: Left sidebar (macwright-style)

**Desktop (≥768px):**
- Left sidebar: ~200px, fixed/sticky. Name at top, nav items below, social links at bottom.
- Content area: fills remaining space, max ~640px for prose, left-aligned (not centered).
- No background color difference in sidebar — just positioned left.

**Mobile (<768px):**
- Top horizontal nav: `Tim Metz` + `Projects Writing About`
- No hamburger — three items fit on one line.
- Social links move to footer.

### Typography

- **Body/UI:** Inter (variable, self-hosted)
- **Headings:** Inter, heavier weight. Single font family keeps it simple.
- **Monospace:** JetBrains Mono — dates, metadata, code
- **Scale:** 1.25 ratio (sm 14px → base 16px → lg 20px → xl 24px → 2xl 30px → 3xl 36px)
- **Measure:** max ~640px for prose content
- **Line height:** 1.6 body, 1.2 headings
- **Antialiased rendering**

### Color

Not afraid of color — but not overwhelming. A personality accent that adds life.

```css
/* Light mode */
--color-bg:            #ffffff;
--color-bg-subtle:     #f7f7f7;
--color-text-primary:  #1a1a1a;
--color-text-secondary: #4a4a4a;
--color-text-muted:    #888888;
--color-border:        #e5e5e5;
--color-accent:        #c05030;     /* terracotta */
--color-accent-hover:  #a0402a;

/* Dark mode */
--color-bg:            #111111;
--color-bg-subtle:     #1a1a1a;
--color-text-primary:  #f0f0f0;
--color-text-secondary: #c0c0c0;
--color-text-muted:    #777777;
--color-border:        #2a2a2a;
--color-accent:        #e07050;
--color-accent-hover:  #f09070;
```

Accent color on links and possibly section headings for emphasis (inspired by zenorocha's bright headers).

### Link styling

```css
a {
  color: var(--color-accent);
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 2px;
  transition: color 150ms ease;
}
a:hover { color: var(--color-accent-hover); }
```

### Content lists (tonsky-inspired year grouping)

```
2026
  ★ Post title                    2/14
    Another post                  1/20

2025
    Post title                   12/15
  ★ Featured post                10/3
```

Star highlights for featured. Dates right-aligned, muted. Year headings bold.

### Micro-interactions

Subtle — don't try to be clever:
- Links: color transition on hover (150ms)
- Nav items: slight weight or opacity change on active
- No translateX shifts, no parallax, no scroll effects
- Clean, expected behavior

### Dark mode

Toggleable via small icon in sidebar. Uses `class` strategy. Smooth transition.

### Distinctive touches (that don't try to be different)

- Year-grouped content lists with star highlights
- "Last updated" timestamps on living pages
- Colophon page about being built with Claude Code
- RSS feed in sidebar
- Clean dark/light toggle
- No pagination — full lists, Cmd+F friendly

---

## 4. Saent.com Migration

### Lifeline

Integrates as a project page at `/projects/lifeline`. saent.com root redirects here. Expanded treatment (App Store badge, features, download link) without separate design.

### Blog content

- Export all saent.com blog posts (~228 URLs)
- Convert to Markdown with frontmatter (category: "productivity", originalSource: "saent")
- Import into `src/content/blog/`
- Preserve original publication dates

### SEO redirect strategy

1. Move saent.com DNS to Cloudflare (free, keep registration at Namecheap)
2. Script generates URL mapping from saent.com sitemap → timmetz.nl equivalents
3. Upload bulk 301 redirects via Cloudflare
4. Monitor Google Search Console for crawl errors

### We Eat Robots

Stays on Substack. Project page at `/projects/we-eat-robots` links to Substack. No individual issue import.

### Animalz AI work

Project page at `/projects/animalz-ai` linking to separate knowledge base.

---

## 5. Implementation Phases

Full architecture planned. MVP scope decided together — phases are logical build order.

### Subagent strategy overview

| Phase | Subagents | Purpose |
|---|---|---|
| 0.1 | `frontend-design` skill | Generate homepage prototype for design review |
| 1.2 | `frontend-design` skill | Translate approved design into Astro components |
| 1.3 | 3 parallel general-purpose | Build page templates concurrently |
| 2.1 | 3 parallel Explore | Research actual project codebases for descriptions |
| 2.2 | 1 general-purpose | Draft homepage + about copy from research |
| 3.1 | 3 parallel (web + Logseq + file) | Deep research on Tim's media, notes, archived projects |
| 3.2 | 3 parallel general-purpose | Create content files from research |
| 4.1 | 1 general-purpose | Scrape saent.com, convert, generate redirects |
| 5.1 | 3 parallel general-purpose | OG images, structured data/RSS, polish |
| 5.2 | 2 parallel review agents | Architecture + code review |

### Phase 0: Design prototype

Build a single-page HTML prototype of the homepage to validate the visual direction.

**Step 0.1 — Homepage prototype (use `frontend-design` skill)**
Generate a standalone page demonstrating:
- **Layout:** Left sidebar nav (desktop) / top nav (mobile)
- **Typography:** Inter, full type scale, antialiased
- **Color:** Light + dark mode with terracotta accent
- **Homepage sections:** Intro, projects list, writing list (year-grouped with stars), work history
- **Sidebar:** Name, nav items, social links, dark mode toggle
- **Links:** Accent-colored with subtle underline
- **Responsive:** Sidebar collapses to top nav on mobile

Uses placeholder content matching the real structure.

**Step 0.2 — Review with Tim**
Iterate on: font choice, accent color, spacing, sidebar feel, dark mode, overall vibe.

Only proceed to Phase 1 after design approval.

### Phase 1: Foundation

**Step 1.1 — Setup**
1. Copy planning docs into `timmetz-nl/docs/planning/`
2. Initialize Astro 5 project with Tailwind 4
3. Define all content schemas (`content.config.ts`)
4. Write CLAUDE.md

**Step 1.2 — Design system + base layout**
Translate approved prototype into Astro. Produces: `Base.astro`, `Sidebar.astro`, `global.css`, `SEOHead.astro`

**Step 1.3 — Page templates (parallel subagents)**
- **Agent 1:** Homepage
- **Agent 2:** Projects pages (index + detail)
- **Agent 3:** Writing pages (index + detail) + About page

**Step 1.4 — Deploy**
Git repo → GitHub → Cloudflare Pages

### Phase 2: Seed content

**Step 2.1 — Project research (parallel subagents)**
- **Agent 1:** Lifeline (from SaentLifeline codebase)
- **Agent 2:** Animalz AI + My-OS (from their codebases)
- **Agent 3:** ClaudeQuote, Claude Carbon, others (from Personal/ projects)

**Step 2.2 — Homepage + about copy (subagent)**
Writing-focused agent drafts intro, "Now" section, about content.

**Step 2.3 — Work history entries**
3-5 work history .md files.

**Potential MVP launch point.**

### Phase 3: Content population

**Step 3.1 — Deep research (parallel)**
- **Agent 1:** Web search for interviews, press, appearances
- **Agent 2:** Logseq mining for content
- **Agent 3:** Scan all projects including `zzz archive`

**Step 3.2 — Content creation (parallel)**
Create media entries, remaining projects, initial blog posts.

### Phase 4: Saent.com migration

**Step 4.1 — Export and convert (subagent)**
Scrape → Markdown → import → redirect CSV

**Step 4.2 — Redirect setup (guided)**
DNS changes, bulk redirects, verification.

### Phase 5: Polish

**Step 5.1 — Technical polish (parallel)**
OG images, structured data, RSS, sitemap

**Step 5.2 — Quality review (parallel review agents)**
Architecture review + code review + Lighthouse audit

---

## 6. Project Structure

```
timmetz-nl/
├── astro.config.mjs
├── package.json
├── tsconfig.json
├── CLAUDE.md
├── docs/
│   └── planning/
│       ├── PLAN.md                 # This plan
│       ├── DESIGN_SYSTEM.md        # Full design specs
│       └── CONTENT_GUIDE.md        # Schema reference
├── src/
│   ├── content.config.ts           # Collection schemas
│   ├── content/
│   │   ├── blog/
│   │   ├── projects/
│   │   ├── work/
│   │   └── media/
│   ├── layouts/
│   │   ├── Base.astro              # HTML shell, sidebar, responsive
│   │   ├── Page.astro              # Standard page
│   │   └── Post.astro              # Blog post
│   ├── components/
│   │   ├── Sidebar.astro           # Left nav (desktop)
│   │   ├── MobileNav.astro         # Top nav (mobile)
│   │   ├── ProjectCard.astro
│   │   ├── SEOHead.astro
│   │   └── ThemeToggle.astro
│   ├── pages/
│   │   ├── index.astro
│   │   ├── about.astro
│   │   ├── projects/
│   │   │   ├── index.astro
│   │   │   └── [...slug].astro
│   │   └── writing/
│   │       ├── index.astro
│   │       └── [...slug].astro
│   ├── styles/
│   │   └── global.css
│   └── lib/
│       └── og.ts
├── public/
│   ├── favicon.svg
│   ├── robots.txt
│   └── images/
└── scripts/
    └── migrate-saent-blog.ts
```

---

## 7. Verification

- `npm run dev` — local preview on localhost:4321
- `npm run build` — verify static build succeeds
- Lighthouse 95+ on Performance, Accessibility, SEO
- All content types render correctly
- Mobile responsive (320px, 768px, 1024px+)
- Dark mode toggle works
- Sidebar collapses correctly on mobile
- Cross-references link correctly
- After deploy: Cloudflare Pages serves correctly
- After migration: spot-check 10+ redirect URLs

---

## 8. Claude Code Workflow

| Operation | Action |
|---|---|
| Add a new project | Create `src/content/projects/[slug].md` |
| Add a blog post | Create `src/content/blog/[slug].md` |
| Update project description | Edit the `.md` file |
| Update work history | Edit `src/content/work/[slug].md` |
| Add media/interview | Create `src/content/media/[slug].md` |
| Update "Now" section | Edit about page content |
| Deploy | Commit + push to main → auto-build |

---

## Appendix A: Content Schema Details

### Project schema
```typescript
z.object({
  title: z.string(),
  description: z.string(),
  status: z.enum(['active', 'on-ice', 'archived', 'completed']),
  role: z.string(),
  startDate: z.coerce.date(),
  endDate: z.coerce.date().optional(),
  url: z.string().url().optional(),
  repo: z.string().url().optional(),
  tags: z.array(z.string()).default([]),
  featured: z.boolean().default(false),
  sortOrder: z.number().default(0),
  relatedWork: z.array(z.string()).default([]),
})
```

### Blog schema
```typescript
z.object({
  title: z.string(),
  description: z.string(),
  pubDate: z.coerce.date(),
  updatedDate: z.coerce.date().optional(),
  category: z.enum(['productivity', 'ai', 'agile', 'startup', 'africa', 'general']),
  tags: z.array(z.string()).default([]),
  draft: z.boolean().default(false),
  originalUrl: z.string().url().optional(),
  originalSource: z.enum(['saent', 'animalz', 'parable', 'other']).optional(),
})
```

### Work schema
```typescript
z.object({
  title: z.string(),
  company: z.string(),
  description: z.string(),
  startDate: z.coerce.date(),
  endDate: z.coerce.date().optional(),
  location: z.string().optional(),
  highlights: z.array(z.string()).default([]),
  relatedProjects: z.array(z.string()).default([]),
  relatedMedia: z.array(z.string()).default([]),
})
```

### Media schema
```typescript
z.object({
  title: z.string(),
  type: z.enum(['interview', 'podcast', 'video', 'article', 'press']),
  date: z.coerce.date(),
  url: z.string().url(),
  publication: z.string().optional(),
  description: z.string().optional(),
  embedUrl: z.string().url().optional(),
})
```

---

## Appendix B: Design System Reference

### Color system
```css
:root {
  --color-bg: #ffffff;
  --color-bg-subtle: #f7f7f7;
  --color-text-primary: #1a1a1a;
  --color-text-secondary: #4a4a4a;
  --color-text-muted: #888888;
  --color-border: #e5e5e5;
  --color-accent: #c05030;
  --color-accent-hover: #a0402a;
}
html.dark {
  --color-bg: #111111;
  --color-bg-subtle: #1a1a1a;
  --color-text-primary: #f0f0f0;
  --color-text-secondary: #c0c0c0;
  --color-text-muted: #777777;
  --color-border: #2a2a2a;
  --color-accent: #e07050;
  --color-accent-hover: #f09070;
}
```

### Typography
```css
body {
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  -webkit-font-smoothing: antialiased;
  font-size: 1rem;
  line-height: 1.6;
  color: var(--color-text-secondary);
}
h1, h2, h3 {
  font-weight: 600;
  color: var(--color-text-primary);
  line-height: 1.2;
}
```

### Links
```css
a {
  color: var(--color-accent);
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 2px;
  transition: color 150ms ease;
}
a:hover { color: var(--color-accent-hover); }
```

### Layout (sidebar)
```css
.site-layout {
  display: flex;
  min-height: 100vh;
}
.sidebar {
  width: 200px;
  position: sticky;
  top: 0;
  height: 100vh;
  padding: 2rem 1.5rem;
  flex-shrink: 0;
}
.main-content {
  flex: 1;
  max-width: 640px;
  padding: 2rem 1.5rem;
}
@media (max-width: 767px) {
  .site-layout { flex-direction: column; }
  .sidebar { width: 100%; height: auto; position: static; }
}
```

---

## Appendix C: Saent.com Migration Details

### Current saent.com structure
- ~228 URLs in sitemap
- Blog with productivity/focus content
- Lifeline landing page
- Privacy policy and legal pages
- Currently hosted on Webflow

### Migration approach
1. **Export content:** Webflow CMS export or scrape
2. **Convert format:** HTML → Markdown with frontmatter
3. **URL mapping:** Script generates CSV mapping old → new URLs
4. **DNS transfer:** Move saent.com nameservers to Cloudflare
5. **Bulk redirects:** Upload CSV to Cloudflare Bulk Redirects
6. **Verification:** Google Search Console monitoring

### Why Cloudflare for redirects
Namecheap only supports domain-level redirects. For SEO value transfer, need path-level 301s. Cloudflare Bulk Redirects handle this at the DNS/edge level.

---

## Appendix D: Astro Configuration Reference

```javascript
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  site: 'https://timmetz.nl',
  integrations: [sitemap()],
  vite: { plugins: [tailwindcss()] },
});
```

### Content config pattern
```typescript
import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const projects = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/projects" }),
  schema: z.object({ /* see Appendix A */ }),
});
export const collections = { projects, blog, work, media };
```

### SEO head pattern
```astro
<title>{title} | Tim Metz</title>
<meta name="description" content={description} />
<link rel="canonical" href={canonicalUrl} />
<meta property="og:title" content={title} />
<meta property="og:description" content={description} />
<meta property="og:image" content={ogImageUrl} />
<meta property="og:type" content={type} />
```

### Structured data patterns
- **Person** schema on homepage/about
- **Article** schema on blog posts
- **BreadcrumbList** on subpages
- **WebSite** with SearchAction on homepage
