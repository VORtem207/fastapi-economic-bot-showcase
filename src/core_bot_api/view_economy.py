from fastapi import APIRouter


router = APIRouter(
    prefix="/economy",
    tags=["economy"],
)


@router.get("/russian_roulette/{user_bet}")
async def russian_roulette(user_bet: int):
    return {"message": "You win!"}
