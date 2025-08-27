## Alpaca Data Engineering Pipeline (Local SQLite)

This project fetches price bars and fundamentals from Alpaca, computes technical indicators with pandas-ta, and persists everything to a local SQLite database.

### Features
- Ingest OHLCV bars (intraday or daily) from Alpaca Market Data API v2
- Ingest fundamentals (best-effort with fallbacks)
- Compute technical indicators (SMA, EMA, RSI, MACD, Bollinger Bands)
- Local persistence with SQLite via SQLAlchemy ORM
- Simple CLI for ETL operations

### Setup
1. Create and activate a virtual environment, then install dependencies:
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

2. Copy environment example and fill in your credentials:
```bash
cp .env.example .env
```

Update `.env` with your Alpaca API keys and desired configuration.

### Environment
- `ALPACA_API_KEY` and `ALPACA_API_SECRET`: Your Alpaca API keys
- `ALPACA_BASE_URL`: Optional. Default `https://data.alpaca.markets`
- `SQLITE_PATH`: Optional. Default `./alpaca.db`
- `SYMBOLS`: Comma-separated list of tickers (e.g., `AAPL,MSFT,SPY`)

### Usage
Initialize the database:
```bash
python -m src.cli init-db
```

Ingest daily bars for the last 60 days:
```bash
python -m src.cli ingest-bars --timeframe=1Day --days=60
```

Ingest fundamentals for configured symbols:
```bash
python -m src.cli ingest-fundamentals
```

Compute technical indicators from stored bars:
```bash
python -m src.cli compute-technicals --timeframe=1Day
```

### Notes
- This template uses SQLite for simplicity. Swap the connection URL in `src/db.py` to use Postgres or another RDBMS.
- Fundamentals coverage and fields depend on your Alpaca plan and the API version available. The client attempts v2 first, then falls back where possible.
