from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.main_handlers.languages import TEXTS

def back_to_language_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS['ru']['keyboards']['language_check_keyboard']['speaking_keyboard']['back']}", callback_data="language_check")]
    ])