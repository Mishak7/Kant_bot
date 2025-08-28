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
from handlers.main_handlers.languages import TEXTS

router = Router()


@router.callback_query(F.data == "loc_uni_building")
async def addresses_handler(callback: CallbackQuery):
    """
    Provides choice of buttons for each university building
    """
    try:
        text = TEXTS['ru']['handlers']['location_handlers']['addresses_handler']
        await callback.message.delete()
        await callback.message.answer(text,
                                        reply_markup=uni_loc_keyboard())
        await callback.answer()
    except Exception as e:
        logger.error(f'Dormitory choice info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS['ru']['errors']['info_error']}")


@router.callback_query(F.data == "loc_1")
async def loc_1_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 1 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_1.jpg')
        caption = TEXTS['ru']['handlers']['location_handlers']['loc_1_handler']
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
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 1: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_1_handler: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_2")
async def loc_2_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 2 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_2.jpg')
        caption = TEXTS['ru']['handlers']['location_handlers']['loc_2_handler']

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
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 2: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_2_handler: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_3")
async def loc_3_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 3 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_3.jpg')
        caption = TEXTS['ru']['handlers']['location_handlers']['loc_3_handler']

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
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 3: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_3_handler: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_4")
async def loc_4_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 4 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_4.jpg')
        caption = TEXTS['ru']['handlers']['location_handlers']['loc_4_handler']

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
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 4: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_4_handler: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_5")
async def loc_5_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 5 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_5.jpg')
        caption = TEXTS['ru']['handlers']['location_handlers']['loc_5_handler']

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
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 5: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_5_handler: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_6")
async def loc_6_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 6 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_6.jpg')
        caption = TEXTS['ru']['handlers']['location_handlers']['loc_6_handler']

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
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 6: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_6_handler: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_7")
async def loc_7_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 7 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_7.jpg')
        caption = TEXTS['ru']['handlers']['location_handlers']['loc_7_handler']
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
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 7: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_7_handler: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_8")
async def loc_8_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 8 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_8.jpg')
        caption = TEXTS['ru']['handlers']['location_handlers']['loc_8_handler']
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
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 8: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_8_handler: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_9")
async def loc_9_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 9 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_9.jpg')
        caption = TEXTS['ru']['handlers']['location_handlers']['loc_9_handler']
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
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 9: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_9_handler: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_10")
async def loc_10_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 10 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_10.jpg')
        caption = TEXTS['ru']['handlers']['location_handlers']['loc_10_handler']
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
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 10: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_10_handler: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_12")
async def loc_12_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 12 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_12.jpg')
        caption = TEXTS['ru']['handlers']['location_handlers']['loc_12_handler']
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
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 12: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_12_handler: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_22")
async def loc_22_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 22 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_22.jpg')
        caption = TEXTS['ru']['handlers']['location_handlers']['loc_22_handler']
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
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 22: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_22_handler: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_24")
async def loc_24_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 24 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_24.jpg')
        caption = TEXTS['ru']['handlers']['location_handlers']['loc_24_handler']
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
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 24: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_24_handler: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_27")
async def loc_27_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 27 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_27.jpg')
        caption = TEXTS['ru']['handlers']['location_handlers']['loc_27_handler']
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
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 27: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_27_handler: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_28")
async def loc_28_handler(callback: CallbackQuery):
    try:
        logger.info(f"User {callback.from_user.id} requested location 28 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_28.jpg')
        caption = TEXTS['ru']['handlers']['location_handlers']['loc_28_handler']
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
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 28: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_28_handler: {e}")
        await callback.message.answer(f"{TEXTS['ru']['errors']['photo_error']}")
    finally:
        await callback.answer()