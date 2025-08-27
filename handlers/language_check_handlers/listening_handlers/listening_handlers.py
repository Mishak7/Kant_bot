from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, FSInputFile, Message
from handlers.language_check_handlers.grammar_handlers.grammar_keyboard import language_keyboard, back_to_language_keyboard, \
    translation_keyboard, back_to_translation
from services.grammar.grammar import gigachat_response

router = Router()

@router.callback_query(F.data == "language_audio")
async def test(callback: CallbackQuery):
    text = "testing"
    await callback.message.edit_text(text,parse_mode="Markdown")
    await callback.answer()