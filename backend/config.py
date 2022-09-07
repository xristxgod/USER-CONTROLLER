import os
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(
    format=u"[%(asctime)s][%(filename)s][LINE:%(lineno)d][%(levelname)s] | %(message)s",
    level=logging.INFO
)


class Config:
    DATABASE_URI = os.getenv("DATABASE_URI", "postgres://postgres:postgrespw@localhost:49153")
    APPS_MODELS = [
        "src.models",
        "aerich.models"
    ]
