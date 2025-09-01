"""
Main router and entry point handlers for the university assistance bot.

This module handles:
- Bot startup command (/start)
- Main menu navigation
- Routing to different functional sections

Sections include:
- University information
- Location services
- Dormitory information
- Emergency contacts
- Language checking
- Main menu navigation

"""

import traceback
from aiogram import Router, types, F
from aiogram.filters import CommandStart
from config.logger import logger
from handlers.main_handlers.keyboard import main_roots_keyboard
from handlers.critical_info_handlers.critical_keyboard import info_keyboard
from handlers.dormitory_handlers.dormitory_keyboard import dormitory_keyboard
from aiogram.types import CallbackQuery
from handlers.critical_info_handlers.critical_keyboard import critical_keyboard
from handlers.location_handlers.location_keyboard import uni_loc_keyboard
from handlers.language_check_handlers.language_check_keyboard import language_keyboard
from handlers.sber_handlers.sber_keyboard import sber_keyboard
from handlers.main_handlers.languages import TEXTS

router = Router()


@router.message(CommandStart())
async def send_welcome(message: types.Message):
    """Handle bot startup command and display main menu."""
    try:
        logger.info(f'User {message.from_user.id} started bot')
        await message.answer(f"{TEXTS['ru']['greetings']}", reply_markup=main_roots_keyboard())
    except Exception as e:
        logger.error(f'Welcome error: {e}\n{traceback.format_exc()}')
        await message.answer(f"{TEXTS['ru']['errors']['start_error']}")


@router.callback_query(F.data == "info")
async def university_info(callback: CallbackQuery):
    """Display university information section."""
    try:
        text = f"🎓 {TEXTS['ru']['keyboards']['main_keyboard']['info']}"
        await callback.message.edit_text(text, reply_markup=info_keyboard(), parse_mode="Markdown")
        await callback.answer()
    except Exception as e:
        logger.error(f'University info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS['ru']['errors']['info_error']}")


@router.callback_query(F.data == "location")
async def location_info(callback: CallbackQuery):
    """Display university location information."""
    try:
        text = f"📍 {TEXTS['ru']['keyboards']['main_keyboard']['location']}"
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=uni_loc_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'Location info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS['ru']['errors']['info_error']}")


@router.callback_query(F.data == "dormitory")
async def dormitory_info(callback: CallbackQuery):
    """Display dormitory information section."""
    try:
        text = f"🏘️ {TEXTS['ru']['keyboards']['main_keyboard']['dormitory']}"
        await callback.message.edit_text(text, reply_markup=dormitory_keyboard(), parse_mode="Markdown")
        await callback.answer()
    except Exception as e:
        logger.error(f'Dormitory info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS['ru']['errors']['info_error']}")


@router.callback_query(F.data == "critical")
async def emergency_info(callback: CallbackQuery):
    """Display emergency contacts and critical information."""
    try:
        text = f"⚠️ {TEXTS['ru']['keyboards']['main_keyboard']['critical']}"
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=critical_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'Emergency info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS['ru']['errors']['info_error']}")

@router.callback_query(F.data == "sber")
async def sber_info(callback: CallbackQuery):
    """SBER"""
    try:
        text = f"💳 {TEXTS['ru']['keyboards']['main_keyboard']['sber']}"
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=sber_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'SBER info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS['ru']['errors']['info_error']}")

@router.callback_query(F.data == "language_check")
async def language_check_info(callback: CallbackQuery):
    """Display language checking tools section."""
    try:
        text = f"🇷🇺 {TEXTS['ru']['keyboards']['main_keyboard']['language_check']}"
        await callback.message.edit_text(text, reply_markup=language_keyboard(), parse_mode="Markdown")
        await callback.answer()
    except Exception as e:
        logger.error(f'Language check error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS['ru']['errors']['info_error']}")


@router.callback_query(F.data == "back_to_main")
async def back_to_main_menu(callback: CallbackQuery):
    """Return to main menu from any section."""
    try:
        text = f"{TEXTS['ru']['greetings']}"
        await callback.message.edit_text(text, reply_markup=main_roots_keyboard(), parse_mode="Markdown")
        await callback.answer()
    except Exception as e:
        logger.error(f'Back to main error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS['ru']['errors']['back_error']}")