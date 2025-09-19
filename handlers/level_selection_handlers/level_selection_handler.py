from aiogram import Router, F, Bot
import os
import tempfile

from aiogram.filters import state
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from config.logger import logger
from services.database.database_functions import get_task, check_task, prepare_question, get_user_id, extract_audio_from_db, explain_multiple_choice, show_progress, give_hint
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import traceback

router = Router()

class AnswerState(StatesGroup):
    waiting_for_answer = State()

levels = ["A1", "A2", "B1", "B2", "C1", "C2"]

@router.callback_query(F.data.startswith('hint'))
async def task_hint(callback: CallbackQuery):
    try:
        task_id = callback.data.split('!ПУ!')[1]
        gigachat_hint = await give_hint(task_id)
        await callback.message.answer(gigachat_hint, parse_mode='Markdown')
        await callback.answer()
    except Exception as e:
        logger.error(f'Error: {e}\n{traceback.format_exc()}')
        await callback.answer('Ошибка при выводе подсказки', show_alert=True)


@router.callback_query(F.data.in_(["A1", "A2", "B1", "B2", "C1", "C2"]))
async def level_handler(callback: CallbackQuery, state: FSMContext):
    """Handler for all tasks"""
    try:
        await callback.message.delete()

        level = callback.data

        await state.set_state(AnswerState.waiting_for_answer)

        telegram_id = callback.from_user.id
        chat_id = callback.message.chat.id
        user_id = await get_user_id(telegram_id)
        task = await get_task(level, user_id)
        prepared_task = await prepare_question(task)
        text = f"""{prepared_task['question']}\n\n{prepared_task['content']}"""
        is_speaking_task = prepared_task.get('type') == 'Speaking'
        if prepared_task.get('audio'):
            audio_file = await extract_audio_from_db(prepared_task['task_id'])
            if audio_file:
                await callback.message.answer(prepared_task['question'], parse_mode="Markdown")
                await callback.bot.send_voice(chat_id=chat_id, voice=audio_file, reply_markup=InlineKeyboardMarkup(
                                              inline_keyboard=[[InlineKeyboardButton(text='💡Подсказка', callback_data=f'hint!ПУ!{prepared_task["task_id"]}')]]))
        else:
            await callback.message.answer(text, parse_mode="Markdown",
                                          reply_markup=InlineKeyboardMarkup(
                                              inline_keyboard=[[InlineKeyboardButton(text='💡Подсказка', callback_data=f'hint!ПУ!{prepared_task["task_id"]}')]]))

        await callback.answer()
        await state.update_data(
            task_id=prepared_task['task_id'],
            user_id=user_id,
            is_speaking_task=is_speaking_task,
            level=level
        )
    except Exception as e:
        logger.error(f'Error: {e}\n{traceback.format_exc()}')
        await callback.answer('Ошибка при загрузке информации', show_alert=True)

