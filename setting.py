import os

from dotenv import load_dotenv
from pydantic import StrictStr

# Load environment variables from the .env file
load_dotenv()


class AllSettings:
    """
        Class representing application settings.

        Attributes:
            api_token (StrictStr): API token loaded from environment variables.
    """
    BINANCE_API_KEY: StrictStr = os.getenv("BINANCE_API_KEY", None)
    BINANCE_SECRET_KEY: StrictStr = os.getenv("BINANCE_SECRET_KEY", None)
