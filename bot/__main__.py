import asyncio
import logging

from aiogram import Bot, Dispatcher
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from bot.database.Database import Database
from bot.database.base import Base
from bot.handlers import menuHandlers, createOrderHandlers, adminHandlers, adminMenuHandlers
from bot.middlewares.DatabaseMiddleware import DatabaseMiddleware
from configreader import config


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=config.bot_token, parse_mode='html')
    dp = Dispatcher()

    engine = create_async_engine(f"sqlite+aiosqlite:///database.sqlite", future=True, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    session = async_sessionmaker(engine, expire_on_commit=True).begin().async_session
    database = Database(session=session)

    dp.include_router(router=menuHandlers.router)
    dp.include_router(router=createOrderHandlers.router)
    dp.include_router(router=adminHandlers.router)
    dp.include_router(router=adminMenuHandlers.router)

    dp.message.middleware(DatabaseMiddleware(database=database))
    dp.callback_query.middleware(DatabaseMiddleware(database=database))

    await bot.delete_webhook(drop_pending_updates=True)

    try:
        await dp.start_polling(bot)
    finally:
        await session.close()
        await engine.dispose()


asyncio.run(main())
