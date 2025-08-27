"""
Keyboards for university info
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def back_to_info_keyboard() -> InlineKeyboardMarkup:
    """Go back to uni info keyboard"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='◀️ Назад', callback_data='info')]
    ])