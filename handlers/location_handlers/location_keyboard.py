"""
Keyboard for location handlers.
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.main_handlers.languages import TEXTS

def back_to_locations_keyboard(language: str):
    """Go back to buildings"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def uni_loc_keyboard(language: str) -> InlineKeyboardMarkup:
    """Buttons for each university building"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_1']}", callback_data="loc_1"),
        InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_2']}", callback_data="loc_2")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_3']}", callback_data="loc_3"),
        InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_4']}", callback_data="loc_4")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_5']}", callback_data="loc_5"),
        InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_6']}", callback_data="loc_6")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_7']}", callback_data="loc_7"),
        InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_8']}", callback_data="loc_8")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_9']}", callback_data="loc_9"),
        InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_10']}", callback_data="loc_10")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_11']}", callback_data="loc_11"),
        InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_12']}", callback_data="loc_12")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_13']}", callback_data="loc_13"),
        InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_14']}", callback_data="loc_14")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_19']}", callback_data="loc_19"),
        InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_20']}", callback_data="loc_20")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_21']}", callback_data="loc_21"),
        InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_22']}", callback_data="loc_22")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_23']}", callback_data="loc_23"),
        InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_24']}", callback_data="loc_24")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_25']}", callback_data="loc_25"),
        InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_27']}", callback_data="loc_27")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_28']}", callback_data="loc_28"),
        InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_29']}", callback_data="loc_29")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_32']}", callback_data="loc_32"),
        InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['loc_35']}", callback_data="loc_35")],
        [InlineKeyboardButton(text=f"{TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="back_to_main")]
    ])


def loc_1_keyboard(language: str):
    """Link on loc_1"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://maps.app.goo.gl/CLeEsq2b7YVxamfp6')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_2_keyboard(language: str):
    """Link on loc_2"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/vbmtm')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_3_keyboard(language: str):
    """Link on loc_3"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/LBTA1')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_4_keyboard(language: str):
    """Link on loc_4"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/W8UZk')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_5_keyboard(language: str):
    """Link on loc_5"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/Z9KxA')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_6_keyboard(language: str):
    """Link on loc_6"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/NchtB')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_7_keyboard(language: str):
    """Link on loc_7"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/SPfF9')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_8_keyboard(language: str):
    """Link on loc_8"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/iWxfE')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_9_keyboard(language: str):
    """Link on loc_9"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/1a5HI')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_10_keyboard(language: str):
    """Link on loc_10"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/Haokw')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_11_keyboard(language: str):
    """Link on loc_11"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/9oJj5')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_12_keyboard(language: str):
    """Link on loc_12"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/jbMqq')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_13_keyboard(language: str):
    """Link on loc_13"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/YxdgJ')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_14_keyboard(language: str):
    """Link on loc_14"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/1h19Z')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_19_keyboard(language: str):
    """Link on loc_19"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/Iyf7b')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_20_keyboard(language: str):
    """Link on loc_20"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/NstRf')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_21_keyboard(language: str):
    """Link on loc_21"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/TniYI')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_22_keyboard(language: str):
    """Link on loc_22"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/XCXjr')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_23_keyboard(language: str):
    """Link on loc_23"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/ry0vN')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_24_keyboard(language: str):
    """Link on loc_24"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/viGCa')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_25_keyboard(language: str):
    """Link on loc_25"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/uvDvG')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_27_keyboard(language: str):
    """Link on loc_27"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/FqGmg')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_28_keyboard(language: str):
    """Link on loc_28"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/0lUI7')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_29_keyboard(language: str):
    """Link on loc_29"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/IkBDX')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_32_keyboard(language: str):
    """Link on loc_32"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/IRXez')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])

def loc_35_keyboard(language: str):
    """Link on loc_35"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://go.2gis.com/zp9wz')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['location_keyboard']['back']}", callback_data="loc_uni_building")]
    ])
