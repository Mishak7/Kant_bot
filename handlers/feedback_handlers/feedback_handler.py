from aiogram import Bot, Router, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from handlers.main_handlers.languages import TEXTS

router = Router()

class FeedbackStates(StatesGroup):
    waiting_for_feedback = State()


@router.callback_query(F.data == "feedback")
async def ask_for_feedback(callback: CallbackQuery, state: FSMContext, language: str):
    try:
        await state.set_state(FeedbackStates.waiting_for_feedback)

        await callback.message.edit_text(
            text=TEXTS[language]['handlers']['feedback_handler']['prompt'],
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[[
                    InlineKeyboardButton(
                        text=f"◀️ {TEXTS[language]['keyboards']['main_keyboard']['back']}",
                        callback_data="back_to_main"
                    )
                ]]
            )
        )
        await callback.answer()

    except Exception as e:
        await callback.message.edit_text(
            f"❌ {TEXTS[language]['errors']['info_error']}",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[[
                    InlineKeyboardButton(
                        text=f"◀️ {TEXTS[language]['keyboards']['main_keyboard']['back']}",
                        callback_data="back_to_main"  # ← ИСПРАВЛЕНО здесь тоже
                    )
                ]]
            )
        )
        await callback.answer()


@router.message(FeedbackStates.waiting_for_feedback)
async def forward_feedback_to_you(message: Message, bot: Bot, state: FSMContext, language: str):
    try:
        await state.clear()

        user_info = (
            f"👤 От: {message.from_user.full_name}\n"
            f"🆔 ID: {message.from_user.id}\n"
            f"📧 @{message.from_user.username}\n"
        )

        await bot.send_message(chat_id=243032257, text=user_info)

        await bot.forward_message(
            chat_id=243032257,
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )

        await message.answer(
            text=TEXTS[language]['handlers']['feedback_handler']['thanks_general'],
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[[
                    InlineKeyboardButton(
                        text=f"◀️ {TEXTS[language]['keyboards']['main_keyboard']['back']}",
                        callback_data="back_to_main"
                    )
                ]]
            )
        )

    except Exception as e:
        await message.answer(
            f"❌ {TEXTS[language]['errors']['info_error']}",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[[
                    InlineKeyboardButton(
                        text=f"◀️ {TEXTS[language]['keyboards']['main_keyboard']['back']}",
                        callback_data="back_to_main"
                    )
                ]]
            )
        )