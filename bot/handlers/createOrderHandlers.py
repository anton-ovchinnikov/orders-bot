from aiogram import Router, F, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.callbacks.CreateOrderCallbackFactory import CreateOrderCallbackFactory, CreateOrderAction
from bot.database.Database import Database
from bot.keyboards.createOrderKeyboards import get_categories_keyboard, get_confirm_order_keyboard
from bot.keyboards.menuKeyboard import get_cancel_keyboard
from bot.labels.messages import SELECT_CATEGORY_MSG, WRITE_TASKS_MSG, WRITE_PRICE_MSG, WRITE_DEADLINE_MSG, \
    CONFIRM_ORDER_MSG, CONFIRMED_ORDER_MSG, NO_USERNAME_ALERT, NEW_ORDER_MSG
from bot.states.OrderStates import OrderStates
from configreader import config

router = Router()


@router.callback_query(StateFilter(None),
                       CreateOrderCallbackFactory.filter(F.action == CreateOrderAction.select_category))
async def create_order_handler(query: CallbackQuery, state: FSMContext):
    if query.from_user.username:
        await state.set_state(OrderStates.select_category)
        await query.message.edit_text(text=SELECT_CATEGORY_MSG, reply_markup=get_categories_keyboard())
    else:
        await query.answer(text=NO_USERNAME_ALERT, show_alert=True)


@router.callback_query(OrderStates.select_category)
async def select_category_handler(query: CallbackQuery, state: FSMContext):
    category = query.data
    await state.update_data({'category': category})

    await state.update_data({'message_to_edit': query.message.message_id})
    await state.set_state(OrderStates.write_tasks)
    await query.message.edit_text(text=WRITE_TASKS_MSG.format(category=category), reply_markup=get_cancel_keyboard())


@router.message(OrderStates.write_tasks)
async def write_tasks_handler(message: Message, state: FSMContext, bot: Bot):
    tasks = message.text
    await state.update_data({'tasks': tasks})

    await message.delete()
    sdata = await state.get_data()
    await state.set_state(OrderStates.write_price)
    await bot.edit_message_text(text=WRITE_PRICE_MSG.format(category=sdata['category']), chat_id=message.chat.id,
                                message_id=sdata['message_to_edit'], reply_markup=get_cancel_keyboard())


@router.message(OrderStates.write_price)
async def write_price_handler(message: Message, state: FSMContext, bot: Bot):
    price = message.text
    await state.update_data({'price': price})

    await message.delete()
    sdata = await state.get_data()
    await state.set_state(OrderStates.write_deadline)
    await bot.edit_message_text(text=WRITE_DEADLINE_MSG.format(category=sdata['category'], price=sdata['price']),
                                chat_id=message.chat.id, message_id=sdata['message_to_edit'],
                                reply_markup=get_cancel_keyboard())


@router.message(OrderStates.write_deadline)
async def write_deadline_handler(message: Message, state: FSMContext, bot: Bot):
    deadline = message.text
    await state.update_data({'deadline': deadline})

    await message.delete()
    sdata = await state.get_data()
    await state.set_state(OrderStates.confirm_order)
    await bot.edit_message_text(text=CONFIRM_ORDER_MSG.format(
        category=sdata['category'],
        tasks=sdata['tasks'],
        price=sdata['price'],
        deadline=sdata['deadline'],
    ),
        chat_id=message.chat.id, message_id=sdata['message_to_edit'],
        reply_markup=get_confirm_order_keyboard())


@router.callback_query(OrderStates.confirm_order,
                       CreateOrderCallbackFactory.filter(F.action == CreateOrderAction.confirm_order))
async def confirm_order_handler(query: CallbackQuery, state: FSMContext, database: Database, bot: Bot):
    chat_id = query.from_user.id
    username = query.from_user.username
    sdata = await state.get_data()

    await database.create_order(user=chat_id,
                                category=sdata['category'],
                                tasks=sdata['tasks'],
                                price=sdata['price'],
                                deadline=sdata['deadline'],
                                contact=username)

    await state.clear()
    await query.message.edit_text(text=CONFIRMED_ORDER_MSG)
    await bot.send_message(chat_id=config.admin_id, text=NEW_ORDER_MSG)
