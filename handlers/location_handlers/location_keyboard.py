"""
Keyboard for location handlers.
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.main_handlers.languages import TEXTS
from handlers.main_handlers.commands import get_user_language

language = get_user_language(callback.from_user.id)

def back_to_locations_keyboard():
    """Go back to buildings"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def uni_loc_keyboard() -> InlineKeyboardMarkup:
    """Buttons for each university building"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_1']}", callback_data="loc_1")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_2']}", callback_data="loc_2")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc']}3", callback_data="loc_3")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_4']}", callback_data="loc_4")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc']}5", callback_data="loc_5")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_6']}", callback_data="loc_6")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc']}7", callback_data="loc_7")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc']}8", callback_data="loc_8")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_9']}", callback_data="loc_9")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_10']}", callback_data="loc_10")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc']}12", callback_data="loc_12")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc']}22", callback_data="loc_22")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc']}24", callback_data="loc_24")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc']}27", callback_data="loc_27")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc']}28", callback_data="loc_28")],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="back_to_main")]
    ])
