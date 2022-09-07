import os
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(
    format=u"[%(asctime)s][%(filename)s][LINE:%(lineno)d][%(levelname)s] | %(message)s",
    level=logging.INFO
)


class Config:
    TOKEN_DADATA = "Token " + os.getenv("TOKEN_DADATA", "41ff19aab5552979a6637edc0740f299dcca6de6")
    DATABASE_URI = os.getenv("DATABASE_URI", "postgres://postgres:postgrespw@localhost:49153")
    APPS_MODELS = [
        "src.models",
        "aerich.models"
    ]

    CACHE_DATABASE_URI = os.getenv("CACHE_DATABASE_URI", "mongodb://docker:mongopw@localhost:49154")
    CACHE_DATABASE_NAME = os.getenv("CACHE_DATABASE_NAME", "dev_cache")
    CACHE_DATABASE_COLLECTION = os.getenv("CACHE_DATABASE_COLLECTION", "dev_collection")
