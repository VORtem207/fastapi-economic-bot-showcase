import pytest_asyncio


from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)


TEST_DATABASE_URL = "postgresql+asyncpg://testuser:testpassword@localhost:5434/testdb"


@pytest_asyncio.fixture(scope="session")
async def async_engine():
    engine = create_async_engine(
        url=TEST_DATABASE_URL,
        echo=False,
    )
    yield engine
    await engine.dispose()


@pytest_asyncio.fixture(scope="function")
async def async_session(async_engine):
    async_session = async_sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with async_session() as session:
        yield session
        await session.rollback()
