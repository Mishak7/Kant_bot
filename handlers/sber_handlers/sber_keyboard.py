from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def sber_keyboard(language: str) -> InlineKeyboardMarkup:
    """Creates main keyboard for sber handlers"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🎓 Образовательный кредит", callback_data="educational_loan")],
            [InlineKeyboardButton(text="💳 Карта для стипендии", callback_data="sber_card")],
            [InlineKeyboardButton(text="🔗 Полезные ссылки", callback_data="useful_links")],
            [InlineKeyboardButton(text='◀️ Назад', callback_data='back_to_main')]

        ]
    )

def card_keyboard(language: str) -> InlineKeyboardMarkup:
    """Go to sber cards info"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='🔗 Подробнее', url='https://kantiana.ru/students/scholarship/sber/')],
        [InlineKeyboardButton(text='◀️ Назад', callback_data='sber')]
    ])

def loan_keyboard(language: str) -> InlineKeyboardMarkup:
    """Go to loan info - MAY BE OUTDATED, WEBSITE MADE BY NOVGU!!!"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='🔗 Подробнее', url='https://telegra.ph/Obrazovatelnyj-kredit-06-19')],
        [InlineKeyboardButton(text='◀️ Назад', callback_data='sber')]
    ])

def back_to_sber_keyboard(language: str) -> InlineKeyboardMarkup:
    """Go back to main sber keyboard"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='◀️ Назад', callback_data='sber')]
    ])


