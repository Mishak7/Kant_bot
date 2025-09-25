from langchain_community.llms import GigaChat
<<<<<<< HEAD
from handlers.language_check_handlers.database.prompts.prompt_check_to_russian import prompt_to_russian
from handlers.language_check_handlers.database.prompts.prompt_check_from_russian import prompt_from_russian
from config.settings import settings
from handlers.language_check_handlers.database.prompts.prompt_check_audio import prompt_audio_check
from config.settings import settings
=======
from services.grammar.prompt_to_russian import prompt_to_russian
from services.grammar.prompt_from_russian import prompt_from_russian
from services.listening.prompt_audio_check import prompt_audio_check
from config.settings import settings


>>>>>>> main
def gigachat_response(text: str, to_russian: bool, audio_file: bool):

    llm = GigaChat(
        credentials=settings.GIGA_CREDENTIALS,
        verify_ssl_certs=False,
<<<<<<< HEAD
        model="GigaChat-Pro",
=======
        model="GigaChat-2-Max",
>>>>>>> main
        temperature=0.1
    )

    try:
        response = llm.invoke(prompt_audio_check if audio_file else prompt_to_russian if to_russian else prompt_from_russian + f"Сообщение от пользователя, которое нужно обработать: {text}")
        return response
    except Exception as e:
        print(f"Ошибка: {e}")
        return e