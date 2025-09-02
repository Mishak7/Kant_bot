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
from handlers.main_handlers.keyboard import main_roots_keyboard, language_selection
from handlers.university_handlers.university_info_keyboard import info_keyboard
from handlers.dormitory_handlers.dormitory_keyboard import dormitory_keyboard
from aiogram.types import CallbackQuery
from handlers.critical_info_handlers.critical_keyboard import critical_keyboard
from handlers.location_handlers.location_keyboard import uni_loc_keyboard
from handlers.language_check_handlers.language_check_keyboard import language_keyboard
from handlers.sber_handlers.sber_keyboard import sber_keyboard
from handlers.main_handlers.languages import TEXTS
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class LanguageState(StatesGroup):
    waiting_for_language = State()

router = Router()
user_languages = {}

@router.message(CommandStart())
async def send_welcome(message: types.Message, state: FSMContext):
    try:
        logger.info(f'User {message.from_user.id} started bot')
        await state.set_state(LanguageState.waiting_for_language)
        await message.answer("Выберите язык / Choose language:",
                           reply_markup=language_selection())
    except Exception as e:
        logger.error(f'Welcome error: {e}\n{traceback.format_exc()}')

@router.callback_query(F.data == 'start')
async def send_welcome_callback(message: types.Message, state: FSMContext):
    try:
        logger.info(f'User {message.from_user.id} started bot')
        await state.set_state(LanguageState.waiting_for_language)
        await message.answer("Выберите язык / Choose language:",
                           reply_markup=language_selection())
    except Exception as e:
        logger.error(f'Welcome error: {e}\n{traceback.format_exc()}')



@router.callback_query(F.data.in_(["russian", "english", "french", "spanish", "chinese", "indian"]))
async def set_language(callback: CallbackQuery, state: FSMContext):
    try:
        lang_map = {
            "russian": "ru",
            "english": "en",
            "french": "fr",
            "spanish": "es",
            "chinese": "cn",
            "indian": "hi"
        }

        lang_code = callback.data
        language = lang_map.get(lang_code, "ru")

        await state.update_data(language=language)

        user_languages[callback.from_user.id] = language

        await callback.message.edit_text(
            text=TEXTS[language]['greetings'],
            reply_markup=main_roots_keyboard(language),
            parse_mode="Markdown"
        )
        await callback.answer()

    except Exception as e:
        logger.error(f'Language selection error: {e}\n{traceback.format_exc()}')
        await callback.answer("Произошла ошибка при выборе языка")


@router.callback_query(F.data == "info")
async def university_info(callback: CallbackQuery, language: str):
    """Display university information section."""
    try:
        text = f"🎓 {TEXTS[language]['keyboards']['main_keyboard']['info']}"
        await callback.message.edit_text(text, reply_markup=info_keyboard(language), parse_mode="Markdown")
        await callback.answer()
    except Exception as e:
        logger.error(f'University info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['info_error']}")


@router.callback_query(F.data == "location")
async def location_info(callback: CallbackQuery, language: str):
    """Display university location information."""
    try:
        text = f"📍 {TEXTS[language]['keyboards']['main_keyboard']['location']}"
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=uni_loc_keyboard(language))
        await callback.answer()
    except Exception as e:
        logger.error(f'Location info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['info_error']}")


@router.callback_query(F.data == "dormitory")
async def dormitory_info(callback: CallbackQuery, language: str):
    """Display dormitory information section."""
    try:
        text = f"🏘️ {TEXTS[language]['keyboards']['main_keyboard']['dormitory']}"
        await callback.message.delete()
        await callback.message.answer(text, reply_markup=dormitory_keyboard(language), parse_mode="Markdown")
        await callback.answer()
    except Exception as e:
        logger.error(f'Dormitory info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['info_error']}")


@router.callback_query(F.data == "critical")
async def emergency_info(callback: CallbackQuery, language: str):
    """Display emergency contacts and critical information."""
    try:
        text = f"⚠️ {TEXTS[language]['keyboards']['main_keyboard']['critical']}"
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=critical_keyboard(language))
        await callback.answer()
    except Exception as e:
        logger.error(f'Emergency info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['info_error']}")


@router.callback_query(F.data == "sber")
async def sber_info(callback: CallbackQuery, language: str):
    """SBER"""
    try:
        text = f"💳 {TEXTS[language]['keyboards']['main_keyboard']['sber']}"
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=sber_keyboard(language))
        await callback.answer()
    except Exception as e:
        logger.error(f'SBER info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['info_error']}")


@router.callback_query(F.data == "language_check")
async def language_check_info(callback: CallbackQuery, language: str):
    """Display language checking tools section."""
    try:
        text = f"🇷🇺 {TEXTS[language]['keyboards']['main_keyboard']['language_check']}"
        await callback.message.edit_text(text, reply_markup=language_keyboard(language), parse_mode="Markdown")
        await callback.answer()
    except Exception as e:
        logger.error(f'Language check error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['info_error']}")


@router.callback_query(F.data == "back_to_main")
async def back_to_main_menu(callback: CallbackQuery, language: str):
    """Return to main menu from any section."""
    try:
        text = f"{TEXTS[language]['greetings']}"
        await callback.message.edit_text(text, reply_markup=main_roots_keyboard(language), parse_mode="Markdown")
        await callback.answer()
    except Exception as e:
        logger.error(f'Back to main error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['back_error']}")