"""
Keyboards for handlers of critical info.
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def critical_keyboard() -> InlineKeyboardMarkup:
    """Creates a keyboard layout for emergency contacts."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='\U0001F46E Полиция', callback_data='critical_police')],
        [InlineKeyboardButton(text='\U0001F4DE Горячая линия ФМС', callback_data='critical_hotline')],
        [InlineKeyboardButton(text='\U0001F3EC Местные органы власти', callback_data='critical_government')],
        [InlineKeyboardButton(text='\U0001F3E2 Консульство', callback_data='critical_consulate')],
        [InlineKeyboardButton(text='◀️ Назад', callback_data='back_to_main')]
    ])

def info_keyboard() -> InlineKeyboardMarkup:
    """Generates an information menu keyboard for university-related details."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📅 Расписание", callback_data="schedule")],
        [InlineKeyboardButton(text="💰 Стипендии", callback_data="scholarship")],
        [InlineKeyboardButton(text="📞 Контакты учебного офиса", callback_data="office_contacts")],
        [InlineKeyboardButton(text="🌍 Визово-миграционный центр", callback_data="visa_center")],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="back_to_main")]
    ])

def back_to_critical_keyboard():
    """Returns a single-button keyboard to go back to the 'Critical' section."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Назад к критическим ситуациям", callback_data="critical")]
    ])