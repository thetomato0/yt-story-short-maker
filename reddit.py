import json
import praw
import random
from edit import *
from tiktokvoice import tts
from colorama import init
from termcolor import colored
init()

def start():
    with open('config.json', 'r') as f:
        config = json.load(f)

    clientid = config["clientid"]
    clientsecret = config["clientsecret"]
    useragent = config["useragent"]
    subreddit = config["subreddit"]
    delay = config["delay"]


    reddit = praw.Reddit(client_id=clientid, client_secret=clientsecret, user_agent=useragent)
    subreddit = reddit.subreddit(subreddit)
    top_posts = list(subreddit.top(limit=100))
    random_post = random.choice(top_posts)

    print(f'Title: {random_post.title}')
    print(f'URL: {random_post.url}')
    print(f'Text: {random_post.selftext}')

    input(colored("if the gender from the story isnt like the config you can go and change it now Press Enter to dismiss","green"))

    voicenameTitle = config["voicenameTitle"]
    voicenameText = config["voicenameText"]

    print("making audio files this may take a while")
    tts(str(random_post.title), voicenameTitle, "file/title.mp3")
    print("created title audio")
    tts(str(random_post.selftext), voicenameText, "file/text.mp3")
    print("created text audio")
    generate_video(delay=delay)
