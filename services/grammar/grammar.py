from langchain_community.llms import GigaChat
from services.grammar.prompt_to_russian import prompt_to_russian
from services.grammar.prompt_from_russian import prompt_from_russian
from config.settings import settings
from services.listening.prompt_audio_check import prompt_audio_check

def gigachat_response(translation: str, to_russian: bool, audio_file: bool):

    llm = GigaChat(
        credentials=settings.GIGA_CHAT_CREDENTIALS,
        verify_ssl_certs=False,
        model="GigaChat-Pro",
        temperature=0.1
    )

    try:
        response = llm.invoke(prompt_audio_check if audio_file else prompt_to_russian if to_russian else prompt_from_russian)
        return response
    except Exception as e:
        print(f"Ошибка: {e}")
        return e