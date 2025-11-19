import uvicorn

from fastapi import FastAPI
from src.core_bot_api.view_economy import router as economy_router
from src.core_bot_api.view_auth import router as auth_router

app = FastAPI()
app.include_router(economy_router)
app.include_router(auth_router)


@app.get("/")
async def home_page() -> dict[str, str]:
    return {"message": "Server started"}


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
