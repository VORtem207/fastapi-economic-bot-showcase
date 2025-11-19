from .database import BaseSQLAlchemyModel

from datetime import datetime

from typing import (
    Optional,
)

from sqlalchemy import (
    String,
    BigInteger,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)


class User(BaseSQLAlchemyModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
    )
    vk_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=True,
    )
    username: Mapped[str] = mapped_column(
        String(100),
        nullable=True,
    )
    created_at: Mapped[Optional[datetime]] = mapped_column(default=datetime.now)
    balance: Mapped[int] = mapped_column(
        BigInteger,
        default=1000,
    )


    def __repr__(self):
        return (
            f"Username: {self.username} | "
            f"User ID: {self.id} |"
        )
