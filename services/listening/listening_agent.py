"""
!!! JUST FOR TESTING !!! BOT DOES NOT USE IT YET
"""
from langchain_gigachat import GigaChat
from langchain.agents import tool
from services.listening.listening import ListeningGeneration
from langchain.schema import HumanMessage

from config.settings import settings
import urllib3
import requests
import uuid
import wave

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ListeningGeneration:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def get_access_token():
        authorization_key = 'Bearer ' + settings.SALUTE_CREDENTIALS
        url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
        payload = {
            'scope': 'SALUTE_SPEECH_PERS'
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'RqUID': str(uuid.uuid4()),
            'Authorization': authorization_key
        }
        response = requests.request("POST",
                                    url,
                                    headers=headers,
                                    data=payload,
                                    verify=False)

        return response.json()

    def synthesize(self):
        url = "https://smartspeech.sber.ru/rest/v1/text:synthesize"
        headers = {
            'Content-Type': 'application/text',
            'Accept': 'audio/x-wav',
            'Authorization': "Bearer " + self.get_access_token()['access_token']}
        response = requests.request("POST", url,
                                    headers=headers,
                                    data=self.text,
                                    verify=False)
        return response.content

    def create_file(self, filename='output.wav'):
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(24000)
            wf.writeframes(self.synthesize())
            return filename




llm = GigaChat(credentials= "M2RiNDYxMjUtNjhkZC00ODRmLWJjNjktMDNiNDU1ZjkxZTVhOjc5OTljYmU5LTM1ZjEtNGI0Yi04M2MwLTJmYTZiYjgxMGI2Ng==",
               model="GigaChat-2-Max",
               profanity_check=False,
               top_p=0,
               timeout=120,
               verify_ssl_certs=False)



from langgraph.prebuilt import create_react_agent


@tool
def generate_audio(text: str) -> str:
    """Генерирует аудиофайл из текста и возвращает путь к файлу."""
    lg = ListeningGeneration(text)
    filename = f"audio_{uuid.uuid4().hex}.wav"
    lg.create_file(filename)
    return f"Аудиофайл создан: {filename}"


tools = [generate_audio]
agent = create_react_agent(llm, tools=tools, prompt="""Ты помощник, способный создавать аудиофайлы из текста.
Для создания файлов используй доступный инструмент generate_audio.
Например, если нужно создать аудиофайл с текстом "Банан", используй команду generate_audio("Банан").""")

response = agent.invoke({"messages": [HumanMessage(content="создай аудио с словом: банан")]})
print(response)
print(response['messages'][-1].content)