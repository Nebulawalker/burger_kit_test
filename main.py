from aiogram import Bot, Dispatcher, executor, types

from environs import Env

env = Env()
env.read_env()


TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN')

bot = Bot(TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    await message.answer(f'Тестовый бот')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)