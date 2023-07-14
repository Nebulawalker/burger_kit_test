from aiogram import Bot, Dispatcher, executor, types
from environs import Env
import datetime

from keyboards import send_notification_kb

env = Env()
env.read_env()


TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN')

bot = Bot(TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    await message.answer(
        'Тестовый бот', reply_markup=send_notification_kb)


async def get_notification():
    # логика для получения параметров напоминания, пока возвращает тестовые
    return {
        'tg_id': 704038777,
        'notification_text': 'Выполнено ли задание?',
        'created_at': datetime.datetime.now(),
        'answer_time': 10
    }


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
