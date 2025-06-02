import sys
import os

baseDirectory = os.path.dirname(os.path.abspath(__file__))

videoDirectory = os.path.join(baseDirectory, 'video')
audioDirectory = os.path.join(baseDirectory, 'audio')

os.makedirs(videoDirectory, exist_ok=True)
os.makedirs(audioDirectory, exist_ok=True)

baseOptions = {
    'progress_hooks': [lambda d: print(f"Progress: {d['_percent_str']} (frag {d.get('fragment_index', 0)}/{d.get('fragment_count', 'desconhecido')})") if d['status'] == 'downloading' else None],
}

videoOptions = {
    **baseOptions,
    'format': 'bestvideo[height<=2160][ext=mp4]+bestaudio/best[height<=2160]/best',
    'outtmpl': os.path.join(videoDirectory, '%(title)s.%(ext)s'),
    'merge_output_format': 'mkv',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mkv',
    }],
}

videoOptionsMP4 = {
    **baseOptions,
    'format': 'bv*[ext=mp4]+ba[ext=m4a]/mp4',
    'outtmpl': os.path.join(videoDirectory, '%(title)s.%(ext)s'),
    'merge_output_format': 'mp4',
    'keep': True,
    'postprocessors': [
        {
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
}

audioOptions = {
    **baseOptions,
    'format': 'bestaudio[ext=m4a]/bestaudio[ext=mp3]/bestaudio',
    'outtmpl': os.path.join(audioDirectory, '%(title)s.%(ext)s'),
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320', 
        }
    ],
    'keep': True,
    'nopost': False,
}