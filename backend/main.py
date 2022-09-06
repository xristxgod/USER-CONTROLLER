from fastapi import FastAPI

from src import main_router, init_db


app = FastAPI(
    title="User worker",
    version="1.0.0"
)

app.include_router(main_router)


@app.on_event("startup")
async def startup():
    await init_db()


if __name__ == '__main__':
    pass
