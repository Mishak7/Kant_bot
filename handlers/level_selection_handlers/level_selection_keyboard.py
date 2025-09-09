from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

"""
Keyboards for handlers of level selection.
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def level_selection() -> InlineKeyboardMarkup:
    """Creates a keyboard layout for level selection."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"✏️ A1", callback_data='a1_level')],
        [InlineKeyboardButton(text=f"📝 A2", callback_data='a2_level')],
        [InlineKeyboardButton(text=f"⭐ B1", callback_data='b1_level')],
        [InlineKeyboardButton(text=f"🔥 B2", callback_data='b2_level')],
        [InlineKeyboardButton(text=f"🏆 C1", callback_data='c1_level')],
        [InlineKeyboardButton(text=f"👑 C2", callback_data='c2_level')],
        [InlineKeyboardButton(text=f"◀️ Назад", callback_data='back_to_main')]
    ])

def back_to_level_selection_keyboard():
    """Returns a single-button keyboard to go back to the level selection."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"◀️ Назад", callback_data="back_to_level_selection")]
    ])
