from langchain_gigachat.chat_models import GigaChat
from langchain.schema import SystemMessage, HumanMessage
from services.listening.listening import ListeningGeneration
from config.settings import settings
from typing import Optional
import requests
from pydub import AudioSegment
import tempfile
import os
<<<<<<< HEAD
from handlers.language_check_handlers.database.prompts.prompt_check_speaking import system_prompt
=======
from services.speaking.speaking_prompt import system_prompt
>>>>>>> main

class SpeakingAnalyzer(ListeningGeneration):
    def __init__(self, text: str):
        super().__init__(text)
        self.transcribed_text: Optional[str] = None
        self.gigachat = self._initialize_gigachat()
        self.system_prompt = system_prompt

    @staticmethod
    def _initialize_gigachat() -> GigaChat:
        """Инициализация GigaChat клиента"""
        try:
            gigachat = GigaChat(
                credentials=settings.GIGA_CREDENTIALS,
                scope="GIGACHAT_API_PERS",
<<<<<<< HEAD
                model='GigaChat-Pro',
=======
                model='GigaChat-2-Max',
>>>>>>> main
                verify_ssl_certs=False
            )
            return gigachat
        except Exception as e:
            raise Exception(f"Ошибка инициализации GigaChat: {e}")

    def transcribe(self, audio_path: str) -> str:
        """Транскрибация аудиофайла"""
        token = self.get_access_token()['access_token']

        audio = AudioSegment.from_file(audio_path)
        audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "audio/x-pcm;bit=16;rate=16000"
        }
        params = {"model": "general", "language": "ru-RU"}

        response = requests.post(
            "https://smartspeech.sber.ru/rest/v1/speech:recognize",
            headers=headers,
            params=params,
            data=audio.raw_data,
            verify=False
        )

        result = response.json()
        print(result)

        self.transcribed_text = ''.join(result['result'])
        return self.transcribed_text

    def compare_with_original(self, audio_path: str) -> str:
        """Сравнение исходного текста с транскрибированным через GigaChat"""
        transcribed = self.transcribe(audio_path)
        print(transcribed)

        response = self.gigachat.invoke([
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=f"Транскрипция: {transcribed}. Тема {self.text}"),
        ])
        return response.content

    async def process_voice_message(self, file_content: bytes, bot=None) -> str:
        """Обработка голосового сообщения из bytes"""
        with tempfile.NamedTemporaryFile(delete=False, suffix='.ogg') as temp_file:
            temp_file.write(file_content)
            temp_path = temp_file.name
            print(temp_path)

        try:
            result = self.compare_with_original(temp_path)
            return result
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)