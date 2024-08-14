class InvalidTimeError(Exception):
    """
    Exception raised for invalid time values.

    Attributes:
        message (str): Error message. Defaults to "Invalid time provided".
    """

    def __init__(self, message: str = "Invalid time provided"):
        """
        Initialize the exception with an optional error message.

        Args:
            message (str): Custom error message.
        """
        self.message = message
        super().__init__(self.message)
