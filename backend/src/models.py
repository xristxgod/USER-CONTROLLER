import uuid
from typing import Optional, Dict
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
        self.client = pymongo.MongoClient(Config.CACHE_DATABASE_URI)
        self.db = self.client.get_database(Config.CACHE_DATABASE_NAME)
        self.collection = self.db.get_collection(Config.CACHE_DATABASE_COLLECTION)

    async def get(self, country: str) -> Optional[Dict]:
        result = self.collection.find_one({"country": country})
        if result is not None:
            return result["data"]

    async def insert(self, country: str, data: Dict) -> Optional:
        self.collection.insert_one({"country": country, "data": data})


storage = StorageDB()


__all__ = [
    "UserModel", "StorageDB", "storage"
]


