# Автор: Настя
# Добавлены новые образы для блондинок и брюнеток
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if "+asyncpg" in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("+asyncpg", "")

engine = create_engine(DATABASE_URL)

def add_looks():
    with engine.connect() as conn:
        # Очищаем старые образы
        conn.execute(text("DELETE FROM looks"))
        conn.commit()
        print("✅ Старые образы удалены")

        # ============ ОБРАЗЫ ДЛЯ БЛОНДИНОК (ВЕСНА) ============
        
        # Романтичный стиль
        conn.execute(text("""
            INSERT INTO looks (gender, hair, eyes, skin, color_type, style, weather, temp_min, temp_max, makeup, outfit, skincare, advice)
            VALUES ('женский', 'блондин', 'голубые', 'светлая', 'весна', 'романтичный', 'clear', 18, 30, 
                   '💄 Лёгкий тональный крем с сиянием, персиковые румяна, светлые тени с шиммером, розовый блеск для губ',
                   '👗 Льняное платье пастельного розового цвета, белые кеды, соломенная сумка',
                   '🧴 SPF 50, увлажняющий спрей',
                   '💡 Добавь тонкий золотой кулон — он подчеркнёт твой цветотип')
        """))
        
        # Деловой стиль
        conn.execute(text("""
            INSERT INTO looks (gender, hair, eyes, skin, color_type, style, weather, temp_min, temp_max, makeup, outfit, skincare, advice)
            VALUES ('женский', 'блондин', 'голубые', 'светлая', 'весна', 'деловой', 'clear', 15, 25,
                   '💄 Матовый тональный крем, нежные румяна, коричневая тушь, нюдовая помада',
                   '👗 Бежевый костюм-двойка, белая блуза, бежевые лоферы',
                   '🧴 SPF 30, увлажняющий крем',
                   '💡 Добавь золотые серьги-кольца — завершат образ')
        """))
        
        # Спортивный стиль
        conn.execute(text("""
            INSERT INTO looks (gender, hair, eyes, skin, color_type, style, weather, temp_min, temp_max, makeup, outfit, skincare, advice)
            VALUES ('женский', 'блондин', 'голубые', 'светлая', 'весна', 'спортивный', 'clouds', 10, 20,
                   '💄 Только консилер, тушь и бальзам для губ',
                   '👗 Серая худи оверсайз, лосины, кроссовки, бейсболка',
                   '🧴 Увлажняющий крем, SPF 30',
                   '💡 Возьми с собой лёгкую ветровку на случай дождя')
        """))
        
        # Дерзкий стиль
        conn.execute(text("""
            INSERT INTO looks (gender, hair, eyes, skin, color_type, style, weather, temp_min, temp_max, makeup, outfit, skincare, advice)
            VALUES ('женский', 'блондин', 'голубые', 'светлая', 'весна', 'дерзкий', 'clear', 15, 28,
                   '💄 Чёрная тушь, стрелки, матовая помада кораллового оттенка',
                   '👗 Кожаная куртка, белая футболка, джинсы-скинни, ботильоны',
                   '🧴 SPF 30, матирующий спрей',
                   '💡 Добавь серебряные украшения — они добавят дерзости')
        """))
        
        # Минимализм
        conn.execute(text("""
            INSERT INTO looks (gender, hair, eyes, skin, color_type, style, weather, temp_min, temp_max, makeup, outfit, skincare, advice)
            VALUES ('женский', 'блондин', 'голубые', 'светлая', 'весна', 'минимализм', 'clear', 15, 28,
                   '💄 Только тушь и увлажняющий бальзам для губ',
                   '👗 Белая рубашка оверсайз, чёрные брюки, белые кроссовки',
                   '🧴 SPF 30, увлажняющий крем',
                   '💡 Минимализм — это всегда стильно!')
        """))
        
        # ============ ОБРАЗЫ ДЛЯ БРЮНЕТОК (ОСЕНЬ) ============
        
        # Романтичный стиль
        conn.execute(text("""
            INSERT INTO looks (gender, hair, eyes, skin, color_type, style, weather, temp_min, temp_max, makeup, outfit, skincare, advice)
            VALUES ('женский', 'брюнет', 'карие', 'смуглая', 'осень', 'романтичный', 'clear', 18, 30,
                   '💄 Лёгкий тональник, коралловые румяна, золотистые тени, нюдовая помада',
                   '👗 Лёгкое шифоновое платье, босоножки на танкетке, клатч',
                   '🧴 SPF 50, увлажняющий спрей',
                   '💡 Добавь золотой кулон — он подчеркнёт цвет глаз')
        """))
        
        # Деловой стиль
        conn.execute(text("""
            INSERT INTO looks (gender, hair, eyes, skin, color_type, style, weather, temp_min, temp_max, makeup, outfit, skincare, advice)
            VALUES ('женский', 'брюнет', 'карие', 'смуглая', 'осень', 'деловой', 'rain', 5, 15,
                   '💄 Консилер, чёрная тушь, матовая помада терракотового оттенка',
                   '👗 Бежевый плащ-тренч, чёрные брюки, водолазка, ботильоны',
                   '🧴 Увлажняющий крем, SPF 30',
                   '💡 Яркий шарф добавит цвета в пасмурный день')
        """))
        
        # Дерзкий стиль
        conn.execute(text("""
            INSERT INTO looks (gender, hair, eyes, skin, color_type, style, weather, temp_min, temp_max, makeup, outfit, skincare, advice)
            VALUES ('женский', 'брюнет', 'карие', 'смуглая', 'осень', 'дерзкий', 'clear', 18, 30,
                   '💄 Матовый тональник, коралловые румяна, золотистые тени, тёмно-вишнёвая помада',
                   '👗 Кожаная юбка-миди, чёрный топ, босоножки на каблуке, клатч',
                   '🧴 SPF 50, матирующий спрей',
                   '💡 Добавь золотые украшения — они идеально подходят к твоему цветотипу')
        """))
        
        # Спортивный стиль
        conn.execute(text("""
            INSERT INTO looks (gender, hair, eyes, skin, color_type, style, weather, temp_min, temp_max, makeup, outfit, skincare, advice)
            VALUES ('женский', 'брюнет', 'карие', 'смуглая', 'осень', 'спортивный', 'clear', 15, 28,
                   '💄 Только консилер и тушь',
                   '👗 Чёрные леггинсы, белая футболка, кроссовки, кепка',
                   '🧴 SPF 30, увлажняющий крем',
                   '💡 Не забудь бутылку воды — спорт требует гидратации!')
        """))
        
        # ============ ОБРАЗЫ ДЛЯ ШАТЕНОК (ЛЕТО) ============
        
        # Романтичный стиль
        conn.execute(text("""
            INSERT INTO looks (gender, hair, eyes, skin, color_type, style, weather, temp_min, temp_max, makeup, outfit, skincare, advice)
            VALUES ('женский', 'шатен', 'зелёные', 'средне-светлая', 'лето', 'романтичный', 'clouds', 10, 20,
                   '💄 Лёгкий тональник, румяна персиковые, бежевые тени, прозрачный блеск',
                   '👗 Серый свитер оверсайз, чёрные джинсы, белые кроссовки',
                   '🧴 Увлажняющий крем, SPF 30',
                   '💡 Добавь серебряные украшения — они подчеркнут зелёные глаза')
        """))
        
        # Деловой стиль
        conn.execute(text("""
            INSERT INTO looks (gender, hair, eyes, skin, color_type, style, weather, temp_min, temp_max, makeup, outfit, skincare, advice)
            VALUES ('женский', 'шатен', 'зелёные', 'средне-светлая', 'лето', 'деловой', 'clear', 15, 25,
                   '💄 Матовый тональник, нежные румяна, коричневая тушь, нюдовая помада',
                   '👗 Серый костюм, белая блуза, чёрные лоферы',
                   '🧴 SPF 30, увлажняющий крем',
                   '💡 Добавь часы на кожаный ремешок')
        """))
        
        # ============ ОБРАЗЫ ДЛЯ ПАРНЕЙ ============
        
        # Парень - брюнет, деловой стиль
        conn.execute(text("""
            INSERT INTO looks (gender, hair, eyes, skin, color_type, style, weather, temp_min, temp_max, makeup, outfit, skincare, advice)
            VALUES ('мужской', 'брюнет', 'карие', 'смуглая', 'осень', 'деловой', 'clear', 15, 28,
                   NULL,
                   '👔 Светлая рубашка, серые брюки, кожаный ремень, лоферы',
                   '🧴 Увлажняющий крем после бритья, SPF 30',
                   '💡 Добавь часы с кожаным ремешком — завершат образ')
        """))
        
        # Парень - блондин, спортивный стиль
        conn.execute(text("""
            INSERT INTO looks (gender, hair, eyes, skin, color_type, style, weather, temp_min, temp_max, makeup, outfit, skincare, advice)
            VALUES ('мужской', 'блондин', 'голубые', 'светлая', 'весна', 'спортивный', 'clear', 15, 28,
                   NULL,
                   '👔 Футболка-поло, бежевые чиносы, белые кеды, кепка',
                   '🧴 Увлажняющий крем, SPF 30',
                   '💡 Добавь солнцезащитные очки — стильно и практично')
        """))
        
        # Парень - шатен, романтичный стиль
        conn.execute(text("""
            INSERT INTO looks (gender, hair, eyes, skin, color_type, style, weather, temp_min, temp_max, makeup, outfit, skincare, advice)
            VALUES ('мужской', 'шатен', 'зелёные', 'средне-светлая', 'лето', 'романтичный', 'clear', 15, 25,
                   NULL,
                   '👔 Белый свитер, тёмные джинсы, ботинки, шарф',
                   '🧴 Увлажняющий крем, SPF 30',
                   '💡 Добавь шерстяное пальто для завершения образа')
        """))
        
        # ============ УНИВЕРСАЛЬНЫЕ ОБРАЗЫ ============
        
        # Для снега
        conn.execute(text("""
            INSERT INTO looks (gender, hair, eyes, skin, color_type, style, weather, temp_min, temp_max, makeup, outfit, skincare, advice)
            VALUES ('универсальный', NULL, NULL, NULL, NULL, NULL, 'snow', -20, 0,
                   '💄 Защитный крем от мороза, гигиеническая помада',
                   '🧥 Тёплый пуховик, шарф, шапка, варежки, зимние ботинки',
                   '🧴 Жирный питательный крем',
                   '💡 Одевайся слоями — так теплее!')
        """))
        
        # Для дождя
        conn.execute(text("""
            INSERT INTO looks (gender, hair, eyes, skin, color_type, style, weather, temp_min, temp_max, makeup, outfit, skincare, advice)
            VALUES ('универсальный', NULL, NULL, NULL, NULL, NULL, 'rain', 5, 15,
                   '💄 Водостойкая тушь (для девушек)',
                   '🧥 Плащ-дождевик, зонт, удобная обувь',
                   '🧴 Увлажняющий крем',
                   '💡 Не забудь зонт! Погода переменчива')
        """))
        
        # Для пасмурной погоды
        conn.execute(text("""
            INSERT INTO looks (gender, hair, eyes, skin, color_type, style, weather, temp_min, temp_max, makeup, outfit, skincare, advice)
            VALUES ('универсальный', NULL, NULL, NULL, NULL, NULL, 'clouds', 5, 18,
                   '💄 Увлажняющий бальзам для губ, лёгкий тональник',
                   '🧥 Уютный свитер, джинсы, удобная обувь',
                   '🧴 Увлажняющий крем',
                   '💡 Добавь яркий шарф — он поднимет настроение!')
        """))
        
        # Универсальный для любой погоды
        conn.execute(text("""
            INSERT INTO looks (gender, hair, eyes, skin, color_type, style, weather, temp_min, temp_max, makeup, outfit, skincare, advice)
            VALUES ('универсальный', NULL, NULL, NULL, NULL, NULL, NULL, 10, 30,
                   '💄 Лёгкий уход, SPF, увлажнение',
                   '👗 Светлая одежда из натуральных тканей, удобная обувь',
                   '🧴 SPF 30, увлажняющий крем',
                   '💡 Главное — комфорт и хорошее настроение!')
        """))
        
        conn.commit()
        print("✅ Все образы добавлены в базу данных!")

if __name__ == "__main__":
    add_looks()
