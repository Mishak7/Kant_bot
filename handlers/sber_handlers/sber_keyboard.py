from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
<<<<<<< HEAD
from handlers.main_handlers.commands import get_user_language
from handlers.main_handlers.languages import TEXTS

language = get_user_language(callback.from_user.id)

def sber_keyboard() -> InlineKeyboardMarkup:
=======
from handlers.main_handlers.languages import TEXTS

def sber_keyboard(language: str) -> InlineKeyboardMarkup:
>>>>>>> main
    """Creates main keyboard for sber handlers"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f"🎓 {TEXTS[language]['keyboards']['sber_keyboard']['educational_loan']}", callback_data="educational_loan")],
            [InlineKeyboardButton(text=f"💳 {TEXTS[language]['keyboards']['sber_keyboard']['sber_card']}", callback_data="sber_card")],
            [InlineKeyboardButton(text=f"🔗 {TEXTS[language]['keyboards']['sber_keyboard']['useful_links']}", callback_data="useful_links")],
<<<<<<< HEAD
            [InlineKeyboardButton(text=f'◀️ {TEXTS[language]['keyboards']['sber_keyboard']['back']}', callback_data='back_to_main')]
=======
            [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['sber_keyboard']['back']}", callback_data='back_to_main')]
>>>>>>> main

        ]
    )

<<<<<<< HEAD
def card_keyboard() -> InlineKeyboardMarkup:
    """Go to sber cards info"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f'🔗 {TEXTS[language]['keyboards']['sber_keyboard']['details']}', url='https://kantiana.ru/students/scholarship/sber/')],
        [InlineKeyboardButton(text=f'◀️ {TEXTS[language]['keyboards']['sber_keyboard']['back']}', callback_data='sber')]
    ])

def loan_keyboard() -> InlineKeyboardMarkup:
    """Go to loan info - MAY BE OUTDATED, WEBSITE MADE BY NOVGU!!!"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f'🔗 {TEXTS[language]['keyboards']['sber_keyboard']['details']}', url='https://telegra.ph/Obrazovatelnyj-kredit-06-19')],
        [InlineKeyboardButton(text=f'◀️ {TEXTS[language]['keyboards']['sber_keyboard']['back']}', callback_data='sber')]
    ])

def back_to_sber_keyboard() -> InlineKeyboardMarkup:
    """Go back to main sber keyboard"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f'◀️ {TEXTS[language]['keyboards']['sber_keyboard']['back']}', callback_data='sber')]
    ])
=======
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


>>>>>>> main