@router.message(AnswerState.waiting_for_answer, F.content_type == 'voice')
async def handle_voice_answer(message: Message, state: FSMContext, bot: Bot):
    """Handler for voice answers from user"""
    try:
        file_id = message.voice.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path

        voice_file = await bot.download_file(file_path)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.ogg') as tmp_file:
            tmp_file.write(voice_file.read())
            voice_file_path = tmp_file.name

        try:
            data = await state.get_data()
            task_id = data.get('task_id')
            user_id = data.get('user_id')
            level = data.get('level')

            new_level = levels[levels.index(level) + 1] if len(levels) >= levels.index(
                level) + 1 else 'всё!'


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
                response_text = f"""
Вы набрали {response['score']} баллов из {response['max_score']} возможных.\n\nОбъяснение такой оценки:
{response['explanation']}
                """
            else:
                response_text = 'Ошибка: неверный формат ответа от системы проверки'

            progress = await show_progress(user_id, level)
            if progress['score'] >= 100:
                await message.answer(f"🎉 Поздравляем, вы закончили уровень {progress['level_name']}!",
                                     parse_mode="Markdown",
                                     reply_markup=InlineKeyboardMarkup(
                                         inline_keyboard=[[InlineKeyboardButton(
                                             text=f"🚀 Перейти на новый уровень: {level} 🛬 {new_level}",
                                             callback_data=new_level)],
                                                          [InlineKeyboardButton(text='🔄 Продолжить текущий',
                                                                                callback_data=level)]]))

            else:
                response_text += '\n' + progress['text']

                await message.answer(
                    response_text,
                    parse_mode="Markdown",
                    reply_markup=InlineKeyboardMarkup(
                        inline_keyboard=[
                                         [InlineKeyboardButton(text="➡️ Следующее задание", callback_data=level)],
                                         [InlineKeyboardButton(text="↩️ Назад к уровням", callback_data="language_check")]]))

        finally:
            os.unlink(voice_file_path)

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
        level = data.get('level')
        is_speaking_task = data.get("is_speaking_task", False)

        new_level = levels[levels.index(level) + 1] if len(levels) >= levels.index(level) + 1 else 'всё!'

        if is_speaking_task:
            await message.answer("Пожалуйста, отправь голосовое сообщение.")
            return

        if not task_id or not user_id:
            await message.answer("Произошла ошибка. Попробуйте начать заново.")
            await state.clear()
            return

        if message.content_type == "voice" and message.voice:
            voice_file = await message.voice.download()
            user_answer = voice_file.name
            is_voice = True
        else:
            user_answer = message.text
            is_voice = False

        answer_check = await check_task(user_id, task_id, user_answer, is_voice)

        if isinstance(answer_check, str):
            if answer_check.startswith('верно'):
                score_message = answer_check.split('!')[1]
                response_text = f'✅ Молодец! Все верно!\n{score_message}'
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

        if response_text == '❌ К сожалению, ответ неверный.':
            await message.answer(response_text,
                                 parse_mode="Markdown",
                                 reply_markup=InlineKeyboardMarkup(
                                     inline_keyboard=[
                                         [InlineKeyboardButton(text='🤔 Объяснение',
                                                               callback_data=f'explanation!ПУ!{task_id}!ПУ!{user_answer}')],
                                         [InlineKeyboardButton(text="➡️ Следующее задание", callback_data=level)],
                                         [InlineKeyboardButton(text="↩️ Назад к уровням", callback_data="language_check")]]
                                        )
                                 )

        else:
            progress = await show_progress(user_id, level)

            if progress['score'] >= 100:

                await message.answer(f"🎉 Поздравляем, вы закончили уровень {progress['level_name']}!",
                                     parse_mode="Markdown",
                                     reply_markup=InlineKeyboardMarkup(
                                         inline_keyboard=[[InlineKeyboardButton(text=f"🚀 Перейти на новый уровень: {level} 🛬 {new_level}", callback_data=new_level)],
                                                          [InlineKeyboardButton(text='🔄 Продолжить текущий', callback_data=level)]]))

            else:
                response_text += '\n' + progress['text']
                await message.answer(
                    response_text,
                    parse_mode="Markdown",
                    reply_markup=InlineKeyboardMarkup(
                        inline_keyboard=[
                            [InlineKeyboardButton(text="➡️ Следующее задание", callback_data=level)],
                            [InlineKeyboardButton(text="↩️ Назад к уровням", callback_data="language_check")]]))

    except Exception as e:
        logger.error(f'Error: {e}\n{traceback.format_exc()}')
        await message.answer('Ошибка при проверке ответа')

@router.callback_query(F.data.startswith('explanation'))
async def explanation_handler(callback: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        level = data.get('level')
        user_id = data.get('user_id')
        new_level = levels[levels.index(level) + 1] if len(levels) >= levels.index(
                level) + 1 else 'всё!'


        explanation, task_id, user_answer = callback.data.split("!ПУ!")
        gigachat_explanation = await explain_multiple_choice(task_ident=task_id, user_answer=user_answer)

        progress = await show_progress(user_id, level)
        if progress['score'] >= 100:
            await callback.message.answer(f"{str(gigachat_explanation)} \n🎉 Поздравляем, вы закончили уровень {progress['level_name']}!",
                                 parse_mode="Markdown",
                                 reply_markup=InlineKeyboardMarkup(
                                     inline_keyboard=[[InlineKeyboardButton(
                                         text=f"🚀 Перейти на новый уровень: {level} 🛬 {new_level}",
                                         callback_data=new_level)],
                                         [InlineKeyboardButton(text='🔄 Продолжить текущий',
                                                               callback_data=level)]]))
        else:
            await callback.message.answer(str(gigachat_explanation),
                                          parse_mode="Markdown",
                                          reply_markup= InlineKeyboardMarkup(
                                              inline_keyboard= [[InlineKeyboardButton(text="➡️ Следующее задание", callback_data=level)],
                                                                [InlineKeyboardButton(text="↩️ Назад к уровням", callback_data="language_check")]]))

        await callback.answer()
        await state.clear()
    except Exception as e:
        logger.error(f'Error: {e}\n{traceback.format_exc()}')
        await callback.answer('Ошибка при объяснении задания multiple_choice', show_alert=True)