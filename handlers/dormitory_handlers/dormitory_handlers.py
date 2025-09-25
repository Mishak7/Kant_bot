"""
Dormitory information handlers for student accommodation.

This module provides handlers for dormitory-related information including:
- Check-in procedures and requirements
- Payment information
- Dormitory addresses and selection
- Rules and regulations
- Laundry facilities
- Certificate requirements
"""

import traceback
from aiogram import Router, F
<<<<<<< HEAD
from aiogram.types import CallbackQuery, FSInputFile
from config.logger import logger
from handlers.dormitory_handlers.dormitory_keyboard import (
    dormitory_check_in_keyboard,
    back_to_dormitory_keyboard,
    dormitories_keyboard_back_to_dormitory_info,
    back_to_check_in_keyboard,
    payment_keyboard
)
from handlers.main_handlers.languages import TEXTS
from handlers.main_handlers.commands import get_user_language


router = Router()
language = get_user_language(callback.from_user.id)


@router.callback_query(F.data == "dormitory_check-in")
async def dormitory_check_in_handler(callback: CallbackQuery):
    """Display dormitory check-in procedures and requirements."""
    try:
        await callback.message.edit_text(
            DORMITORY_TEXT,
            parse_mode="Markdown",
            reply_markup=dormitory_check_in_keyboard()
        )
=======
from aiogram.types import CallbackQuery
from config.logger import logger
from handlers.dormitory_handlers.dormitory_keyboard import (
    back_to_dormitory_keyboard,
    dormitories_keyboard_back_to_dormitory_info,
    back_to_check_in_keyboard,
payment_keyboard
)
from handlers.main_handlers.languages import TEXTS
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


router = Router()

@router.callback_query(F.data == "dormitory_check-in")
async def dormitory_check_in_handler(callback: CallbackQuery, language: str):
    """Display dormitory check-in procedures and requirements."""
    try:
        DORMITORY_TEXT = TEXTS[language]['handlers']['dormitory_handlers']['dormitory_text']
        await callback.message.edit_text(
            DORMITORY_TEXT,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text=f"🧳  {TEXTS[language]['keyboards']['dormitory_keyboard']['check-in']}", url=f'https://telegra.ph/Zaselenie-v-obshchezhitie-{language}-09-04')],
                [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory")]]))
>>>>>>> main
        await callback.answer()
    except Exception as e:
        logger.error(f'Dormitory check-in error: {e}\n{traceback.format_exc()}')
        await callback.answer(TEXTS[language]['errors']['info_error'])


@router.callback_query(F.data == "dormitory_payment")
<<<<<<< HEAD
async def dormitory_payment_handler(callback: CallbackQuery):
    """Display dormitory payment information and procedures."""
    try:
        await callback.message.edit_text(
            PAYMENT_TEXT,
            parse_mode="Markdown",
            reply_markup=payment_keyboard()
=======
async def dormitory_payment_handler(callback: CallbackQuery, language: str):
    """Display dormitory payment information and procedures."""
    try:
        PAYMENT_TEXT = TEXTS[language]['handlers']['dormitory_handlers']['payment_text']
        await callback.message.edit_text(
            PAYMENT_TEXT,
            parse_mode="Markdown",
            reply_markup=payment_keyboard(language)
>>>>>>> main
        )
        await callback.answer()
    except Exception as e:
        logger.error(f'Dormitory payment error: {e}\n{traceback.format_exc()}')
        await callback.answer(TEXTS[language]['errors']['info_error'])

<<<<<<< HEAD
@router.callback_query(F.data == "sber_payment")
async def sber_payment_handler(callback: CallbackQuery):
    """Handle case when student doesn't have required certificate."""
    try:
        pass
    except Exception as e:
        logger.error(f'No certificate error: {e}\n{traceback.format_exc()}')
        await callback.answer(TEXTS[language]['errors']['info_error'])

@router.callback_query(F.data == "dormitory_address")
async def dormitory_addresses_handler(callback: CallbackQuery):
=======

@router.callback_query(F.data == "dormitory_address")
async def dormitory_addresses_handler(callback: CallbackQuery, language: str):
>>>>>>> main
    """Display dormitory selection menu for address information."""
    try:
        await callback.message.delete()
        await callback.message.answer(
            'Выбери общежитие',
<<<<<<< HEAD
            reply_markup=dormitories_keyboard_back_to_dormitory_info()
=======
            reply_markup=dormitories_keyboard_back_to_dormitory_info(language)
>>>>>>> main
        )
        await callback.answer()
    except Exception as e:
        logger.error(f'Dormitory addresses error: {e}\n{traceback.format_exc()}')
        await callback.answer(TEXTS[language]['errors']['info_error'])


@router.callback_query(F.data == "dormitory_rules")
<<<<<<< HEAD
async def dormitory_rules_handler(callback: CallbackQuery):
    """Display dormitory rules and regulations with photo."""
    try:
        photo = FSInputFile('handlers/location_handlers/dormitory_pictures/dormitory_rules.jpg')

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=RULES_TEXT,
            parse_mode="Markdown",
            reply_markup=back_to_dormitory_keyboard()
=======
async def dormitory_rules_handler(callback: CallbackQuery, language: str):
    """Display dormitory rules and regulations with photo."""
    try:
        RULES_TEXT = TEXTS[language]['handlers']['dormitory_handlers']['rules_text']
        await callback.message.edit_text(
            text=RULES_TEXT,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"🔗 {TEXTS[language]['keyboards']['dormitory_keyboard']['rules']}", url='https://telegra.ph/Pravila-zhizni-v-obshchezhitii-09-02')],
        [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory")]
    ])
