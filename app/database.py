from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from app.core.settings import settings

engine = create_async_engine(settings.database_url)
async_session = async_sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

async def get_db():
    async_db = async_session()
    try:
        yield async_db
    finally:
        await async_db.close()