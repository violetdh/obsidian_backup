# violet's obsidian backup tool

this is a tool I'm writing in python to take a folder and back it up daily, with a history going back 7 days and maybe a monthly copy too, not sure yet. 

it is intended for use with syncthing and my obsidian vault. basically, it will take the folder my vault is synced to and store backups of it daily that aren't influenced by syncthing, so that if something happens to the vault it won't be unrecoverable due to being synchronised.
