from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.callbacks.CreateOrderCallbackFactory import CreateOrderCallbackFactory, CreateOrderAction
from bot.labels.buttons import CREATE_ORDER_BTN, CANCEL_BTN


def get_menu_keyboard() -> InlineKeyboardMarkup:
    create_order_cb = CreateOrderCallbackFactory(action=CreateOrderAction.select_category).pack()
    keyboard = [
        [InlineKeyboardButton(text=CREATE_ORDER_BTN, callback_data=create_order_cb)],
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup


def get_cancel_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text=CANCEL_BTN, callback_data='cancel')]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup
