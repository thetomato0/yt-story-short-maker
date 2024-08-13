import os
import json
from reddit import *
from colorama import init
from termcolor import colored

if not os.path.exists('file'):
    os.makedirs('file')
    print("Folder 'file' created.")
else:
    print("Folder 'file' already exists.")

if not os.path.exists('config.json'):
    default_content = {
        "voicenameTitle": "en_us_007",
        "voicenameText": "en_us_007",
        "subreddit": "stories",
        "clientid": "",
        "clientsecret": "",
        "useragent": "",
        "delay": 0
    }
    
    # Create 'config.json' with default content
    with open('config.json', 'w') as json_file:
        json.dump(default_content, json_file, indent=4)
    print("File 'config.json' created with default content.")
else:
    print("File 'config.json' already exists.")


input(colored("all files and folders already exist or have been created change first please copy the background of your choice to the file folder rename it to bg.mp4 mp4 is the supported format and then change the config.json file to your liking then press Enter key","red"))

start()
