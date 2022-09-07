from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src import main_router
from config import Config


app = FastAPI(
    title="User worker",
    version="1.0.0"
)

app.include_router(main_router)


register_tortoise(
    app,
    db_url=Config.DATABASE_URI,
    modules={"models": Config.APPS_MODELS},
    generate_schemas=True,
    add_exception_handlers=True,
)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app")
