"""
Module for university info handling
"""

from aiogram import Router, F
from aiogram.types import CallbackQuery
from handlers.university_handlers.university_info_keyboard import back_to_info_keyboard

router = Router()

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


SCHEDULE_TEXT = '''
    *Расписание занятий*:
    https://schedule.kantiana.ru/
    '''
SCHOLARSHIP_TEXT ='''
    *Информация о стипендиях и материальной помощи*:
    https://kantiana.ru/students/scholarship/
    '''
OFFICE_CONTACTS_TEXT = '''
    *Контакты*:

    _Адрес_: 236041, Калининград, ул. Александра Невского, 14
    _Контактный телефон_: +7 (4012) 59-55-95
    _Приемная комиссия_: ул. Александра Невского, 14

    8 (800) 600-52-39 звонок бесплатный
    +7 (4012) 59-55-96

    _Канцелярия_: +7 (4012) 59-55-97

    _E-mail_: post@kantiana.ru

    *Время работы административных служб*

    Понедельник: 9:00 — 18:00    _перерыв_: 13:00—13:45

    Вторник: 9:00 — 18:00        _перерыв_: 13:00—13:45

    Среда: неприемный день (работа с документами)

    Четверг: 9:00 — 18:00        _перерыв_: 13:00—13:45

    Пятница: 9:00 — 16:45        _перерыв_: 13:00—13:45

    Суббота и воскресенье: выходные дни
    '''

VISA_CENTER_TEXT = '''
    *Визово-миграционный центр*:
    https://kantiana.ru/universitys/administration/mezhdunarodnyy-ofis/

    *Контакты*

    _Адрес_: 236041, Россия, Калининград, ул. А. Невского 14, корпус 2, каб. 119
    _Часы_ _работы_: Понедельник — четверг с 9:00 до 18:00, пятница до с 9:00 до 16:45
    _Телефон_: +7 (4012) 31-33-99
    _Email_: international-study@kantiana.ru
    '''