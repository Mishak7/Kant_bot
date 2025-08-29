from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.main_handlers.languages import TEXTS
from handlers.main_handlers.commands import get_user_language

language = get_user_language(callback.from_user.id)

def back_to_language_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['language_check_keyboard']['grammar_keyboard']['back']}", callback_data="language_check")]
    ])

def translation_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['language_check_keyboard']['grammar_keyboard']['to_russian']}", callback_data='translate_to_russian')],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['language_check_keyboard']['grammar_keyboard']['from_russian']}", callback_data='translate_from_russian')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['language_check_keyboard']['grammar_keyboard']['back']}", callback_data='language_check')],
    ])

def back_to_translation() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['language_check_keyboard']['grammar_keyboard']['back']}", callback_data='language_grammar')]
    ])
