from langchain_community.llms import GigaChat
from config.settings import settings

def gigachat_response(text: str, prompt: str):

    llm = GigaChat(
        credentials=settings.GIGA_CREDENTIALS,
        verify_ssl_certs=False,
        model="GigaChat-2-Max",
        temperature=0,
        top_p = 0.1
    )

    try:
        response = llm.invoke(prompt + f"Сообщение от пользователя, которое нужно обработать: {text}")
        return response
    except Exception as e:
        print(f"Ошибка: {e}")
        return e