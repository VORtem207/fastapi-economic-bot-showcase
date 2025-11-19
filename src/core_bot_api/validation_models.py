from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    vk_id: int

