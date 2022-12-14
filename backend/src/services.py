from typing import Optional, Dict
from datetime import datetime

import aiohttp
from tortoise.exceptions import IncompleteInstanceError

from .models import UserModel, storage
from .schemas import BodyUser, ResponseSuccessfully
from config import Config, logger


class ExternalDaData:
    URL = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/country"

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(ExternalDaData, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.cache = storage

    async def __external(self, country: str) -> Dict:
        async with aiohttp.ClientSession(headers={"Authorization": Config.TOKEN_DADATA}) as session:
            async with session.post(self.URL, json={"query": country}) as response:
                return await response.json()

    async def get_code(self, country: str) -> int:
        result: Optional[Dict] = await self.cache.get(country)
        if result is None:
            data = await self.__external(country)
            if len(data["suggestions"]) == 0:
                return 0
            await self.cache.insert(country=country, data=data["suggestions"][0]["data"])
            result = await self.cache.get(country)
        return result.get("code")


class ServiceUserCRUD:
    @staticmethod
    async def create(body: BodyUser) -> ResponseSuccessfully:
        if await UserModel.filter(phone_number=body.phone_number).exists():
            return await ServiceUserCRUD.update(body.phone_number, body=body)
        try:
            user = UserModel(**body.dict())
            await user.save()
            status = True
        except IncompleteInstanceError as e:
            logger.error(f"{e}")
            status = False
        return ResponseSuccessfully(successfully=status)

    @staticmethod
    async def get(phone_number: str) -> Optional[UserModel]:
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
        if not await UserModel.filter(phone_number=phone_number).exists():
            return None
        try:
            await UserModel.filter(phone_number=phone_number).delete()
            status = True
        except Exception as ex:
            logger.error(f"{ex}")
            status = False
        return ResponseSuccessfully(successfully=status)


external = ExternalDaData()


__all__ = [
    "ServiceUserCRUD", "ExternalDaData", "external"
]
