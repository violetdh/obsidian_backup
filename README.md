# violet's obsidian backup tool
this is a script i wrote in python to take a folder and back it up daily, with a history going back 7 days.

it takes a specified src folder and copies it to a destination folder, renaming it to the current date. it will keep up to 7 of these in the folder at a time.

this is intended to be run daily as a cron job.
## todo:
- maybe extra monthly copies - not sure how far back i would want these to go, though
- mayyyybe implement a basic tkinter GUI for funsies that lets you choose the directories without editing the script itself
## faq
- why bother making this?

because I identified a problem in my life (syncthing also syncs file deletions and I'm scared of losing my obsidian vault) and wanted to solve it, while also flexing my atrophying python muscles a bit.
- don't solutions already exist?

I'm sure they do, but I wanted to write something to solve it myself. Again, atrophying python muscles.
