from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.main_handlers.languages import TEXTS

def hospital_keyboard(language: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📍 2GIS", url='https://2gis.ru/kaliningrad/search/236041%2C%20%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F%2C%20%D0%9A%D0%B0%D0%BB%D0%B8%D0%BD%D0%B8%D0%BD%D0%B3%D1%80%D0%B0%D0%B4%2C%20%D1%83%D0%BB.%209%20%D0%B0%D0%BF%D1%80%D0%B5%D0%BB%D1%8F%2C%2060/firm/70000001006212174/20.524707%2C54.71579?m=20.524833%2C54.715617%2F19.07')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['main_keyboard']['back']}", callback_data="back_to_main")]
    ])