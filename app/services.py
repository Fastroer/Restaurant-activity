from .models import DaySchedule, OpeningHour
from .utils import format_time
from .exceptions import InvalidTimeError
from typing import List


async def process_day(
    day: List[OpeningHour],
    day_name: str,
    next_day: List[OpeningHour] = None
) -> str:
    """
    Process the schedule for a single day, considering the transition to the next day.

    Args:
        day (List[OpeningHour]): The list of opening and closing times for the day.
        day_name (str): The name of the day.
        next_day (List[OpeningHour], optional): The list of opening and closing times
                                                for the next day.

    Returns:
        str: A formatted string representing the opening hours for the day.
    """
    if not day:
        return f"{day_name}: Closed"

    intervals = []
    i = 0
    while i < len(day):
        if i + 1 >= len(day) and next_day is None:
            raise InvalidTimeError(f"Time data for {day_name} is incomplete.")

        open_time = await format_time(day[i].value)
        if i + 1 < len(day) and day[i + 1].type == "close":
            close_time = await format_time(day[i + 1].value)
            intervals.append(f"{open_time} - {close_time}")
            i += 2
        else:
            if next_day and next_day[0].type == "close":
                close_time = await format_time(next_day[0].value)
                if close_time != open_time:
                    intervals.append(f"{open_time} - {close_time}")
            i += 1

    return f"{day_name}: {', '.join(intervals) if intervals else 'Closed'}"


async def format_schedule(schedule: DaySchedule) -> str:
    """
    Format the weekly schedule into a human-readable string.

    Args:
        schedule (DaySchedule): The weekly schedule with opening and closing times.

    Returns:
        str: A formatted string representing the opening hours for the entire week.
    """
    result = []
    result.append(await process_day(schedule.monday, "Monday", schedule.tuesday))
    result.append(await process_day(schedule.tuesday, "Tuesday", schedule.wednesday))
    result.append(await process_day(schedule.wednesday, "Wednesday", schedule.thursday))
    result.append(await process_day(schedule.thursday, "Thursday", schedule.friday))
    result.append(await process_day(schedule.friday, "Friday", schedule.saturday))
    result.append(await process_day(schedule.saturday, "Saturday", schedule.sunday))
    result.append(await process_day(schedule.sunday, "Sunday", schedule.monday))

    return "\n".join(result)
