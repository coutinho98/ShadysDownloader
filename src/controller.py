from src.downloader import downloadVideoMKV, downloadVideoMP4, downloadAudio

class DownloadController:
    def download(self, url: str, format: str):
        match format:
            case "mkv": return downloadVideoMKV(url)
            case "mp4": return downloadVideoMP4(url)
            case "mp3": return downloadAudio(url)
            case _: raise ValueError(f"Formato inválido: {format}")