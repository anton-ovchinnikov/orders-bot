from aiogram.fsm.state import StatesGroup, State


class OrderStates(StatesGroup):
    select_category = State()
    write_tasks = State()
    write_price = State()
    write_deadline = State()
    confirm_order = State()
