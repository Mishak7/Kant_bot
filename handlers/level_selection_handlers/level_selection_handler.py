import traceback
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from config.logger import logger
from services.database.database_functions import get_task, check_task, prepare_question, get_user_id
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()


class AnswerState(StatesGroup):
    waiting_for_answer = State()


@router.callback_query(F.data.in_(["a1_level", "a2_level", "b1_level", "b2_level", "c1_level", "c2_level"]))
async def level_handler(callback: CallbackQuery, state: FSMContext):
    """Handler for all tasks"""
    try:
        await state.set_state(AnswerState.waiting_for_answer)
        #level = callback.data.split('_')[0]
        level = 'A1'
        telegram_id = callback.from_user.id
        user_id = await get_user_id(telegram_id)
        task = await get_task(level, user_id)
        prepared_task = await prepare_question(task)
        text = f"""{prepared_task['question']}\n{prepared_task['content']}"""
        await callback.message.edit_text(text, parse_mode="Markdown")
        await callback.answer()

        await state.update_data(
            task_id=prepared_task['task_id'],
            user_id=user_id
        )
    except Exception as e:
        logger.error(f'Error: {e}\n{traceback.format_exc()}')
        await callback.answer('Ошибка при загрузке информации', show_alert=True)


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

        answer_check = await check_task(user_id, task_id, message.text)

        if isinstance(answer_check, str):
            if answer_check == 'верно':
                response_text = '✅ Молодец! Все верно!'
            elif answer_check == 'неверно':
                response_text = '❌ К сожалению, не верно.'
            else:
                response_text = 'Неизвестный ответ от системы проверки'
        elif isinstance(answer_check, dict):
            response = answer_check
            response_text = f"""
{'✅ Верно!' if response['correct'] is True else '❌ Не верно.'}
{response['explanation']}
"""
        else:
            response_text = 'Ошибка: неверный формат ответа от системы проверки'
        await message.answer(response_text, parse_mode="Markdown")
        await state.clear()

    except Exception as e:
        logger.error(f'Error: {e}\n{traceback.format_exc()}')
        await message.answer('Ошибка при проверке ответа')
