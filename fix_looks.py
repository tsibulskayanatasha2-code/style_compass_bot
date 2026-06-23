import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if "+asyncpg" in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("+asyncpg", "")

engine = create_engine(DATABASE_URL)

def fix_looks():
    with engine.connect() as conn:
        # Удаляем старую таблицу
        conn.execute(text("DROP TABLE IF EXISTS looks CASCADE"))
        conn.commit()
        print("✅ Старая таблица удалена")
        
        # Создаём новую с правильными размерами
        conn.execute(text("""
            CREATE TABLE looks (
                id SERIAL PRIMARY KEY,
                gender VARCHAR(20),
                hair VARCHAR(20),
                eyes VARCHAR(20),
                skin VARCHAR(20),
                color_type VARCHAR(20),
                style VARCHAR(50),
                weather VARCHAR(50),
                temp_min INTEGER,
                temp_max INTEGER,
                makeup TEXT,
                outfit TEXT,
                skincare TEXT,
                advice TEXT
            )
        """))
        conn.commit()
        print("✅ Новая таблица создана!")

if __name__ == "__main__":
    fix_looks()