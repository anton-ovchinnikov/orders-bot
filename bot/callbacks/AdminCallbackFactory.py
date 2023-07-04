from enum import Enum

from aiogram.filters.callback_data import CallbackData


class AdminAction(str, Enum):
    show_orders = 'show_orders'


class OrderAdminAction(str, Enum):
    read_order = 'read_order'
    next_order = 'next_order'
    prev_order = 'prev_order'


class AdminCallbackFactory(CallbackData, prefix='admin'):
    action: AdminAction | OrderAdminAction
