"""
Module for searching info on university buildings
Handler for each building - may not be optimal
"""

from aiogram import Router, F
<<<<<<< HEAD
from handlers.location_handlers.location_keyboard import back_to_locations_keyboard
=======
from handlers.location_handlers.location_keyboard import loc_1_keyboard, loc_2_keyboard, loc_3_keyboard, loc_4_keyboard, loc_5_keyboard, loc_6_keyboard, loc_7_keyboard, loc_8_keyboard, loc_9_keyboard, loc_10_keyboard, loc_11_keyboard, loc_12_keyboard, loc_13_keyboard, loc_14_keyboard, loc_19_keyboard, loc_20_keyboard, loc_21_keyboard, loc_22_keyboard, loc_23_keyboard, loc_24_keyboard, loc_25_keyboard, loc_27_keyboard, loc_28_keyboard, loc_29_keyboard, loc_32_keyboard, loc_35_keyboard
>>>>>>> main
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.exceptions import TelegramBadRequest
from config.logger import logger
from handlers.location_handlers.location_keyboard import uni_loc_keyboard
import traceback
from handlers.main_handlers.languages import TEXTS
<<<<<<< HEAD
from handlers.main_handlers.commands import get_user_language

router = Router()
language = get_user_language(callback.from_user.id)

@router.callback_query(F.data == "loc_uni_building")
async def addresses_handler(callback: CallbackQuery):
=======

router = Router()


@router.callback_query(F.data == "loc_uni_building")
async def addresses_handler(callback: CallbackQuery, language: str):
>>>>>>> main
    """
    Provides choice of buttons for each university building
    """
    try:
        text = TEXTS[language]['handlers']['location_handlers']['addresses_handler']
        await callback.message.delete()
        await callback.message.answer(text,
<<<<<<< HEAD
                                        reply_markup=uni_loc_keyboard())
=======
                                        reply_markup=uni_loc_keyboard(language))
>>>>>>> main
        await callback.answer()
    except Exception as e:
        logger.error(f'Dormitory choice info error: {e}\n{traceback.format_exc()}')
        await callback.answer(f"{TEXTS[language]['errors']['info_error']}")


@router.callback_query(F.data == "loc_1")
<<<<<<< HEAD
async def loc_1_handler(callback: CallbackQuery):
=======
async def loc_1_handler(callback: CallbackQuery, language: str):
>>>>>>> main
    try:
        logger.info(f"User {callback.from_user.id} requested location 1 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_1.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_1_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
<<<<<<< HEAD
            reply_markup=back_to_locations_keyboard()
=======
            reply_markup=loc_1_keyboard(language)
>>>>>>> main
        )
        logger.info(f"Photo for location 1 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 1: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 1: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_1_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_2")
<<<<<<< HEAD
async def loc_2_handler(callback: CallbackQuery):
=======
async def loc_2_handler(callback: CallbackQuery, language: str):
>>>>>>> main
    try:
        logger.info(f"User {callback.from_user.id} requested location 2 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_2.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_2_handler']

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
<<<<<<< HEAD
            reply_markup=back_to_locations_keyboard()
=======
            reply_markup=loc_2_keyboard(language)
>>>>>>> main
        )
        logger.info(f"Photo for location 2 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 2: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 2: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_2_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_3")
<<<<<<< HEAD
async def loc_3_handler(callback: CallbackQuery):
=======
async def loc_3_handler(callback: CallbackQuery, language: str):
>>>>>>> main
    try:
        logger.info(f"User {callback.from_user.id} requested location 3 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_3.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_3_handler']

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
<<<<<<< HEAD
            reply_markup=back_to_locations_keyboard()
=======
            reply_markup=loc_3_keyboard(language)
>>>>>>> main
        )
        logger.info(f"Photo for location 3 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 3: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 3: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_3_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_4")
<<<<<<< HEAD
async def loc_4_handler(callback: CallbackQuery):
=======
async def loc_4_handler(callback: CallbackQuery, language: str):
>>>>>>> main
    try:
        logger.info(f"User {callback.from_user.id} requested location 4 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_4.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_4_handler']

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
<<<<<<< HEAD
            reply_markup=back_to_locations_keyboard()
=======
            reply_markup=loc_4_keyboard(language)
>>>>>>> main
        )
        logger.info(f"Photo for location 4 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 4: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 4: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_4_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_5")
<<<<<<< HEAD
async def loc_5_handler(callback: CallbackQuery):
=======
async def loc_5_handler(callback: CallbackQuery, language: str):
>>>>>>> main
    try:
        logger.info(f"User {callback.from_user.id} requested location 5 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_5.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_5_handler']

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
<<<<<<< HEAD
            reply_markup=back_to_locations_keyboard()
=======
            reply_markup=loc_5_keyboard(language)
>>>>>>> main
        )
        logger.info(f"Photo for location 5 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 5: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 5: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_5_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_6")
