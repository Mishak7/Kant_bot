from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#Клавиатура, открывающаяся при нажатии на общежития
def dormitory_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏠 Заселение в общежитие", callback_data="dormitory_check-in")],
        [InlineKeyboardButton(text="💵 Оплата", callback_data="dormitory_payment")],
        [InlineKeyboardButton(text="📍 Адреса общежитий", callback_data="dormitory_address")],
        [InlineKeyboardButton(text="📖 Правила проживания", callback_data="dormitory_rules")],
        [InlineKeyboardButton(text="🧺 Прачечная", callback_data="dormitory_laundry")],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="back_to_main")]
    ])

def dormitory_check_in_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="❌ Нет сертификата прививок или флюорографии", callback_data="no_certificate")],
        [InlineKeyboardButton(text="◀️ Назад к общежитиям", callback_data="dormitory")]
    ])

def back_to_dormitory_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Назад к общежитиям", callback_data="dormitory")]
    ])


def dormitories_keyboard_back_to_dormitory_info() -> InlineKeyboardMarkup:
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
        [InlineKeyboardButton(text="◀️ Назад к общежитиям", callback_data="dormitory")]
    ])

def back_to_addresses_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Назад к адресам общежитий", callback_data="dormitory_address")]
    ])
