from yt_dlp import YoutubeDL
import os

os.environ["PATH"] += os.pathsep + "C:\\ffmpeg\\bin"

def download_video(url):
    ydl_opts={
        'format':'bv*[height<=1080][ext=mp4]+ba[ext=m4a]/b[ext=mp4]',
        'merge_output_format':'mp4',
        'outtmpl':'%(title)s%(ext)s'
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

url = "영상링크" 
download_video(url)