>>>>>>> main
        )
        await callback.answer()
    except Exception as e:
        logger.error(f'Dormitory rules error: {e}\n{traceback.format_exc()}')
        await callback.answer(TEXTS[language]['errors']['info_error'])


@router.callback_query(F.data == "dormitory_laundry")
<<<<<<< HEAD
async def dormitory_laundry_handler(callback: CallbackQuery):
    """Display laundry facilities information."""
    try:
        await callback.message.edit_text(
            LAUNDRY_TEXT,
            reply_markup=back_to_dormitory_keyboard(),
=======
async def dormitory_laundry_handler(callback: CallbackQuery, language: str):
    """Display laundry facilities information."""
    try:
        LAUNDRY_TEXT = TEXTS[language]['handlers']['dormitory_handlers']['laundry_text']
        await callback.message.edit_text(
            LAUNDRY_TEXT,
            reply_markup=back_to_dormitory_keyboard(language),
>>>>>>> main
            parse_mode="Markdown"
        )
        await callback.answer()
    except Exception as e:
        logger.error(f'Dormitory laundry error: {e}\n{traceback.format_exc()}')
        await callback.answer(TEXTS[language]['errors']['info_error'])


@router.callback_query(F.data == "no_certificate")
<<<<<<< HEAD
async def dormitory_no_certificate_handler(callback: CallbackQuery):
    """Handle case when student doesn't have required certificate."""
    try:
=======
async def dormitory_no_certificate_handler(callback: CallbackQuery, language: str):
    """Handle case when student doesn't have required certificate."""
    try:
        NO_CERIFICATION_TEXT = TEXTS[language]['handlers']['dormitory_handlers']['no_certificate_text']
>>>>>>> main
        await callback.message.delete()
        await callback.message.answer(
            NO_CERIFICATION_TEXT,
            parse_mode="Markdown",
<<<<<<< HEAD
            reply_markup=back_to_check_in_keyboard()
=======
            reply_markup=back_to_check_in_keyboard(language)
>>>>>>> main
        )
        await callback.answer()
    except Exception as e:
        logger.error(f'No certificate error: {e}\n{traceback.format_exc()}')
        await callback.answer(TEXTS[language]['errors']['info_error'])
<<<<<<< HEAD


DORMITORY_TEXT = TEXTS[language]['handlers']['dormitory_handlers']['dormitory_text']

PAYMENT_TEXT = TEXTS[language]['handlers']['dormitory_handlers']['payment_text']

RULES_TEXT = TEXTS[language]['handlers']['dormitory_handlers']['rules_text']

LAUNDRY_TEXT = TEXTS[language]['handlers']['dormitory_handlers']['laundry_text']

NO_CERIFICATION_TEXT = TEXTS[language]['handlers']['dormitory_handlers']['no_certificate_text']
=======
>>>>>>> main
