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

def download_audio(youtube_url: str, download_path: str) -> None:
    """
    Download the audio from a YouTube video.
    """
    try:
        yt = YouTube(youtube_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path=download_path, filename="audio.mp4")
    except Exception as e:
        print(f"Error downloading audio: {e}")

def convert_mp4_to_mp3(input_path: str, output_path: str) -> None:
    """
    Convert an audio file from mp4 format to mp3.
    """
    try:
        audio_clip = AudioFileClip(input_path + "/audio.mp4")
        audio_clip.write_audiofile(output_path + "/audio.mp3")
        audio_clip.close()
    except Exception as e:
        print(f"Error converting file: {e}")
