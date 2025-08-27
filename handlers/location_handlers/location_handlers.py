"""
Module for searching info on university buildings
Handler for each building - may not be optimal
"""

from aiogram import Router, F
from handlers.location_handlers.location_keyboard import back_to_locations_keyboard
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.exceptions import TelegramBadRequest
from config.logger import logger
from handlers.location_handlers.location_keyboard import uni_loc_keyboard
import traceback

router = Router()


@router.callback_query(F.data == "loc_uni_building")
async def addresses_handler(callback: CallbackQuery):
    """
    Provides choice of buttons for each university building
    """
    try:
        text = 'Выбери корпус'
        await callback.message.delete()
        await callback.message.answer(text,
                                        reply_markup=uni_loc_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'Dormitory choice info error: {e}\n{traceback.format_exc()}')
        await callback.answer("Ошибка при загрузке информации про корпуса")


@router.callback_query(F.data == "loc_1")
async def loc_1_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 1 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_1.jpg')
        caption = """
        *Административный корпус, ул. А.Невского, 14*
        
Здесь находятся:
· Делопроизводство (каб. 115)
· Служба бухгалтерского учета (каб. 212)
· Архив (каб. 221)
· Группа расчетов по доходам и налоговому учету (каб.222)
· Касса (второй этаж)
· Зал Аквариум
· Зал Максимум
· Столовая (первый этаж)

*Локация*: https://goo.gl/maps/zRT7KcqxLXtAVaUE7"""
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_locations_keyboard()
        )
        logger.info(f"Photo for location 1 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 1: {e}")
        await callback.message.answer("Фото места №1 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 1: {e}")
        await callback.message.answer("Фото места №1 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in loc_1_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_2")
async def loc_2_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 2 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_2.jpg')
        caption = """
        *Корпус №2, Институт физики, математики и информационных технологий («Физмат»), ул. А.Невского, 14*

Здесь находятся:
· Отдел по работе с иностранными обучающимися (каб. 119)
· Сектор визово-миграционной поддержки (каб. 114)
· Приемная комиссия (каб. 116 и 117)
· Библиотека, кабинет 202 («Читальный зал»)
· Служба обслуживания IT-инфраструктуры (каб. 121)

*Локация*: https://goo.gl/maps/6yt18jT8DoS5KgQv5"""

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_locations_keyboard()
        )
        logger.info(f"Photo for location 2 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 2: {e}")
        await callback.message.answer("Фото места №2 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 2: {e}")
        await callback.message.answer("Фото места №2 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in loc_2_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_3")
async def loc_3_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 3 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_3.jpg')
        caption = """
        *Корпус №3, ул. Университетская, 2*
        
Здесь находятся:
· Институт живых систем
· Главная университетская библиотека: научный абонемент (каб. 126), читальный зал (каб. 115)

*Локация*: https://goo.gl/maps/y2XnUi5vj5MxbRPeA"""

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_locations_keyboard()
        )
        logger.info(f"Photo for location 3 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 3: {e}")
        await callback.message.answer("Фото места №3 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 3: {e}")
        await callback.message.answer("Фото места №3 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in loc_3_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_4")
async def loc_4_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 4 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_4.jpg')
        caption = """
        *Корпус №4, ул. Чернышевского, 56 («Корпус с часами»)*
        
Здесь находятся:
· Институт гуманитарных наук
· Центр русского языка (каб. 01)
· Музей советского детства

*Локация*: https://goo.gl/maps/EBrY5H86euoPi6Sn9"""

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_locations_keyboard()
        )
        logger.info(f"Photo for location 4 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 4: {e}")
        await callback.message.answer("Фото места №4 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 4: {e}")
        await callback.message.answer("Фото места №4 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in loc_4_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_5")
async def loc_5_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 5 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_5.jpg')
        caption = """
        *Корпус №5, ул. Чернышевского, 56а*
        
Здесь находится:
· Институт образования

*Локация*: https://goo.gl/maps/xgHnL2PJ7ASXTFGG6"""

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_locations_keyboard()
        )
        logger.info(f"Photo for location 5 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 5: {e}")
        await callback.message.answer("Фото места №5 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 5: {e}")
        await callback.message.answer("Фото места №5 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in loc_5_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_6")
async def loc_6_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 6 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_6.jpg')
        caption = """
        *Корпус №6, ул. А. Невского, 14б («Шайба»)*
        
Здесь находятся:
·Комплекс студенческих общежитий (каб. 101)
·Управление внеучебной деятельности
*Локация *: https: // maps.app.goo.gl / pKu1EREgTPvJ6VGN7
"""

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_locations_keyboard()
        )
        logger.info(f"Photo for location 6 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 6: {e}")
        await callback.message.answer("Фото места №6 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 6: {e}")
        await callback.message.answer("Фото места №6 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in loc_6_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_7")
