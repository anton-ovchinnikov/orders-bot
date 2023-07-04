from datetime import datetime
from typing import NoReturn, List

from sqlalchemy import select, update
from sqlalchemy.dialects.sqlite import insert

from bot.database.models import User, Referral, Order


# noinspection PyTypeChecker
class Database:
    def __init__(self, session):
        self.session = session

    async def create_user(self, chat_id: int, username: str) -> NoReturn:
        values = {'chat_id': chat_id, 'username': username, 'registered_at': datetime.now()}

        stmt = insert(User).values(**values).on_conflict_do_nothing()
        await self.session.execute(stmt)
        await self.session.commit()

    async def read_user(self, chat_id: int) -> User | None:
        stmt = select(User).where(User.chat_id == chat_id)
        user = await self.session.execute(stmt)
        return user.scalar_one_or_none()

    async def create_referral(self, chat_id: int, referer: int) -> NoReturn:
        values = {'chat_id': chat_id, 'referer': referer}

        stmt = insert(Referral).values(**values).on_conflict_do_nothing()
        await self.session.execute(stmt)
        await self.session.commit()

    async def read_referral(self, chat_id: int) -> Referral | None:
        stmt = select(Referral).where(Referral.chat_id == chat_id)
        referral = await self.session.execute(stmt)
        return referral.scalar_one_or_none()

    async def create_order(
            self, user: int, category: str, tasks: str, price: str, deadline: str, contact: str
    ) -> NoReturn:
        status = 'new'
        values = {'user': user,
                  'category': category,
                  'tasks': tasks,
                  'price': price,
                  'deadline': deadline,
                  'contact': contact,
                  'status': status}

        stmt = insert(Order).values(**values).on_conflict_do_nothing()
        await self.session.execute(stmt)
        await self.session.commit()

    async def read_order(self, order_id: int) -> Order | None:
        stmt = select(Order).where(Order.id == order_id)
        order = await self.session.execute(stmt)
        return order.scalar_one_or_none()

    async def update_order(self, order_id, **kwargs) -> NoReturn:
        stmt = update(Order).where(Order.id == order_id).values(**kwargs)
        await self.session.execute(stmt)
        await self.session.commit()

    async def read_new_orders(self) -> List[Order]:
        status = 'new'
        stmt = select(Order).where(Order.status == status)
        orders = await self.session.execute(stmt)
        return orders.scalars().all()
