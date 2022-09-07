from fastapi import APIRouter, HTTPException, status

from .schemas import BodyUser, BodyNumber, ResponseSuccessfully, ResponseUser
from .services import ServiceUserCRUD, external


router = APIRouter(
    tags=["USER"]
)


@router.post(
    "/save_user_data",
    response_model=ResponseSuccessfully
)
async def save_user(body: BodyUser):
    return await ServiceUserCRUD.create(body=body)


@router.post(
    "/get_user_data",
    response_model=ResponseUser
)
async def get_user(body: BodyNumber):
    result = await ServiceUserCRUD.get(phone_number=body.phoneNumber)
    if result is None:
        raise HTTPException(detail="User with given phone number not found!", status_code=status.HTTP_404_NOT_FOUND)
    return ResponseUser(
        name=result.name,
        surname=result.surname,
        patronymic=result.patronymic,
        phone_number=result.phone_number,
        email=result.email,
        country=result.country,
        country_code=await external.get_code(result.country)
    )


@router.post(
    "/delete_user_data",
    response_model=ResponseSuccessfully
)
async def delete_user(body: BodyNumber):
    result = await ServiceUserCRUD.delete(phone_number=body.phoneNumber)
    if result is None:
        raise HTTPException(detail="User with given phone number not found!", status_code=status.HTTP_404_NOT_FOUND)
    return result


__all__ = [
    "router"
]
