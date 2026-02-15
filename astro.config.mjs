import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';
import remarkGfm from 'remark-gfm';

export default defineConfig({
  site: 'https://timmetz.nl',
  integrations: [sitemap()],
  vite: { plugins: [tailwindcss()] },
  markdown: {
    remarkPlugins: [remarkGfm],
  },
});
