"""
Keyboard for location handlers.
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.main_handlers.languages import TEXTS

def back_to_locations_keyboard():
    """Go back to buildings"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS['ru']['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def uni_loc_keyboard() -> InlineKeyboardMarkup:
    """Buttons for each university building"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{TEXTS['ru']['keyboards']['location_keyboard']['loc_1']}", callback_data="loc_1"),
        InlineKeyboardButton(text=f"{TEXTS['ru']['keyboards']['location_keyboard']['loc_2']}", callback_data="loc_2")],
        [InlineKeyboardButton(text=f"{TEXTS['ru']['keyboards']['location_keyboard']['loc_3']}", callback_data="loc_3"),
        InlineKeyboardButton(text=f"{TEXTS['ru']['keyboards']['location_keyboard']['loc_4']}", callback_data="loc_4")],
        [InlineKeyboardButton(text=f"{TEXTS['ru']['keyboards']['location_keyboard']['loc_5']}", callback_data="loc_5"),
        InlineKeyboardButton(text=f"{TEXTS['ru']['keyboards']['location_keyboard']['loc_6']}", callback_data="loc_6")],
        [InlineKeyboardButton(text=f"{TEXTS['ru']['keyboards']['location_keyboard']['loc_7']}", callback_data="loc_7"),
        InlineKeyboardButton(text=f"{TEXTS['ru']['keyboards']['location_keyboard']['loc_8']}", callback_data="loc_8")],
        [InlineKeyboardButton(text=f"{TEXTS['ru']['keyboards']['location_keyboard']['loc_9']}", callback_data="loc_9"),
        InlineKeyboardButton(text=f"{TEXTS['ru']['keyboards']['location_keyboard']['loc_10']}", callback_data="loc_10")],
        [InlineKeyboardButton(text=f"{TEXTS['ru']['keyboards']['location_keyboard']['loc_12']}", callback_data="loc_12"),
        InlineKeyboardButton(text=f"{TEXTS['ru']['keyboards']['location_keyboard']['loc_22']}", callback_data="loc_22")],
        [InlineKeyboardButton(text=f"{TEXTS['ru']['keyboards']['location_keyboard']['loc_24']}", callback_data="loc_24"),
        InlineKeyboardButton(text=f"{TEXTS['ru']['keyboards']['location_keyboard']['loc_27']}", callback_data="loc_27")],
        [InlineKeyboardButton(text=f"{TEXTS['ru']['keyboards']['location_keyboard']['loc_28']}", callback_data="loc_28")],
        [InlineKeyboardButton(text=f"{TEXTS['ru']['keyboards']['location_keyboard']['back']}", callback_data="back_to_main")]
    ])


def loc_1_keyboard():
    """Link on loc_1"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://maps.app.goo.gl/CLeEsq2b7YVxamfp6')],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="loc_uni_building")]
    ])

def loc_2_keyboard():
    """Link on loc_2"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/vbmtm')],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="loc_uni_building")]
    ])

def loc_3_keyboard():
    """Link on loc_3"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/LBTA1')],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="loc_uni_building")]
    ])

def loc_4_keyboard():
    """Link on loc_4"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/W8UZk')],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="loc_uni_building")]
    ])

def loc_5_keyboard():
    """Link on loc_5"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/Z9KxA')],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="loc_uni_building")]
    ])

def loc_6_keyboard():
    """Link on loc_6"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/NchtB')],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="loc_uni_building")]
    ])

def loc_7_keyboard():
    """Link on loc_7"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/SPfF9')],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="loc_uni_building")]
    ])

def loc_8_keyboard():
    """Link on loc_8"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/iWxfE')],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="loc_uni_building")]
    ])

def loc_9_keyboard():
    """Link on loc_9"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/1a5HI')],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="loc_uni_building")]
    ])

def loc_10_keyboard():
    """Link on loc_10"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/Haokw')],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="loc_uni_building")]
    ])

def loc_12_keyboard():
    """Link on loc_12"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/jbMqq')],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="loc_uni_building")]
    ])

def loc_22_keyboard():
    """Link on loc_22"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/XCXjr')],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="loc_uni_building")]
    ])

def loc_24_keyboard():
    """Link on loc_24"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/viGCa')],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="loc_uni_building")]
    ])

def loc_27_keyboard():
    """Link on loc_27"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/FqGmg')],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="loc_uni_building")]
    ])

def loc_28_keyboard():
    """Link on loc_28"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/0lUI7')],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="loc_uni_building")]
    ])