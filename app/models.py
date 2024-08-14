from pydantic import BaseModel, Field
from typing import List, Optional


class OpeningHour(BaseModel):
    """
    Represents an opening or closing time.

    Attributes:
        type (str): 'open' or 'close'.
        value (int): UNIX time for the event.
    """
    type: str = Field(
        ..., description="Type of operation, either 'open' or 'close'"
    )
    value: int = Field(
        ..., description="UNIX time representing the time of opening or closing"
    )


class DaySchedule(BaseModel):
    """
    Weekly schedule for the restaurant.

    Attributes:
        monday (Optional[List[OpeningHour]]): Monday hours.
        tuesday (Optional[List[OpeningHour]]): Tuesday hours.
        wednesday (Optional[List[OpeningHour]]): Wednesday hours.
        thursday (Optional[List[OpeningHour]]): Thursday hours.
        friday (Optional[List[OpeningHour]]): Friday hours.
        saturday (Optional[List[OpeningHour]]): Saturday hours.
        sunday (Optional[List[OpeningHour]]): Sunday hours.
    """
    monday: Optional[List[OpeningHour]] = []
    tuesday: Optional[List[OpeningHour]] = []
    wednesday: Optional[List[OpeningHour]] = []
    thursday: Optional[List[OpeningHour]] = []
    friday: Optional[List[OpeningHour]] = []
    saturday: Optional[List[OpeningHour]] = []
    sunday: Optional[List[OpeningHour]] = []
