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
import os
import traceback
from aiogram import Router, types, F
from aiogram.filters import CommandStart
from config.logger import logger
from handlers.level_selection_handlers.level_selection_keyboard import level_selection_keyboard
from handlers.main_handlers.keyboard import main_roots_keyboard, language_selection
from handlers.university_handlers.university_info_keyboard import info_keyboard
from handlers.dormitory_handlers.dormitory_keyboard import dormitory_keyboard
from aiogram.types import CallbackQuery, FSInputFile, Message
from handlers.critical_info_handlers.critical_keyboard import critical_keyboard
from handlers.location_handlers.location_keyboard import uni_loc_keyboard
from handlers.language_check_handlers.language_check_keyboard import  go_to_lessons
from handlers.sber_handlers.sber_keyboard import sber_keyboard
from handlers.main_handlers.languages import TEXTS
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from services.database.database_functions import check_user_exists, create_user, get_user_name
from handlers.level_selection_handlers.level_selection_keyboard import level_selection_keyboard

class LanguageState(StatesGroup):
    waiting_for_language = State()


class UserRegistration(StatesGroup):
    waiting_for_name = State()

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

@router.callback_query(F.data == 'start_again')
async def send_welcome_callback(callback: CallbackQuery, state: FSMContext):
    try:
        logger.info(f'User {callback.from_user.id} started bot')
        await state.set_state(LanguageState.waiting_for_language)
        await callback.message.edit_text("Выберите язык / Choose language:",
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

        if os.path.exists('utility_files/gif_kant.gif'):
            gif_file = FSInputFile('utility_files/gif_kant.gif')
            await callback.message.answer_animation(
                animation=gif_file,
                caption=TEXTS[language]['greetings'],
                reply_markup=main_roots_keyboard(language),
                parse_mode="Markdown"
            )

            await callback.message.delete()


        else:
            await callback.message.edit_text(
                text=TEXTS[language]['greetings'],
                reply_markup=main_roots_keyboard(language),
                parse_mode="Markdown")

        await callback.answer()

    except Exception as e:
        logger.error(f'Language selection error: {e}\n{traceback.format_exc()}')
        await callback.answer("Произошла ошибка при выборе языка")


@router.callback_query(F.data == "info")
async def university_info(callback: CallbackQuery, language: str):
    """Display university information section."""
    try:
        text = f"🎓 {TEXTS[language]['keyboards']['main_keyboard']['info']}"
        await callback.message.delete()
        await callback.message.answer(text, reply_markup=info_keyboard(language), parse_mode="Markdown")
        await callback.answer()
    except Exception as e:
        logger.error(f'University info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['info_error']}")


@router.callback_query(F.data == "location")
async def location_info(callback: CallbackQuery, language: str):
    """Display university location information."""
    try:
        text = f"📍 {TEXTS[language]['keyboards']['main_keyboard']['location']}"
        await callback.message.delete()
        await callback.message.answer(text, parse_mode="Markdown", reply_markup=uni_loc_keyboard(language))
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
        await callback.message.delete()
        await callback.message.answer(text, parse_mode="Markdown", reply_markup=critical_keyboard(language))
        await callback.answer()
    except Exception as e:
        logger.error(f'Emergency info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['info_error']}")


@router.callback_query(F.data == "sber")
async def sber_info(callback: CallbackQuery, language: str):
    """SBER"""
    try:
        text = f"💳 {TEXTS[language]['keyboards']['main_keyboard']['sber']}"
        await callback.message.delete()
        await callback.message.answer(text, parse_mode="Markdown", reply_markup=sber_keyboard(language))
        await callback.answer()
    except Exception as e:
        logger.error(f'SBER info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['info_error']}")



@router.callback_query(F.data == "language_check")
async def language_check_info(callback: CallbackQuery, language: str, state: FSMContext):
    """Display language checking tools section with user check."""
    try:
        user_id = callback.from_user.id

        user_info = await get_user_name(user_id)

        if not user_info:
            await callback.message.delete()
            await callback.message.answer("👋 Для начала работы введите ваше имя:")
            await state.set_state(UserRegistration.waiting_for_name)
            return

        text = f"Привет, {user_info[0]}! Переходи к заданиям: 👇"
        await callback.message.delete()
        await callback.message.answer(text, reply_markup=level_selection_keyboard(), parse_mode="Markdown")
        await callback.answer()

    except Exception as e:
        logger.error(f'Language check error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['info_error']}")



@router.message(UserRegistration.waiting_for_name)
async def process_name(message: Message, state: FSMContext, language: str):
    try:
        user_name = message.text.strip()
        user_id = message.from_user.id

        if len(user_name) < 2:
            await message.answer("❌ Имя должно содержать минимум 2 символа. Попробуйте еще раз:")
            return

        if len(user_name) > 50:
            await message.answer("❌ Имя слишком длинное. Максимум 50 символов. Попробуйте еще раз:")
            return

        success = await create_user(
            telegram_id=user_id,
            username=user_name
        )

        if success:
            await message.answer(f"✅ Отлично, {user_name}! Регистрация завершена! 🎉")
            await state.clear()

            text = f'Переходи к заданиями: '
            await message.answer(text, reply_markup=level_selection_keyboard(), parse_mode="Markdown")
        else:
            await message.answer("❌ Произошла ошибка при регистрации. Попробуйте позже.")
            await state.clear()

    except Exception as e:
        logger.error(f"Name processing error: {e}")
        await message.answer("❌ Произошла ошибка. Попробуйте позже.")
        await state.clear()

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
