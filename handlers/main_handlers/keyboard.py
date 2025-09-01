"""
Keyboard layouts for the main menu and navigation.

This module provides inline keyboards for the bot's main menu
and navigation back button. All keyboards are built using
aiogram's InlineKeyboardMarkup and InlineKeyboardButton.
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.main_handlers.languages import TEXTS

def main_roots_keyboard(language: str) -> InlineKeyboardMarkup:
    """Create the main menu keyboard with all available options."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f"🎓 {TEXTS[language]['keyboards']['main_keyboard']['info']}", callback_data="info"),
            InlineKeyboardButton(text=f"📍 {TEXTS[language]['keyboards']['main_keyboard']['location']}", callback_data="location")],
            [InlineKeyboardButton(text=f"🏘️ {TEXTS[language]['keyboards']['main_keyboard']['dormitory']}", callback_data="dormitory"),
            InlineKeyboardButton(text=f"🏥 {TEXTS[language]['keyboards']['main_keyboard']['hospital']}", callback_data="hospital")],
            [InlineKeyboardButton(text=f"⚠️ {TEXTS[language]['keyboards']['main_keyboard']['critical']}", callback_data="critical"),
            InlineKeyboardButton(text=f"🇷🇺 {TEXTS[language]['keyboards']['main_keyboard']['language_check']}", callback_data="language_check")],
            [InlineKeyboardButton(text=f"💳 {TEXTS[language]['keyboards']['main_keyboard']['sber']}", callback_data="sber")]
        ]
    )

def back_to_main_keyboard(language: str) -> InlineKeyboardMarkup:
    """Create a simple back button keyboard for returning to main menu."""
    return InlineKeyboardMarkup(inline_keyboard=[
                                [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['main_keyboard']['back']}", callback_data="back_to_main")]]
    )


def language_selection() -> InlineKeyboardMarkup:
    """Creates a language selection keyboard at the start"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🇷🇺 Русский', callback_data='russian'),
            InlineKeyboardButton(text='🇬🇧 English', callback_data='english')],
            [InlineKeyboardButton(text='🇫🇷 Français', callback_data='french'),
            InlineKeyboardButton(text='🇪🇸 Español', callback_data='spanish')],
            [InlineKeyboardButton(text='🇨🇳 中國的', callback_data='chinese'),
            InlineKeyboardButton(text='🇮🇳 हिंदी', callback_data='indian')]
        ]
    )