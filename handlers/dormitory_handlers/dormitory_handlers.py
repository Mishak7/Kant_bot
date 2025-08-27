"""
Dormitory information handlers for student accommodation.

This module provides handlers for dormitory-related information including:
- Check-in procedures and requirements
- Payment information
- Dormitory addresses and selection
- Rules and regulations
- Laundry facilities
- Certificate requirements
"""

import traceback
from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from config.logger import logger
from handlers.dormitory_handlers.dormitory_keyboard import (
    dormitory_check_in_keyboard,
    back_to_dormitory_keyboard,
    dormitories_keyboard_back_to_dormitory_info,
    back_to_check_in_keyboard
)


router = Router()

@router.callback_query(F.data == "dormitory_check-in")
async def dormitory_check_in_handler(callback: CallbackQuery):
    """Display dormitory check-in procedures and requirements."""
    try:
        await callback.message.edit_text(
            DORMITORY_TEXT,
            parse_mode="Markdown",
            reply_markup=dormitory_check_in_keyboard()
        )
        await callback.answer()
    except Exception as e:
        logger.error(f'Dormitory check-in error: {e}\n{traceback.format_exc()}')
        await callback.answer("Ошибка при загрузке информации о заселении")


@router.callback_query(F.data == "dormitory_payment")
async def dormitory_payment_handler(callback: CallbackQuery):
    """Display dormitory payment information and procedures."""
    try:
        await callback.message.edit_text(
            PAYMENT_TEXT,
            parse_mode="Markdown",
            reply_markup=back_to_dormitory_keyboard()
        )
        await callback.answer()
    except Exception as e:
        logger.error(f'Dormitory payment error: {e}\n{traceback.format_exc()}')
        await callback.answer("Ошибка при загрузке информации об оплате")


@router.callback_query(F.data == "dormitory_address")
async def dormitory_addresses_handler(callback: CallbackQuery):
    """Display dormitory selection menu for address information."""
    try:
        await callback.message.delete()
        await callback.message.answer(
            'Выбери общежитие',
            reply_markup=dormitories_keyboard_back_to_dormitory_info()
        )
        await callback.answer()
    except Exception as e:
        logger.error(f'Dormitory addresses error: {e}\n{traceback.format_exc()}')
        await callback.answer("Ошибка при загрузке адресов общежитий")


@router.callback_query(F.data == "dormitory_rules")
async def dormitory_rules_handler(callback: CallbackQuery):
    """Display dormitory rules and regulations with photo."""
    try:
        photo = FSInputFile('handlers/location_handlers/dormitory_pictures/dormitory_rules.jpg')

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=RULES_TEXT,
            parse_mode="Markdown",
            reply_markup=back_to_dormitory_keyboard()
        )
        await callback.answer()
    except Exception as e:
        logger.error(f'Dormitory rules error: {e}\n{traceback.format_exc()}')
        await callback.answer("Ошибка при загрузке правил общежития")


@router.callback_query(F.data == "dormitory_laundry")
async def dormitory_laundry_handler(callback: CallbackQuery):
    """Display laundry facilities information."""
    try:
        await callback.message.edit_text(
            LAUNDRY_TEXT,
            reply_markup=back_to_dormitory_keyboard()
        )
        await callback.answer()
    except Exception as e:
        logger.error(f'Dormitory laundry error: {e}\n{traceback.format_exc()}')
        await callback.answer("Ошибка при загрузке информации о прачечной")


@router.callback_query(F.data == "no_certificate")
async def dormitory_no_certificate_handler(callback: CallbackQuery):
    """Handle case when student doesn't have required certificate."""
    try:
        await callback.message.delete()
        await callback.message.answer(
            NO_CERIFICATION_TEXT,
            parse_mode="Markdown",
            reply_markup=back_to_check_in_keyboard()
        )
        await callback.answer()
    except Exception as e:
        logger.error(f'No certificate error: {e}\n{traceback.format_exc()}')
        await callback.answer("Ошибка при обработке запроса о справке")


