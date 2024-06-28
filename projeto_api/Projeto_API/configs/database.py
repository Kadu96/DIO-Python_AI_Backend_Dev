from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from Projeto_API.configs.settings import settings


engine = create_async_engine(settings.DB_URL, echo=False)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)  # type: ignore


async def get_session() -> AsyncGenerator:
    async with async_session() as session:  # type: ignore
        yield session
