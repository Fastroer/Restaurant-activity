from fastapi import FastAPI
from app.models import DaySchedule
from app.services import format_schedule
from app.config import config
import uvicorn

app = FastAPI(docs_url=config.DOCS_URL)


@app.post("/format-hours/")
async def format_hours(schedule: DaySchedule):
    """
    Asynchronous API endpoint for formatting restaurant opening hours.

    Args:
        schedule (DaySchedule): The schedule of the restaurant, containing opening
                                and closing times for each day of the week.

    Returns:
        dict: A dictionary with the formatted opening hours.
    """
    return {"result": await format_schedule(schedule)}


if __name__ == "__main__":
    uvicorn.run(app, host=config.HOST, port=config.PORT)
