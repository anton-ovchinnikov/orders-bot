from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.callbacks.AdminCallbackFactory import AdminCallbackFactory, AdminAction, OrderAdminAction
from bot.labels.buttons import ORDERS_ADMIN_BTN, PREV_ORDER_ADMIN_BTN, NEXT_ORDER_ADMIN_BTN, READ_ORDER_ADMIN_BTN, \
    CANCEL_BTN


def get_admin_keyboard() -> InlineKeyboardMarkup:
    orders_cb = AdminCallbackFactory(action=AdminAction.show_orders).pack()
    keyboard = [
        [InlineKeyboardButton(text=ORDERS_ADMIN_BTN, callback_data=orders_cb)]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup


def get_admin_show_orders_keyboard(next_order: int, orders_count: int) -> InlineKeyboardMarkup:
    read_order_cb = AdminCallbackFactory(action=OrderAdminAction.read_order).pack()
    next_order_cb = AdminCallbackFactory(action=OrderAdminAction.next_order).pack()
    prev_order_cb = AdminCallbackFactory(action=OrderAdminAction.prev_order).pack()
    keyboard = []
    if 1 < next_order < orders_count:
        keyboard.append([InlineKeyboardButton(text=PREV_ORDER_ADMIN_BTN, callback_data=prev_order_cb),
                         InlineKeyboardButton(text=NEXT_ORDER_ADMIN_BTN, callback_data=next_order_cb)])
    elif next_order == 1 and next_order == orders_count:
        pass
    elif next_order >= orders_count:
        keyboard.append([InlineKeyboardButton(text=PREV_ORDER_ADMIN_BTN, callback_data=prev_order_cb)])
    elif next_order <= 1:
        keyboard.append([InlineKeyboardButton(text=NEXT_ORDER_ADMIN_BTN, callback_data=next_order_cb)])
    keyboard.append([InlineKeyboardButton(text=READ_ORDER_ADMIN_BTN, callback_data=read_order_cb)])
    keyboard.append([InlineKeyboardButton(text=CANCEL_BTN, callback_data='cancel')])
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup
