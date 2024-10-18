import asyncio

from aiogram import *
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = ''

bot = Bot(TOKEN)
dp = Dispatcher() # dispatcher

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")

@dp.message()
async def input_handler(message: Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
