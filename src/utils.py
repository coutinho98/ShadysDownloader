from urllib.parse import urlparse

def validateURL(url: str):
    return url.startswith(('http://', 'https://'))

def getFileName(info: str):
    return f"{info['title']}.{info.get('ext', 'mkv')}"