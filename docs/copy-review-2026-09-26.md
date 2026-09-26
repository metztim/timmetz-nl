---
source_of_truth: /Users/timmetz/Developer/Projects/Personal/timmetz-nl/docs/copy-review-2026-09-26.md
note: Review record. Selected edits applied locally on 2026-09-26; current copy lives in src/.
---

# Website Copy Review

Reviewed 2026-09-26. Scope: homepage, About, listing copy, all project descriptions, and work-history descriptions. Article files under `src/content/writing/` were excluded. Originals below are exact source excerpts; line breaks are preserved. These are recommendations for selection, not a request to replace all of the site's prose.

The strongest improvements are to remove the generic homepage/About opening, correct MyScreen's contradictory storage promise, remove About's exclusive Claude Code attribution, and describe the Animalz and Sentinel projects more concretely. Much of the personal history is already specific and worth keeping.

## Priority edits

### Homepage opener

Path: `src/pages/index.astro`

The current opening could describe many people. This names the work directly. In the following sentence, change “Currently leading marketing and AI innovation at” to “My work includes AI systems at” to avoid repeating the marketing role, and preserve its links. An alternative with less editing is simply to remove the first sentence and start with “I lead marketing and AI innovation at”. Prefer that shorter alternative if the second sentence already does enough.

Before:

```text
I build things at the intersection of productivity, AI, and content.
```

After:

```text
I make software, write about AI and productivity, and lead marketing at Animalz.
```

### About opening

Path: `src/pages/about.astro`

Remove the generic opener and name what the systems do. Leave the rest of this paragraph and its project links intact.

Before:

```text
      I build things at the intersection of productivity, AI, and content. I lead marketing
      and AI innovation at <a href="https://www.animalz.co" target="_blank" rel="noopener noreferrer">Animalz</a>,
      a B2B content marketing agency, where I build the AI systems behind the agency's
      editorial work.
```

After:

```text
      I lead marketing and AI innovation at <a href="https://www.animalz.co" target="_blank" rel="noopener noreferrer">Animalz</a>,
      a B2B content marketing agency, where I build AI systems for research, writing,
      and editing.
```

### About career transition

Path: `src/pages/about.astro`

The career itself supplies the variety. The prefatory claim adds little.

Before:

```text
      My path here was anything but linear. I started building websites in 1998, during the
      first dot-com wave, then spent years in video and television:
```

After:

```text
      I started building websites in 1998, during the first dot-com wave, then spent years
      in video and television:
```

### About site description

Path: `src/pages/about.astro`

Shorten the redundant description and remove an exclusive tooling claim that this Codex session makes outdated. There is no need to replace it with another tooling claim in the bio.

Before:

```text
      This site is the home for everything I make: projects, writing, videos, and experiments,
      collected in one place. It's built and maintained entirely with Claude Code.
```

After:

```text
      This site collects my projects, writing, videos, and experiments.
```

### MyScreen recording and sharing

Path: `src/content/projects/myscreen.md`

The original promise that recordings never touch another server conflicts with optional Dropbox uploads. Keep the local-first behavior explicit and clarify when an account is involved. This is an accuracy fix as well as a copy edit.

Before:

```text
MyScreen is a free, open-source alternative to Loom for macOS: record your screen with an optional camera bubble, get an MP4 saved locally, and optionally upload a share link through your own Dropbox. No accounts, no subscriptions, and your recordings never touch anyone else's server.
```

After:

```text
MyScreen is a free, open-source alternative to Loom for macOS. Record your screen with an optional camera bubble and save an MP4 locally. If you want a share link, you can upload the recording to your own Dropbox account. There is no MyScreen subscription.
```

### Animalz project description

Path: `src/content/projects/animalz-intelligence-os.md`

Replace vague “AI leverage” and an unqualified editorial-quality claim with the functions already described in the source.

Before:

```text
Animalz Intelligence OS is the internal AI platform I build and run at [Animalz](/about), a content marketing agency. It captures each customer's brand voice, automates research and drafting workflows, and gives writers and editors AI leverage without giving up editorial quality.
```

After:

```text
Animalz Intelligence OS is the internal AI platform I build and run at [Animalz](/about), a content marketing agency. It stores each customer's brand voice and runs research and drafting workflows for the agency's writers and editors.
```

### Sentinel behavior

Path: `src/content/projects/sentinel.md`

Describe what the agent does without implying that it can reliably identify every urgent message. The cadence and integrations are retained from the source, not independently verified.

Before:

```text
Sentinel is an urgent-flag for your inbox: an always-on background agent, powered by Claude Code, that scans email (and optionally Slack) every 15 minutes, asks Claude whether anything genuinely cannot wait, and pushes only those items to your phone. You keep the inbox closed and trust that real urgency surfaces itself.
```

After:

```text
Sentinel is a background agent powered by Claude Code that checks email and, optionally, Slack every 15 minutes. It uses Claude to assess which messages are urgent and sends those to your phone as push notifications.
```

### Sentinel shared infrastructure

Path: `src/content/projects/sentinel.md`

Remove “inherit that layer for free” sales phrasing. Verify that the shared layer includes these three functions before using this replacement; otherwise retain “a shared ops layer for running and tuning them”.

Before:

