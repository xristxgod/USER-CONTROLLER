import re
from typing import Optional

from pydantic import BaseModel, Field, EmailStr, constr, validator


class BodyUser(BaseModel):
    name: constr(max_length=50) = Field(description="Имя пользователя")
    surname: constr(max_length=50) = Field(description="Фамилия пользователя")
    patronymic: Optional[constr(max_length=50)] = Field(description="Отчество пользователя")
    phone_number: constr(min_length=11, max_length=11) = Field(description="Телефонный номер")
    email: Optional[EmailStr] = Field(description="Email")
    country: constr(max_length=50) = Field(description="Старана")

    @validator("name", "surname", "patronymic", "country")
    def valid_fio(cls, value: Optional[str] = None):
        if value is None:
            return None
        if not bool(re.fullmatch(r'(?i)[а-яё ]+', value)):
            raise ValueError("Only Cyrillic is allowed for the string!")
        return value.title()

    @validator("phone_number")
    def valid_phone_number(cls, number: str):
        if not number.isdigit():
            raise ValueError("The number must consist of integers. Example: 79281304521")
        if number[0] != "7":
            raise ValueError("The number must start with 7. Example: 79281304521")
        return number

    class Config:
        schema_extra = {
            "example": {
                "name": "Иван",
                "surname": "Иванов",
                "patronymic": "Иванович",
                "phone_number": "79281304521",
                "email": "ivanov@mail.ru",
                "country": "Россия"
            }
        }


class BodyNumber(BaseModel):
    phoneNumber: constr(min_length=11, max_length=11) = Field(description="Телефонный номер", alias="phone_number")

    @validator("phoneNumber")
    def valid_phone_number(cls, number: str):
        if not number.isdigit():
            raise ValueError("The number must consist of integers. Example: 79281304521")
        if number[0] != "7":
            raise ValueError("The number must start with 7. Example: 79281304521")
        return number

    class Config:
        schema_extra = {
            "example": {
                "phone_number": "79281304521"
            }
        }


class ResponseUser(BaseModel):
    name: constr(max_length=50) = Field(description="Имя пользователя")
    surname: constr(max_length=50) = Field(description="Фамилия пользователя")
    patronymic: Optional[constr(max_length=50)] = Field(description="Отчество пользователя", default=None)
    phone_number: constr(min_length=11, max_length=11) = Field(description="Телефонный номер")
    email: Optional[EmailStr] = Field(description="Email", default=None)
    country: constr(max_length=50) = Field(description="Старана")
    country_code: int = Field(description="Код страны")

    class Config:
        schema_extra = {
            "example": {
                "name": "Иван",
                "surname": "Иванов",
                "patronymic": "Иванович",
                "phone_number": "79281304521",
                "email": "ivanov@mail.ru",
                "country": "Россия",
                "country_code": 12
            }
        }


class ResponseSuccessfully(BaseModel):
    successfully: bool = Field(description="Статус", default=True)

    class Config:
        schema_extra = {
            "example": {
                "successfully": True
            }
        }


__all__ = [
    "BodyUser", "BodyNumber",
    "ResponseUser", "ResponseSuccessfully"
]
