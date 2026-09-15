import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import remarkGfm from "remark-gfm";

export default defineConfig({
  site: "https://wakingmatter.com",
  trailingSlash: "always",
  integrations: [
    sitemap({
      changefreq: "monthly",
      priority: 0.7,
      lastmod: new Date("2026-09-15"),
      filter: (page) => !page.includes("404"),
    }),
  ],
  markdown: {
    remarkPlugins: [remarkGfm],
    shikiConfig: {
      theme: "css-variables",
    },
  },
  build: {
    format: "directory",
    inlineStylesheets: "auto",
  },
});
