from fastapi import APIRouter
from tortoise import Tortoise

from .endpoints import router


main_router = APIRouter()


main_router.include_router(router)


async def init_db():
    # Here we connect to a SQLite DB file.
    # also specify the app name of "models"
    # which contain models from "app.models"
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['src.models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


__all__ = [
    "main_router", "init_db"
]
