---
date: 2021-07-27
tags:
  - blog
  - neuron
  - markdown
  - digital_garden
---

# Digital Garden

I have simple requirements for a digital garden.  It should be easy to edit using my favourite tools, and trivial to deploy.  I want the content in the most simple form it can be, and easy to move around.  I want to edit with Vim keystrokes.

Without going into details about previous attempts (wordpress, tiddlywiki, hugo, jekyll, etc.), here is a great system I've settled on.

All my blog and articles are trivial markdown files.  Links with double square brackets between pages.  A little bit of front matter in the markdown files to add dates for blogs and the occasional tags.

Visual Studio code and Vim have great plugins for working with Markdown.  In particular Visual Studio Code lets me trivially jump between markdown links, and shows my inline images in the preview window.  These tools automatically install and work great; along with the Vim extension - a requirement for me.

[Neuron](https://neuron.zettel.page) is great as a static site generator, taking my markdown notes and turning them into a clean set of pages.  Github actions mean that all I have to do is **git push** my site to publish it.  I've customised it a bit with some JS script for adding social sharing links, etc.  And I have to add 4 lines of **div** elements to each blog page; only a minor annoyance and I could automate it too.

[Obsidian](https://obsidian.md) is an alternative editor, for when I want deep search and cool graph visualization of my pages.

<div class="ui section divider"></div>
<section id="socialMediaLinks"></section>
<div class="ui section divider"></div>
<div id="disqus_thread"></div>