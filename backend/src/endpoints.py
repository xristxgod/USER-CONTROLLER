from fastapi import APIRouter


router = APIRouter(
    tags=["USER"]
)


@router.post("/save_user_data")
async def save_user():
    pass


@router.post("/get_user_data")
async def get_user():
    pass


@router.post("/delete_user_data")
async def delete_user():
    pass


__all__ = [
    "router"
]
