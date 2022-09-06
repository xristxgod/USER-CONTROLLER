import os
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(
    format=u"[%(asctime)s][%(filename)s][LINE:%(lineno)d][%(levelname)s] | %(message)s",
    level=logging.INFO
)


class Config:
    MONGODB_URL = os.getenv("MONGODB_URL")
    MONGODB_NAME = os.getenv("MONGODB_NAME")
    MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION")
