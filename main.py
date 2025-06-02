import customtkinter as ctk
import threading
import os

try:
    from src.downloader import downloadVideoMKV, downloadVideoMP4, downloadAudio
except ImportError:
    print("WARNING: 'src.downloader' not found. Using placeholder functions.")
    def downloadVideoMKV(url):
        import time
        time.sleep(2)
        return f"Simulação: Download MKV concluído para '{url}'"
    def downloadVideoMP4(url):
        import time
        time.sleep(2)
        return f"Simulação: Download MP4 concluído para '{url}'"
    def downloadAudio(url):
        import time
        time.sleep(2)
        return f"Simulação: Download MP3 concluído para '{url}'"

class DownloaderApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.SetupWindow()
        self.SetupTheme()
        self.SetupUI()
        self.is_downloading = False

    def SetupWindow(self):
        self.title("Shadys Media Downloader")
        self.resizable(False, False)
        icon_path = "./image/shadys.ico"
        self.iconbitmap(icon_path)

        window_width = 450
        window_height = 300

        center_x = int((self.winfo_screenwidth() - window_width) / 2)
        center_y = int((self.winfo_screenheight() - window_height) / 2)

        self.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

    def SetupTheme(self):
        ctk.set_appearance_mode("dark")
        self.colors = {
            'primary': '#8B5CF6',
            'primary_hover': '#7C3AED',
            'secondary': '#1F1B24',
            'accent': '#A855F7',
            'accent_hover': '#9333EA',
            'background': '#0D0A14',
            'cardBG': '#1A1625',
            'text_primary': '#E5E7EB',
            'text_secondary': '#9CA3AF',
            'success': '#10B981',
            'warning': '#F59E0B',
            'error': '#EF4444'
        }
        self.configure(fg_color=self.colors['background'])

    def SetupUI(self):
        main_container = ctk.CTkFrame(self, fg_color="transparent")
        main_container.pack(fill="both", expand=True, padx=20, pady=20)

        self.CreateHeader(main_container)
        self.CreateMainCard(main_container)

    def CreateHeader(self, parent):
        title_label = ctk.CTkLabel(
            parent,
            text="Shadys Media Downloader",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=self.colors['text_primary']
        )
        title_label.pack(pady=(0, 10))

    def CreateMainCard(self, parent):
        cardFrame = ctk.CTkFrame(
            parent,
            fg_color=self.colors['cardBG'],
            corner_radius=15
        )
       
        cardFrame.pack(fill="both", expand=True, pady=(0, 20)) 

        content_frame = ctk.CTkFrame(cardFrame, fg_color="transparent")
        content_frame.pack(fill="both", padx=30, pady=20)

        self.CreateUrlInput(content_frame)
        self.CreateDownloadButtons(content_frame)
        self.CreateProgressSection(content_frame)

    def CreateUrlInput(self, parent):
        self.url_entry = ctk.CTkEntry(
            parent,
            placeholder_text="Cole a URL aqui.",
            height=40,
            font=ctk.CTkFont(size=14),
            fg_color=self.colors['secondary'],
            border_color=self.colors['primary'],
            border_width=1,
            corner_radius=8,
            text_color=self.colors['text_primary']
        )
        self.url_entry.pack(fill="x", pady=(0, 20))
        self.url_entry.bind("<Button-3>", self.pasteFromClipboard)

    def pasteFromClipboard(self, event=None):
        try:   
            clipboardContent = self.clipboard_get()
            self.url_entry.delete(0, ctk.END) 
            self.url_entry.insert(0, clipboardContent)
        except ctk.TclError:
            print("Não pode colar aqui!") 
            
    def CreateDownloadButtons(self, parent):
        buttons_container = ctk.CTkFrame(parent, fg_color="transparent")
        buttons_container.pack(pady=(0, 20))

        button_config = {
            'width': 80,
            'height': 35,
            'font': ctk.CTkFont(size=12, weight="bold"),
            'corner_radius': 6
        }

        self.mkv_button = ctk.CTkButton(
            buttons_container,
            text="MKV",
            fg_color=self.colors['primary'],
            hover_color=self.colors['primary_hover'],
            command=lambda: self.StartDownload('mkv'),
            **button_config
        )
        self.mkv_button.pack(side="left", padx=(0, 8))

        self.mp4_button = ctk.CTkButton(
            buttons_container,
            text="MP4",
            fg_color=self.colors['primary'],
            hover_color=self.colors['primary_hover'],
            command=lambda: self.StartDownload('mp4'),
            **button_config
        )
        self.mp4_button.pack(side="left", padx=4)

        self.audio_button = ctk.CTkButton(
            buttons_container,
            text="MP3",
            fg_color=self.colors['accent'],
            hover_color=self.colors['accent_hover'],
            command=lambda: self.StartDownload('audio'),
            **button_config
        )
        self.audio_button.pack(side="left", padx=(8, 0))

    def CreateProgressSection(self, parent):
        self.status_label = ctk.CTkLabel(
            parent,
            text="Aguardando...",
            font=ctk.CTkFont(size=14),
            text_color=self.colors['text_secondary']
        )
        self.status_label.pack(pady=(0, 10))

        self.progress_bar = ctk.CTkProgressBar(
            parent,
            height=3,
            corner_radius=2,
            fg_color=self.colors['secondary'],
            progress_color=self.colors['primary']
        )
        self.progress_bar.pack(fill="x")
        self.progress_bar.set(0)

    def UpdateStatus(self, message, msg_type="info"):
        color_map = {
            "info": self.colors['text_secondary'],
            "success": self.colors['success'],
            "warning": self.colors['warning'],
            "error": self.colors['error']
        }
        color = color_map.get(msg_type, self.colors['text_secondary'])
        self.status_label.configure(text=message, text_color=color)
        self.update()

    def SetDownloadingState(self, downloading, keep_status=False):
        self.is_downloading = downloading
        state = "disabled" if downloading else "normal"

        for button in [self.mkv_button, self.mp4_button, self.audio_button]:
            button.configure(state=state)

        self.url_entry.configure(state=state)

        if downloading:
            self.progress_bar.set(0.3)
            self.UpdateStatus("Processando...", "info")
        elif not keep_status:
            self.progress_bar.set(0)
            self.UpdateStatus("Aguardando...", "info")

    def StartDownload(self, format_type):
        if self.is_downloading:
            return

        url = self.url_entry.get().strip()

        download_functions = {
            'mkv': self.DownloadMKV,
            'mp4': self.DownloadMP4,
            'audio': self.DownloadAudio
        }

        if format_type in download_functions:
            threading.Thread(
                target=download_functions[format_type],
                args=(url,),
                daemon=True
            ).start()

    def DownloadMKV(self, url):
        self.SetDownloadingState(True)
        self.UpdateStatus("Baixando MKV...", "info")

        try:
            result = downloadVideoMKV(url)
            self.UpdateStatus("Arquivo MKV baixado com sucesso!!", "success")
            self.progress_bar.set(1.0)
        except Exception as e:
            self.UpdateStatus("Erro no download MKV", "error")
        finally:
            self.SetDownloadingState(False, keep_status=True)

    def DownloadMP4(self, url):
        self.SetDownloadingState(True)
        self.UpdateStatus("Baixando MP4...", "info")

        try:
            result = downloadVideoMP4(url)
            self.UpdateStatus("Arquivo MP4 baixado com sucesso!", "success")
            self.progress_bar.set(1.0)
        except Exception as e:
            self.UpdateStatus("Erro no download MP4", "error")
        finally:
            self.SetDownloadingState(False, keep_status=True)

    def DownloadAudio(self, url):
        self.SetDownloadingState(True)
        self.UpdateStatus("Baixando MP3...", "info")

        try:
            result = downloadAudio(url)
            self.UpdateStatus("Arquivo MP3 baixado com sucesso!", "success")
            self.progress_bar.set(1.0)
        except Exception as e:
            self.UpdateStatus("Erro no download MP3", "error")
        finally:
            self.SetDownloadingState(False, keep_status=True)

if __name__ == "__main__":
    app = DownloaderApp()
    app.mainloop()