# vidformygirl

Este projeto foi criado com carinho para minha namorada, para que ela possa baixar vídeos do YouTube de forma fácil e rápida sem ter que ver um trilhão de anúncios. 💖

## Instalação

Este projeto usa Python e requer pacotes específicos. Siga as instruções abaixo para instalar as dependências.

### Pré-requisitos
- **Python 3.6+**: Baixe e instale em [python.org](https://www.python.org/downloads/).
- **FFmpeg**: Necessário para mesclar áudio e vídeo.
  - **Windows**: Baixe em [ffmpeg.org](https://ffmpeg.org/download.html) e adicione ao PATH.
  - **macOS**: `brew install ffmpeg` (com [Homebrew](https://brew.sh/)).
  - **Linux**: `sudo apt install ffmpeg` (Debian/Ubuntu) ou `sudo dnf install ffmpeg` (Fedora).

### Passos
1. **Clone o repositório** (ou copie o script):
   ```bash
   git clone <https://github.com/coutinho98/vidformygirl>
   cd <vidformygirl>
   ```

2. **Crie um ambiente virtual** (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale os pacotes Python**:
   ```bash
   pip install yt-dlp
   ```

4. **Verifique o FFmpeg**:
   ```bash
   ffmpeg -version
   ```
   Se não funcionar, instale o FFmpeg conforme acima.

### Uso
- Execute o script:
  ```bash
  python main.py
  ```
- Insira a URL do vídeo do YouTube quando solicitado.
- Escolha a pasta de saída (opcional).

### Notas
- Mantenha o `yt-dlp` atualizado: `pip install --upgrade yt-dlp`.
- Para suporte a playlists ou outras opções, consulte o código ou a documentação do [yt-dlp](https://github.com/yt-dlp/yt-dlp).