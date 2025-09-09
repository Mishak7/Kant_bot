import traceback
from aiogram import Router, F
from aiogram.types import CallbackQuery
from config.logger import logger
from handlers.level_selection_handlers.level_selection_keyboard import back_to_level_selection_keyboard, back_to_after_level_selection_keyboard, after_level_selection_keyboard, level_selection_keyboard
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.callback_query(F.data == "a1_level" | F.data == 'a2_level' | F.data == 'b1_level' | F.data == 'b2_level' | F.data == 'c1_level' | F.data == 'c2_level')
async def level_handler(callback: CallbackQuery):
    """Handler for all tasks"""
    try:
        level = callback.data.split('_')[0]
        text = ''''''
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=after_level_selection_keyboard(level))
        await callback.answer()
    except Exception as e:
        logger.error(f'Error: {e}\n{traceback.format_exc()}')
        await callback.answer('Ошибка при загрузке информации', show_alert=True)
