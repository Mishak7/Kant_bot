"""
Keyboard layouts for the main menu and navigation.

This module provides inline keyboards for the bot's main menu
and navigation back button. All keyboards are built using
aiogram's InlineKeyboardMarkup and InlineKeyboardButton.
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_roots_keyboard() -> InlineKeyboardMarkup:
    """Create the main menu keyboard with all available options."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🎓 Информация про университет", callback_data="info")],
            [InlineKeyboardButton(text="📍 Местоположение корпуса", callback_data="location")],
            [InlineKeyboardButton(text="🏘️ Общежития", callback_data="dormitory")],
            [InlineKeyboardButton(text="🏥 Медцентр", callback_data="hospital")],
            [InlineKeyboardButton(text="⚠️ Критические ситуации", callback_data="critical")],
            [InlineKeyboardButton(text="🇷🇺 Проверка русского языка", callback_data="language_check")]
        ]
    )

def back_to_main_keyboard() -> InlineKeyboardMarkup:
    """Create a simple back button keyboard for returning to main menu."""
    return InlineKeyboardMarkup(inline_keyboard=[
                                [InlineKeyboardButton(text="◀️ Назад", callback_data="back_to_main")]]
    )