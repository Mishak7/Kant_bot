from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from services.grammar.grammar import gigachat_response
from handlers.language_check_handlers.grammar_handlers.grammar_keyboard import back_to_language_keyboard
from handlers.main_handlers.languages import TEXTS
<<<<<<< HEAD
from handlers.main_handlers.commands import get_user_language

router = Router()
language = get_user_language(callback.from_user.id)
=======

router = Router()
>>>>>>> main

class TranslationState(StatesGroup):
    waiting_for_text = State()

@router.callback_query(F.data == "language_audio")
<<<<<<< HEAD
async def send_voice(callback: CallbackQuery, state: FSMContext):
    voice_file =  FSInputFile('file_name.ogg')
    text = TEXTS[language]['handlers']['language_check_handlers']['listening_handlers']['send_voice']
    await callback.message.edit_text(text, parse_mode="Markdown")
    await callback.message.answer_voice(voice=voice_file)
=======
async def send_voice(callback: CallbackQuery, state: FSMContext, language: str):
    voice_file =  FSInputFile('file_name.opus')
    text = TEXTS[language]['handlers']['language_check_handlers']['listening_handlers']['send_voice']
    await callback.message.edit_text(text, parse_mode="Markdown")
    await callback.message.answer_voice(voice=voice_file, duration=255)
>>>>>>> main
    await state.set_state(TranslationState.waiting_for_text)
    await callback.answer()


@router.message(TranslationState.waiting_for_text, F.text)
<<<<<<< HEAD
async def audio_text_analysis(message: Message, state: FSMContext):
    try:
        transcription_text = message.text
        transcription_result = gigachat_response(transcription_text, to_russian=False, audio_file=True)
        await message.answer(transcription_result, parse_mode="Markdown", reply_markup=back_to_language_keyboard())
    except Exception as e:
        await message.answer(f"{TEXTS[language]['errors']['audio_error']}: {str(e)}")
    finally:
        await state.clear()
=======
async def audio_text_analysis(message: Message, state: FSMContext, language: str):
    try:
        transcription_text = message.text
        transcription_result = gigachat_response(transcription_text, to_russian=False, audio_file=True)
        await message.answer(transcription_result, parse_mode="Markdown", reply_markup=back_to_language_keyboard(language))
    except Exception as e:
        await message.answer(f"{TEXTS[language]['errors']['audio_error']}: {str(e)}")
    finally:
        await state.clear()
>>>>>>> main
