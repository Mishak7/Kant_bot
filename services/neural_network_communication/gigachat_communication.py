from langchain_gigachat.chat_models import GigaChat
from config.settings import Settings

async def gigachat_response(text: str, prompt: str):
    llm = GigaChat(
        credentials=Settings.GIGA_CREDENTIALS,
        verify_ssl_certs=False,
        model="GigaChat-2-Max",
        temperature=0,
        top_p=0.1
    )
    try:
        response = await llm.ainvoke(prompt + f"Сообщение от пользователя, которое нужно обработать: {text}")
        return response
    except Exception as e:
        print(f"Ошибка: {e}")
        return e
