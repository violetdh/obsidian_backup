import shutil
import os
from datetime import datetime as dt

# directory with both source and target directories. you can edit how this works easily if you don't want them in the same place.
dir = "./backup_test/"

src = dir+"source"
backup_dir = dir+"target/"

def copy():
    date = dt.now().date().strftime("%d-%m-%Y") # gets current date as string
    # converts date strings in filenames to date objects
    dates = [dt.strptime(ts, "%d-%m-%Y") for ts in os.listdir(backup_dir)]
    dates.sort() # sorts them
    backups = [dt.strftime(ts, "%d-%m-%Y") for ts in dates] # converts them back to strings
    print(backups)
    if len(backups) >= 7: # checks if 7 or more backups exist
        to_delete = backups[0]
        shutil.rmtree(backup_dir + to_delete) # deletes the 7th
        print(f"deleted oldest backup: {to_delete}")
    if not date in backups:
        shutil.copytree(src, backup_dir+date) # copies src folder to target folder as current date 
        print("backup " + date + " done!")
    else:
        print("uh oh! that file already exists!")
        print("try again tomorrow.")

copy()
