# Shadys Downloader

Este projeto foi criado com carinho para minha namorada, para que ela possa baixar vídeos de forma fácil e rápida sem ter que ver um trilhão de anúncios. 💖

## Principais sites suportados

A ferramenta usa `yt-dlp`, que oferece suporte a centenas de plataformas. Alguns exemplos populares:

- **YouTube** (vídeos, playlists, Shorts)  
- **Instagram Reels**  
- **Twitch** (VODs e lives)  
- E muitos outros: [lista completa aqui](https://ytdl-org.github.io/youtube-dl/supportedsites.html)

## Instalação

Este projeto usa Python e requer pacotes específicos. Siga as instruções abaixo para instalar as dependências.

### Pré-requisitos
- **Python 3.6+**: Baixe e instale em [python.org](https://www.python.org/downloads/)
- **FFmpeg**: Necessário para mesclar áudio e vídeo.
  - **Windows**: Baixe em [ffmpeg.org](https://ffmpeg.org/download.html) e adicione ao PATH.
  - **macOS**: `brew install ffmpeg`
  - **Linux**: `sudo apt install ffmpeg` ou `sudo dnf install ffmpeg`

### Passos

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/coutinho98/vidformygirl
   cd vidformygirl
   ```

2. **(Opcional) Crie um ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install yt-dlp
   ```

4. **Verifique se o FFmpeg está disponível**:
   ```bash
   ffmpeg -version
   ```
   Se não estiver, instale conforme descrito acima.

## Uso

- Execute a aplicação:
  ```bash
  python main.py
  ```
- Insira a URL do vídeo ou playlist quando solicitado.
- Escolha a pasta de saída (opcional).

## Notas

- Mantenha o `yt-dlp` atualizado:
  ```bash
  pip install --upgrade yt-dlp
  ```
- Para suporte completo de formatos e opções avançadas, consulte a [documentação oficial do yt-dlp](https://github.com/yt-dlp/yt-dlp).
