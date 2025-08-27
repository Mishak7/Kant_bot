import random
from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from services.speaking.speaking import SpeakingAnalyzer
from handlers.language_check_handlers.speaking_handlers.speaking_keyboard import back_to_language_keyboard


class SpeakingStates(StatesGroup):
    waiting_for_voice = State()

router = Router()

@router.callback_query(F.data == 'language_speaking')
async def speaking_send(callback: CallbackQuery, state: FSMContext):
    topics = [
        'Расскажите немного о своей семье.',
        'Есть ли у вас домашнее животное?',
        'Какие блюда вам нравятся?',
        'Опишите свою комнату.',
        'Какой ваш любимый вид транспорта?',
        'Где вы любите проводить свободное время?',
        'Как вы проводите свое воскресенье?',
        'Ваше самое яркое воспоминание детства?',
        'Куда вы хотели бы отправиться в путешествие?',
        'Какие привычки помогают вам оставаться продуктивным?',
        'Как прошёл твой вчерашний день?',
        'Кем ты работаешь и чем занимаешься на работе?',
        'О чём мечтает твоя семья?',
        'Что интересного произошло с тобой на прошлой неделе?',
        'Чем увлекается твой лучший друг?',
        'Поделись своими впечатлениями от последнего фильма, который смотрел.',
        'Почему ты решил учиться в Калининграде?'
    ]
    chosen_topic = random.choice(topics)

    await state.update_data(topic=chosen_topic)
    await callback.message.answer(f'Жду твой рассказ на тему: {chosen_topic}')
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
        await message.answer(f"Произошла ошибка при обработке: {e}")

    await state.clear()