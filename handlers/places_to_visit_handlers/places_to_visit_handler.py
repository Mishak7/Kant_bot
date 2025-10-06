from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from config.logger import logger
import traceback
from handlers.places_to_visit_handlers.places_to_visit_services import VisitAgent
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from handlers.main_handlers.languages import TEXTS


class VisitStates(StatesGroup):
    waiting_for_mood = State()


router = Router()

@router.callback_query(F.data == "places_to_visit")
async def places_to_visit_handler(callback: CallbackQuery, state: FSMContext, language: str):
    try:
        text = TEXTS[language]['handlers']['places_handler']
        sent_message = await callback.message.edit_text(
            text=text,
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[[InlineKeyboardButton(text=f"🎲 {TEXTS[language]['keyboards']['places_keyboard']['random']}", callback_data='random_place')],
                                 [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['main_keyboard']['back']}", callback_data="back_to_main")]]))

        await state.update_data(places_message_id=sent_message.message_id)

        await state.set_state(VisitStates.waiting_for_mood)
        await callback.answer()
    except Exception as e:
        logger.error(f'Places to visit error: {e}\n{traceback.format_exc()}')
        await callback.answer()


@router.message(VisitStates.waiting_for_mood)
async def process_mood(message: Message, state: FSMContext, bot: Bot, language: str):
    processing_message = None
    try:
        user_message = message.text

        state_data = await state.get_data()
        places_message_id = state_data.get('places_message_id')

        processing_message = await message.answer(f"🎯 {TEXTS[language]['keyboards']['places_keyboard']['analysis']}")

        spinner_frames = ["🔄", "⏳", "💭", "🎯"]
        for i, frame in enumerate(spinner_frames):
            try:
                await bot.edit_message_text(
                    chat_id=message.chat.id,
                    message_id=processing_message.message_id,
                    text=f"{frame} {TEXTS[language]['keyboards']['places_keyboard']['processing']}"
                )
                if i < len(spinner_frames) - 1:
                    await asyncio.sleep(0.5)
            except:
                pass

        agent = VisitAgent(language = language)
        response = await agent.get_recommendations(user_message)

        await bot.delete_message(chat_id=message.chat.id, message_id=processing_message.message_id)

        if places_message_id:
            try:
                await bot.delete_message(chat_id=message.chat.id, message_id=places_message_id)
            except Exception as e:
                logger.warning(f"Could not delete places message: {e}")

        await message.answer(
            response,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[ [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['main_keyboard']['back']}", callback_data=f"back_to_main_no_delete:{language}")]]
            ),
            disable_web_page_preview=True
        )

        await state.clear()

    except Exception as e:
        logger.error(f'Error processing mood: {e}\n{traceback.format_exc()}')

        if processing_message:
            try:
                await bot.delete_message(chat_id=message.chat.id, message_id=processing_message.message_id)
            except:
                pass

        await message.answer(
            f"❌ {TEXTS[language]['errors']['info_error']}",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[ [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['main_keyboard']['back']}", сallback_data=f"back_to_main_no_delete:{language}")]]
            )
        )


@router.callback_query(F.data == "random_place")
async def random_place_handler(callback: CallbackQuery, state: FSMContext, bot: Bot, language: str):
    try:
        state_data = await state.get_data()
        places_message_id = state_data.get('places_message_id')

        processing_message = await callback.message.answer(f"🎯 {TEXTS[language]['keyboards']['places_keyboard']['analysis']}")

        spinner_frames = ["🔄", "⏳", "💭", "🎯"]
        for i, frame in enumerate(spinner_frames):
            try:
                await bot.edit_message_text(
                    chat_id=callback.message.chat.id,
                    message_id=processing_message.message_id,
                    text=f"{frame} {TEXTS[language]['keyboards']['places_keyboard']['processing']}"
                )
                if i < len(spinner_frames) - 1:
                    await asyncio.sleep(0.5)
            except:
                pass

        agent = VisitAgent(language = language, is_random=True)
        response = await agent.get_recommendations(' ')

        await bot.delete_message(chat_id=callback.message.chat.id, message_id=processing_message.message_id)

        if places_message_id:
            try:
                await bot.delete_message(chat_id=callback.message.chat.id, message_id=places_message_id)
            except Exception as e:
                logger.warning(f"Could not delete places message in random handler: {e}")

        await callback.message.answer(
            response,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[[InlineKeyboardButton(text=f"🎲 {TEXTS[language]['keyboards']['places_keyboard']['random']}",
                                                 callback_data='random_place')],
                                [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['main_keyboard']['back']}",
                                                 callback_data=f"back_to_main_no_delete:{language}")]]),
            disable_web_page_preview=True)


        await state.set_state(VisitStates.waiting_for_mood)
        await callback.answer()
    except Exception as e:
        logger.error(f'Places to visit error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['info_error']}")