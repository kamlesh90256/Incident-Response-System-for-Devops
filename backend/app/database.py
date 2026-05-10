from sqlalchemy.engine import make_url
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///./monitoring.db"
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ENVIRONMENT: str = "development"
    
    class Config:
        env_file = ".env"

settings = Settings()


def _normalize_database_url(database_url: str) -> str:
    url = make_url(database_url)

    if url.drivername in {"sqlite", "sqlite+pysqlite"}:
        return url.set(drivername="sqlite+aiosqlite").render_as_string(hide_password=False)

    if url.drivername in {"postgresql", "postgres"}:
        return url.set(drivername="postgresql+asyncpg").render_as_string(hide_password=False)

    return database_url

# SQLAlchemy setup - use async driver based on the configured URL
database_url = _normalize_database_url(settings.DATABASE_URL)
engine = create_async_engine(
    database_url,
    echo=settings.ENVIRONMENT == "development",
    future=True,
    connect_args={"check_same_thread": False} if database_url.startswith("sqlite") else {},
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
