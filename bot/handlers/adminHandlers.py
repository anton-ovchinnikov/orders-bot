from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.filters.IsAdmin import IsAdmin
from bot.keyboards.adminKeyboards import get_admin_keyboard
from bot.labels.messages import ADMIN_MSG

router = Router()


@router.message(IsAdmin(), Command('admin'))
async def admin_cmd_handler(message: Message):
    await message.answer(text=ADMIN_MSG, reply_markup=get_admin_keyboard())
    await message.delete()
