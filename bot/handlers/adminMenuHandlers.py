from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.callbacks.AdminCallbackFactory import AdminCallbackFactory, AdminAction, OrderAdminAction
from bot.database.Database import Database
from bot.filters.IsAdmin import IsAdmin
from bot.keyboards.adminKeyboards import get_admin_show_orders_keyboard, get_admin_keyboard
from bot.labels.messages import SHOW_ORDERS_MSG, NO_ORDERS_ALERT, READ_ALERT, ADMIN_MSG

router = Router()


@router.callback_query(IsAdmin(), AdminCallbackFactory.filter(F.action == AdminAction.show_orders))
async def show_orders_handler(query: CallbackQuery, database: Database, state: FSMContext):
    new_orders = await database.read_new_orders()
    if new_orders:
        await state.update_data({'new_orders': new_orders, 'current_order': new_orders[0]})

        order = new_orders[0]
        await query.message.edit_text(text=SHOW_ORDERS_MSG.format(
            order_id=order.id,
            user_id=order.user,
            category=order.category,
            tasks=order.tasks,
            price=order.price,
            deadline=order.deadline,
            contact=order.contact
        ), reply_markup=get_admin_show_orders_keyboard(next_order=1, orders_count=len(new_orders)))
    else:
        await query.answer(NO_ORDERS_ALERT, show_alert=True)


@router.callback_query(IsAdmin(), AdminCallbackFactory.filter(F.action == OrderAdminAction.next_order))
async def next_order_handler(query: CallbackQuery, state: FSMContext):
    sdata = await state.get_data()
    new_orders = sdata['new_orders']

    current_order_index = new_orders.index(sdata['current_order'])
    next_order = new_orders[current_order_index + 1]
    await state.update_data({'current_order': next_order})
    await query.message.edit_text(text=SHOW_ORDERS_MSG.format(
        order_id=next_order.id,
        user_id=next_order.user,
        category=next_order.category,
        tasks=next_order.tasks,
        price=next_order.price,
        deadline=next_order.deadline,
        contact=next_order.contact
    ), reply_markup=get_admin_show_orders_keyboard(next_order=current_order_index + 2, orders_count=len(new_orders)))


@router.callback_query(IsAdmin(), AdminCallbackFactory.filter(F.action == OrderAdminAction.prev_order))
async def prev_order_handler(query: CallbackQuery, state: FSMContext):
    sdata = await state.get_data()
    new_orders = sdata['new_orders']

    current_order_index = new_orders.index(sdata['current_order'])
    prev_order = new_orders[current_order_index - 1]
    await state.update_data({'current_order': prev_order})
    await query.message.edit_text(text=SHOW_ORDERS_MSG.format(
        order_id=prev_order.id,
        user_id=prev_order.user,
        category=prev_order.category,
        tasks=prev_order.tasks,
        price=prev_order.price,
        deadline=prev_order.deadline,
        contact=prev_order.contact
    ), reply_markup=get_admin_show_orders_keyboard(next_order=current_order_index - 2, orders_count=len(new_orders)))


@router.callback_query(IsAdmin(), AdminCallbackFactory.filter(F.action == OrderAdminAction.read_order))
async def read_order_handler(query: CallbackQuery, state: FSMContext, database: Database):
    sdata = await state.get_data()

    current_order = sdata['current_order']
    await database.update_order(order_id=current_order.id, status='read')

    await state.clear()
    await query.message.edit_text(text=ADMIN_MSG, reply_markup=get_admin_keyboard())
    await query.answer(READ_ALERT)
