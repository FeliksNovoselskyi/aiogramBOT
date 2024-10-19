import asyncio
import os

from aiogram import *
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

import keyboards as kb

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher() # dispatcher

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}! \nОтветь на сообщение в поле твоего ввода, для продолжения", reply_markup=kb.startsMenu)

@dp.message()
async def input_handler(message: Message):
    if message.text == "Покажи свой функционал":
        await message.answer("Отлично! Вот что я могу:")

    elif message.text == "Закончить диалог":
        await message.answer("Жаль, было бы приятно поболтать")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
