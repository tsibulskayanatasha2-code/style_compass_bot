import os
import asyncio
from sqlalchemy import text
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine

load_dotenv()

async def test():
    database_url = os.getenv('DATABASE_URL')
    print(f"Подключаюсь к: {database_url}")
    
    engine = create_async_engine(database_url, echo=True)
    
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 'hello world'"))
        print("✅ Подключение работает!")
        print(f"Результат: {result.fetchall()}")
    
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(test())