from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.main_handlers.languages import TEXTS


def back_to_language_keyboard(language: str):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['language_check_keyboard']['grammar_keyboard']['back']}", callback_data="language_check")]
    ])

def translation_keyboard(language: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['language_check_keyboard']['grammar_keyboard']['to_russian']}", callback_data='translate_to_russian')],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['language_check_keyboard']['grammar_keyboard']['from_russian']}", callback_data='translate_from_russian')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['language_check_keyboard']['grammar_keyboard']['back']}", callback_data='language_check')],
    ])

def back_to_translation(language: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['language_check_keyboard']['grammar_keyboard']['back']}", callback_data='language_grammar')]
    ])