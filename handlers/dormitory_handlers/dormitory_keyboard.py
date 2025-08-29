"""
Keyboards for handlers of dormitory info.
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.main_handlers.languages import TEXTS

def dormitory_keyboard() -> InlineKeyboardMarkup:
    """Create the dormitory keyboard with all available options."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"🏠 {TEXTS['ru']['keyboards']['dormitory_keyboard']['check-in']}", callback_data="dormitory_check-in")],
        [InlineKeyboardButton(text=f"💵 {TEXTS['ru']['keyboards']['dormitory_keyboard']['payment']}", callback_data="dormitory_payment")],
        [InlineKeyboardButton(text=f"📍 {TEXTS['ru']['keyboards']['dormitory_keyboard']['address']}", callback_data="dormitory_address")],
        [InlineKeyboardButton(text=f"📖 {TEXTS['ru']['keyboards']['dormitory_keyboard']['rules']}", callback_data="dormitory_rules")],
        [InlineKeyboardButton(text=f"🧺 {TEXTS['ru']['keyboards']['dormitory_keyboard']['laundry']}", callback_data="dormitory_laundry")],
        [InlineKeyboardButton(text=f"◀️ {TEXTS['ru']['keyboards']['dormitory_keyboard']['back']}", callback_data="back_to_main")]
    ])

def dormitory_check_in_keyboard() -> InlineKeyboardMarkup:
    """Create the keyboard to go back to the dormitory menu or open branch with certificates"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"❌ {TEXTS['ru']['keyboards']['dormitory_keyboard']['no_certificate']}", callback_data="no_certificate")],
        [InlineKeyboardButton(text=f"◀️ {TEXTS['ru']['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory")]
    ])

def back_to_dormitory_keyboard():
    """Create the keyboard to go back to the dormitory menu"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS['ru']['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory")]
    ])


def dormitories_keyboard_back_to_dormitory_info() -> InlineKeyboardMarkup:
    """Create the keyboard to choose between the dormitory buildings"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"🪖 {TEXTS['ru']['keyboards']['dormitory_keyboard']['dormitory_1']} №1",callback_data="dormitory_1"),
        InlineKeyboardButton(text=f"📝 {TEXTS['ru']['keyboards']['dormitory_keyboard']['dormitory_2']} №2", callback_data="dormitory_2")],
        [InlineKeyboardButton(text=f"🛡️ {TEXTS['ru']['keyboards']['dormitory_keyboard']['dormitory_3']} №3", callback_data="dormitory_3"),
        InlineKeyboardButton(text=f"🗡 {TEXTS['ru']['keyboards']['dormitory_keyboard']['dormitory_4']} №4", callback_data="dormitory_4")],
        [InlineKeyboardButton(text=f"🎻 {TEXTS['ru']['keyboards']['dormitory_keyboard']['dormitory_5']} №5", callback_data="dormitory_5"),
        InlineKeyboardButton(text=f"🌊 {TEXTS['ru']['keyboards']['dormitory_keyboard']['dormitory_6']} №6", callback_data="dormitory_6")],
        [InlineKeyboardButton(text=f"🌲 {TEXTS['ru']['keyboards']['dormitory_keyboard']['dormitory_7']} №7", callback_data="dormitory_7"),
        InlineKeyboardButton(text=f"🎄 {TEXTS['ru']['keyboards']['dormitory_keyboard']['dormitory_8']} №8", callback_data="dormitory_8")],
        [InlineKeyboardButton(text=f"🎉  {TEXTS['ru']['keyboards']['dormitory_keyboard']['dormitory_9']} №9-13", callback_data="dormitory_9"),
        InlineKeyboardButton(text=f"◀️ {TEXTS['ru']['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory")]
    ])

def back_to_addresses_keyboard():
    """Create the keyboard to go back to the choice of dormitory addresses"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS['ru']['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory_address")]
    ])

def back_to_check_in_keyboard():
    """Create the keyboard to go back to the dormitory check-in menu"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS['ru']['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory_check-in")]
    ])


def payment_keyboard():
    """Create the keyboard to go back to the dormitory check-in menu"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"🏦 {TEXTS['ru']['keyboards']['dormitory_keyboard']['sber_payment']}", url="http://sberbank.com/sms/shpa/?cs=1444813186989&psh=p&did=1756363598644000596")],
        [InlineKeyboardButton(text=f"◀️ {TEXTS['ru']['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory")]
    ])
