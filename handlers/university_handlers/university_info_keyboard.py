"""
Keyboards for university info
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.main_handlers.languages import TEXTS
from handlers.main_handlers.commands import get_user_language

language = get_user_language(callback.from_user.id)

def info_keyboard() -> InlineKeyboardMarkup:
    """Generates an information menu keyboard for university-related details."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"📅 {TEXTS[language]['keyboards']['university_info_keyboard']['schedule']}", callback_data="schedule")],
        [InlineKeyboardButton(text=f"💰 {TEXTS[language]['keyboards']['university_info_keyboard']['scholarship']}", callback_data="scholarship")],
        [InlineKeyboardButton(text=f"📞 {TEXTS[language]['keyboards']['university_info_keyboard']['office_contacts']}", callback_data="office_contacts")],
        [InlineKeyboardButton(text=f"🌍 {TEXTS[language]['keyboards']['university_info_keyboard']['visa_center']}", callback_data="visa_center")],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['university_info_keyboard']['back']}", callback_data="back_to_main")]
    ])

def back_to_info_keyboard() -> InlineKeyboardMarkup:
    """Go back to uni info keyboard"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['university_info_keyboard']['back']}", callback_data='info')]
    ])
