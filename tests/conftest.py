from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    # Keep tests deterministic by restoring in-memory state around every test.
    original_state = deepcopy(activities)
    yield
    activities.clear()
    activities.update(deepcopy(original_state))
