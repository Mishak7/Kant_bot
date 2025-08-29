import random
from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from services.speaking.speaking import SpeakingAnalyzer
from handlers.language_check_handlers.speaking_handlers.speaking_keyboard import back_to_language_keyboard
from handlers.main_handlers.languages import TEXTS
from handlers.main_handlers.commands import get_user_language


class SpeakingStates(StatesGroup):
    waiting_for_voice = State()

router = Router()
language = get_user_language(callback.from_user.id)

@router.callback_query(F.data == 'language_speaking')
async def speaking_send(callback: CallbackQuery, state: FSMContext):
    topics = TEXTS[language]['handlers']['language_check_handlers']['speaking_handlers']['topics']
    chosen_topic = random.choice(topics)

    await state.update_data(topic=chosen_topic)
    await callback.message.answer(f"{TEXTS[language]['handlers']['language_check_handlers']['speaking_handlers']['speaking_send']} {chosen_topic}")
    await state.set_state(SpeakingStates.waiting_for_voice)


@router.message(F.voice, SpeakingStates.waiting_for_voice)
async def handle_voice_message(message: Message, state: FSMContext, bot: Bot):
    state_data = await state.get_data()
    topic = state_data.get('topic', 'Неизвестная тема')

    file_info = await bot.get_file(message.voice.file_id)
    file_content = await bot.download_file(file_info.file_path)

    analyzer = SpeakingAnalyzer(topic)

    try:
        result = await analyzer.process_voice_message(file_content.read())
        await message.answer(f"Результат анализа:\n\n{result}", parse_mode="Markdown", reply_markup=back_to_language_keyboard())
    except Exception as e:
        await message.answer(f"{TEXTS[language]['errors']['audio_error']}: {e}")

    await state.clear()
