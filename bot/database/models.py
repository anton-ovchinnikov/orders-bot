from sqlalchemy import Column, Integer, BigInteger, Text, DateTime, ForeignKey

from bot.database.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    chat_id = Column(BigInteger, nullable=False, unique=True)
    username = Column(Text, nullable=True, unique=True)
    registered_at = Column(DateTime, nullable=False)


class Referral(Base):
    __tablename__ = 'referrals'

    id = Column(Integer, primary_key=True)
    chat_id = Column(BigInteger, ForeignKey('users.id'), nullable=False, unique=False)
    referer = Column(BigInteger, ForeignKey('users.id'), nullable=False, unique=False)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('users.id'), nullable=False, unique=False)
    category = Column(Text, nullable=False, unique=False)
    tasks = Column(Text, nullable=False, unique=False)
    price = Column(Text, nullable=False, unique=False)
    deadline = Column(Text, nullable=False, unique=False)
    contact = Column(Integer, ForeignKey('users.username'), nullable=False, unique=False)
    status = Column(Text, nullable=True, unique=False)
