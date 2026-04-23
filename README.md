<p align="center">
  <img src="assets/banner.png" alt="YT Faceless Factory Banner" width="100%">
</p>

<h1 align="center">🎥 YT Faceless Factory</h1>

<p align="center">
  <strong>Automating the production of high-retention financial documentaries.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/FFmpeg-Ready-green?style=for-the-badge&logo=ffmpeg" alt="FFmpeg">
  <img src="https://img.shields.io/badge/AI-Powered-gold?style=for-the-badge&logo=openai" alt="AI">
  <img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge" alt="License">
</p>

---

## 🚀 Overview
**YT Faceless Factory** is a multi-stage production pipeline designed to clone the success of channels like *ClearValue Tax*. It automates everything from viral trend analysis to final video assembly.

### ✨ Key Features
- 🧬 **Viral DNA Extraction**: Advanced scraping and analysis of competitor transcripts.
- ✍️ **Engaged Scriptwriting**: AI-driven narratives focused on retention loops and blunt "news-style" hooks.
- 🖼️ **Cinematic Asset Generation**: Automated 16:9 photorealistic image generation via Gathos API.
- 🎙️ **High-Fidelity Voiceover**: Professional TTS with custom-cloned financial voices.
- 🎬 **Automated Montage**: Seamless assembly of clips, transitions, and background music.

## 🛠️ Tech Stack
| Component | Technology |
| :--- | :--- |
| **Logic** | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) |
| **Video Processing** | ![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white) |
| **Data Fetching** | ![yt-dlp](https://img.shields.io/badge/yt--dlp-FF0000?style=for-the-badge&logo=youtube&logoColor=white) |
| **Environment** | ![dotenv](https://img.shields.io/badge/dotenv-ECD53F?style=for-the-badge&logo=dotenv&logoColor=black) |

## 📦 Setup & Installation

### 1️⃣ Clone & Prepare
```bash
git clone https://github.com/DataSpieler12345/faceless-youtube-agents.git
cd faceless-youtube-agents
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2️⃣ Configure Secrets 🔑
Create a `.env` file in the root. **This file is ignored by Git.**
```env
GATHOS_IMAGE_API_KEY=your_key
GATHOS_TTS_API_KEY=your_key
ZERNIO_API_KEY=your_key
```

## 🎯 How to Run
To generate a full video from a topic:
```bash
python pipeline.py --run-id "inflation-2026" --run-all
```

---
<p align="center">
  <i>Developed for the next generation of financial educators.</i>
</p>
