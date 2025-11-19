from .validation_models import UserCreate
from .database import get_db_session
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .sqlalchemy_models import User

from fastapi import (
    APIRouter,
    Depends, HTTPException,
)


router = APIRouter(
    prefix="/user_auth",
    tags=[
        "user_auth",
        "user",
    ],
)


@router.post("/register/")
async def register_user(user_data: UserCreate, db_session: AsyncSession  = Depends(get_db_session)):
    is_user_in_db_query = select(User).filter(User.vk_id == user_data.vk_id)
    is_user_in_db = await db_session.execute(is_user_in_db_query)
    is_user_in_db = is_user_in_db.scalar_one_or_none()

    if is_user_in_db:
        raise HTTPException(
            status_code=400,
            detail="User with this VK ID already exists"
        )

    new_user = User(
        vk_id = user_data.vk_id,
        username = user_data.username,
    )

    db_session.add(new_user)
    await db_session.commit()
    await db_session.refresh(new_user)

    return {"message": "User registered successfully!"}
