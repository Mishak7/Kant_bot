from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#Клавиатура, открывающаяся при нажатии на информацию про университет
def info_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📅 Расписание", callback_data="schedule")],
        [InlineKeyboardButton(text="💰 Стипендии", callback_data="scholarship")],
        [InlineKeyboardButton(text="📞 Контакты учебного офиса", callback_data="office_contacts")],
        [InlineKeyboardButton(text="🌍 Визово-миграционный центр", callback_data="visa_center")],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="back_to_main")]
    ])

def back_to_info_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='◀️ Назад', callback_data='info')]
    ])