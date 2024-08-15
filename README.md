# YouTube Short Story Maker

This program automatically creates short videos from Reddit stories, complete with subtitles!

## Advantages

Using this project for content creation offers several benefits compared to websites like vsub:

- **Open Source**: Full control over functionality and customization.
- **Customizable**: Edit any aspect of the application to suit your needs.
- **Free**: No subscription fees, unlike vsub, which costs $29 per month.

## How to Use

1. **Install Dependencies**: First, install the required dependencies and **FFmpeg**:
   ```bash
   pip install -r requirements.txt
   ```

   You can download **FFmpeg** from [ffmpeg.org](https://www.ffmpeg.org).

2. **Run the Script**: Execute the following command:
   ```bash
   python ./start.py
   ```
   > **Note**: If the script appears to freeze, it may still be running. If you encounter issues, please report them in the issues tab.

## Configuration

After running the script, you will see a red message, and a new folder named **file** will be created, along with a **config.json** file.

### Steps to Configure:

1. Place your chosen background video in the **file** folder and rename it to **bg.mp4** (only MP4 format is supported).
   
2. Open **config.json** with a text editor. It should look like this:

   ```json
   {
       "voicenameTitle": "en_us_007",
       "voicenameText": "en_us_007",
       "subreddit": "stories",
       "clientid": "",
       "clientsecret": "",
       "useragent": "",
       "delay": 0
   }
   ```

   - **voicenameTitle**: Voice for reading the title.
   - **voicenameText**: Voice for reading the story.
   - **subreddit**: The subreddit to pull stories from.
   - **clientid, clientsecret, useragent**: Your Reddit credentials (see [this guide](https://www.bit.ly/3Aotv9G) for obtaining them).
   - **delay**: Defines the pause after the video ends (recommended to leave unchanged).

3. **Available Voices**: You can see the available voices in `tiktokvoice.py`.

After adjusting the configuration to your preference, press **Enter** in the script.

## How It Works

Each time you run the script, it:

1. Fetches a post from your chosen subreddit.
2. Uses TikTok AI voice to generate audio.
3. Merges the audio with your background video (**bg.mp4**) and adds subtitles.
4. Produces the final output video.

## Coming Soon (Maybe)

- [ ] Graphical User Interface (GUI)
- [ ] Thumbnail image of the post title at the beginning of the video
- [ ] Automatic upload to YouTube
- [ ] Enhanced subtitle options
- [ ] Voice customization based on the story
