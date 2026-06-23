import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if "+asyncpg" in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("+asyncpg", "")

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    # Проверяем, какие таблицы есть
    result = conn.execute(text("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public'
    """))
    
    print("📋 Таблицы в базе данных:")
    for row in result:
        print(f"  - {row[0]}")