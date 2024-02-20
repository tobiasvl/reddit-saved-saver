Reddit Saved Saver
==================

A simple Python script for converting your saved posts and comments on Reddit to Markdown files with YAML frontmatter metadata.

I made this to dump all my saved Reddit stuff into [Obsidian](https://obsidian.md). It's not at all customizable or user friendly right now.

Usage
-----

You need to create a Reddit app on https://old.reddit.com/prefs/apps/ and then put the client ID, secret key, as well as your Reddit username and password into `config.py`.

Make sure `praw` is installed, and then run the script with `python reddit-saved-saver.py`.

The script will create a directory called `reddit` and then make a new subdirectory per subreddit.
