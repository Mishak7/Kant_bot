"""
Keyboard layouts for the main menu and navigation.

This module provides inline keyboards for the bot's main menu
and navigation back button. All keyboards are built using
aiogram's InlineKeyboardMarkup and InlineKeyboardButton.
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.main_handlers.languages import TEXTS
from handlers.main_handlers.commands import get_user_language

language = get_user_language(callback.from_user.id)

def main_roots_keyboard() -> InlineKeyboardMarkup:
    """Creates the main menu keyboard with all available options."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f"🎓 {TEXTS[language]['keyboards']['main_keyboard']['info']}", callback_data="info")],
            [InlineKeyboardButton(text=f"📍 {TEXTS[language]['keyboards']['main_keyboard']['location']}", callback_data="location")],
            [InlineKeyboardButton(text=f"🏘️ {TEXTS[language]['keyboards']['main_keyboard']['dormitory']}", callback_data="dormitory")],
            [InlineKeyboardButton(text=f"🏥 {TEXTS[language]['keyboards']['main_keyboard']['hospital']}", callback_data="hospital")],
            [InlineKeyboardButton(text=f"⚠️ {TEXTS[language]['keyboards']['main_keyboard']['critical']}", callback_data="critical")],
            [InlineKeyboardButton(text=f"🇷🇺 {TEXTS[language]['keyboards']['main_keyboard']['language_check']}", callback_data="language_check")]
        ]
    )

def lenguage_selection() -> InlineKeyboardMarkup:
    """Creates a language selection keyboard at the start"""
    return InlineKeyboardButton(
        inline_keyboard=[
            [InlineKeyboardButton(text='🇷🇺 Русский', callback_data='russian')],
            [InlineKeyboardButton(text='🇬🇧 English', callback_data='english')],
            [InlineKeyboardButton(text='🇫🇷 Français', callback_data='french')],
            [InlineKeyboardButton(text='🇪🇸 Español', callback_data='spanish')],
            [InlineKeyboardButton(text='🇨🇳 中國的', callback_data='chinese')],
            [InlineKeyboardButton(text='🇮🇳 हिंदी', callback_data='indian')]
        ]
    )

def back_to_language_selection() -> InlineKeyboardMarkup:
    """Creates a back button keyboard for language selection"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f'◀️ {TEXTS[language]['keyboards']['language_selection_keyboard']['back']}', callback_data='back_to_language_selection')]
        ]
    )

def back_to_main_keyboard() -> InlineKeyboardMarkup:
    """Creates a simple back button keyboard for returning to main menu."""
    return InlineKeyboardMarkup(inline_keyboard=[
                                [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['main_keyboard']['back']}", callback_data="back_to_main")]]
    )
