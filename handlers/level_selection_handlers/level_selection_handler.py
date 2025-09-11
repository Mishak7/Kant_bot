import traceback
from aiogram import Router, F, types
from aiogram.types import CallbackQuery
from config.logger import logger
from handlers.language_check_handlers.database.bot_logic import get_task, check_task, prepare_question, get_user_id
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()
user_tasks = {}

class AnswerState(StatesGroup):
    waiting_for_answer = State()

@router.callback_query(F.data == "a1_level" | F.data == 'a2_level' | F.data == 'b1_level' | F.data == 'b2_level' | F.data == 'c1_level' | F.data == 'c2_level')
async def level_handler(callback: CallbackQuery, message: types.Message, state: FSMContext):
    """Handler for all tasks"""
    try:
        await state.set_state(AnswerState.waiting_for_answer)
        level = callback.data.split('_')[0]
        telegram_id = message.from_user.id
        user_id = get_user_id(telegram_id)
        task = get_task(level, user_id)
        prepared_task = prepare_question(task)
        user_tasks[callback.from_user.id] = prepared_task['task_id']
        text = f'''
{prepared_task['question']}

{prepared_task['content']}
'''
        await callback.message.edit_text(text, parse_mode="Markdown")
        await callback.answer()
    except Exception as e:
        logger.error(f'Error: {e}\n{traceback.format_exc()}')
        await callback.answer('Ошибка при загрузке информации', show_alert=True)


@router.callback_query(F.text)
async def check_user_answer(callback: CallbackQuery, message: types.Message, state: FSMContext):
    """Проверка ответа от польхоателя"""
    try:
        await state.update_data(answer_send=True)
        telegram_id = message.from_user.id
        user_id = get_user_id(telegram_id)
        answer_check = check_task(user_id, user_tasks[callback.from_user.id], )