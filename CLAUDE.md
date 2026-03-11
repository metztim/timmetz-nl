# timmetz.nl

Personal website for Tim Metz. Static site built with Astro 5 + Tailwind 4, deployed on Cloudflare Pages.

## Project structure

```
src/
├── content.config.ts          # Content collection schemas (Zod)
├── content/
│   ├── projects/              # Project .md files
│   ├── writing/               # Writing/blog .md files
│   ├── workflows/             # Workflow and command .md files
│   ├── work/                  # Work history .md files
│   └── media/                 # Media/press .md files
├── layouts/
│   ├── Base.astro             # HTML shell, sidebar + mobile nav
│   └── Post.astro             # Writing post layout (prose styling)
├── components/
│   ├── Sidebar.astro          # Desktop left sidebar
│   ├── MobileNav.astro        # Mobile top nav
│   ├── MobileFooter.astro     # Mobile footer with social links
│   ├── ThemeToggle.astro      # Dark/light mode toggle
│   └── SEOHead.astro          # Meta tags, OG
├── pages/
│   ├── index.astro            # Homepage hub
│   ├── about.astro            # Bio, work history
│   ├── projects/
│   │   ├── index.astro        # Project listing (grouped by status)
│   │   └── [...slug].astro    # Project detail
│   └── writing/
│       ├── index.astro        # Writing listing (year-grouped)
│       └── [...slug].astro    # Writing detail
├── styles/
│   └── global.css             # Theme, typography, prose, footnotes
└── lib/                       # Utilities (future: OG image generation)
public/
├── fonts/                     # Self-hosted Inter + JetBrains Mono
├── favicon.svg
└── images/
```

## Conventions

* **"Writing" not "Blog"** — use "Writing" in all UI, URLs, and references

* **Date format:** `MM.DD` zero-padded dot notation (02.10, 11.22) in JetBrains Mono

* **No stars** in writing lists — removed during Phase 0 review

* **Collection name:** `writing` (not `blog`) in content config and everywhere

* **Footnotes:** Supported via remark-gfm on all Markdown content

## Content operations

| Operation       | <span data-proof="authored" data-by="ai:claude">Action</span>   |
| --------------- | --------------------------------------------------------------- |
| Add project     | Create `src/content/projects/{slug}.md` with schema frontmatter |
| Add writing     | Create `src/content/writing/{slug}.md` with schema frontmatter  |
| Add work entry  | Create `src/content/work/{slug}.md`                             |
| Add media entry | Create `src/content/media/{slug}.md`                            |
| Deploy          | Commit + push to main → auto-build on Cloudflare Pages          |

## Design system

* **Fonts:** Inter (variable, self-hosted), JetBrains Mono (self-hosted)

* **Accent:** Terracotta — light `#c05030`, dark `#e07050`

* **Layout:** Left sidebar 200px desktop, top nav mobile (breakpoint 767px)

* **Prose max-width:** 640px

* **Dark mode:** `class="dark"` on `<html>`, localStorage + system preference

## Commands

```bash
npm run dev        # Dev server at localhost:4321
npm run build      # Static build to dist/
npm run preview    # Preview production build
```

## Planning docs

* `docs/planning/PLAN.md` — Full implementation plan with phases

* `docs/planning/DESIGN_RESEARCH.md` — Design decisions and reference review

## People

* **Tim Metz** — Site owner, product manager. Non-technical; reviews output in browser.

<!-- PROOF
{
  "version": 2,
  "marks": {
    "m1771403492076_3": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-02-18T08:31:32.076Z",
      "range": {
        "from": 1182,
        "to": 1310
      },
      "content": "│   ├── writing/\n│   │   ├── index.astro        # Writing listing (year-grouped)\n│   │   └── [...slug].astro    # Writing detail\n│   └── workflows/\n│       ├── index.astro        # Workflows listing (grouped by type)\n│       └── [...slug].astro    # Workflow/command detail",
      "status": "pending"
    },
    "m1771403492073_2": {
      "kind": "insert",
      "by": "ai:claude",
      "createdAt": "2026-02-18T08:32:39.405Z",
      "range": {
        "from": 2138,
        "to": 2280
      },
      "content": "\nAdd workflow\nCreate src/content/workflows/{slug}.md with type: workflow\nAdd command\nCreate src/content/workflows/{slug}.md with type: command",
      "status": "pending"
    }
  }
}
-->

<!-- PROOF:END -->
