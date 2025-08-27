"""
Keyboard for location handlers.
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def back_to_locations_keyboard():
    """Go back to buildings"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Назад к корпусам", callback_data="loc_uni_building")]
    ])

def uni_loc_keyboard() -> InlineKeyboardMarkup:
    """Buttons for each university building"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Административный корпус", callback_data="loc_1")],
        [InlineKeyboardButton(text="Корпус №2, Институт физики, математики и ИТ («Физмат»)", callback_data="loc_2")],
        [InlineKeyboardButton(text="Корпус №3", callback_data="loc_3")],
        [InlineKeyboardButton(text="Корпус №4 («Корпус с часами»)", callback_data="loc_4")],
        [InlineKeyboardButton(text="Корпус №5", callback_data="loc_5")],
        [InlineKeyboardButton(text="Корпус №6 («Шайба»)", callback_data="loc_6")],
        [InlineKeyboardButton(text="Корпус №7", callback_data="loc_7")],
        [InlineKeyboardButton(text="Корпус №8", callback_data="loc_8")],
        [InlineKeyboardButton(text="Корпус №9 («ФОК»)", callback_data="loc_9")],
        [InlineKeyboardButton(text="Корпус №10 («Свечка»)", callback_data="loc_10")],
        [InlineKeyboardButton(text="Корпус №12", callback_data="loc_12")],
        [InlineKeyboardButton(text="Корпус №22", callback_data="loc_22")],
        [InlineKeyboardButton(text="Корпус №24", callback_data="loc_24")],
        [InlineKeyboardButton(text="Корпус №27", callback_data="loc_27")],
        [InlineKeyboardButton(text="Корпус №28", callback_data="loc_28")],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="back_to_main")]
    ])

