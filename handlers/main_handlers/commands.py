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
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from handlers.main_handlers.keyboard import main_roots_keyboard, language_selection
from handlers.critical_info_handlers.critical_keyboard import info_keyboard
from handlers.dormitory_handlers.dormitory_keyboard import dormitory_keyboard
from aiogram.types import CallbackQuery
from handlers.critical_info_handlers.critical_keyboard import critical_keyboard
from handlers.location_handlers.location_keyboard import uni_loc_keyboard
from handlers.language_check_handlers.language_check_keyboard import language_keyboard
from handlers.main_handlers.languages import TEXTS

router = Router()
storage = MemoryStorage()
user_languages = {}

language = get_user_language(callback.from_user.id)

class LanguageStates(StatesGroup):
    choosing_language = State()

@router.message(CommandStart())
async def send_welcome(message: types.Message):
    """Handle bot startup command and display main menu."""
    try:
        logger.info(f'User {message.from_user.id} started bot')
        await message.answer(f"{TEXTS[language]['language_selection']}", reply_markup=language_selection())
    except Exception as e:
        logger.error(f'Welcome error: {e}\n{traceback.format_exc()}')
        await message.answer(f"{TEXTS[language]['errors']['start_error']}")
        await state.set_state(LanguageStates.choosing_language)


@router.callback_query(F.data == "info")
async def university_info(callback: CallbackQuery):
    """Display university information section."""
    try:
        text = f"🎓 {TEXTS[language]['keyboards']['main_keyboard']['info']}"
        await callback.message.edit_text(text, reply_markup=info_keyboard(), parse_mode="Markdown")
        await callback.answer()
    except Exception as e:
        logger.error(f'University info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['info_error']}")


@router.callback_query(F.data == "location")
async def location_info(callback: CallbackQuery):
    """Display university location information."""
    try:
        text = f"📍 {TEXTS[language]['keyboards']['main_keyboard']['location']}"
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=uni_loc_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'Location info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['info_error']}")


@router.callback_query(F.data == "dormitory")
async def dormitory_info(callback: CallbackQuery):
    """Display dormitory information section."""
    try:
        text = f"🏘️ {TEXTS[language]['keyboards']['main_keyboard']['dormitory']}"
        await callback.message.delete()
        await callback.message.answer(text, reply_markup=dormitory_keyboard(), parse_mode="Markdown")
        await callback.answer()
    except Exception as e:
        logger.error(f'Dormitory info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['info_error']}")


@router.callback_query(F.data == "critical")
async def emergency_info(callback: CallbackQuery):
    """Display emergency contacts and critical information."""
    try:
        text = f"⚠️ {TEXTS[language]['keyboards']['main_keyboard']['critical']}"
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=critical_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'Emergency info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['info_error']}")


@router.callback_query(F.data == "language_check")
async def language_check_info(callback: CallbackQuery):
    """Display language checking tools section."""
    try:
        text = f"🇷🇺 {TEXTS[language]['keyboards']['main_keyboard']['language_check']}"
        await callback.message.edit_text(text, reply_markup=language_keyboard(), parse_mode="Markdown")
        await callback.answer()
    except Exception as e:
        logger.error(f'Language check error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['info_error']}")


@router.callback_query(F.data == "back_to_main")
async def back_to_main_menu(callback: CallbackQuery):
    """Return to main menu from any section."""
    try:
        text = f"{TEXTS[language]['greetings']}"
        await callback.message.edit_text(text, reply_markup=main_roots_keyboard(), parse_mode="Markdown")
        await callback.answer()
    except Exception as e:
        logger.error(f'Back to main error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['back_error']}")


@router.callback_query(F.data == "back_to_language_selection")
async def back_to_language_selection(callback: CallbackQuery):
    """Return to language selection from any section."""
    try:
        text = f"{TEXTS[language]['language_selection']}"
        await callback.message.edit_text(text, reply_markup=language_selection(), parse_mode="Markdown")
        await callback.answer()
    except Exception as e:
        logger.error(f'Back to main error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['back_error']}")

@router.callback_query(F.data == "russian")
async def emergency_info(callback: CallbackQuery, state: FSMContext):
    """Changes a language to Russian"""
    try:
        user_id = callback.from_user.id
        set_user_language(user_id, language)
        text = f"⚠️ {TEXTS['ru']['greetings']}"
        await state.update_data(language=language)
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=main_roots_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'Emergency info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['info_error']}")

@router.callback_query(F.data == "english")
async def emergency_info(callback: CallbackQuery, state: FSMContext):
    """Changes a language to English"""
    try:
        user_id = callback.from_user.id
        set_user_language(user_id, 'en')
        text = f"⚠️ {TEXTS['en']['greetings']}"
        await state.update_data(language='en')
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=main_roots_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'Emergency info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS['en']['errors']['info_error']}")

@router.callback_query(F.data == "french")
async def emergency_info(callback: CallbackQuery, state: FSMContext):
    """Changes a language to French"""
    try:
        user_id = callback.from_user.id
        set_user_language(user_id, 'fr')
        text = f"⚠️ {TEXTS['fr']['greetings']}"
        await state.update_data(language='fr')
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=main_roots_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'Emergency info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS['fr']['errors']['info_error']}")

@router.callback_query(F.data == "spanish")
async def emergency_info(callback: CallbackQuery, state: FSMContext):
    """Changes a language to Spanish"""
    try:
        user_id = callback.from_user.id
        set_user_language(user_id, 'es')
        text = f"⚠️ {TEXTS['es']['greetings']}"
        await state.update_data(language='es')
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=main_roots_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'Emergency info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS['es']['errors']['info_error']}")

@router.callback_query(F.data == "chinese")
async def emergency_info(callback: CallbackQuery, state: FSMContext):
    """Changes a language to Chinese"""
    try:
        user_id = callback.from_user.id
        set_user_language(user_id, 'cn')
        text = f"⚠️ {TEXTS['cn']['greetings']}"
        await state.update_data(language='cn')
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=main_roots_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'Emergency info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS['cn']['errors']['info_error']}")

@router.callback_query(F.data == "indian")
async def emergency_info(callback: CallbackQuery, state: FSMContext):
    """Changes a language to Indian"""
    try:
        user_id = callback.from_user.id
        set_user_language(user_id, 'in')
        text = f"⚠️ {TEXTS['in']['greetings']}"
        await state.update_data(language='in')
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=main_roots_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'Emergency info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS['in']['errors']['info_error']}")

def get_user_language(user_id: int) -> str:
    """Returns a users language"""
    return user_languages.get(user_id)

def set_user_language(user_id: int, language: str):
    """Sets a language"""
    user_languages[user_id] = language
