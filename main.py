from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from environs import Env

from keyboards import send_notification_kb, answer_kb
from readgsheet import get_notifications
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.base import JobLookupError

env = Env()
env.read_env()


TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN')
MANAGER_TG_ID = env.str('MANAGER_TG_ID')

bot = Bot(TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
scheduler = AsyncIOScheduler()
scheduler.start()


@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    await message.answer(
        'Тестовый бот', reply_markup=send_notification_kb)


async def time_is_up(employee_tg_id):
    await bot.send_message(
        MANAGER_TG_ID,
        f'Сотрудник {employee_tg_id} не ответил вовремя!'
    )
    await bot.send_message(
        employee_tg_id,
        'Время для ответа вышло!'
    )
    scheduler.remove_job(str(employee_tg_id))


@dp.callback_query_handler(Text('send_notification'))
async def send_notification(callback_query: types.CallbackQuery):
    await callback_query.message.edit_reply_markup()
    notifications = await get_notifications()
    for notification in notifications:
        await bot.send_message(
            notification['tg_id'],
            f'{notification["text"]}\n'
            f'время для ответа {notification["answer_time"]} сек',
            reply_markup=answer_kb
        )
        scheduler.add_job(
            time_is_up,
            'interval',
            [notification['tg_id']],
            seconds=notification['answer_time'],
            id=str(notification['tg_id'])
        )
    await callback_query.answer()


@dp.callback_query_handler(Text('done'))
async def done_button_handler(callback_query: types.CallbackQuery):
    await callback_query.message.edit_reply_markup()

    try:
        scheduler.remove_job(callback_query.from_user.id)
        await bot.send_message(
            MANAGER_TG_ID,
            'Сотрудник ответил: Выполнено!'
        )
    except JobLookupError:
        await callback_query.message.answer('Время для ответа вышло!')
    await callback_query.answer()


@dp.callback_query_handler(Text('not_done'))
async def not_done_button_handler(callback_query: types.CallbackQuery):
    await callback_query.message.edit_reply_markup()
    try:
        scheduler.remove_job(str(callback_query.from_user.id))
        await bot.send_message(
            MANAGER_TG_ID,
            'Сотрудник ответил: Не выполнено!'
        )
    except JobLookupError:
        await callback_query.message.answer('Время для ответа вышло!')
    await callback_query.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
