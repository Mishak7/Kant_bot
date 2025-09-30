from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, reply_keyboard_markup, KeyboardButton, \
    ReplyKeyboardMarkup, ReplyKeyboardRemove

"""
Keyboards for handlers of level selection.
"""

def level_selection_keyboard() -> InlineKeyboardMarkup:
    """Creates a keyboard layout for level selection."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"✏️ A1", callback_data='A1')],
        [InlineKeyboardButton(text=f"📝 A2", callback_data='A2')],
        [InlineKeyboardButton(text=f"⭐ B1", callback_data='B1')],
        [InlineKeyboardButton(text=f"🔥 B2", callback_data='B2')],
        [InlineKeyboardButton(text=f"🏆 C1", callback_data='C1')],
        [InlineKeyboardButton(text=f"👑 C2", callback_data='C2')],
        [InlineKeyboardButton(text=f"◀️ Назад", callback_data='back_to_main')]
    ])

def back_to_level_selection_keyboard():
    """Returns a single-button keyboard to go back to the level selection."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ Назад", callback_data="back_to_level_selection")]
    ])


def answer_keyboard(number_of_buttons:int):

    keyboards = {
        2: ReplyKeyboardMarkup(keyboard=
            [[KeyboardButton(text="1"), KeyboardButton(text="2")]],
                               resize_keyboard=True, one_time_keyboard=True),

        3: ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="1"), KeyboardButton(text="2"),KeyboardButton(text="3")]], resize_keyboard=True, one_time_keyboard=True),

        4: ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="1"), KeyboardButton(text="2")],
        [KeyboardButton(text="3"), KeyboardButton(text="4")]],
            resize_keyboard=True, one_time_keyboard=True),}

    return keyboards[number_of_buttons]

