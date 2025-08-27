"""
!!! JUST FOR TESTING !!! BOT DOES NOT USE IT YET (EXCEPT LISTENINGGENERATION CLASS)
"""
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

test = ListeningGeneration(text='Абезьяны Абезьяныыы')
test.create_file()


