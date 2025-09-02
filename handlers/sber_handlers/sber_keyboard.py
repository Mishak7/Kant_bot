from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.main_handlers.languages import TEXTS

def sber_keyboard(language: str) -> InlineKeyboardMarkup:
    """Creates main keyboard for sber handlers"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f"🎓 {TEXTS[language]['keyboards']['sbeк_keyboard']['educational_loan']}", callback_data="educational_loan")],
            [InlineKeyboardButton(text=f"💳 {TEXTS[language]['keyboards']['sber_keyboard']['sber_card']}", callback_data="sber_card")],
            [InlineKeyboardButton(text=f"🔗 {TEXTS[language]['keyboards']['sber_keyboard']['useful_links']}", callback_data="useful_links")],
            [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['sber_keyboard']['back']}", callback_data='back_to_main')]

        ]
    )

def card_keyboard(language: str) -> InlineKeyboardMarkup:
    """Go to sber cards info"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"🔗 {TEXTS[language]['keyboards']['sber_keyboard']['details']}", url='https://kantiana.ru/students/scholarship/sber/')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['sber_keyboard']['back']}", callback_data='sber')]
    ])

def loan_keyboard(language: str) -> InlineKeyboardMarkup:
    """Go to loan info - MAY BE OUTDATED, WEBSITE MADE BY NOVGU!!!"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"🔗 {TEXTS[language]['keyboards']['sber_keyboard']['details']}", url='https://telegra.ph/Obrazovatelnyj-kredit-06-19')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['sber_keyboard']['back']}", callback_data='sber')]
    ])

def back_to_sber_keyboard(language: str) -> InlineKeyboardMarkup:
    """Go back to main sber keyboard"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['sber_keyboard']['back']}", callback_data='sber')]
    ])


