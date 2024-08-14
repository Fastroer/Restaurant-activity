import os


class Config:
    """
    Configuration class for application settings.

    This class is responsible for loading environment variables from a .env file and
    providing the configuration for the app, such as the host, port, and doc URL.

    Attributes:
        HOST (str): The host on which the application will run. Defaults to "127.0.0.1".
        PORT (int): The port on which the application will listen. Defaults to 8000.
        DOCS_URL (str): The URL path for accessing the API doc. Defaults to "/docs".
    """
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", 8000))
    DOCS_URL = os.getenv("DOCS_URL", "/docs")


config = Config()
