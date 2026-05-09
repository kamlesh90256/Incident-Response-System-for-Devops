import os
from sqlalchemy import create_engine, event
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./monitoring.db"
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ENVIRONMENT: str = "development"
    
    class Config:
        env_file = ".env"

settings = Settings()

# SQLAlchemy setup - use async SQLite
engine = create_async_engine(
    "sqlite+aiosqlite:///./monitoring.db",
    echo=settings.ENVIRONMENT == "development",
    future=True,
    connect_args={"check_same_thread": False}
)

async_session = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()

async def get_db():
    async with async_session() as session:
        yield session

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