DORMITORY_TEXT = text = """Подробнее про заселение ты можешь узнать (https://kantiana.ru/students/kampus/obshchezhitiya/zaselenie-v-obshchezhitie/).

*Как подать заявление на место в общежитии?*

1. После твоего зачисления на образовательную программу необходимо подать заявление на место на сайте по https://vk.com/away.php?to=https%3A%2F%2Fkantiana.ru%2Fstudents%2Fdormitory%2F&cc_key=

_Обращаем внимание, что количество мест в общежитии ограничено._

2. Если тебе на почту пришло уведомление о том, что общежитие одобрено, это значит, что твоя заявка принята, и теперь ты участвуешь в конкурсе. Статус своего заявления можно отслеживать по группе Комплекса студенческих общежитий: [группа КСО] https://vk.com/kso_bfu

3. Когда ты увидел свое имя в рейтинге, это значит, что тебе можно получать 2 необходимых допуска для заселения. О них подробно расскажем далее.

4. С полученными допусками подходи на подписание договора в КСО (ул.Невского, 14/1, кабинет 101).

5. После заключения договора и оплаты проживания с направлением подходи к заведующей указанного общежития для заселения и инструктажа.

По приезде необходимо подписать договор найма жилого помещения в студенческом общежитии в Центре социально-экономической поддержки студентов, получить направление и оплатить общежитие за первый семестр. 

_С собой обязательно взять паспорт._

*Приемные часы Центра социально-экономической поддержки студентов:*

- Понедельник: C 10:00 до 17:00
- Вторник: C 10:00 до 17:00
- Четверг: C 10:00 до 17:00
- Пятница: C 10:00 до 16:45 

Обеденный перерыв с 13:00 до 14:00

*Адрес: ул. А. Невского, 14, корпус 10, 1 этаж, кабинет 14.*

*Медицинская справка*

Чтобы проживать в общежитии, необходимо предоставить коменданту общежития справку о прохождении медицинской комиссии. Для получения такой справки тебе нужно посетить кабинет 2 в Клинико-диагностическом центре БФУ им. И.Канта (КДЦ). 

*С собой возьми:*

- паспорт;
- прививочный сертификат (документ, в котором указаны все прививки, которые тебе делались в течение жизни, в частности там должны быть справки о прививках от кори, дифтерии, столбняка и гепатита В);
- флюорографию не старше 1 года;
- 2 отрицательных результата ПЦР-теста на COVID-19/ допуск к занятиям.

_Документы должны быть на русском языке или иметь заверенный перевод на русский._

*Адрес* КДЦ БФУ им.И.Канта: (https://goo.gl/maps/bwq24xTh5P1EctiU8)

_В случае если на момент заселения у тебя этих справок нет, их необходимо сделать за свой счет в любой клинике._
"""

PAYMENT_TEXT = """
    Оплатить общежитие можно двумя путями.

1. Лично. В кабинет № 222 административного корпуса, 2 этаж. Здесь ты получишь квитанцию для оплаты в кассе на том же этаже. Оплатить через кассу можно наличными в рублях или банковской картой.

2. Удаленно на сайте.

Первокурсники оплачивают при заселении полностью первый семестр. Далее осенний семестр оплачивается до 15 сентября, а весенний – до 15 февраля.
"""

RULES_TEXT = """
- Содержи комнату и кухню в чистоте самостоятельно.
- Заводить домашних животных запрещено.
- Уважай соседей: соблюдай тишину с 23:00 до 08:00, будь вежлив и внимателен.
- До 22:00 можешь приглашать гостей, но ночная гостевая стоянка исключена.
- Курение и употребление алкоголя на территории университета категорически запрещено.
- Тщательно изучи технику безопасности, узнай расположение ближайших эвакуационных выходов.
- При неисправности оборудования немедленно уведомляй коменданта.
- Свяжись с администрацией общежития по любым вопросам проживания.
- Не осуществляй переезд в другую комнату без одобрения Центра социальной поддержки студентов.

_Не все общежития оснащены посудой, но еженедельно предоставляется свежее постельное бельё._

*Совет*: знакомься с комендантом сразу после вселения — он твой главный помощник в вопросах быта.
"""

LAUNDRY_TEXT = """
    Прачечные находятся в здании каждого общежития. Комендант или вахтер расскажут, где именно находится комната со стиральными машинами и в какое время можно брать ключ.

Стиральный порошок нужно приносить с собой. Прачечная оборудована несколькими стиральными машинами, в которых можно стирать одновременно, если много белья для стирки. Стирать нижнее белье обязательно в специальных мешках. Стирать обувь запрещается, так как это приводит к поломке стиральных машин. Внимательно перед использованием машинки ознакомься с инструкцией в комнате. Сушить белье после стирки можно в специальной комнате, которая оборудована сушилками для одежды.

*Помни*, что другие студенты в общежитии тоже хотят постирать свою одежду, поэтому возвращай ключ вахтеру или коменданту сразу после стирки, именно в то время, когда пообещал его вернуть.
"""

NO_CERIFICATION_TEXT = """
    ЕСЛИ НЕТ СЕРТИФИКАТА ПРИВИВОК ИЛИ ФЛЮОРОГРАФИИ
    
1 *Если у вас отсутствует свежая флюорография*
Вы можете сделать ее в нескольких местах, например:
- В КДЦ БФУ за 320 руб. по карте студента (она должна быть в
наличии). Расположение КДЦ: [https://goo.gl/maps/P4djCkwJ3ZQHThgGA]
(https://goo.gl/maps/P4djCkwJ3ZQHThgGA)
- в Медэксперте (ул. Космическая или московский пр-т), до 17:00, за
450 руб. без снимка. Расположение:
[https://goo.gl/maps/rRiC1Nh35BNPw2w3A](https://goo.gl/maps/rRiC1Nh35B
NPw2w3A)
- Novomed (Гагарина 2В) до 17:00, 350 руб.
Расположение:
[https://goo.gl/maps/kgEkj4yLnWBNbFUm6](https://goo.gl/maps/kgEkj4yLnW
BNbFUm6)

2 *Если у вас отсутствуют сертификаты о прививках*

Обратитесь в любое отделение Медэксперта. Там вам необходимо
сдать анализ крови, который называется “Напряженность к иммунитету
для кори и дифтерии”. Анализ можно сдать каждый день, понедельник
- пятница с 7:30 до 19, выходные с 7:30 до 17:00.

Анализ сдается натощак.

Результат выдается через 4 рабочих дня (результат можно получить в
личном кабинете).
    """