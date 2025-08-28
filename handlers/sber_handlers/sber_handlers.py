from aiogram import Router, F
from aiogram.types import CallbackQuery
from handlers.sber_handlers.sber_keyboard import back_to_sber_keyboard, card_keyboard, loan_keyboard
from config.logger import logger
import traceback

router = Router()


@router.callback_query(F.data == "educational_loan")
async def educational_loan_handler(callback: CallbackQuery):
    try:
        await callback.message.edit_text(EDUCATIONAL_LOAN_TEXT,
                                         parse_mode="Markdown",
                                         reply_markup=loan_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'sber error: {e}\n{traceback.format_exc()}')
        await callback.answer("Ошибка при загрузке информации про сбербанк")


@router.callback_query(F.data == "sber_card")
async def sber_card_handler(callback: CallbackQuery):
    try:
        await callback.message.edit_text(SBER_CARD_TEXT,
                                         parse_mode="Markdown",
                                         reply_markup=card_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'sber card error: {e}\n{traceback.format_exc()}')
        await callback.answer("Ошибка при загрузке информации про карту сбербанк")


@router.callback_query(F.data == "useful_links")
async def useful_links_handler(callback: CallbackQuery):
    try:
        await callback.message.edit_text(USEFUL_LINKS_TEXT,
                                         parse_mode="Markdown",
                                         disable_web_page_preview=True,
                                         reply_markup=back_to_sber_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'sber error: {e}\n{traceback.format_exc()}')
        await callback.answer("Ошибка при загрузке информации про сбербанк")


USEFUL_LINKS_TEXT = """
🔗 Полезные ресурсы Сбера и партнёров:

• [Платформа Нетология](https://netology.ru/navigation) — онлайн‑курсы и профессии
• [Тренируй спокойствие](http://interview.sberstudent.ru/?utm_source=sber&utm_medium=internal&utm_campaign=salaryprojectmanagement) — тренажёр для собеседований
• [Школа 21](https://sbergraduate.ru/careerofthefuture/) — бесплатное IT‑образование
• [СберСова](https://sbersova.ru/academy/courses/kibergramotnost?utm_source=event&utm_medium=free&utm_campaign=speaker) — образовательная платформа
• [Кибрарий](https://sber.ru/kibrary) — цифровая библиотека
• [Цифровой марафон](https://it-marathon.21-school.ru/?utm_source=ter_bank&utm_medium=referral&utm_campaign) — соревнования и челленджи
• [Стартап от Сбера](https://sberstudent.sberclass.ru/) — поддержка стартапов
• [Стажировки](https://sbergraduate.ru/practice/) — вакансии и стажировки
"""

SBER_CARD_TEXT = """
💳 *Карта Сбера*

✨ *Бесплатное обслуживание навсегда*
💸 *До 5% кэшбэка* за любимые покупки
📈 *Проценты на накопительный счёт* до *16%* годовых
🎨 *Уникальные стикеры от Сбера* для каждой транзакции — коллекционируй и делись с друзьями!
🎯 *Специальные предложения для молодежи* — скидки на развлечения, образование и многое другое

Нажми *кнопку ниже* для подробностей:
"""

EDUCATIONAL_LOAN_TEXT = """
🎓 *Образовательный кредит от Сбера*

🎯 *Всего 3% годовых*
📚 *Платите только проценты во время обучения* 
👨‍🎓 *Оформление с 14 лет*
⏳ *Рассрочка до 15 лет после выпуска*

Нажми *кнопку ниже* для подробностей:
"""