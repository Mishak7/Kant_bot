from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from config.logger import logger
from services.database.database_functions import get_task, check_task, prepare_question, get_user_id, extract_audio_from_db
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import traceback

router = Router()

class AnswerState(StatesGroup):
    waiting_for_answer = State()

@router.callback_query(F.data.in_(["a1_level", "a2_level", "b1_level", "b2_level", "c1_level", "c2_level"]))
async def level_handler(callback: CallbackQuery, state: FSMContext):
    """Handler for all tasks"""
    try:
        await state.set_state(AnswerState.waiting_for_answer)
        level = 'A1'
        telegram_id = callback.from_user.id
        chat_id = callback.message.chat.id
        user_id = await get_user_id(telegram_id)
        task = await get_task(level, user_id)
        prepared_task = await prepare_question(task)
        text = f"""{prepared_task['question']}\n\n{prepared_task['content']}"""
        if prepared_task.get('audio'):
            audio_file = await extract_audio_from_db(prepared_task['task_id'])
            if audio_file:
                await callback.message.edit_text(prepared_task['question'], parse_mode="Markdown")
                await callback.bot.send_voice(chat_id=chat_id, voice=audio_file)
        else:
            await callback.message.edit_text(text, parse_mode="Markdown")
        await callback.answer()
        await state.update_data(
            task_id=prepared_task['task_id'],
            user_id=user_id
        )
    except Exception as e:
        logger.error(f'Error: {e}\n{traceback.format_exc()}')
        await callback.answer('Ошибка при загрузке информации', show_alert=True)

@router.message(AnswerState.waiting_for_answer, F.content_type == 'voice')
async def handle_voice_answer(message: Message, state: FSMContext, bot: Bot):
    """Handler for voice answers from user"""
    try:
        # Получаем информацию о файле
        file_id = message.voice.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path

        # Скачиваем файл
        voice_file = await bot.download_file(file_path)

        # Сохраняем файл локально
        voice_file_path = f"voice_message_{message.message_id}.ogg"
        with open(voice_file_path, 'wb') as f:
            f.write(voice_file.read())

        # Проверка ответа
        data = await state.get_data()
        task_id = data.get('task_id')
        user_id = data.get('user_id')
        if not task_id or not user_id:
            await message.answer("Произошла ошибка. Попробуйте начать заново.")
            await state.clear()
            return

        user_answer = voice_file_path
        is_voice = True
        answer_check = await check_task(user_id, task_id, user_answer, is_voice=is_voice)

        if isinstance(answer_check, str):
            if answer_check == 'верно':
                response_text = '✅ Молодец! Все верно!'
            elif answer_check == 'неверно':
                response_text = '❌ К сожалению, ответ неверный.'
            else:
                response_text = 'Неизвестный ответ от системы проверки'
        elif isinstance(answer_check, dict):
            response = answer_check
            print(response)
            response_text = f"""
Вы набрали {response['score']} баллов из {response['max_score']} возможных.\n\nОбъяснение такой оценки:
{response['explanation']}
            """
        else:
            response_text = 'Ошибка: неверный формат ответа от системы проверки'

        await message.answer(response_text,
                             parse_mode="Markdown",
                             reply_markup=InlineKeyboardMarkup(
                                 inline_keyboard=[[InlineKeyboardButton(text="➡️ Следующее задание", callback_data="a1_level")]]
                             )
                             )
        await state.clear()
    except Exception as e:
        logger.error(f'Error: {e}\n{traceback.format_exc()}')
        await message.answer('Ошибка при обработке голосового сообщения')


@router.message(AnswerState.waiting_for_answer)
async def check_text_answer(message: Message, state: FSMContext):
    """Проверка текстового ответа от пользователя"""
    try:
        data = await state.get_data()
        task_id = data.get('task_id')
        user_id = data.get('user_id')
        if not task_id or not user_id:
            await message.answer("Произошла ошибка. Попробуйте начать заново.")
            await state.clear()
            return

        user_answer = message.text
        is_voice = False
        answer_check = await check_task(user_id, task_id, user_answer, is_voice=is_voice)

        if isinstance(answer_check, str):
            if answer_check == 'верно':
                response_text = '✅ Молодец! Все верно!'
            elif answer_check == 'неверно':
                response_text = '❌ К сожалению, ответ неверный.'
            else:
                response_text = 'Неизвестный ответ от системы проверки'
        elif isinstance(answer_check, dict):
            response = answer_check
            print(response)
            response_text = f"""
Вы набрали {response['score']} баллов из {response['max_score']} возможных.\n\nОбъяснение такой оценки:
{response['explanation']}
            """
        else:
            response_text = 'Ошибка: неверный формат ответа от системы проверки'

        await message.answer(response_text,
                             parse_mode="Markdown",
                             reply_markup=InlineKeyboardMarkup(
                                 inline_keyboard=[[InlineKeyboardButton(text="➡️ Следующее задание", callback_data="a1_level")]]
                             )
                             )
        await state.clear()
    except Exception as e:
        logger.error(f'Error: {e}\n{traceback.format_exc()}')
        await message.answer('Ошибка при проверке ответа')
