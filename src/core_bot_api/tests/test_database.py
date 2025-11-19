import pytest

from sqlalchemy import text


@pytest.mark.asyncio
async def test_can_async_engine_connect(async_engine):
    async with async_engine.connect() as conn:
        result_of_simple_request_to_db = await conn.execute(text("SELECT 1"))
        assert result_of_simple_request_to_db.scalar() == 1


@pytest.mark.asyncio
async def test_session_can_be_created(async_session):
    assert async_session is not None


@pytest.mark.asyncio
async def test_session_can_use_commit_method(async_session):
    await async_session.commit()


@pytest.mark.asyncio
async def test_session_context_manager_is_valid(async_session):
    async with async_session:
        ...
