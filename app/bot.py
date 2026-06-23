#Автор: Даша
import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import httpx

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# СОСТОЯНИЯ ДЛЯ АНКЕТЫ
class Form(StatesGroup):
    name = State()
    gender = State()
    hair = State()
    eyes = State()
    skin = State()
    color_type = State()
    style = State()
    city = State()

# ============ ВСЕ КЛАВИАТУРЫ ============

# Пол
gender_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="👨 Мужской", callback_data="мужской")],
    [InlineKeyboardButton(text="👩 Женский", callback_data="женский")]
])

# Цвет волос
hair_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🟡 Блондин(ка)", callback_data="блондин")],
    [InlineKeyboardButton(text="🟤 Шатен(ка)", callback_data="шатен")],
    [InlineKeyboardButton(text="⚫ Брюнет(ка)", callback_data="брюнет")],
    [InlineKeyboardButton(text="🔴 Рыжий(ая)", callback_data="рыжий")],
    [InlineKeyboardButton(text="⚪ Русый(ая)", callback_data="русый")]
])

# Цвет глаз
eyes_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💙 Голубые", callback_data="голубые")],
    [InlineKeyboardButton(text="💚 Зелёные", callback_data="зелёные")],
    [InlineKeyboardButton(text="🤎 Карие", callback_data="карие")],
    [InlineKeyboardButton(text="🩶 Серые", callback_data="серые")],
    [InlineKeyboardButton(text="🟫 Ореховые", callback_data="ореховые")]
])

# Оттенок кожи
skin_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🩷 Светлая", callback_data="светлая")],
    [InlineKeyboardButton(text="💗 Средне-светлая", callback_data="средне-светлая")],
    [InlineKeyboardButton(text="🟫 Оливковая", callback_data="оливковая")],
    [InlineKeyboardButton(text="🤎 Смуглая", callback_data="смуглая")],
    [InlineKeyboardButton(text="🖤 Тёмная", callback_data="тёмная")]
])

# Цветотип
color_type_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🌸 Весна", callback_data="весна")],
    [InlineKeyboardButton(text="☀️ Лето", callback_data="лето")],
    [InlineKeyboardButton(text="🍁 Осень", callback_data="осень")],
    [InlineKeyboardButton(text="❄️ Зима", callback_data="зима")]
])

# Стиль
style_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🌸 Романтичный", callback_data="романтичный")],
    [InlineKeyboardButton(text="💼 Деловой", callback_data="деловой")],
    [InlineKeyboardButton(text="🏃 Спортивный", callback_data="спортивный")],
    [InlineKeyboardButton(text="🔥 Дерзкий", callback_data="дерзкий")],
    [InlineKeyboardButton(text="✨ Минимализм", callback_data="минимализм")]
])

# ============ КОМАНДЫ ============

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Привет! Я Style Compass — твой стилист в кармане! 💅\n\n"
        "Чтобы я мог подбирать образы именно для тебя, давай заполним анкету!\n"
        "Напиши /register"
    )

