import os

from dotenv import load_dotenv
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine

# Carregar variáveis do .env
load_dotenv()

app = FastAPI()

# Pega a URL do Postgres do .env
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=False)


@app.get("/health")
async def health_check():
    try:
        async with engine.connect() as conn:
            await conn.execute("SELECT 1")
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        return {"status": "error", "database": str(e)}
