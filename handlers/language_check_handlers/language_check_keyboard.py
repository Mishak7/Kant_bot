"""
Keyboard to choose from language exercises
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.main_handlers.languages import TEXTS

def language_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"\U0001F508 {TEXTS['ru']['keyboards']['language_check_keyboard']['language_check_keyboard']['audio']}", callback_data='language_audio')],
        [InlineKeyboardButton(text=f"\U0001F4DA {TEXTS['ru']['keyboards']['language_check_keyboard']['language_check_keyboard']['grammar']}", callback_data='language_grammar')],
        [InlineKeyboardButton(text=f"\U0001F4AC {TEXTS['ru']['keyboards']['language_check_keyboard']['language_check_keyboard']['speaking']}", callback_data='language_speaking')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS['ru']['keyboards']['language_check_keyboard']['language_check_keyboard']['back']}", callback_data='back_to_main')],
    ])

