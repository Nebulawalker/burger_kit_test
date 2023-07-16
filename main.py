from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from environs import Env

from keyboards import send_notification_kb, answer_kb
from readgsheet import get_notifications

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


async def answer_timer(answer_time):
    #тут устанавливается задание на отсылку сообщения менеджеру, что время ответа вышло
    #
    pass


@dp.callback_query_handler(Text('send_notification'))
async def send_notification(callback_query: types.CallbackQuery):
    notifications = await get_notifications()
    for notification in notifications:
        await bot.send_message(
            notification['tg_id'],
            f'{notification["text"]}',
            reply_markup=answer_kb
        )
        await answer_timer(notification['answer_time'])
    await callback_query.answer()


@dp.callback_query_handler(Text('done'))
async def done_button_handler(callback_query: types.CallbackQuery):
    await bot.send_message(
        MANAGER_TG_ID,
        'Сотрудник ответил: Выполнено!'
    )
    #тут отменяется задание на отсылку сообщения менеджеру, что время ответа вышло, если время еще не вышло:)
    await callback_query.answer()


@dp.callback_query_handler(Text('not_done'))
async def not_done_button_handler(callback_query: types.CallbackQuery):
    await bot.send_message(
        MANAGER_TG_ID,
        'Сотрудник ответил: Не выполнено!'
    )
    #тут отменяется задание на отсылку сообщения менеджеру, что время ответа вышло, если время еще не вышло:)
    await callback_query.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
