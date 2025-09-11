import traceback
from aiogram import Router, F
from aiogram.types import CallbackQuery
from config.logger import logger

router = Router()

@router.callback_query(F.data == "a1_level" | F.data == 'a2_level' | F.data == 'b1_level' | F.data == 'b2_level' | F.data == 'c1_level' | F.data == 'c2_level')
async def level_handler(callback: CallbackQuery):
    """Handler for all tasks"""
    try:
        level = callback.data.split('_')[0]
        text = '''

'''
        await callback.message.edit_text(text, parse_mode="Markdown")
        await callback.answer()
    except Exception as e:
        logger.error(f'Error: {e}\n{traceback.format_exc()}')
        await callback.answer('Ошибка при загрузке информации', show_alert=True)
