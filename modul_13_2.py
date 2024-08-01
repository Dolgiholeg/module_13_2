from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7276421876:AAH99Xjc6JEbJOJDe2Mnj6rfrvdC1zF0wRQ"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(text = ['Urban', 'ff'])
async def urban_message(message):
    print('urban_message')
    await message.answer('urban_message!')

@dp.message_handler(commands = ['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Рады вас видеть в нашем боте!')

@dp.message_handler()
async  def all_message(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer(message.text.upper())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
