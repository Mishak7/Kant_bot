from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def language_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='\U0001F508 Аудирование', callback_data='language_audio')],
        [InlineKeyboardButton(text='\U0001F4DA Грамматика', callback_data='language_grammar')],
        [InlineKeyboardButton(text='\U0001F4AC Говорение', callback_data='language_speaking')],
        [InlineKeyboardButton(text='◀️ Назад', callback_data='back_to_main')],
    ])


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