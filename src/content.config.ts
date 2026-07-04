import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const projects = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/projects' }),
  schema: z.object({
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
  }),
});

const writing = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/writing' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
    originalUrl: z.string().url().optional(),
    sourceName: z.string().optional(),
    excerpt: z.string().optional(),
    lang: z.string().optional(),
  }),
});

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/posts' }),
  schema: z.object({
    pubDate: z.coerce.date(),
    linkedinUrl: z.string().url().optional(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
  }),
});

const work = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/work' }),
  schema: z.object({
    title: z.string(),
    company: z.string(),
    description: z.string(),
    startDate: z.coerce.date(),
    endDate: z.coerce.date().optional(),
    location: z.string().optional(),
    highlights: z.array(z.string()).default([]),
    relatedProjects: z.array(z.string()).default([]),
    relatedMedia: z.array(z.string()).default([]),
  }),
});

const workflows = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/workflows' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    type: z.enum(['workflow', 'command']),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
    tool: z.string().optional(),
    complexity: z.enum(['simple', 'intermediate', 'advanced']).optional(),
  }),
});

const media = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/media' }),
  schema: z.object({
    title: z.string(),
    type: z.enum(['interview', 'podcast', 'video', 'article', 'press']),
    date: z.coerce.date(),
    url: z.string().url(),
    publication: z.string().optional(),
    description: z.string().optional(),
    embedUrl: z.string().url().optional(),
  }),
});

export const collections = { projects, writing, work, media, workflows, posts };
