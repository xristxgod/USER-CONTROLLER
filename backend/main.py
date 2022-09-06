from fastapi import FastAPI

from src import main_router


app = FastAPI(
    title="User worker",
    version="1.0.0"
)

app.include_router(main_router)


if __name__ == '__main__':
    pass
