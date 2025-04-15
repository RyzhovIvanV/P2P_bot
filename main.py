import sqlite3
from aiogram import Bot, Dispatcher, types, executor
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)

# Подготовка базы данных
conn = sqlite3.connect("test.db")  # Обычно используют расширение .db для баз данных
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, user_name TEXT)")
conn.commit()  # Не забываем сохранять изменения
conn.close()


# Реакция на команду старт
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    user_name = message.from_user.username

    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("SELECT user_name FROM users")
    result = cursor.fetchall()
    conn.close()

    # Проверяем, есть ли пользователь в базе
    found = False
    for row in result:
        if str(row[0]) == str(user_name):
            found = True
            break

    if found:
        await message.answer("СВО ГОЙДА ОРЕШНИК")
    else:
        await message.answer("ИДИ НАХУЙ")


executor.start_polling(dp)