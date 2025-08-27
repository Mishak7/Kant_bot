from aiogram import Router, F
from aiogram.types import CallbackQuery
router = Router()

@router.callback_query(F.data == "language_audio")
async def test(callback: CallbackQuery):
    text = "testing"
    await callback.message.edit_text(text,parse_mode="Markdown")
    await callback.answer()