<<<<<<< HEAD
async def loc_6_handler(callback: CallbackQuery):
=======
async def loc_6_handler(callback: CallbackQuery, language: str):
>>>>>>> main
    try:
        logger.info(f"User {callback.from_user.id} requested location 6 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_6.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_6_handler']

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
<<<<<<< HEAD
            reply_markup=back_to_locations_keyboard()
=======
            reply_markup=loc_6_keyboard(language)
>>>>>>> main
        )
        logger.info(f"Photo for location 6 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 6: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 6: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_6_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_7")
<<<<<<< HEAD
async def loc_7_handler(callback: CallbackQuery):
=======
async def loc_7_handler(callback: CallbackQuery, language: str):
>>>>>>> main
    try:
        logger.info(f"User {callback.from_user.id} requested location 7 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_7.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_7_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
<<<<<<< HEAD
            reply_markup=back_to_locations_keyboard()
=======
            reply_markup=loc_7_keyboard(language)
>>>>>>> main
        )
        logger.info(f"Photo for location 7 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 7: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 7: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_7_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_8")
<<<<<<< HEAD
async def loc_8_handler(callback: CallbackQuery):
=======
async def loc_8_handler(callback: CallbackQuery, language: str):
>>>>>>> main
    try:
        logger.info(f"User {callback.from_user.id} requested location 8 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_8.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_8_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
<<<<<<< HEAD
            reply_markup=back_to_locations_keyboard()
=======
            reply_markup=loc_8_keyboard(language)
>>>>>>> main
        )
        logger.info(f"Photo for location 8 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 8: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 8: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_8_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_9")
<<<<<<< HEAD
async def loc_9_handler(callback: CallbackQuery):
=======
async def loc_9_handler(callback: CallbackQuery, language: str):
>>>>>>> main
    try:
        logger.info(f"User {callback.from_user.id} requested location 9 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_9.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_9_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
<<<<<<< HEAD
            reply_markup=back_to_locations_keyboard()
=======
            reply_markup=loc_9_keyboard(language)
>>>>>>> main
        )
        logger.info(f"Photo for location 9 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 9: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 9: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_9_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_10")
