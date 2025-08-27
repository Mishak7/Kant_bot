from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def back_to_language_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Назад к проверке", callback_data="language_check")]
    ])