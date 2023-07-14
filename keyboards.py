from aiogram import types

send_notification_kb = types.InlineKeyboardMarkup()

send_buttons = [
        types.InlineKeyboardButton(
            'Выслать напоминание',
            callback_data='send_notification'
        )
    ]

send_notification_kb.add(*send_buttons)
