from fastapi import APIRouter
from tortoise import Tortoise

from .endpoints import router
from config import Config


main_router = APIRouter()


main_router.include_router(router)


async def init_db():
    await Tortoise.init(
        db_url=Config.DATABASE_URI,
        modules={'models': ['src.models']}
    )
    await Tortoise.generate_schemas()


__all__ = [
    "main_router", "init_db"
]
