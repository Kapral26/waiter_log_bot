from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine

from config.config_reader import Settings
from models import Base, Users, Groups, FoundErrors

__all__ = [
    "Base",
    "Users",
    "Groups",
    "FoundErrors"
]

SETTINGS = Settings()


async def session_factory() -> async_sessionmaker[AsyncSession]:
    """Получение сессии"""
    engine = create_async_engine(
            await get_db_url(),
            echo=SETTINGS.db_echo,
            # Количество подключений, которых будет создано для подключения к БД
            pool_size=SETTINGS.db_pool_size,
            # Максимально количество дополнительных подключений
            max_overflow=SETTINGS.db_max_overflow,
    )
    session = async_sessionmaker(bind=engine)
    return session


async def get_db_url() -> URL:
    """Получение URL для подключения к БД"""
    url_object_sync = URL.create(
            "postgresql+asyncpg",
            port=SETTINGS.pg_port,
            host=SETTINGS.pg_host,
            database=SETTINGS.pg_dbname,
            username=SETTINGS.pg_login,
            password=SETTINGS.pg_pass.get_secret_value(),
    )
    return url_object_sync


async def create_engine_async() -> AsyncEngine:
    """
    Получение синхронного движка
    :return:
    """
    url_object_sync = await get_db_url()

    # Синхронный движок
    engine_async = create_async_engine(
            # url="DSN для подключения к БД" или объект sqlalchemy.URL,
            url=url_object_sync,
            # В консоль будут сыпаться все запросы к БД.
            echo=True,
            # Количество подключений, которых будет создано для подключения к БД
            pool_size=5,
            # Максимально количество дополнительных подключений
            max_overflow=10,
    )

    return engine_async

