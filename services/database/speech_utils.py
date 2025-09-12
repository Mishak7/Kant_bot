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

def transcribe_voice_message(file_path: str):
    """Конвертация и транскрипция голосового сообщения"""
    token = salute_speech_token()

    audio = AudioSegment.from_file(file_path, format="ogg")
    audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
    audio.export("audio.raw", format="raw")

    with open("audio.raw", "rb") as f:
        audio_data = f.read()

    url = "https://smartspeech.sber.ru/rest/v1/speech:recognize"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "audio/x-pcm;bit=16;rate=16000"
    }
    params = {"model": "general", "language": "ru-RU"}

    response = requests.post(url, headers=headers, params=params, data=audio_data, verify=False)
    result_json = response.json()

    salute_text = ''.join(result_json.get('result', []))
    return salute_text

def text_to_speech(text: str, filename: str = "temp.wav") -> str:
    """
    To get path of the file
    """
    lg = ListeningGeneration(text)
    lg.create_file(filename)
    return filename