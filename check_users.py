import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if "+asyncpg" in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("+asyncpg", "")

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM users"))
    users = result.fetchall()
    
    if users:
        print("👤 Пользователи в базе:")
        for user in users:
            print(f"  - ID: {user[0]}, Telegram ID: {user[1]}, Имя: {user[2]}, Город: {user[9]}")
    else:
        print("❌ В таблице users нет пользователей!")
        print("   Напиши /register в Telegram и заполни анкету.")