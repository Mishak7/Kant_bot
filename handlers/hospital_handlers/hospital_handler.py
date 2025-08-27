"""
Handler for hospital button
"""

from aiogram import Router, F
from aiogram.types import CallbackQuery
from handlers.main_handlers.keyboard import back_to_main_keyboard
from config.logger import logger
import traceback

router = Router()

@router.callback_query(F.data == "hospital")
async def hospital_handler(callback: CallbackQuery):
    try:
        await callback.message.edit_text(HOSPITAL_TEXT,
                                     parse_mode="Markdown",
                                     reply_markup=back_to_main_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'Hospital info error: {e}\n{traceback.format_exc()}')
        await callback.answer("Ошибка при загрузке информации про медцентр")


HOSPITAL_TEXT = text = '''
    *Университетская клиника БФУ им. И. Канта*

    *Адрес*: 236041, Россия, Калининград, ул. 9 апреля, 60
    *Контакты*: +7 (4012) 31-33-39    kdc@kantiana.ru

    *Медицинское страхование*:
    https://kantiana.ru/international/inostrannomu-studentu/oms/

    *Инструкция по прикреплению к поликлинике*: 
    https://kantiana.ru/students/polyclinic/

    *Клиника на карте*:
    https://2gis.ru/kaliningrad/search/236041%2C%20%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F%2C%20%D0%9A%D0%B0%D0%BB%D0%B8%D0%BD%D0%B8%D0%BD%D0%B3%D1%80%D0%B0%D0%B4%2C%20%D1%83%D0%BB.%209%20%D0%B0%D0%BF%D1%80%D0%B5%D0%BB%D1%8F%2C%2060/firm/70000001006212174/20.524707%2C54.71579?m=20.524833%2C54.715617%2F19.07
    '''