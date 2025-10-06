import uuid
import requests
from pydub import AudioSegment
from config.settings import Settings
from services.listening.listening import ListeningGeneration

def salute_speech_token():
    """Получение токена для SberSpeech"""
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "RqUID": str(uuid.uuid4()),
        "Authorization": f"Basic {Settings.SALUTE_CREDENTIALS}",
    }
    data = {"scope": "SALUTE_SPEECH_PERS"}

    response = requests.post(url, headers=headers, data=data, verify=False)

    return response.json()['access_token']


def transcribe_voice_message(file_path: str) -> str:
    """Оптимизированная версия с буферизацией в памяти"""
    token = salute_speech_token()
    audio = AudioSegment.from_file(file_path, format="ogg")
    audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)

    max_length_ms = 60000
    full_text = ""

    if len(audio) <= max_length_ms:
        full_text = process_audio_in_memory(audio, token)
    else:
        for i in range(0, len(audio), max_length_ms):
            segment = audio[i:i + max_length_ms]
            segment_text = process_audio_in_memory(segment, token)
            full_text += segment_text + " "

    return full_text.strip()


def process_audio_in_memory(audio_segment: AudioSegment, token: str) -> str:
    """Обработка аудио без создания временных файлов"""
    try:
        audio_buffer = audio_segment.export(format="raw").read()

        url = "https://smartspeech.sber.ru/rest/v1/speech:recognize"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "audio/x-pcm;bit=16;rate=16000"
        }
        params = {"model": "general", "language": "ru-RU"}

        response = requests.post(url, headers=headers, params=params, data=audio_buffer, verify=False)
        result_json = response.json()

        return ''.join(result_json.get('result', []))

    except Exception as e:
        print(f"Ошибка при обработке аудио: {e}")
        return ""

def text_to_speech(text: str, filename: str = "temp.wav") -> str:
    """
    To get path of the file
    """
    lg = ListeningGeneration(text)
    lg.create_file(filename)
    return filename