async def loc_7_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 7 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_7.jpg')
        caption = """
        *Корпус №7, ул. Фрунзе, 6*
        
Здесь находятся:
·Учебная телестудия
· Юридический институт

*Локация*: https://goo.gl/maps/39LxmNSyZdSjnme16
"""
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_locations_keyboard()
        )
        logger.info(f"Photo for location 7 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 7: {e}")
        await callback.message.answer("Фото места №7 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 7: {e}")
        await callback.message.answer("Фото места №7 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in loc_7_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_8")
async def loc_8_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 8 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_8.jpg')
        caption = """
        *Корпус №8, ул. 9 Апреля, 5*
        
Здесь находится:
· Медицинская библиотека

*Локация*: https://goo.gl/maps/Tja71g7t1QPRqtbt7
"""
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_locations_keyboard()
        )
        logger.info(f"Photo for location 8 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 8: {e}")
        await callback.message.answer("Фото места №8 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 8: {e}")
        await callback.message.answer("Фото места №8 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in loc_8_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_9")
async def loc_9_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 9 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_9.jpg')
        caption = """
        *Корпус №9, ул. А.Невского,14 («ФОК»)*
        
Здесь находится:
Физкультурно-оздоровительный комплекс

*Локация*: https://g.page/kantiana-sport?share
"""
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_locations_keyboard()
        )
        logger.info(f"Photo for location 9 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 9: {e}")
        await callback.message.answer("Фото места №9 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 9: {e}")
        await callback.message.answer("Фото места №9 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in loc_9_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_10")
async def loc_10_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 10 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_10.jpg')
        caption = """
        *Корпус №10, ул. А. Невского. 14 («Свечка»)*
        
Здесь находятся:
· Центр социально-экономической поддержки студентов (каб. 14)
· Центр карьеры

*Локация*: https://goo.gl/maps/djfHWwTNer12z7caA
"""
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_locations_keyboard()
        )
        logger.info(f"Photo for location 10 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 10: {e}")
        await callback.message.answer("Фото места №10 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 10: {e}")
        await callback.message.answer("Фото места №10 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in loc_10_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_12")
async def loc_12_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 12 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_12.jpg')
        caption = """
        *Корпус №12, ул.Боткина, 4-6*
        
Здесь находится:
· Медицинский институт

*Локация*: https://goo.gl/maps/BKJMV9WAR9G6PpaJ6
"""
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_locations_keyboard()
        )
        logger.info(f"Photo for location 12 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 12: {e}")
        await callback.message.answer("Фото места №12 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 12: {e}")
        await callback.message.answer("Фото места №12 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in loc_12_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_22")
async def loc_22_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 22 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_22.jpg')
        caption = """
        *Корпус №22, ул. А.Невского,14*
        
Здесь находится:
Учебно-физкультурный комплекс с бассейном

*Локация*: https://goo.gl/maps/VevnRkQyv8FmZPXcA
"""
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_locations_keyboard()
        )
        logger.info(f"Photo for location 22 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 22: {e}")
        await callback.message.answer("Фото места №22 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 22: {e}")
        await callback.message.answer("Фото места №22 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in loc_22_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_24")
async def loc_24_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 24 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_24.jpg')
        caption = """
        *Корпус №24, ул. Зоологическая, 2*
        
Здесь находятся:
· Университетский колледж

*Локация*: https://goo.gl/maps/Fb76GxbTCQUm3zEa7
"""
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_locations_keyboard()
        )
        logger.info(f"Photo for location 24 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 24: {e}")
        await callback.message.answer("Фото места №24 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 24: {e}")
        await callback.message.answer("Фото места №24 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in loc_24_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_27")
async def loc_27_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 27 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_27.jpg')
        caption = """
        *Корпус №27, ул. Генерала-лейтенанта Озерова, 57*
        
Здесь находятся:
· Инженерно-технический институт
· Арена «Кантиана»

*Локация*: https://goo.gl/maps/H126DeMnucPJvA1U9
"""
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_locations_keyboard()
        )
        logger.info(f"Photo for location 27 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 27: {e}")
        await callback.message.answer("Фото места №27 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 27: {e}")
        await callback.message.answer("Фото места №27 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in loc_27_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_28")
async def loc_28_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 28 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_28.jpg')
        caption = """*Корпус №28, ул. Горького, 23*
        
Здесь находятся:
· Институт экономики и менеджмента

*Локация*: https://goo.gl/maps/THR3WG17cF2EBtvW6
"""
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=back_to_locations_keyboard()
        )
        logger.info(f"Photo for location 28 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 28: {e}")
        await callback.message.answer("Фото места №28 временно недоступно")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 28: {e}")
        await callback.message.answer("Фото места №28 не найдено")
    except Exception as e:
        logger.error(f"Unexpected error in loc_28_handler: {e}")
        await callback.message.answer("Произошла ошибка при загрузке фото")
    finally:
        await callback.answer()