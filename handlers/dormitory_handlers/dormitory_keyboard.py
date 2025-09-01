"""
Keyboards for handlers of dormitory info.
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.main_handlers.languages import TEXTS
from handlers.main_handlers.commands import get_user_language

language = get_user_language(callback.from_user.id)

def dormitory_keyboard() -> InlineKeyboardMarkup:
    """Create the dormitory keyboard with all available options."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"🏠 {TEXTS[language]['keyboards']['dormitory_keyboard']['check-in']}", callback_data="dormitory_check-in")],
        [InlineKeyboardButton(text=f"💵 {TEXTS[language]['keyboards']['dormitory_keyboard']['payment']}", callback_data="dormitory_payment")],
        [InlineKeyboardButton(text=f"📍 {TEXTS[language]['keyboards']['dormitory_keyboard']['address']}", callback_data="dormitory_address")],
        [InlineKeyboardButton(text=f"📖 {TEXTS[language]['keyboards']['dormitory_keyboard']['rules']}", callback_data="dormitory_rules")],
        [InlineKeyboardButton(text=f"🧺 {TEXTS[language]['keyboards']['dormitory_keyboard']['laundry']}", callback_data="dormitory_laundry")],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['dormitory_keyboard']['back']}", callback_data="back_to_main")]
    ])

def dormitory_check_in_keyboard() -> InlineKeyboardMarkup:
    """Create the keyboard to go back to the dormitory menu or open branch with certificates"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"❌ {TEXTS[language]['keyboards']['dormitory_keyboard']['no_certificate']}", callback_data="no_certificate")],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory")]
    ])

def back_to_dormitory_keyboard():
    """Create the keyboard to go back to the dormitory menu"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory")]
    ])


def dormitories_keyboard_back_to_dormitory_info() -> InlineKeyboardMarkup:
    """Create the keyboard to choose between the dormitory buildings"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['dormitory_location_keyboard']['dormitory_1']}", callback_data="dormitory_1")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['dormitory_location_keyboard']['dormitory_2']}", callback_data="dormitory_2")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['dormitory_location_keyboard']['dormitory_3']}", callback_data="dormitory_3")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['dormitory_location_keyboard']['dormitory_4']}", callback_data="dormitory_4")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['dormitory_location_keyboard']['dormitory_5']}", callback_data="dormitory_5")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['dormitory_location_keyboard']['dormitory_6']}", callback_data="dormitory_6")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['dormitory_location_keyboard']['dormitory_7']}", callback_data="dormitory_7")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['dormitory_location_keyboard']['dormitory_8']}", callback_data="dormitory_8")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['dormitory_location_keyboard']['dormitory_9']}", callback_data="dormitory_9")],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory")]
    ])

def back_to_addresses_keyboard():
    """Create the keyboard to go back to the choice of dormitory addresses"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory_address")]
    ])

def back_to_check_in_keyboard():
    """Create the keyboard to go back to the dormitory check-in menu"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory_check-in")]
    ])

def payment_keyboard():
    """Create the keyboard for payment ways"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['payment_keyboard']['sber_payment']}", callback_data="sber_payment")],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['payment_keyboard']['back']}", callback_data="dormitory")]
    ])
