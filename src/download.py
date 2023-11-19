import os
import re
from pytube import YouTube
from moviepy.editor import AudioFileClip

def video_title(youtube_url: str) -> str:
    """
    Retrieve the title of a YouTube video.
    """
    try:
        yt = YouTube(youtube_url)
        return yt.title
    except Exception as e:
        print(f"Error retrieving video title: {e}")
        return ""

def safe_filename(filename: str) -> str:
    """
    Generate a safe filename by removing or replacing invalid characters.
    """
    return re.sub(r'[\\/*?:"<>|]', '', filename)


def download_audio(youtube_url: str, download_path: str) -> str:
    """
    Download the audio from a YouTube video.
    """
    try:
        youtube = YouTube(youtube_url)
        audio_stream = youtube.streams.filter(only_audio=True, file_extension='mp4').first()
        # Определяем, является ли download_path полным путем к файлу или директорией
        if os.path.isdir(download_path):
            audio_filename = safe_filename(youtube.title) + ".mp4"
        else:
            audio_filename = os.path.basename(download_path)

        audio_stream.download(output_path=os.path.dirname(download_path), filename=audio_filename)
        return os.path.join(os.path.dirname(download_path), audio_filename)
    except Exception as e:
        print(f"Error downloading audio: {e}")
        return ""


def convert_mp4_to_mp3(input_file: str, output_file: str) -> None:
    """
    Convert an audio file from mp4 format to mp3.
    """
    try:
        audio_clip = AudioFileClip(input_file)
        audio_clip.write_audiofile(output_file, codec='mp3')  # Указываем кодек mp3
        audio_clip.close()
        os.remove(input_file)
    except Exception as e:
        print(f"Error converting file: {e}")