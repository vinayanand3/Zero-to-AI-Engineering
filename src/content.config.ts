import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    order: z.number(),
    season: z.number(),
    slug: z.string(),
    pubDate: z.string().optional()
  })
});

export const collections = { posts };
