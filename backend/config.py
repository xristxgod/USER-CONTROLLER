import os


class Config:
    MONGODB_URL = os.getenv("MONGODB_URL")
    MONGODB_NAME = os.getenv("MONGODB_NAME")
    MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION")
