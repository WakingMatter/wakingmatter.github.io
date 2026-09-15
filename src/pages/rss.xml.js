import rss from "@astrojs/rss";
import { getCollection } from "astro:content";

export async function GET(context) {
  const notes = (await getCollection("notes")).sort(
    (a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf(),
  );

  return rss({
    title: "Waking Matter Notes",
    description:
      "Notes on systems for cumulative intelligence, from Waking Matter.",
    site: context.site,
    items: notes.map((note) => ({
      title: note.data.title,
      description: note.data.description,
      pubDate: note.data.pubDate,
      link: `/notes/${note.id}/`,
    })),
    customData: `<language>en-us</language>`,
  });
}
