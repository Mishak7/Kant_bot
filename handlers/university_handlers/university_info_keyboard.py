"""
Keyboards for university info
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.main_handlers.languages import TEXTS

def info_keyboard(language: str) -> InlineKeyboardMarkup:
    """Generates an information menu keyboard for university-related details."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"📅 {TEXTS[language]['keyboards']['university_info_keyboard']['schedule']}", callback_data="schedule")],
        [InlineKeyboardButton(text=f"💰 {TEXTS[language]['keyboards']['university_info_keyboard']['scholarship']}", callback_data="scholarship")],
        [InlineKeyboardButton(text=f"📞 {TEXTS[language]['keyboards']['university_info_keyboard']['office_contacts']}", callback_data="office_contacts")],
        [InlineKeyboardButton(text=f"🌍 {TEXTS[language]['keyboards']['university_info_keyboard']['visa_center']}", callback_data="visa_center")],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['university_info_keyboard']['back']}", callback_data="back_to_main")]
    ])

def back_to_info_keyboard(language: str) -> InlineKeyboardMarkup:
    """Go back to uni info keyboard"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['university_info_keyboard']['back']}", callback_data='info')]
    ])

def schedule_info_keyboard(language: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text= f"📅 {TEXTS[language]['keyboards']['university_info_keyboard']['schedule']}" , url="https://schedule.kantiana.ru/")],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['university_info_keyboard']['back']}",
                              callback_data='info')]
    ])

def scholarship_info_keyboard(language: str) -> InlineKeyboardMarkup:
    """Go back to uni info keyboard"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"💰{TEXTS[language]['keyboards']['university_info_keyboard']['scholarship']}", url="https://kantiana.ru/students/scholarship/")],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['university_info_keyboard']['back']}", callback_data='info')]
    ])

def visa_info_keyboard(language: str) -> InlineKeyboardMarkup:
    """Go back to uni info keyboard"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"🌍 {TEXTS[language]['keyboards']['university_info_keyboard']['visa_center']}", url="https://kantiana.ru/universitys/administration/mezhdunarodnyy-ofis/")],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['university_info_keyboard']['back']}", callback_data='info')]
    ])



