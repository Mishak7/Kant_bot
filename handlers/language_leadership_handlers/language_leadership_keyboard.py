from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def language_leadership_or_level_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📝 Перейти к заданиям:', callback_data='go_to_levels')],
        [InlineKeyboardButton(text='🏆 Доска лидеров', callback_data='leadership_board')],
        [InlineKeyboardButton(text=f"◀️ Назад", callback_data='back_to_main')]
    ])