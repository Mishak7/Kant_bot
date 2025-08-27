from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def back_to_language_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Назад к проверке", callback_data="language_check")]
    ])

def translation_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Перевести на русский', callback_data='translate_to_russian')],
        [InlineKeyboardButton(text='Перевести с русского', callback_data='translate_from_russian')],
        [InlineKeyboardButton(text='◀️ Назад', callback_data='language_check')],
    ])

def back_to_translation() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='◀️ Назад к выбору', callback_data='language_grammar')]
    ])