# Module shows the pictures of dormitory buildings and corresponding info/address
# Handler for each button - may not be optimal

from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.exceptions import TelegramBadRequest
from config.logger import logger
from handlers.main_handlers.languages import TEXTS
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()


@router.callback_query(F.data == "dormitory_1")
async def dormitory_1_handler(callback: CallbackQuery, language: str):
    try:
        logger.info(f"User {callback.from_user.id} requested dormitory 1 photo")
        photo = FSInputFile('handlers/location_handlers/dormitory_pictures/dormitory_1.JPG')
        caption = TEXTS[language]['handlers']['dormitory_location_handlers'] + ' 1'

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text=f"📌️ {TEXTS[language]['keyboards']['dormitory_keyboard']['details']}", url="https://kantiana.ru/students/kampus/obshchezhitiya/obshchezhitie-1/")],
                [InlineKeyboardButton(text="📍 2GIS", url="https://go.2gis.com/abgd0/")],
                [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory_address")]
            ])
        )
        logger.info(f"Photo for dormitory 1 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for dormitory 1: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    except FileNotFoundError as e:
        logger.error(f"File not found for dormitory 1: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    except Exception as e:
        logger.error(f"Unexpected error in dormitory_1_handler: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    finally:
        await callback.answer()


@router.callback_query(F.data == "dormitory_2")
async def dormitory_2_handler(callback: CallbackQuery, language: str):
    try:
        logger.info(f"User {callback.from_user.id} requested dormitory 2 photo")
        photo = FSInputFile('handlers/location_handlers/dormitory_pictures/dormitory_2.JPG')
        caption = TEXTS[language]['handlers']['dormitory_location_handlers'] + ' 2'

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text=f"📌️ {TEXTS[language]['keyboards']['dormitory_keyboard']['details']}", url="https://kantiana.ru/students/kampus/obshchezhitiya/obshchezhitie-2/")],
                [InlineKeyboardButton(text="📍 2GIS", url="https://go.2gis.com/4MzCv")],
                [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory_address")]
            ])
        )
        logger.info(f"Photo for dormitory 2 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for dormitory 2: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    except FileNotFoundError as e:
        logger.error(f"File not found for dormitory 2: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    except Exception as e:
        logger.error(f"Unexpected error in dormitory_2_handler: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    finally:
        await callback.answer()


@router.callback_query(F.data == "dormitory_3")
async def dormitory_3_handler(callback: CallbackQuery, language: str):
    try:
        logger.info(f"User {callback.from_user.id} requested dormitory 3 photo")
        photo = FSInputFile('handlers/location_handlers/dormitory_pictures/dormitory_3.JPG')
        caption = TEXTS[language]['handlers']['dormitory_location_handlers'] + ' 3'

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text=f"📌️ {TEXTS[language]['keyboards']['dormitory_keyboard']['details']}",
                                      url="https://kantiana.ru/students/kampus/obshchezhitiya/obshchezhitie-3/")],
                [InlineKeyboardButton(text="📍 2GIS", url="https://go.2gis.com/jZ2vc")],
                [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory_address")]
            ])
        )
        logger.info(f"Photo for dormitory 3 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for dormitory 3: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    except FileNotFoundError as e:
        logger.error(f"File not found for dormitory 3: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    except Exception as e:
        logger.error(f"Unexpected error in dormitory_3_handler: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    finally:
        await callback.answer()


@router.callback_query(F.data == "dormitory_4")
async def dormitory_4_handler(callback: CallbackQuery, language: str):
    try:
        logger.info(f"User {callback.from_user.id} requested dormitory 4 photo")
        photo = FSInputFile('handlers/location_handlers/dormitory_pictures/dormitory_4.jpg')
        caption = TEXTS[language]['handlers']['dormitory_location_handlers'] + ' 4'

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text=f"📌️ {TEXTS[language]['keyboards']['dormitory_keyboard']['details']}",
                                      url="https://kantiana.ru/students/kampus/obshchezhitiya/obshchezhitie-4/")],
                [InlineKeyboardButton(text="📍 2GIS", url="https://go.2gis.com/D5pwn")],
                [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory_address")]
            ])
        )
        logger.info(f"Photo for dormitory 4 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for dormitory 4: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    except FileNotFoundError as e:
        logger.error(f"File not found for dormitory 4: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    except Exception as e:
        logger.error(f"Unexpected error in dormitory_4_handler: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    finally:
        await callback.answer()


@router.callback_query(F.data == "dormitory_5")
async def dormitory_5_handler(callback: CallbackQuery, language: str):
    try:
        logger.info(f"User {callback.from_user.id} requested dormitory 5 photo")
        photo = FSInputFile('handlers/location_handlers/dormitory_pictures/dormitory_5.jpg')
        caption = TEXTS[language]['handlers']['dormitory_location_handlers'] + ' 5'

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text=f"📌️ {TEXTS[language]['keyboards']['dormitory_keyboard']['details']}",
                                      url="https://kantiana.ru/students/kampus/obshchezhitiya/obshchezhitie-5/")],
                [InlineKeyboardButton(text="📍 2GIS", url="https://go.2gis.com/Z7ALI")],
                [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory_address")]
            ])
        )
        logger.info(f"Photo for dormitory 5 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for dormitory 5: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    except FileNotFoundError as e:
        logger.error(f"File not found for dormitory 5: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    except Exception as e:
        logger.error(f"Unexpected error in dormitory_5_handler: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    finally:
        await callback.answer()


@router.callback_query(F.data == "dormitory_6")
async def dormitory_6_handler(callback: CallbackQuery, language: str):
    try:
        logger.info(f"User {callback.from_user.id} requested dormitory 6 photo")
        photo = FSInputFile('handlers/location_handlers/dormitory_pictures/dormitory_6.jpg')
        caption = TEXTS[language]['handlers']['dormitory_location_handlers'] + ' 6'

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text=f"📌️ {TEXTS[language]['keyboards']['dormitory_keyboard']['details']}",
                                      url="https://kantiana.ru/students/kampus/obshchezhitiya/obshchezhitie-6/")],
                [InlineKeyboardButton(text="📍 2GIS", url="https://go.2gis.com/00ye5")],
                [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory_address")]
            ])
        )
        logger.info(f"Photo for dormitory 6 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for dormitory 6: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    except FileNotFoundError as e:
        logger.error(f"File not found for dormitory 6: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    except Exception as e:
        logger.error(f"Unexpected error in dormitory_6_handler: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    finally:
        await callback.answer()


@router.callback_query(F.data == "dormitory_7")
async def dormitory_7_handler(callback: CallbackQuery, language: str):
    try:
        logger.info(f"User {callback.from_user.id} requested dormitory 7 photo")
        photo = FSInputFile('handlers/location_handlers/dormitory_pictures/dormitory_7.jpg')
        caption = TEXTS[language]['handlers']['dormitory_location_handlers'] + ' 7'

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text=f"📌️ {TEXTS[language]['keyboards']['dormitory_keyboard']['details']}",
                                      url="https://kantiana.ru/students/kampus/obshchezhitiya/obshchezhitie-7/")],
                [InlineKeyboardButton(text="📍 2GIS", url="https://go.2gis.com/L6vPS")],
                [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory_address")]
            ])
        )
        logger.info(f"Photo for dormitory 7 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for dormitory 7: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    except FileNotFoundError as e:
        logger.error(f"File not found for dormitory 7: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    except Exception as e:
        logger.error(f"Unexpected error in dormitory_7_handler: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    finally:
        await callback.answer()


@router.callback_query(F.data == "dormitory_8")
async def dormitory_8_handler(callback: CallbackQuery, language: str):
    try:
        logger.info(f"User {callback.from_user.id} requested dormitory 8 photo")
        photo = FSInputFile('handlers/location_handlers/dormitory_pictures/dormitory_8.jpg')
        caption = TEXTS[language]['handlers']['dormitory_location_handlers'] + ' 8'

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text=f"📌️ {TEXTS[language]['keyboards']['dormitory_keyboard']['details']}",
                                      url="https://kantiana.ru/students/kampus/obshchezhitiya/obshchezhitie-8/")],
                [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['dormitory_keyboard']['back']}",
                                      callback_data="dormitory_check-in")]

            ])
        )
        logger.info(f"Photo for dormitory 8 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for dormitory 8: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    except FileNotFoundError as e:
        logger.error(f"File not found for dormitory 8: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    except Exception as e:
        logger.error(f"Unexpected error in dormitory_8_handler: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    finally:
        await callback.answer()


@router.callback_query(F.data == "dormitory_9")
async def dormitory_9_handler(callback: CallbackQuery, language: str):
    try:
        logger.info(f"User {callback.from_user.id} requested dormitory 9 photo")
        photo = FSInputFile('handlers/location_handlers/dormitory_pictures/dormitory_9.jpg')
        caption = TEXTS[language]['handlers']['dormitory_location_handlers'] + ' 9-13'

        await callback.message.delete()
        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text=f"📌️ {TEXTS[language]['keyboards']['dormitory_keyboard']['details']}",
                                      url="https://kantiana.ru/students/kampus/obshchezhitiya/obshchezhitie-9-13/")],
                [InlineKeyboardButton(text="📍 2GIS", url="https://go.2gis.com/O83CE")],
                [InlineKeyboardButton(text=f"◀️ {TEXTS[language]['keyboards']['dormitory_keyboard']['back']}", callback_data="dormitory_address")]
            ])
        )
        logger.info(f"Photo for dormitory 9 sent to user {callback.from_user.id}")
    except TelegramBadRequest as e:
        logger.error(f"Telegram error for dormitory 9: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    except FileNotFoundError as e:
        logger.error(f"File not found for dormitory 9: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    except Exception as e:
        logger.error(f"Unexpected error in dormitory_9_handler: {e}")
        await callback.message.answer(TEXTS[language]['errors']['photo_error'])
    finally:
        await callback.answer()