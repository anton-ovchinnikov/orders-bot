from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.database.Database import Database
from bot.keyboards.menuKeyboard import get_menu_keyboard
from bot.labels.messages import START_MSG, CANCEL_ALERT

router = Router()


@router.message(CommandStart())
async def start_cmd_handler(message: Message, database: Database):
    chat_id = message.chat.id
    username = message.from_user.username
    await database.create_user(chat_id=chat_id, username=username)
    await message.answer(text=START_MSG, reply_markup=get_menu_keyboard())
    await message.delete()


@router.callback_query(F.data == 'cancel')
async def cancel_handler(query: CallbackQuery, state: FSMContext):
    await state.clear()
    await query.message.edit_text(text=START_MSG, reply_markup=get_menu_keyboard())
    await query.answer(CANCEL_ALERT)
