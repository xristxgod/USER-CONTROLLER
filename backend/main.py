from fastapi import FastAPI
from tortoise import Tortoise

from src import main_router
from config import Config


app = FastAPI(
    title="User worker",
    version="1.0.0"
)

app.include_router(main_router)


@app.on_event("startup")
async def startup():
    await Tortoise.init(db_url=Config.DATABASE_URI, modules={'models': ['src.models']})
    await Tortoise.generate_schemas()


@app.on_event("shutdown")
async def shutdown():
    await Tortoise.close_connections()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app")
