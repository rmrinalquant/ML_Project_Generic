from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .db import Base


class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String(32), unique=True, nullable=False, index=True)
    name = Column(String(256), nullable=True)
    exchange = Column(String(64), nullable=True)
    asset_class = Column(String(64), nullable=True)
    sector = Column(String(128), nullable=True)
    industry = Column(String(128), nullable=True)

    bars = relationship("Bar", back_populates="asset", cascade="all, delete-orphan")
    fundamentals = relationship("Fundamentals", back_populates="asset", cascade="all, delete-orphan")
    technicals = relationship("Technical", back_populates="asset", cascade="all, delete-orphan")


class Bar(Base):
    __tablename__ = "bars"
    __table_args__ = (
        UniqueConstraint("asset_id", "time", "timeframe", name="uq_bar_asset_time_timeframe"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    asset_id = Column(Integer, ForeignKey("assets.id", ondelete="CASCADE"), nullable=False, index=True)
    timeframe = Column(String(16), nullable=False)  # e.g., 1Min, 5Min, 1Hour, 1Day
    time = Column(DateTime, nullable=False, index=True)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(Float, nullable=True)
    trade_count = Column(Integer, nullable=True)
    vwap = Column(Float, nullable=True)

    asset = relationship("Asset", back_populates="bars")


class Fundamentals(Base):
    __tablename__ = "fundamentals"
    __table_args__ = (
        UniqueConstraint("asset_id", name="uq_fundamentals_asset"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    asset_id = Column(Integer, ForeignKey("assets.id", ondelete="CASCADE"), nullable=False, index=True)

    # Key fundamentals (extend as needed)
    market_cap = Column(Float, nullable=True)
    pe_ratio = Column(Float, nullable=True)
    eps_ttm = Column(Float, nullable=True)
    dividend_yield = Column(Float, nullable=True)
    shares_outstanding = Column(Float, nullable=True)
    beta = Column(Float, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    asset = relationship("Asset", back_populates="fundamentals")


class Technical(Base):
    __tablename__ = "technicals"
    __table_args__ = (
        UniqueConstraint("asset_id", "time", "timeframe", name="uq_technical_asset_time_timeframe"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    asset_id = Column(Integer, ForeignKey("assets.id", ondelete="CASCADE"), nullable=False, index=True)
    timeframe = Column(String(16), nullable=False)
    time = Column(DateTime, nullable=False, index=True)

    # Common indicators
    sma_20 = Column(Float, nullable=True)
    sma_50 = Column(Float, nullable=True)
    ema_20 = Column(Float, nullable=True)
    ema_50 = Column(Float, nullable=True)
    rsi_14 = Column(Float, nullable=True)
    macd = Column(Float, nullable=True)
    macd_signal = Column(Float, nullable=True)
    macd_hist = Column(Float, nullable=True)
    bb_upper = Column(Float, nullable=True)
    bb_middle = Column(Float, nullable=True)
    bb_lower = Column(Float, nullable=True)

    asset = relationship("Asset", back_populates="technicals")