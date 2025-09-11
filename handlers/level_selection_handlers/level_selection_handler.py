import traceback
from aiogram import Router, F
from aiogram.types import CallbackQuery
from config.logger import logger
from services.database.database_functions import get_module_progress

router = Router()

@router.callback_query(F.data == "a1_level" or F.data == 'a2_level' or F.data == 'b1_level' or F.data == 'b2_level' or F.data == 'c1_level' or F.data == 'c2_level')
async def level_handler(callback: CallbackQuery):
    """Handler for all tasks"""
    try:
        text = str(await get_module_progress(telegram_id=1,  module_id=1))
        await callback.message.answer(text, parse_mode="Markdown")
    except Exception as e:
        logger.error(f'Error: {e}\n{traceback.format_exc()}')
        await callback.answer('Ошибка при загрузке информации', show_alert=True)
