"""
Keyboard to choose from language exercises
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def language_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='\U0001F508 Аудирование', callback_data='language_audio')],
        [InlineKeyboardButton(text='\U0001F4DA Грамматика', callback_data='language_grammar')],
        [InlineKeyboardButton(text='\U0001F4AC Говорение', callback_data='language_speaking')],
        [InlineKeyboardButton(text='◀️ Назад', callback_data='back_to_main')],
    ])

