import unittest
from unittest.mock import Mock, patch
from typing import Optional, Dict

from src.models import StorageDB
from src.services import ServiceUserCRUD, external


TEST_DATA = {
    "value": "Россия",
    "unrestricted_value": "Российская Федерация",
    "data": {
        "code": "643",
        "alfa2": "RU",
        "alfa3": "RUS",
        "name_short": "Россия",
        "name": "Российская Федерация"
    }
}


class TestCacheDB:
    def __init__(self):
        self.cache = {}

    async def get(self, country: str) -> Optional[Dict]:
        return self.cache.get(country)

    async def insert(self, country: str, data: Dict) -> Optional:
        self.cache[country] = data


class TestExternal(unittest.IsolatedAsyncioTestCase):
    @patch("src.services.external.cache")
    @patch("src.services.external.__external")
    async def test_get_code(self, cache: Mock, _external: Mock):
        cache.return_value = TestCacheDB()
        _external.return_value = TEST_DATA
