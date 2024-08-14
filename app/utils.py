from datetime import datetime, timezone


async def format_time(unix_time: int) -> str:
    """Asynchronously format UNIX time into a 12-hour time format."""
    time_str = (
        datetime.fromtimestamp(unix_time, tz=timezone.utc)
        .strftime('%I:%M %p')
        .lstrip('0')
    )
    if time_str.endswith(':00 AM') or time_str.endswith(':00 PM'):
        time_str = time_str.replace(':00', '')
    return time_str
