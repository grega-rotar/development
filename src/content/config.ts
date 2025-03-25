import { defineCollection, z } from "astro:content"

const journey = defineCollection({
  type: "content",
  schema: z.object({
    company: z.string(),
    role: z.string(),
    dateStart: z.coerce.date(),
    dateEnd: z.union([z.coerce.date(), z.string()]),
    searchTags: z.array(z.string()).optional(),
  }),
})

const blog = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    date: z.coerce.date(),
    authors: z.array(z.string()).optional(),
    tags: z.array(z.string()),
    draft: z.boolean().optional(),
    searchTags: z.array(z.string()).optional(),
  }),
})

const projects = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    date: z.coerce.date(),
    authors: z.array(z.string()).optional(),
    tags: z.array(z.string()),
    draft: z.boolean().optional(),
    demoUrl: z.string().optional(),
    repoUrl: z.string().optional(),
    searchTags: z.array(z.string()).optional(),
  }),
})

const devHub = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    date: z.coerce.date(),
    authors: z.array(z.string()).optional(),
    tags: z.array(z.string()),
    draft: z.boolean().optional(),
    demoUrl: z.string().optional(),
    repoUrl: z.string().optional(),
    searchTags: z.array(z.string()).optional(),
  }),
})

const connect = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    date: z.coerce.date(),
    team: z.array(z.string()).optional(),
    tags: z.array(z.string()),
    draft: z.boolean().optional(),
    website: z.string().optional(),
    repoUrl: z.string().optional(),
    searchTags: z.array(z.string()).optional(),
  }),
})


const legal = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
  }),
})

export const collections = { journey, blog, projects, legal, devHub, connect}
