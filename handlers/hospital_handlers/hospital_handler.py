"""
Handler for hospital button
"""

from aiogram import Router, F
from aiogram.types import CallbackQuery
from handlers.main_handlers.keyboard import back_to_main_keyboard
from config.logger import logger
import traceback
from handlers.main_handlers.languages import TEXTS

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
        await callback.answer(f"{TEXTS['ru']['errors']['info_error']}")


HOSPITAL_TEXT = TEXTS['ru']['handlers']['hospital_handlers']['hospital_text']