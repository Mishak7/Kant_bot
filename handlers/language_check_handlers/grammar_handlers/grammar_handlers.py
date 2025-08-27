from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from handlers.language_check_handlers.grammar_handlers.grammar_keyboard import translation_keyboard, back_to_translation
from services.grammar.grammar import gigachat_response

router = Router()
user_states = {}


@router.callback_query(F.data == "language_grammar")
async def language_grammar_handler(callback: CallbackQuery):
    text = '''
    *Выберите вариант перевода*:
    '''
    await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=translation_keyboard())
    await callback.answer()



@router.callback_query(F.data == "translate_to_russian")
async def translate_to_russian_handler(callback: CallbackQuery):
    user_states[callback.from_user.id] = {"to_russian": True}
    text = '''
    Переведите данный текст на русский язык:
    
    I want to tell you something interesting... 
    so these events began, well, they actually began with my practically birth, there were a lot of different prerequisites, but in particular, these events began with such a situation, which means that we once had a door that stood back in the Soviet Union, we once removed it, replaced it with metal, put it on on the balcony.. 
    An Azerbaijani friend called us, who saw it from below, saw that the door was standing, wanted to buy it, and called: "I'll buy a door from you," okay, okay, then after a while he basically, especially me, just, well, forgot about this door.. So then, one night, I had a hunch that I needed to perform a certain algorithm: 
    I lay down on the couch, raised my legs, lifted my legs on the table, put them on a chair and opened the window. I had such thoughts that I have, so to speak, an acquaintance, well, I know him, for example, as Evgeny Dmitrievich Metilan, but in particular I once saw him, well, there are such concepts as personality transformation..

    '''

    await callback.message.edit_text(text, parse_mode="Markdown")
    await callback.answer()


@router.callback_query(F.data == "translate_from_russian")
async def translate_from_russian_handler(callback: CallbackQuery):
    user_states[callback.from_user.id] = {"to_russian": False}
    text = '''
    Переведите данный текст с русского языка на свой:
    
Мои земные тленные мечты православного крестьянина ныне:

- Профессиональный топор мясника,
- Профессиональный пень для разделки туши быка, а лучше два пня, а лучше три. 
- Много много сухих дров
- Здоровье ближних
- Шикарная ручная пила, а лучше три
- Английские луки и стрелы к ним
- Православные невесты для сыновей 
- Никуда никогда не ездить
- Достроить деревянный забор
- Навес для лошадиной мельницы
- Построить умный дом 15-го века с печью по-черному и в нём дожить
- Чтоб Большая ремесленная выставка 29-30 августа прошла нормально
- Радоваться возрождению забытых ручных ремесел - то, чем занимаются сыновья. 

Но теперь у меня кроме этих суетных земных мечтаний есть одна главная и единственно-реальная мечта, о которой я, пока был безбожным дебилом, вообще не думал - попасть в рай. 

Поэтому теперь меня все дебилы держат за дебила. И это хорошо. 


Герман Стерлигов (русский крестьянин)
    '''

    await callback.message.edit_text(text, parse_mode="Markdown")
    await callback.answer()


@router.message(F.text)
async def translation_analysis_handler(message: Message):
    user_id = message.from_user.id
    to_russian = user_states[user_id]["to_russian"]
    translate_text = message.text

    translation_result = gigachat_response(translate_text, to_russian)
    await message.answer(translation_result, parse_mode="Markdown", reply_markup=back_to_translation())