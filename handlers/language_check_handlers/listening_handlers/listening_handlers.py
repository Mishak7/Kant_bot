from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from services.grammar.grammar import gigachat_response
from handlers.language_check_handlers.grammar_handlers.grammar_keyboard import back_to_language_keyboard

router = Router()

class TranslationState(StatesGroup):
    waiting_for_text = State()

@router.callback_query(F.data == "language_audio")
async def send_voice(callback: CallbackQuery, state: FSMContext):
    voice_file =  FSInputFile('file_name.ogg')
    text = 'Прослушайте текст и попробуйте написать его на русском.'
    await callback.message.edit_text(text, parse_mode="Markdown")
    await callback.message.answer_voice(voice=voice_file)
    await state.set_state(TranslationState.waiting_for_text)
    await callback.answer()


@router.message(TranslationState.waiting_for_text, F.text)
async def audio_text_analysis(message: Message, state: FSMContext):
    try:
        transcription_text = message.text
        transcription_result = gigachat_response(transcription_text, to_russian=False, audio_file=True)
        await message.answer(transcription_result, parse_mode="Markdown", reply_markup=back_to_language_keyboard())
    except Exception as e:
        await message.answer(f"Ошибка при обработке текста: {str(e)}")
    finally:
        await state.clear()