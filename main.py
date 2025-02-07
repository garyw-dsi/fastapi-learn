from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from models import Account
from sqlalchemy.future import select

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello, FastAPI!"}

@app.post("/account/")
async def create_account(name: str, balance: int, session: AsyncSession = Depends(get_async_session)):
    new_account = Account(name=name, balance=balance)
    session.add(new_account)
    await session.commit()
    await session.refresh(new_account)
    return new_account

@app.get("/accounts/")
async def list_accounts(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Account))
    accounts = result.scalars().all()
    return accounts
