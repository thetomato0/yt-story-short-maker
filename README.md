
# Youtube short story maker
its a program that automatically makes short videos from reddit stories with subtitles!


# #Advantage

Using this project for content creation has some advantages over using websites like vsub

 - Open source: its means you have full control over how it works
 - Customizable: because its open source you can edit any aspect of the app
 - Free: unlike vsub where you have to pay 29 usd per month this app is completely free

### how to use

first install dependencies and **ffmpeg**
```pip install -r requirements.txt```

you can install **ffmepg** here:
www.ffmpeg.org

running the script:
```python ./start.py```
> **Note:** sometimes it seams its frozen but its not its not if you encounter any issue post it in the issues tab>


## Config

After running the script there will be will be a red message **DO NOT CLOSE THE WINDOW** there will be a new folder named **file** and a new file named **config.json** put your background of your choice there and rename it to bg.mp4 this script only supports mp4 this will be the background of your video then open the config.json file with your text editor  it should look something like this

```
{

"voicenameTitle":  "en_us_007",

"voicenameText":  "en_us_007",

"subreddit":  "stories",

"clientid":  "",

"clientsecret":  "",

"useragent":  "",

"delay":  0

}
```

voicenameTitle is the how it reads the title
voicenameTextis the how it reads the story itself
subreddit is the subreddit that it takes the story from
clientid,clientsecret,useragent are your reddit credentials here is how to get them:
www.bit.ly/3Aotv9G
its better not to touch delay but it defines how much room there is after the video ends

**after changing the config to your liking press enter in the script**



## how it works
every time you run the script it first takes a post of your subreddit of choice then uses the tiktok ai voice to make the audio then merges the audio and your video (bg.mp4) then adds subtitels and then you get the output

## coming soon (Maybe)

- [ ] photo of the post title for the beginning of the video
- [ ] automatic upload to youtube
- [ ] better subtitles
- [ ] voice based on the story