```text
It lives in [claude-agents](https://github.com/metztim/claude-agents), a small open-source home for always-on Claude agents with a shared ops layer for running and tuning them. New agents drop in beside Sentinel and inherit that layer for free.
```

After:

```text
It lives in [claude-agents](https://github.com/metztim/claude-agents), an open-source collection of always-on Claude agents. They share tools for deployment, monitoring, and configuration.
```

## Secondary edits

### We Eat Robots introduction

Path: `src/content/projects/we-eat-robots.md`

Keep the stated subject and point of view while removing the familiar “use these tools without letting them use you” turn of phrase.

Before:

```text
We Eat Robots is my newsletter about productivity for humans in the age of AI: how to use these tools without letting them use you, and how to keep thinking for yourself while working alongside machines that think fast.
```

After:

```text
We Eat Robots is my newsletter about AI, productivity, and thinking for yourself. I write about using AI in everyday work and where human judgment still matters.
```

### Lifeline history

Path: `src/content/projects/lifeline.md`

Replace “software continuation of the same mission” with the concrete transition. The rating is preserved but needs a current check.

Before:

```text
It grew out of [Saent](/projects/saent), the productivity startup I co-founded: after the hardware years, Lifeline became the software continuation of the same mission. It holds a 4.8★ rating on the Mac App Store.
```

After:

```text
Lifeline grew out of [Saent](/projects/saent), the productivity startup I co-founded. After we stopped making hardware, I kept working on the software. It holds a 4.8★ rating on the Mac App Store.
```

### Animalz role description

Path: `src/content/work/animalz-innovation.md`

“Top” is an unsupported ranking and adds little to a work-history description.

Before:

```text
Leading marketing and AI innovation at a top B2B content marketing agency.
```

After:

```text
Leading marketing and AI innovation at a B2B content marketing agency.
```

## Metadata and short descriptions

If the main edits are applied, keep the homepage JSON-LD description in `src/pages/index.astro` and the default description in `src/components/SEOHead.astro` aligned. Both repeat “at the intersection of productivity, AI, and content.” Suggested shared opening: “Tim Metz makes software, writes about AI and productivity, and leads marketing and AI innovation at Animalz.” Add the existing project details where appropriate.

The We Eat Robots project card description, “Newsletter about staying productive and human in the AI era”, could become “Newsletter about AI, productivity, and thinking for yourself”. Apply the same wording in the About bio if this change is selected.

The Claude Carbon project description says “tracking the energy and carbon footprint”. Its body correctly describes estimates. Change the short description to “macOS menu bar app estimating the energy and carbon footprint of Claude Code sessions”. The body can stay as it is unless Tim wants a broader tonal pass.

## Keep as written

- **About history:** The specific places, jobs, and family paragraph carry Tim's voice. Keep the detail and longer sentences.
- **EmojiFinder:** The personal reason for the fork, credit to the original creators, and precise account of changes work well. No polish needed.
- **ClaudeQuote:** “the funny, the profound, and the occasionally unhinged” suits the project. Do not flatten it into a generic product description.
- **md-clip:** Its short second paragraph supplies an understandable personal reason for the tool. Technical wording in the first paragraph is appropriate for its audience.
- **Historical work descriptions:** Most are concise and concrete. Happylatte's clarification that Tim joined after the game's peak is especially useful context.
- **Listing pages:** Projects and Writing have no prose introduction needing a rewrite. The Workflows empty-state copy is adequate. Their main issues are interaction and layout, not voice.

## Claims to verify separately

These were not fact-checked in this copy review. Do not silently replace them with new numbers or assertions.

- **MyScreen:** Verify signing/notarization and current recording modes against the project. The Dropbox contradiction can be fixed from the current page alone.
- **We Eat Robots:** Confirm “5,000+ subscribers” and whether a book is still in progress. The “workbench” sentence could become “The newsletter has more than 5,000 subscribers. I'm also working on a book about human strengths in an AI-driven world.” only if both statements remain current.
- **Lifeline:** Confirm the displayed App Store rating and whether it varies by storefront; “4.8★” appears in both the card description and body.
- **Sentinel:** Confirm current supported integrations, polling cadence, public repository, and shared infrastructure before using the proposed infrastructure sentence.
- **My-OS:** Confirm whether “Claude Code agents” still accurately describes the system. Do not infer its current architecture from this website repository.
- **Claude Code Plugins:** Confirm all listed plugins remain publicly installable.
- **Saent and KaiOS:** Retain historical campaign, patent, publication, device-volume, and award claims until a factual review is requested or reliable source material is available.

## Implementation notes

Use a colon or other punctuation instead of the rendered em dash separators in homepage, About, and project listings, in line with Tim's writing preference. Preserve links and factual scope when editing. Work-history body text does not currently appear in the About list, so editing it has lower immediate visitor impact than the homepage, About bio, and project descriptions.

## Applied edits

Applied locally: About opening, career transition, and site description; MyScreen recording and sharing; Animalz project and role descriptions; Sentinel behavior; We Eat Robots introduction; Lifeline history; aligned metadata; Claude Carbon estimate wording. Homepage uses the shorter proposed alternative. Sentinel infrastructure retains only the functions already in its source. Article files remain unchanged.
