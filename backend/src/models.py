import uuid
from typing import Dict, Optional
from datetime import datetime

import pymongo
from tortoise import fields
from tortoise.models import Model

from config import Config


class UserModel(Model):
    user_id = fields.CharField(max_length=12, pk=True, unique=True, default=uuid.uuid1().hex[:12])
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


class StorageDB:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(StorageDB, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.__client = pymongo.MongoClient(Config.CACHE_DATABASE_URI)
        self.__db = self.__client.get_database(Config.CACHE_DATABASE_NAME)
        self.__collection = self.__db.get_collection(Config.CACHE_DATABASE_COLLECTION)

    @property
    def collection(self):
        return self.__collection

    def __setitem__(self, key: str, data: Dict):
        self.collection.insert_one({"country": key, "data": data})

    def __getitem__(self, key: str) -> Optional[Dict]:
        return self.collection.find({}, {"country": key})[0]


__all__ = [
    "UserModel", "StorageDB"
]


