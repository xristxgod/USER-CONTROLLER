from datetime import datetime

from tortoise import fields
from tortoise.models import Model


class UserModel(Model):
    user_id = fields.CharField(max_length=12, pk=True, unique=True)
    name = fields.CharField(max_length=50)
    surname = fields.CharField(max_length=50)
    patronymic = fields.CharField(max_length=50, default=None, null=True)
    phone_number = fields.CharField(max_length=11, unique=True)
    email = fields.CharField(max_length=255, unique=True, default=None, null=True)
    country = fields.CharField(max_length=50)
    date_modified = fields.DatetimeField(default=datetime.now())
    date_created = fields.DatetimeField(default=datetime.now())

    class Meta:
        table = "user_model"

    def __str__(self):
        return f"{self.surname} {self.name}"


__all__ = [
    "UserModel"
]
