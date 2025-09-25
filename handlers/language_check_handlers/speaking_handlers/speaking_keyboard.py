from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.main_handlers.languages import TEXTS
<<<<<<< HEAD
from handlers.main_handlers.commands import get_user_language

language = get_user_language(callback.from_user.id)

def back_to_language_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['language_check_keyboard']['speaking_keyboard']['back']}", callback_data="language_check")]
    ])
=======

def back_to_language_keyboard(language: str):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['language_check_keyboard']['speaking_keyboard']['back']}", callback_data="language_check")]
    ])
>>>>>>> main
