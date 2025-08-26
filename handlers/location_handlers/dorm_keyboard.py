from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def dormitories_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Общежитие №1", callback_data="dormitory_1")],
        [InlineKeyboardButton(text="Общежитие №2", callback_data="dormitory_2")],
        [InlineKeyboardButton(text="Общежитие №3", callback_data="dormitory_3")],
        [InlineKeyboardButton(text="Общежитие №4", callback_data="dormitory_4")],
        [InlineKeyboardButton(text="Общежитие №5", callback_data="dormitory_5")],
        [InlineKeyboardButton(text="Общежитие №6", callback_data="dormitory_6")],
        [InlineKeyboardButton(text="Общежитие №7", callback_data="dormitory_7")],
        [InlineKeyboardButton(text="Общежитие №8", callback_data="dormitory_8")],
        [InlineKeyboardButton(text="Общежитие №9-13", callback_data="dormitory_9")],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="location")]
    ])

def back_to_dormitories_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Назад к общежитиям", callback_data="loc_dormitory_building")]
    ])