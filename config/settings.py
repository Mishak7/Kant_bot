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
    # Путь к ффмпег
    FFMPEG_PATH = os.getenv("FFMPEG_PATH", "/opt/homebrew/bin/ffmpeg")
    # Путь к ffprobe
    FFPROBE_PATH = os.getenv("FFPROBE_PATH", "/opt/homebrew/bin/ffprobe")
    # Изменение PATH
    os.environ["PATH"] += os.pathsep + os.getenv("EXTRA_PATH", "/opt/homebrew/bin")

    AudioSegment.converter = os.getenv("FFMPEG_PATH", None)
    AudioSegment.ffprobe = os.getenv("FFPROBE_PATH", None)


settings = Settings()


