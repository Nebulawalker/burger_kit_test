from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from environs import Env
import datetime

from keyboards import send_notification_kb, answer_kb


env = Env()
env.read_env()


TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN')
MANAGER_TG_ID = env.str('MANAGER_TG_ID')

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
        'text': 'Выполнено ли задание?',
        'created_at': datetime.datetime.now(),
        'answer_time': 10
    }


@dp.callback_query_handler(Text('send_notification'))
async def send_notification(callback_query: types.CallbackQuery):
    notification = await get_notification()
    await bot.send_message(
        notification['tg_id'],
        f'{notification["text"]}',
        reply_markup=answer_kb
    )
    await callback_query.answer()


@dp.callback_query_handler(Text('done'))
async def done_button_handler(callback_query: types.CallbackQuery):
    await bot.send_message(
        MANAGER_TG_ID,
        'Сотрудник ответил: Выполнено!'
    )
    await callback_query.answer()


@dp.callback_query_handler(Text('not_done'))
async def not_done_button_handler(callback_query: types.CallbackQuery):
    await bot.send_message(
        MANAGER_TG_ID,
        'Сотрудник ответил: Не выполнено!'
    )
    await callback_query.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
