import traceback
from aiogram import Router, F, types
from aiogram.types import CallbackQuery, Message
from config.logger import logger
from handlers.language_check_handlers.database.bot_logic import get_task, check_task, prepare_question, get_user_id
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()

class AnswerState(StatesGroup):
    waiting_for_answer = State()

@router.callback_query(F.data == "a1_level" | F.data == 'a2_level' | F.data == 'b1_level' | F.data == 'b2_level' | F.data == 'c1_level' | F.data == 'c2_level')
async def level_handler(callback: CallbackQuery, state: FSMContext):
    """Handler for all tasks"""
    try:
        await state.set_state(AnswerState.waiting_for_answer)
        level = callback.data.split('_')[0]
        telegram_id = callback.from_user.id
        user_id = get_user_id(telegram_id)
        task = get_task(level, user_id)
        prepared_task = prepare_question(task)
        text = f'''
{prepared_task['question']}

{prepared_task['content']}
'''
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
        
        answer_check = check_task(user_id, task_id, message.text)
        
        if answer_check == 'верно':
            response_text = 'Молодец! Все верно!'
        elif answer_check == 'неверно':
            response_text = 'К сожалению, не верно.'
        else:
            response_text = answer_check
        
        await message.answer(response_text, parse_mode="Markdown")
        await state.clear()
        
    except Exception as e:
        logger.error(f'Error: {e}\n{traceback.format_exc()}')
        await message.answer('Ошибка при проверке ответа')