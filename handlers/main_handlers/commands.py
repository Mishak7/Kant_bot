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
from handlers.language_check_handlers.grammar_handlers.grammar_keyboard import language_keyboard

router = Router()


@router.message(CommandStart())
async def send_welcome(message: types.Message):
    """Handle bot startup command and display main menu."""
    try:
        logger.info(f'User {message.from_user.id} started bot')
        await message.answer('Привет! С чем помочь?', reply_markup=main_roots_keyboard())
    except Exception as e:
        logger.error(f'Welcome error: {e}\n{traceback.format_exc()}')
        await message.answer("Произошла ошибка при запуске бота. Пожалуйста, попробуйте позже.")


@router.callback_query(F.data == "info")
async def university_info(callback: CallbackQuery):
    """Display university information section."""
    try:
        text = "🎓 Информация о университете"
        await callback.message.edit_text(text, reply_markup=info_keyboard(), parse_mode="Markdown")
        await callback.answer()
    except Exception as e:
        logger.error(f'University info error: {e}\n{traceback.format_exc()}')
        await callback.answer("Ошибка при загрузке информации об университете")


@router.callback_query(F.data == "location")
async def location_info(callback: CallbackQuery):
    """Display university location information."""
    try:
        text = "📍 Местоположение корпуса"
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=uni_loc_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'Location info error: {e}\n{traceback.format_exc()}')
        await callback.answer("Ошибка при загрузке информации о местоположении")


@router.callback_query(F.data == "dormitory")
async def dormitory_info(callback: CallbackQuery):
    """Display dormitory information section."""
    try:
        text = "🏘️ Общежития"
        await callback.message.delete()
        await callback.message.answer(text, reply_markup=dormitory_keyboard(), parse_mode="Markdown")
        await callback.answer()
    except Exception as e:
        logger.error(f'Dormitory info error: {e}\n{traceback.format_exc()}')
        await callback.answer("Ошибка при загрузке информации об общежитиях")


@router.callback_query(F.data == "critical")
async def emergency_info(callback: CallbackQuery):
    """Display emergency contacts and critical information."""
    try:
        text = "⚠️ Критические ситуации"
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=critical_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'Emergency info error: {e}\n{traceback.format_exc()}')
        await callback.answer("Ошибка при загрузке экстренной информации")


@router.callback_query(F.data == "language_check")
async def language_check_info(callback: CallbackQuery):
    """Display language checking tools section."""
    try:
        text = "🇷🇺 Проверка русского языка"
        await callback.message.edit_text(text, reply_markup=language_keyboard(), parse_mode="Markdown")
        await callback.answer()
    except Exception as e:
        logger.error(f'Language check error: {e}\n{traceback.format_exc()}')
        await callback.answer("Ошибка при загрузке инструментов проверки языка")


@router.callback_query(F.data == "back_to_main")
async def back_to_main_menu(callback: CallbackQuery):
    """Return to main menu from any section."""
    try:
        text = "Привет! С чем помочь?"
        await callback.message.edit_text(text, reply_markup=main_roots_keyboard(), parse_mode="Markdown")
        await callback.answer()
    except Exception as e:
        logger.error(f'Back to main error: {e}\n{traceback.format_exc()}')
        await callback.answer("Ошибка при возврате в главное меню")