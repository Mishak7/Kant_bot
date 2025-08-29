"""
Module for university info handling
"""

from aiogram import Router, F
from aiogram.types import CallbackQuery
from handlers.university_handlers.university_info_keyboard import back_to_info_keyboard
from handlers.main_handlers.languages import TEXTS
from handlers.main_handlers.commands import get_user_language

router = Router()
language = get_user_language(callback.from_user.id)

@router.callback_query(F.data == "schedule")
async def schedule_handler(callback: CallbackQuery):
    await callback.message.edit_text(SCHEDULE_TEXT, parse_mode="Markdown", reply_markup=back_to_info_keyboard())
    await callback.answer()


@router.callback_query(F.data == "scholarship")
async def scholarship_handler(callback: CallbackQuery):
    await callback.message.edit_text(SCHOLARSHIP_TEXT, parse_mode="Markdown", reply_markup=back_to_info_keyboard())
    await callback.answer()


@router.callback_query(F.data == "office_contacts")
async def office_contacts_handler(callback: CallbackQuery):
    await callback.message.edit_text(OFFICE_CONTACTS_TEXT, parse_mode='Markdown', reply_markup=back_to_info_keyboard())
    await callback.answer()


@router.callback_query(F.data == "visa_center")
async def visa_center_handler(callback: CallbackQuery):
    await callback.message.edit_text(VISA_CENTER_TEXT, parse_mode='Markdown', reply_markup=back_to_info_keyboard())
    await callback.answer()


SCHEDULE_TEXT = TEXTS[language]['handlers']['university_info_handlers']['schedule_text']
SCHOLARSHIP_TEXT = TEXTS[language]['handlers']['university_info_handlers']['scholarship_text']
OFFICE_CONTACTS_TEXT = TEXTS[language]['handlers']['university_info_handlers']['office_contacts_text']
VISA_CENTER_TEXT = TEXTS[language]['handlers']['university_info_handlers']['visa_center_text']
