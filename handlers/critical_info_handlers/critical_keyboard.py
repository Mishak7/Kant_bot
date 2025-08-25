from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def critical_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='\U0001F46E Полиция', callback_data='critical_police')],
        [InlineKeyboardButton(text='\U0001F4DE Горячая линия ФМС', callback_data='critical_hotline')],
        [InlineKeyboardButton(text='\U0001F3EC Местные органы власти', callback_data='critical_government')],
        [InlineKeyboardButton(text='\U0001F3E2 Консульство', callback_data='critical_consulate')],
        [InlineKeyboardButton(text='◀️ Назад', callback_data='back_to_main')]
    ])

def back_to_critical_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Назад к критическим ситуациям", callback_data="critical")]
    ])