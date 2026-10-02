import asyncio
import os
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from Databaze.models import Base
from sqlalchemy import create_engine
DATABASE_URL = "postgresql+asyncpg://postgres:123321@localhost:5432/databaze"

engine = create_async_engine(
    DATABASE_URL, echo=False, pool_size=10, max_overflow=20
)

session_maker = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)