from yt_dlp import YoutubeDL
from .utils import validateURL, getFileName

def downloadVideo(url: str, options):
    if not validateURL(url):
        raise ValueError("Invalid URL")
    try:
        with YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=True)
            return f"Downloaded: {getFileName(info)} in {info.get('height', 'Unknown Resolution')}p"
    except Exception as e:
        return f"Error: {e}"

def downloadVideoMKV(url: str):
    from .config import videoOptions
    return downloadVideo(url, videoOptions)

def downloadVideoMP4(url: str):
    from .config import videoOptionsMP4
    return downloadVideo(url, videoOptionsMP4)

def downloadAudio(url: str):
    from .config import audioOptions
    return downloadVideo(url, audioOptions)