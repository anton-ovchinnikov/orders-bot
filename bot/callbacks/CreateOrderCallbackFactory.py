from enum import Enum

from aiogram.filters.callback_data import CallbackData


class CreateOrderAction(str, Enum):
    select_category = 'select_category'
    confirm_order = 'confirm_order'


class CreateOrderCallbackFactory(CallbackData, prefix='create_order'):
    action: CreateOrderAction
