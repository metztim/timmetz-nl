---
source_of_truth: /Users/timmetz/Developer/Projects/Personal/timmetz-nl/docs/site-review-2026-09-26.md
note: Local implementation and verification record. Production deployment is pending.
---

# Website Review and Priorities

Reviewed the live site at https://www.timmetz.nl and the local Astro source on 2026-09-26. Changes below are implemented locally and browser-checked. The live site has not been updated. Article source files are unchanged.

## Implemented, highest impact first

| Priority | Finding | Change |
| --- | --- | --- |
| High | Writing exposes 137 tags, many containing several migration-era topics joined together. First article starts at 2,533 px on desktop. | Search, eight readable topic groups, and publication filter. First article now starts at about 329 px on desktop and 433 px at 375 px mobile width. Original article tags remain intact. |
| High | Desktop theme button does nothing because two controls share an ID and only the first receives a listener. | Bind both controls by class; remove duplicate IDs. |
| Medium | Mobile header squeezes Tim's name onto two lines. | Separate name/theme row and wrapping navigation row. |
| Medium | Workflows navigation leads to an empty coming-soon page. | Remove it from both navigation menus. Keep its URL with links to Writing and Projects. Restore navigation when the first workflow is published. |
| Medium | Non-article copy includes generic phrasing and conflicting MyScreen storage claims. | Polish homepage, About, selected project descriptions, and metadata; clarify Dropbox sharing and footprint estimates. See the separate copy review. |
| Medium | Small muted text has weak contrast. | Darken light-mode secondary metadata and lighten dark-mode metadata; add keyboard focus indicators and a skip link. |
| Medium | Writing detail route generation includes drafts even though listings and RSS exclude them. | Exclude draft detail routes too. No existing drafts were found. |
| Low | Canonical URLs and sitemap use the bare domain while live navigation ends at www. | Align canonical origin, RSS, robots, and structured profile URL with www. |
| Low | Missing legacy internal route and no useful 404 page. | Add an exact Cloudflare redirect for `/get-more-done-by-taking-your-time/`; add a 404 page linking to the archive, projects, and home. Redirect takes effect only on Cloudflare deployment. |
| Low | Saent project offers a Visit link to the retired site and names a history series without linking it. | Remove the retired-site link and link the existing series introduction. |

## Migration audit

Run `npm run build`, then `python3 scripts/audit-site.py`. The script reads generated HTML without changing content. It does not crawl or certify external links.

- 227 writing entries: 154 hosted article pages and 73 external pointers.
- 173 built HTML pages after adding the 404 page.
- No duplicate HTML IDs, stray linked-image bracket paragraphs, raw embed-script text, or missing local image assets found.
- One broken internal article route has a known destination and now has a deployment redirect.
- Six unresolved links point to two missing destinations: five links to `/find-your-focus-book` and one to `/writing/favorite-reads-2016`. Recover the original pages/assets or choose replacements before changing these links.
- 27 links across archived articles reference the retired Saent community. Their original destinations need recovery or an editorial decision; no replacement was invented.
- 10 images have raw URLs as alt text; 94 have empty alt text. Each needs image-specific review before adding descriptions.
- 12 paragraphs on nine article pages contain only whitespace or invisible characters. These are remaining presentation cleanup candidates.

No article wording, frontmatter, or source markup was changed. The audit is complete; the remaining article-level cleanup is still open.

## Notion backlog order

The personal Timmetz.nl project has 13 linked tasks: four Done and nine open. The Substack migration is in the local roadmap rather than a separate linked task.

| Order | Open task | Disposition |
| --- | --- | --- |
| 1 | Sweep remaining writing entries for Webflow migration artifacts | Audit completed; findings above. Keep open for targeted cleanup and destination recovery. |
| 2 | Strengthen personal online presence so LLMs cite me | Site copy, navigation, canonical URLs, and discoverability improved locally. External bios, X, and automatic updates remain outside this pass. |
| 3 | Repoint SaentLifeline release-post publishing | Bounded follow-up, but changes another repository's publishing process. Review that process separately. |
| 4 | Interlink external bios | Requires edits on LinkedIn, Animalz, and We Eat Robots. Prepare exact changes before publishing externally. |
| 5 | Create a design system with Claude Design | Deferred. This pass preserves the current design; a redesign and reusable design system need a separate brief. |
| 6 | Export Medium posts | Needs account access and import/deduplication review. No import performed. |
| 7 | Add Definitions from Logseq somewhere | Needs a selected source set and decision about what private notes can be published. |
| 8 | Auto-publish hook for commands/workflows | Cross-project automation and private-content publication risk; design a draft/review flow first. |
| 9 | Verify Webflow was cancelled and finish shutdown | Account/billing action. No cancellation performed. |
| Deferred | We Eat Robots/Substack migration | Explicitly excluded by Tim: provider, subscribers, and migration decisions. |

## Analytics

No Google Analytics or Cloudflare Web Analytics script was found in the inspected live pages or source. Cloudflare's dashboard requires sign-in in the in-app browser.

Cloudflare Web Analytics is the recommended first step for basic audience and performance statistics. Enable it under Workers & Pages → timmetz-nl → Metrics → Web Analytics, then deploy and confirm the beacon appears on the live site. Setup is not yet complete. Official guide: https://developers.cloudflare.com/pages/how-to/web-analytics/.

## Verification

- Production build passes. Existing warnings concern empty media, workflows, and posts collections.
- Browser: title/topic search, publication filter, combined zero-result state, clear/reset, empty year-group hiding, and desktop/mobile theme switches checked.
- All 227 entries return after clearing filters; Pomodoro search returns 15, AI topic returns 14, and Pomodoro + Animalz returns zero.
- Writing visually checked at desktop and 375 px mobile; About checked at 375 px and measured at 320 px. No horizontal overflow on those checked pages.
- `git diff --check` passes; `git diff -- src/content/writing` is empty.
- Ratings, subscriber numbers, and historical product claims were retained, not independently reverified.
- No Lighthouse run or exhaustive external-link crawl was performed.
