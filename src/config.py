from pydantic import BaseModel
import os
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseModel):
    alpaca_api_key: str = os.getenv("ALPACA_API_KEY", "")
    alpaca_api_secret: str = os.getenv("ALPACA_API_SECRET", "")
    alpaca_base_url: str = os.getenv("ALPACA_BASE_URL", "https://data.alpaca.markets")
    sqlite_path: str = os.getenv("SQLITE_PATH", "./alpaca.db")
    symbols: list[str] = [s.strip() for s in os.getenv("SYMBOLS", "AAPL,MSFT,SPY").split(",") if s.strip()]


settings = Settings()