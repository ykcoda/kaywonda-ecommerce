from app.config import database_settings
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm.session import sessionmaker


async_db_session = create_async_engine(url=database_settings.database_url, echo=True)


async def get_db_async_session():
    async_session = sessionmaker(
        bind=async_db_session, class_=AsyncSession, expire_on_commit=False
    )

    async with async_session() as session:
        yield session
