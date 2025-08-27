from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, FSInputFile, Message
from handlers.language_check_handlers.grammar_handlers.grammar_keyboard import translation_keyboard, back_to_translation
from services.grammar.grammar import gigachat_response

router = Router()

class TranslationState(StatesGroup):
    waiting_to_russian = State()
    waiting_from_russian = State()


@router.callback_query(F.data == "language_grammar")
async def language_grammar_handler(callback: CallbackQuery):
    text = '''
    *Выберите вариант перевода*:
    '''

    await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=translation_keyboard())
    await callback.answer()


@router.callback_query(F.data == "translate_to_russian")
async def translate_to_russian_handler(callback: CallbackQuery, state: FSMContext):
    await state.set_state(TranslationState.waiting_to_russian)
    text = '''
    Переведите данный текст на русский язык:

    '''

    await callback.message.edit_text(text, parse_mode="Markdown")
    await callback.answer()


@router.callback_query(F.data == "translate_from_russian")
async def translate_from_russian_handler(callback: CallbackQuery, state: FSMContext):
    await state.set_state(TranslationState.waiting_from_russian)
    text = '''
    Переведите данный текст с русского языка на свой:

    '''

    await callback.message.edit_text(text, parse_mode="Markdown")
    await callback.answer()



@router.message(TranslationState.waiting_to_russian, F.text)
async def handle_to_russian_text(message: Message, state: FSMContext):
    translate_text = message.text
    translation_result = gigachat_response(translate_text, to_russian=True, audio_file=False)
    await message.answer(translation_result, parse_mode="Markdown", reply_markup=back_to_translation())
    await state.clear()


@router.message(TranslationState.waiting_from_russian, F.text)
async def handle_from_russian_text(message: Message, state: FSMContext):
    translate_text = message.text
    translation_result = gigachat_response(translate_text, to_russian=False, audio_file=False)
    await message.answer(translation_result, parse_mode="Markdown", reply_markup=back_to_translation())
    await state.clear()