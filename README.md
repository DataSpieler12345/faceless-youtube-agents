# YT Faceless Factory 🚀

Automated production of documentary-style financial videos, modeled after the "ClearValue Tax" YouTube channel. This system uses AI to extract viral patterns, generate scripts, create cinematic visuals, and assemble high-quality videos.

## 🌟 Features
- **Viral DNA Extraction**: Analyzes top-performing videos to mirror successful hooks and pacing.
- **AI Scriptwriting**: Generates engagement-focused financial scripts.
- **Cinematic Visuals**: Automated image generation via Gathos API (optimized for daily quotas).
- **Voice Cloning**: High-fidelity TTS using cloned voices (e.g., 'Josh' style).
- **Automated Assembly**: Full video montage with background music and transitions using FFmpeg.

## 🛠️ Setup Instructions

### 1. Prerequisites
- Python 3.10+
- FFmpeg (installed and added to PATH)
- Git

### 2. Installation
Clone the repository and set up the virtual environment:
```bash
git clone https://github.com/DataSpieler12345/faceless-youtube-agents.git
cd faceless-youtube-agents
python -m venv .venv
# Activate venv (Windows)
.\.venv\Scripts\activate
# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration ⚠️
Create a `.env` file in the root directory. **DO NOT COMMIT THIS FILE.**
```env
GATHOS_IMAGE_API_KEY=your_image_key_here
GATHOS_TTS_API_KEY=your_tts_key_here
ZERNIO_API_KEY=your_zernio_key_here
```
*Note: `.env` is already included in `.gitignore` to prevent accidental leaks.*

## 🚀 Usage
Run the full pipeline for a specific topic:
```bash
python pipeline.py --run-id "my-video-topic" --run-all
```

## 📂 Project Structure
- `lib/`: Core logic and API clients.
- `skills/`: AI prompt engineering and viral DNA frameworks.
- `outputs/`: Generated assets (scripts, images, audio, final videos).
- `state/`: Persistent tracking of pipeline progress.

---
*Created with ❤️ for automated financial education.*
