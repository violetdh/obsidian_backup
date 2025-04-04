import shutil
import os
from datetime import datetime as dt

src = "../backup_test/source"
backup_dir = "../backup_test/target/"

def copy():
    date = dt.now().date().strftime("%d-%m-%Y") # gets current date as string
    if len(os.listdir(backup_dir)) >= 7: # checks if 7 or more backups exist
        shutil.rmtree(backup_dir+backups[6]) # deletes the 7th
    shutil.copytree(src, backup_dir+date) # copies src folder to target folder as current date 
    print("backup " + date + "done!")

copy()
