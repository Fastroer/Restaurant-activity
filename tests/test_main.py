import pytest
from httpx import AsyncClient
from httpx import ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_format_hours():
    """
    Test the /format-hours/ API endpoint.

    This test verifies that the API correctly formats the provided weekly schedule
    and returns the expected response in JSON format.
    """
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        response = await ac.post(
            "/format-hours/",
            json={
                "monday": [],
                "tuesday": [
                    {"type": "open", "value": 36000},
                    {"type": "close", "value": 64800}
                ],
                "wednesday": [],
                "thursday": [
                    {"type": "open", "value": 37800},
                    {"type": "close", "value": 64800}
                ],
                "friday": [
                    {"type": "open", "value": 36000}
                ],
                "saturday": [
                    {"type": "close", "value": 3600},
                    {"type": "open", "value": 36000}
                ],
                "sunday": [
                    {"type": "close", "value": 3600},
                    {"type": "open", "value": 43200},
                    {"type": "close", "value": 75600}
                ]
            }
        )
    assert response.status_code == 200
    assert response.json() == {
        "result": (
            "Monday: Closed\n"
            "Tuesday: 10 AM - 6 PM\n"
            "Wednesday: Closed\n"
            "Thursday: 10:30 AM - 6 PM\n"
            "Friday: 10 AM - 1 AM\n"
            "Saturday: 10 AM - 1 AM\n"
            "Sunday: 12 PM - 9 PM"
        )
    }
