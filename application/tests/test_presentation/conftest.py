from typing import Any, Generator
from httpx import AsyncClient, HTTPTransport, ASGITransport
import pytest
from fastapi import FastAPI
import pytest_asyncio
import mock
from fastapi.testclient import TestClient

from main import app as main_app



@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    """
    """
    mock.patch("events.event_repository.EventManager", return_value=mock.MagicMock())
    _app = main_app
    yield _app

@pytest_asyncio.fixture(scope="function")
async def client(app: FastAPI) -> Generator[TestClient, Any, None]:
    # async def client(app: FastAPI) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client