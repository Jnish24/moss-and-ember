from typing import Any
from fastapi import FastAPI
from config import settings
from routes import test

app = FastAPI()
app.include_router(test.router)


@app.get("/")
async def func() -> dict[str, Any]:
    return {"message": settings.db_host}
