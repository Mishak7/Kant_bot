"""
Configuration module for application settings.

This module handles:
- Environment variables loading via dotenv
- Application configuration settings
- Audio processing tools configuration
"""

import os
from dotenv import load_dotenv
from config.logger import logger
from pydub import AudioSegment

try:
    load_dotenv()
except Exception as e:
    logger.error(f'.env load failed {e}')

class Settings:
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    GIGA_CREDENTIALS = os.getenv("GIGA_CREDENTIALS")
    SALUTE_CREDENTIALS = os.getenv("SALUTE_CREDENTIALS")
    FFMPEG_PATH = os.getenv("FFMPEG_PATH", "/opt/homebrew/bin/ffmpeg")
    FFPROBE_PATH = os.getenv("FFPROBE_PATH", "/opt/homebrew/bin/ffprobe")

    def __init__(self):
        """Initializing instruments for audio handling"""
        os.environ["PATH"] += os.pathsep + os.getenv("EXTRA_PATH", "/opt/homebrew/bin")
        AudioSegment.converter = self.FFMPEG_PATH
        AudioSegment.ffprobe = self.FFPROBE_PATH


settings = Settings()