@dp.message(Command("register"))
async def register(message: types.Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer("📝 Как тебя зовут?")

# ============ ВОПРОС 1: ИМЯ ============
@dp.message(Form.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.gender)
    await message.answer("👤 Твой пол?", reply_markup=gender_kb)

# ============ ВОПРОС 2: ПОЛ ============
@dp.callback_query(lambda c: c.data in ["мужской", "женский"])
async def process_gender(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(gender=callback.data)
    await state.set_state(Form.hair)
    await callback.message.delete()
    await callback.message.answer("💇‍♀️ Твой цвет волос?", reply_markup=hair_kb)
    await callback.answer()

# ============ ВОПРОС 3: ЦВЕТ ВОЛОС ============
@dp.callback_query(lambda c: c.data in ["блондин", "шатен", "брюнет", "рыжий", "русый"])
async def process_hair(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(hair=callback.data)
    await state.set_state(Form.eyes)
    await callback.message.delete()
    await callback.message.answer("👁️ Твой цвет глаз?", reply_markup=eyes_kb)
    await callback.answer()

# ============ ВОПРОС 4: ЦВЕТ ГЛАЗ ============
@dp.callback_query(lambda c: c.data in ["голубые", "зелёные", "карие", "серые", "ореховые"])
async def process_eyes(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(eyes=callback.data)
    await state.set_state(Form.skin)
    await callback.message.delete()
    await callback.message.answer("🧴 Твой оттенок кожи?", reply_markup=skin_kb)
    await callback.answer()

# ============ ВОПРОС 5: ОТТЕНОК КОЖИ ============
@dp.callback_query(lambda c: c.data in ["светлая", "средне-светлая", "оливковая", "смуглая", "тёмная"])
async def process_skin(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(skin=callback.data)
    await state.set_state(Form.color_type)
    await callback.message.delete()
    await callback.message.answer("🎨 Твой цветотип?", reply_markup=color_type_kb)
    await callback.answer()

# ============ ВОПРОС 6: ЦВЕТОТИП ============
@dp.callback_query(lambda c: c.data in ["весна", "лето", "осень", "зима"])
async def process_color_type(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(color_type=callback.data)
    await state.set_state(Form.style)
    await callback.message.delete()
    await callback.message.answer("👗 Твой любимый стиль?", reply_markup=style_kb)
    await callback.answer()

# ============ ВОПРОС 7: СТИЛЬ ============
@dp.callback_query(lambda c: c.data in ["романтичный", "деловой", "спортивный", "дерзкий", "минимализм"])
async def process_style(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(style=callback.data)
    await state.set_state(Form.city)
    await callback.message.delete()
    await callback.message.answer("🌆 Напиши название своего города (например, Москва, Санкт-Петербург)")
    await callback.answer()

# ============ ВОПРОС 8: ГОРОД С ПРОВЕРКОЙ ============
    #проверка города
@dp.message(Form.city)
async def process_city(message: types.Message, state: FSMContext):
    from sqlalchemy import create_engine, text
    from dotenv import load_dotenv
    import os
    import httpx
    
    load_dotenv()
    DATABASE_URL = os.getenv("DATABASE_URL")
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    
    if "+asyncpg" in DATABASE_URL:
        DATABASE_URL = DATABASE_URL.replace("+asyncpg", "")
    
    city = message.text.strip()
    
    # ============ ПРОВЕРЯЕМ ГОРОД ============
    await message.answer("⏳ Проверяю город...")
    
    # Отправляем запрос в OpenWeatherMap
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(weather_url)
        
        if response.status_code != 200:
            # Город не найден
            await message.answer(
                "❌ Я не нашла такой город 😅\n"
                "Проверь, пожалуйста, правильность написания.\n"
                "Или напиши ближайший крупный город.\n\n"
                "Попробуй ещё раз:"
            )
            return  # Оставляем пользователя в состоянии Form.city
        
        # Город найден!
        weather_data = response.json()
        city_name = weather_data.get("name", city)
        
        await state.update_data(city=city_name)
        data = await state.get_data()
    
    # ============ СОХРАНЯЕМ В БАЗУ ДАННЫХ ============
    engine = create_engine(DATABASE_URL)
    
    with engine.connect() as conn:
        # Проверяем, есть ли уже такой пользователь
        user = conn.execute(
            text("SELECT * FROM users WHERE telegram_id = :telegram_id"),
            {"telegram_id": message.from_user.id}
        ).fetchone()
        
        if user:
            # Обновляем данные
            conn.execute(
                text("""
                    UPDATE users SET 
                        name = :name,
                        gender = :gender,
                        hair = :hair,
                        eyes = :eyes,
                        skin = :skin,
                        color_type = :color_type,
                        style = :style,
                        city = :city
                    WHERE telegram_id = :telegram_id
                """),
                {
                    "name": data['name'],
                    "gender": data['gender'],
                    "hair": data['hair'],
                    "eyes": data['eyes'],
                    "skin": data['skin'],
                    "color_type": data['color_type'],
                    "style": data['style'],
                    "city": city_name,
                    "telegram_id": message.from_user.id
                }
            )
        else:
            # Создаём нового пользователя
            conn.execute(
                text("""
                    INSERT INTO users 
                    (telegram_id, name, gender, hair, eyes, skin, color_type, style, city)
                    VALUES (:telegram_id, :name, :gender, :hair, :eyes, :skin, :color_type, :style, :city)
                """),
                {
                    "telegram_id": message.from_user.id,
                    "name": data['name'],
                    "gender": data['gender'],
                    "hair": data['hair'],
                    "eyes": data['eyes'],
                    "skin": data['skin'],
                    "color_type": data['color_type'],
                    "style": data['style'],
                    "city": city_name
                }
            )
        conn.commit()
    
    # Словарь для красивых названий
    gender_names = {"мужской": "Мужской", "женский": "Женский"}
    hair_names = {"блондин": "Блондин(ка)", "шатен": "Шатен(ка)", "брюнет": "Брюнет(ка)", "рыжий": "Рыжий(ая)", "русый": "Русый(ая)"}
    eye_names = {"голубые": "Голубые", "зелёные": "Зелёные", "карие": "Карие", "серые": "Серые", "ореховые": "Ореховые"}
    skin_names = {"светлая": "Светлая", "средне-светлая": "Средне-светлая", "оливковая": "Оливковая", "смуглая": "Смуглая", "тёмная": "Тёмная"}
    color_names = {"весна": "🌸 Весна", "лето": "☀️ Лето", "осень": "🍁 Осень", "зима": "❄️ Зима"}
    style_names = {"романтичный": "🌸 Романтичный", "деловой": "💼 Деловой", "спортивный": "🏃 Спортивный", "дерзкий": "🔥 Дерзкий", "минимализм": "✨ Минимализм"}
    
    answer = (
        "✅ Анкета сохранена в базе данных! 💾\n\n"
        f"👤 Имя: {data['name']}\n"
        f"👤 Пол: {gender_names.get(data['gender'], data['gender'])}\n"
        f"💇 Волосы: {hair_names.get(data['hair'], data['hair'])}\n"
        f"👁 Глаза: {eye_names.get(data['eyes'], data['eyes'])}\n"
        f"🧴 Кожа: {skin_names.get(data['skin'], data['skin'])}\n"
        f"🎨 Цветотип: {color_names.get(data['color_type'], data['color_type'])}\n"
        f"👗 Стиль: {style_names.get(data['style'], data['style'])}\n"
        f"🌆 Город: {city_name} ✅\n\n"
        "✨ Теперь я знаю всё о тебе!\n"
        "Напиши /today, чтобы получить образ на сегодня 💫"
    )
    
    await message.answer(answer)
    await state.clear()

@dp.message(Command("today"))
async def today(message: types.Message):
    from sqlalchemy import create_engine, text
    from dotenv import load_dotenv
    import os
    import random
    import httpx
    
    load_dotenv()
    DATABASE_URL = os.getenv("DATABASE_URL")
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    
    if "+asyncpg" in DATABASE_URL:
        DATABASE_URL = DATABASE_URL.replace("+asyncpg", "")
    
    engine = create_engine(DATABASE_URL)
    
    try:
        # Получаем пользователя из БД
        with engine.connect() as conn:
            user = conn.execute(
                text("SELECT * FROM users WHERE telegram_id = :telegram_id"),
                {"telegram_id": message.from_user.id}
            ).fetchone()
            
            if not user:
                await message.answer(
                    "📝 Ты ещё не зарегистрировался!\n"
                    "Напиши /register, чтобы я узнал тебя получше 💅"
                )
                return
            
            # ============ ПОЛУЧАЕМ РЕАЛЬНУЮ ПОГОДУ ============
            city = user[9]  # город пользователя
            weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
            
            async with httpx.AsyncClient() as client:
                weather_response = await client.get(weather_url)
                
                if weather_response.status_code == 200:
                    weather_data = weather_response.json()
                    temp = round(weather_data["main"]["temp"])
                    weather_condition = weather_data["weather"][0]["main"].lower()
                    weather_description = weather_data["weather"][0]["description"]
                else:
                    # Если погода не пришла — используем заглушку
                    temp = 22
                    weather_condition = "clear"
                    weather_description = "ясно"
            
            # ============ ИЩЕМ ПОДХОДЯЩИЙ ОБРАЗ ============
            look = conn.execute(
                text("""
                    SELECT * FROM looks 
                    WHERE 
                        (gender = :gender OR gender = 'универсальный')
                        AND (hair = :hair OR hair IS NULL)
                        AND (eyes = :eyes OR eyes IS NULL)
                        AND (skin = :skin OR skin IS NULL)
                        AND (color_type = :color_type OR color_type IS NULL)
                        AND (style = :style OR style IS NULL)
                        AND (weather = :weather OR weather IS NULL)
                        AND temp_min <= :temp
                        AND temp_max >= :temp
                    ORDER BY RANDOM()
                    LIMIT 1
                """),
                {
                    "gender": user[2],  # gender
                    "hair": user[3],    # hair
                    "eyes": user[4],    # eyes
                    "skin": user[5],    # skin
                    "color_type": user[6],  # color_type
                    "style": user[7],   # style
                    "weather": weather_condition,
                    "temp": temp
                }
            ).fetchone()
            
            if not look:
                await message.answer(
                    "😅 К сожалению, я не нашёл подходящий образ для тебя.\n"
                    "Попробуй изменить параметры в анкете или напиши позже!"
                )
                return
            
            # Смайлик погоды
            weather_emojis = {
                "clear": "☀️",
                "clouds": "☁️",
                "rain": "🌧️",
                "snow": "❄️",
                "thunderstorm": "⛈️",
                "drizzle": "🌦️",
                "mist": "🌫️"
            }
            weather_emoji = weather_emojis.get(weather_condition, "🌤️")
            
            # Формируем красивый ответ
            answer = (
                f"✨ {user[2]}, твой образ на сегодня!\n\n"
                f"🌤 Погода в {city}: {weather_emoji} +{temp}°C, {weather_description}\n\n"
                f"💄 Макияж:\n{look[10]}\n\n"
                f"👗 Одежда:\n{look[11]}\n\n"
                f"🧴 Уход:\n{look[12]}\n\n"
                f"💡 Совет:\n{look[13]}"
            )
            
            await message.answer(answer)
    except Exception as e:
        await message.answer(f"❌ Произошла ошибка: {str(e)}")

async def main():
    print("🤖 Бот запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
