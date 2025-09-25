from aiogram import Router, F
from aiogram.types import CallbackQuery
from handlers.sber_handlers.sber_keyboard import back_to_sber_keyboard, card_keyboard, loan_keyboard
from config.logger import logger
import traceback
from handlers.main_handlers.languages import TEXTS

router = Router()


@router.callback_query(F.data == "educational_loan")
async def educational_loan_handler(callback: CallbackQuery, language: str):
    try:
        await callback.message.edit_text(TEXTS[language]['handlers']['sber_handlers']['educational_loan_text'],
                                         parse_mode="Markdown",
                                         reply_markup=loan_keyboard(language))
        await callback.answer()
    except Exception as e:
        logger.error(f'sber error: {e}\n{traceback.format_exc()}')
        await callback.answer(TEXTS[language]['errors']['info_error'])


@router.callback_query(F.data == "sber_card")
async def sber_card_handler(callback: CallbackQuery, language: str):
    try:
        await callback.message.edit_text(TEXTS[language]['handlers']['sber_handlers']['sber_card_text'],
                                         parse_mode="Markdown",
                                         reply_markup=card_keyboard(language))
        await callback.answer()
    except Exception as e:
        logger.error(f'sber card error: {e}\n{traceback.format_exc()}')
        await callback.answer(TEXTS[language]['errors']['info_error'])


@router.callback_query(F.data == "useful_links")
async def useful_links_handler(callback: CallbackQuery, language: str):
    try:
        await callback.message.edit_text(TEXTS[language]['handlers']['sber_handlers']['useful_links_text'],
                                         parse_mode="Markdown",
                                         disable_web_page_preview=True,
                                         reply_markup=back_to_sber_keyboard(language))
        await callback.answer()
    except Exception as e:
        logger.error(f'sber error: {e}\n{traceback.format_exc()}')
        await callback.answer(TEXTS[language]['errors']['info_error'])

