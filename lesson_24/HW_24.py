import requests
import pytest
import logging
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"

# Logging to console and file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("test_search.log")
    ]
)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def login():
    session = requests.Session()
    r = session.post(f"{BASE_URL}/auth", auth=HTTPBasicAuth("test_user", "test_pass"))
    access_token = r.json()["access_token"]
    session.headers.update({"Authorization": "Bearer " + access_token})
    logger.info("Login successful")
    return session


@pytest.mark.parametrize("params", [
    {"sort_by": "year",          "limit": 5},
    {"sort_by": "price",         "limit": 10},
    {"sort_by": "engine_volume", "limit": 3},
    {"sort_by": "brand",         "limit": 7},
    {"sort_by": "year",          "limit": 25},
    {"sort_by": "price",         "limit": 1},
    {"sort_by": "engine_volume", "limit": 15},
])
class TestCarSearch:
    def test_cars(self, login, params):
        sort_by = params["sort_by"]
        limit = params["limit"]

        logger.info(f"Request: sort_by={sort_by}, limit={limit}")
        r = login.get(f"{BASE_URL}/cars", params=params)
        data = r.json()
        logger.info(f"Got {len(data)} items")

        assert r.status_code == 200
        assert isinstance(data, list)
        assert len(data) == limit

        for i in range(len(data) - 1):
            assert data[i][sort_by] <= data[i + 1][sort_by]