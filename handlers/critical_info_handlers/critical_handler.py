"""
Emergency contacts handlers for critical situations.

This module provides callback handlers for emergency contact information
including police, migration services, government agencies, and consulate services.
All handlers return formatted contact information with a back button to critical menu.
"""

import traceback
from aiogram import Router, F
from aiogram.types import CallbackQuery
from config.logger import logger
from handlers.critical_info_handlers.critical_keyboard import back_to_critical_keyboard
from handlers.main_handlers.languages import TEXTS
from handlers.main_handlers.commands import get_user_language

router = Router()
language = get_user_language(callback.from_user.id)


@router.callback_query(F.data == "critical_police")
async def critical_police_handler(callback: CallbackQuery):
    """Provide emergency police, rescue, and medical contact numbers."""
    try:
        text = TEXTS[language]['handlers']['critical_handlers']['critical_police_handler']
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=back_to_critical_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'Police contacts error: {e}\n{traceback.format_exc()}')
        await callback.answer(TEXTS[language]['errors']['info_error'], show_alert=True)


@router.callback_query(F.data == "critical_hotline")
async def critical_hotline_handler(callback: CallbackQuery):
    """Provide visa and migration support hotline information."""
    try:
        text = TEXTS[language]['handlers']['critical_handlers']['critical_hotline_handler']
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=back_to_critical_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'Hotline contacts error: {e}\n{traceback.format_exc()}')
        await callback.answer(TEXTS[language]['errors']['info_error'], show_alert=True)


@router.callback_query(F.data == "critical_government")
async def critical_government_handler(callback: CallbackQuery):
    """Provide local government contact information and procedures."""
    try:
        text = TEXTS[language]['handlers']['critical_handlers']['critical_government_handler']
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=back_to_critical_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'Government contacts error: {e}\n{traceback.format_exc()}')
        await callback.answer(TEXTS[language]['errors']['info_error'], show_alert=True)


@router.callback_query(F.data == "critical_consulate")
async def critical_consulate_handler(callback: CallbackQuery):
    """Provide consulate office information and working hours."""
    try:
        text = TEXTS[language]['handlers']['critical_handlers']['critical_consulate_handler']
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=back_to_critical_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'Consulate contacts error: {e}\n{traceback.format_exc()}')
        await callback.answer(TEXTS[language]['errors']['info_error'], show_alert=True)