<<<<<<< HEAD
async def loc_10_handler(callback: CallbackQuery):
=======
async def loc_10_handler(callback: CallbackQuery, language: str):
>>>>>>> main
    try:
        logger.info(f"User {callback.from_user.id} requested location 10 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_10.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_10_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
<<<<<<< HEAD
            reply_markup=back_to_locations_keyboard()
=======
            reply_markup=loc_10_keyboard(language)
>>>>>>> main
        )
        logger.info(f"Photo for location 10 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 10: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 10: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_10_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


<<<<<<< HEAD
@router.callback_query(F.data == "loc_12")
async def loc_12_handler(callback: CallbackQuery):
=======
@router.callback_query(F.data == "loc_11")
async def loc_11_handler(callback: CallbackQuery, language: str):
    try:
        logger.info(f"User {callback.from_user.id} requested location 11 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_11.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_11_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=loc_11_keyboard(language)
        )
        logger.info(f"Photo for location 11 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 11: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 11: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_11_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_12")
async def loc_12_handler(callback: CallbackQuery, language: str):
>>>>>>> main
    try:
        logger.info(f"User {callback.from_user.id} requested location 12 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_12.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_12_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
<<<<<<< HEAD
            reply_markup=back_to_locations_keyboard()
=======
            reply_markup=loc_12_keyboard(language)
>>>>>>> main
        )
        logger.info(f"Photo for location 12 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 12: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 12: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_12_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


<<<<<<< HEAD
@router.callback_query(F.data == "loc_22")
async def loc_22_handler(callback: CallbackQuery):
=======
@router.callback_query(F.data == "loc_13")
async def loc_13_handler(callback: CallbackQuery, language: str):
    try:
        logger.info(f"User {callback.from_user.id} requested location 13 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_13.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_13_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=loc_13_keyboard(language)
        )
        logger.info(f"Photo for location 13 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 13: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 13: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_13_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_14")
async def loc_14_handler(callback: CallbackQuery, language: str):
    try:
        logger.info(f"User {callback.from_user.id} requested location 14 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_14.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_14_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=loc_14_keyboard(language)
        )
        logger.info(f"Photo for location 14 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 14: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 14: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_14_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_19")
async def loc_19_handler(callback: CallbackQuery, language: str):
    try:
        logger.info(f"User {callback.from_user.id} requested location 19 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_19.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_19_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=loc_19_keyboard(language)
        )
        logger.info(f"Photo for location 19 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 19 {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 19: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_19_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_20")
async def loc_20_handler(callback: CallbackQuery, language: str):
    try:
        logger.info(f"User {callback.from_user.id} requested location 20 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_20.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_20_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=loc_20_keyboard(language)
        )
        logger.info(f"Photo for location 20 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 20: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 20: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_20_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_21")
async def loc_21_handler(callback: CallbackQuery, language: str):
    try:
        logger.info(f"User {callback.from_user.id} requested location 21 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_21.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_21_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=loc_21_keyboard(language)
        )
        logger.info(f"Photo for location 21 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 21: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 21: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_21_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_22")
async def loc_22_handler(callback: CallbackQuery, language: str):
>>>>>>> main
    try:
        logger.info(f"User {callback.from_user.id} requested location 22 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_22.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_22_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
<<<<<<< HEAD
            reply_markup=back_to_locations_keyboard()
=======
            reply_markup=loc_22_keyboard(language)
>>>>>>> main
        )
        logger.info(f"Photo for location 22 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 22: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 22: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_22_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


<<<<<<< HEAD
@router.callback_query(F.data == "loc_24")
async def loc_24_handler(callback: CallbackQuery):
=======
@router.callback_query(F.data == "loc_23")
async def loc_23_handler(callback: CallbackQuery, language: str):
    try:
        logger.info(f"User {callback.from_user.id} requested location 23 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_23.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_23_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=loc_23_keyboard(language)
        )
        logger.info(f"Photo for location 22 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 23: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 23: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_23_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_24")
async def loc_24_handler(callback: CallbackQuery, language: str):
>>>>>>> main
    try:
        logger.info(f"User {callback.from_user.id} requested location 24 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_24.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_24_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
<<<<<<< HEAD
            reply_markup=back_to_locations_keyboard()
=======
            reply_markup=loc_24_keyboard(language)
>>>>>>> main
        )
        logger.info(f"Photo for location 24 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 24: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 24: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_24_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


<<<<<<< HEAD
@router.callback_query(F.data == "loc_27")
async def loc_27_handler(callback: CallbackQuery):
=======
@router.callback_query(F.data == "loc_25")
async def loc_25_handler(callback: CallbackQuery, language: str):
    try:
        logger.info(f"User {callback.from_user.id} requested location 25 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_25.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_25_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=loc_25_keyboard(language)
        )
        logger.info(f"Photo for location 25 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 25: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 25: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_25_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_27")
async def loc_27_handler(callback: CallbackQuery, language: str):
>>>>>>> main
    try:
        logger.info(f"User {callback.from_user.id} requested location 27 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_27.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_27_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
<<<<<<< HEAD
            reply_markup=back_to_locations_keyboard()
=======
            reply_markup=loc_27_keyboard(language)
>>>>>>> main
        )
        logger.info(f"Photo for location 27 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 27: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 27: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_27_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_28")
<<<<<<< HEAD
async def loc_28_handler(callback: CallbackQuery):
=======
async def loc_28_handler(callback: CallbackQuery, language: str):
>>>>>>> main
    try:
        logger.info(f"User {callback.from_user.id} requested location 28 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_28.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_28_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
<<<<<<< HEAD
            reply_markup=back_to_locations_keyboard()
=======
            reply_markup=loc_28_keyboard(language)
>>>>>>> main
        )
        logger.info(f"Photo for location 28 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 28: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 28: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_28_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()
<<<<<<< HEAD
=======


@router.callback_query(F.data == "loc_29")
async def loc_29_handler(callback: CallbackQuery, language: str):
    try:
        logger.info(f"User {callback.from_user.id} requested location 29 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_29.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_29_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=loc_29_keyboard(language)
        )
        logger.info(f"Photo for location 29 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 29: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 29: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_29_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_32")
async def loc_32_handler(callback: CallbackQuery, language: str):
    try:
        logger.info(f"User {callback.from_user.id} requested location 32 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_32.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_32_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=loc_32_keyboard(language)
        )
        logger.info(f"Photo for location 32 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 32: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 32: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_32_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()


@router.callback_query(F.data == "loc_35")
async def loc_35_handler(callback: CallbackQuery, language: str):
    try:
        logger.info(f"User {callback.from_user.id} requested location 35 photo")
        photo = FSInputFile('handlers/location_handlers/location_pictures/loc_35.jpg')
        caption = TEXTS[language]['handlers']['location_handlers']['loc_35_handler']
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            parse_mode="Markdown",
            reply_markup=loc_35_keyboard(language)
        )
        logger.info(f"Photo for location 35 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for location 35: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except FileNotFoundError as e:
        logger.error(f"File not found for location 35: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    except Exception as e:
        logger.error(f"Unexpected error in loc_35_handler: {e}")
        await callback.message.answer(f"{TEXTS[language]['errors']['photo_error']}")
    finally:
        await callback.answer()
>>>>>>> main
