from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import URL
from settings import settings

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
)


database_url = URL.create(
    drivername="postgresql+asyncpg",
    username=settings.db_username,
    password=settings.db_password,
    host=settings.db_host,
    port=settings.db_port,
    database=settings.db_name,
)

async_engine = create_async_engine(
    url=database_url,
    echo=True,
)

async_session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class BaseSQLAlchemyModel(DeclarativeBase):
    ...


async def get_db_session():
    async with async_session() as session:
        yield session
