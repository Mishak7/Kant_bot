"""
Keyboard to choose from language exercises
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.main_handlers.languages import TEXTS

def language_keyboard(language: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['language_check_keyboard']['language_check_keyboard']['back']}", callback_data='back_to_main')],
    ])

def go_to_lessons(language: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"🇷🇺️ {TEXTS[language]['keyboards']['language_check_keyboard']['language_check_keyboard']['to_lessons']}",callback_data='lessons')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['language_check_keyboard']['language_check_keyboard']['back']}", callback_data='back_to_main')],
    ])


