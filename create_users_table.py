import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if "+asyncpg" in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("+asyncpg", "")

engine = create_engine(DATABASE_URL)

def create_users_table():
    with engine.connect() as conn:
        # Удаляем старую таблицу, если она есть (чтобы пересоздать с правильной структурой)
        conn.execute(text("DROP TABLE IF EXISTS users CASCADE"))
        conn.commit()
        print("✅ Старая таблица users удалена (если была)")

        # Создаём таблицу users
        conn.execute(text("""
            CREATE TABLE users (
                id SERIAL PRIMARY KEY,
                telegram_id BIGINT UNIQUE NOT NULL,
                name VARCHAR(100),
                gender VARCHAR(10),
                hair VARCHAR(20),
                eyes VARCHAR(20),
                skin VARCHAR(20),
                color_type VARCHAR(20),
                style VARCHAR(50),
                city VARCHAR(100),
                created_at TIMESTAMP DEFAULT NOW()
            )
        """))
        conn.commit()
        print("✅ Таблица users создана!")

if __name__ == "__main__":
    create_users_table()