"""
Keyboards for handlers of critical info.
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

"""
Keyboards for handlers of critical info.
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.main_handlers.languages import TEXTS
from handlers.main_handlers.commands import get_user_language

language = get_user_language(callback.from_user.id)

def critical_keyboard() -> InlineKeyboardMarkup:
    """Creates a keyboard layout for emergency contacts."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"\U0001F46E {TEXTS[language]['keyboards']['critical_keyboard']['police']}", callback_data='critical_police')],
        [InlineKeyboardButton(text=f"\U0001F4DE {TEXTS[language]['keyboards']['critical_keyboard']['hotline']}", callback_data='critical_hotline')],
        [InlineKeyboardButton(text=f"\U0001F3EC {TEXTS[language]['keyboards']['critical_keyboard']['government']}", callback_data='critical_government')],
        [InlineKeyboardButton(text=f"\U0001F3E2 {TEXTS[language]['keyboards']['critical_keyboard']['consulate']}", callback_data='critical_consulate')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['critical_keyboard']['back']}", callback_data='back_to_main')]
    ])

def back_to_critical_keyboard():
    """Returns a single-button keyboard to go back to the 'Critical' section."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['critical_keyboard']['back']}", callback_data="critical")]
    ])
