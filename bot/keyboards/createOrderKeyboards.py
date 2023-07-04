from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.callbacks.CreateOrderCallbackFactory import CreateOrderAction, CreateOrderCallbackFactory
from bot.labels.buttons import SITE_CATEGORY_BTN, BOT_CATEGORY_BTN, SCRIPT_CATEGORY_BTN, OTHER_CATEGORY_BTN, \
    CANCEL_BTN, CONFIRM_ORDER_BTN


def get_categories_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text=SITE_CATEGORY_BTN, callback_data=SITE_CATEGORY_BTN)],
        [InlineKeyboardButton(text=BOT_CATEGORY_BTN, callback_data=BOT_CATEGORY_BTN)],
        [InlineKeyboardButton(text=SCRIPT_CATEGORY_BTN, callback_data=SCRIPT_CATEGORY_BTN)],
        [InlineKeyboardButton(text=OTHER_CATEGORY_BTN, callback_data=OTHER_CATEGORY_BTN)],
        [InlineKeyboardButton(text=CANCEL_BTN, callback_data='cancel')]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup


def get_confirm_order_keyboard() -> InlineKeyboardMarkup:
    confirm_order_cb = CreateOrderCallbackFactory(action=CreateOrderAction.confirm_order).pack()
    keyboard = [
        [InlineKeyboardButton(text=CONFIRM_ORDER_BTN, callback_data=confirm_order_cb)],
        [InlineKeyboardButton(text=CANCEL_BTN, callback_data='cancel')]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup
