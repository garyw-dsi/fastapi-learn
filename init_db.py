import asyncio
from database import engine
from models import Base

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)  # Creates all tables
    print("Database tables created!")

asyncio.run(init_db())  # Run this script to create tables
