import pytest
from app.utils import format_time


@pytest.mark.asyncio
async def test_format_time():
    """
    Test the format_time utility function.

    This test verifies that the format_time function correctly formats UNIX timestamps
    into a 12-hour time format without leading zeros.
    """
    assert await format_time(43200) == "12 PM"
    assert await format_time(3600) == "1 AM"
    assert await format_time(75600) == "9 PM"
