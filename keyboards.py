from aiogram import types

send_notification_kb = types.InlineKeyboardMarkup()

send_buttons = [
        types.InlineKeyboardButton(
            'Выслать напоминание',
            callback_data='send_notification'
        )
    ]

send_notification_kb.add(*send_buttons)


answer_kb = types.InlineKeyboardMarkup()

answer_buttons = [
    types.InlineKeyboardButton('Выполнено', callback_data='done'),
    types.InlineKeyboardButton('Не выполнено', callback_data='not_done')
]

answer_kb.add(*answer_buttons)