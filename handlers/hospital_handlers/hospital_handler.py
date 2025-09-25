"""
Handler for hospital button
"""

from aiogram import Router, F
from aiogram.types import CallbackQuery
from handlers.main_handlers.keyboard import back_to_main_keyboard
<<<<<<< HEAD
from config.logger import logger
import traceback
from handlers.main_handlers.languages import TEXTS
from handlers.main_handlers.commands import get_user_language

router = Router()
language = get_user_language(callback.from_user.id)

@router.callback_query(F.data == "hospital")
async def hospital_handler(callback: CallbackQuery):
    try:
        await callback.message.edit_text(HOSPITAL_TEXT,
                                     parse_mode="Markdown",
                                     reply_markup=back_to_main_keyboard())
=======
from handlers.hospital_handlers.hospital_keyboard import hospital_keyboard
from config.logger import logger
import traceback
from handlers.main_handlers.languages import TEXTS

router = Router()

@router.callback_query(F.data == "hospital")
async def hospital_handler(callback: CallbackQuery, language: str):
    try:
        HOSPITAL_TEXT = TEXTS[language]['handlers']['hospital_handlers']['hospital_text']
        await callback.message.edit_text(HOSPITAL_TEXT,
                                     parse_mode="Markdown",
                                     reply_markup=hospital_keyboard(language))
>>>>>>> main
        await callback.answer()
    except Exception as e:
        logger.error(f'Hospital info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['info_error']}")


<<<<<<< HEAD
HOSPITAL_TEXT = TEXTS[language]['handlers']['hospital_handlers']['hospital_text']
=======
>>>>>>> main
