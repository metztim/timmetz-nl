import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
  const writing = (await getCollection('writing', ({ data }) => !data.draft)).sort(
    (a, b) => b.data.pubDate.getTime() - a.data.pubDate.getTime()
  );

  return rss({
    title: 'Tim Metz — Writing',
    description:
      'Writing by Tim Metz on productivity, AI, and building software.',
    site: context.site,
    items: writing.map(entry => ({
      title: entry.data.title,
      pubDate: entry.data.pubDate,
      description: entry.data.description ?? entry.data.excerpt ?? '',
      // Pointer entries link to their canonical external home; hosted entries link here.
      link: entry.data.originalUrl ?? `/writing/${entry.id}/`,
    })),
    customData: '<language>en</language>',
  });
}
