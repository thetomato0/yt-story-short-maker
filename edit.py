from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_audioclips
import ffmpeg
import whisper

def extract_audio(video_path):
    audio_path = "extracted_audio.wav"
    ffmpeg.input(video_path).output(audio_path).run(overwrite_output=True)
    return audio_path

def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result['segments']

def generate_subtitle_file(segments, subtitle_file):
    with open(subtitle_file, 'w') as f:
        for i, segment in enumerate(segments):
            start = format_time(segment['start'])
            end = format_time(segment['end'])
            text = segment['text'].strip()
            f.write(f"{i + 1}\n{start} --> {end}\n{text}\n\n")

def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02}:{int(minutes):02}:{seconds:.3f}"

def add_subtitle_to_video(video_path, subtitle_file):
    output_video_path = "output_video.mp4"
    (
        ffmpeg
        .input(video_path)
        .output(
            output_video_path,
            vf=f"subtitles={subtitle_file}:force_style='FontSize=24,PrimaryColour=&HFFFFFF&,BackColour=&H80000000&,BorderStyle=1,Outline=1,OutlineColour=&H000000&,Alignment=2'",
            audio_bitrate='192k',
            codec='copy',
            acodec='aac',
            vcodec='libx264'
        )
        .run(overwrite_output=True)
    )
    return output_video_path

def run(video_path):
    audio_path = extract_audio(video_path)
    segments = transcribe_audio(audio_path)
    subtitle_file = "subtitles.srt"
    generate_subtitle_file(segments, subtitle_file)
    output_video = add_subtitle_to_video(video_path, subtitle_file)
    print(f"Output video with subtitles saved as: {output_video}")


def generate_video(delay):
    video = VideoFileClip("file/bg.mp4")
    audio1 = AudioFileClip("file/title.mp3")
    audio2 = AudioFileClip("file/text.mp3")
    #mixing audio
    combined_audio = concatenate_audioclips([audio1, audio2])
    final_clip = video.set_audio(combined_audio)
    final_clip = final_clip.set_duration(combined_audio.duration + delay)
    final_clip.write_videofile("file/video-audio.mp4")
    video = VideoFileClip("file/video-audio.mp4")
    run("file/video-audio.mp4")
