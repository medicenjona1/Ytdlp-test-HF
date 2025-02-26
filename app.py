import gradio as gr
import yt_dlp
import os
from pydub import AudioSegment
from pydub.playback import play

def download_audio(url):
    output_path = "downloads"
    os.makedirs(output_path, exist_ok=True)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'cookiefile': '/teamspace/studios/this_studio/cookies.txt',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info).replace(".webm", ".mp3").replace(".m4a", ".mp3")
        
    return filename, f"Downloaded: {filename}"

def play_audio(url):
    filename, message = download_audio(url)
    return filename

iface = gr.Interface(
    fn=play_audio,
    inputs=gr.Textbox(label="YT TEST"),
    outputs=gr.Audio(label="Downloaded Audio"),
    title="YTEST Downloader",
    description="Enter a YouTube or YouTube Music URL to download and play the song."
)

if __name__ == "__main__":
    iface.launch(share=True)

