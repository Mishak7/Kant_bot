from aiogram import Router, F
from aiogram.types import CallbackQuery
from handlers.sber_handlers.sber_keyboard import back_to_sber_keyboard, card_keyboard, loan_keyboard
from config.logger import logger
import traceback
<<<<<<< HEAD
from handlers.main_handlers.commands import get_user_language
from handlers.main_handlers.languages import TEXTS

router = Router()
language = get_user_language(callback.from_user.id)

@router.callback_query(F.data == "educational_loan")
async def educational_loan_handler(callback: CallbackQuery):
    try:
        await callback.message.edit_text(EDUCATIONAL_LOAN_TEXT,
                                         parse_mode="Markdown",
                                         reply_markup=loan_keyboard())
=======
from handlers.main_handlers.languages import TEXTS

router = Router()


@router.callback_query(F.data == "educational_loan")
async def educational_loan_handler(callback: CallbackQuery, language: str):
    try:
        await callback.message.edit_text(TEXTS[language]['handlers']['sber_handlers']['educational_loan_text'],
                                         parse_mode="Markdown",
                                         reply_markup=loan_keyboard(language))
>>>>>>> main
        await callback.answer()
    except Exception as e:
        logger.error(f'sber error: {e}\n{traceback.format_exc()}')
        await callback.answer(TEXTS[language]['errors']['info_error'])


@router.callback_query(F.data == "sber_card")
<<<<<<< HEAD
async def sber_card_handler(callback: CallbackQuery):
    try:
        await callback.message.edit_text(SBER_CARD_TEXT,
                                         parse_mode="Markdown",
                                         reply_markup=card_keyboard())
=======
async def sber_card_handler(callback: CallbackQuery, language: str):
    try:
        await callback.message.edit_text(TEXTS[language]['handlers']['sber_handlers']['sber_card_text'],
                                         parse_mode="Markdown",
                                         reply_markup=card_keyboard(language))
>>>>>>> main
        await callback.answer()
    except Exception as e:
        logger.error(f'sber card error: {e}\n{traceback.format_exc()}')
        await callback.answer(TEXTS[language]['errors']['info_error'])


@router.callback_query(F.data == "useful_links")
<<<<<<< HEAD
async def useful_links_handler(callback: CallbackQuery):
    try:
        await callback.message.edit_text(USEFUL_LINKS_TEXT,
                                         parse_mode="Markdown",
                                         disable_web_page_preview=True,
                                         reply_markup=back_to_sber_keyboard())
=======
async def useful_links_handler(callback: CallbackQuery, language: str):
    try:
        await callback.message.edit_text(TEXTS[language]['handlers']['sber_handlers']['useful_links_text'],
                                         parse_mode="Markdown",
                                         disable_web_page_preview=True,
                                         reply_markup=back_to_sber_keyboard(language))
>>>>>>> main
        await callback.answer()
    except Exception as e:
        logger.error(f'sber error: {e}\n{traceback.format_exc()}')
        await callback.answer(TEXTS[language]['errors']['info_error'])

<<<<<<< HEAD

USEFUL_LINKS_TEXT = TEXTS[language]['handlers']['sber_handlers']['useful_links_text']

SBER_CARD_TEXT = TEXTS[language]['handlers']['sber_handlers']['sber_card_text']

EDUCATIONAL_LOAN_TEXT = TEXTS[language]['handlers']['sber_handlers']['educational_loan_text']
=======
>>>>>>> main
