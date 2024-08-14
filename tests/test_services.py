import pytest
from app.models import OpeningHour, DaySchedule
from app.services import process_day, format_schedule


@pytest.mark.asyncio
async def test_process_day():
    """
    Test the process_day service function.

    This test verifies that the process_day function correctly formats a single day's
    opening and closing times into a readable string format.
    """
    day = [
        OpeningHour(type="open", value=36000),  # 10:00 AM
        OpeningHour(type="close", value=64800)  # 6:00 PM
    ]
    result = await process_day(day, "Monday")
    assert result == "Monday: 10 AM - 6 PM"


@pytest.mark.asyncio
async def test_format_schedule():
    """
    Test the format_schedule service function.

    This test verifies that the format_schedule function correctly formats the weekly
    schedule into a readable string format.
    """
    schedule = DaySchedule(
        monday=[],
        tuesday=[
            OpeningHour(type="open", value=36000),
            OpeningHour(type="close", value=64800)
        ],
        wednesday=[],
        thursday=[
            OpeningHour(type="open", value=37800),
            OpeningHour(type="close", value=64800)
        ],
        friday=[
            OpeningHour(type="open", value=36000)
        ],
        saturday=[
            OpeningHour(type="close", value=3600),
            OpeningHour(type="open", value=36000)
        ],
        sunday=[
            OpeningHour(type="close", value=3600),
            OpeningHour(type="open", value=43200),
            OpeningHour(type="close", value=75600)
        ]
    )
    result = await format_schedule(schedule)
    assert result == (
        "Monday: Closed\n"
        "Tuesday: 10 AM - 6 PM\n"
        "Wednesday: Closed\n"
        "Thursday: 10:30 AM - 6 PM\n"
        "Friday: 10 AM - 1 AM\n"
        "Saturday: 10 AM - 1 AM\n"
        "Sunday: 12 PM - 9 PM"
    )
