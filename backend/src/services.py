from typing import Optional
from datetime import datetime

from tortoise.exceptions import IncompleteInstanceError

from .models import UserModel
from .schemas import BodyUser, ResponseGetUser, ResponseSuccessfully
from config import logger


class ServiceUserCRUD:
    @staticmethod
    async def create(body: BodyUser) -> ResponseSuccessfully:
        if UserModel.filter(phone_number=body.phone_number).exists():
            return await ServiceUserCRUD.update(body.phone_number, body=body)
        try:
            user = UserModel(**body.dict())
            await user.save()
            status = True
        except IncompleteInstanceError as ex:
            logger.error(f"{ex}")
            status = False
        return ResponseSuccessfully(successfully=status)

    @staticmethod
    async def get(phone_number: str) -> Optional[ResponseGetUser]:
        return await UserModel.filter(phone_number=phone_number).first()

    @staticmethod
    async def update(phone_number: str, *, body: BodyUser) -> ResponseSuccessfully:
        try:
            await UserModel.filter(phone_number=phone_number).update(
                **body.dict(),
                date_modified=datetime.now()
            )
            status = True
        except Exception as ex:
            logger.error(f"{ex}")
            status = False
        return ResponseSuccessfully(successfully=status)

    @staticmethod
    async def delete(phone_number: str) -> Optional[ResponseSuccessfully]:
        if UserModel.filter(phone_number=phone_number).exists():
            return None
        try:
            await UserModel.filter(phone_number=phone_number).delete()
            status = True
        except Exception as ex:
            logger.error(f"{ex}")
            status = False
        return ResponseSuccessfully(successfully=status)


__all__ = [
    "ServiceUserCRUD"
]
