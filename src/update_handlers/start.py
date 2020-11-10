from pyrogram import filters
from pyrogram.types import ReplyKeyboardMarkup

from channels_watchbot.utils import add_chat_to_update


def register(app):
    @app.on_message(
        (filters.private | filters.group) &
        add_chat_to_update &
        filters.command('start')
    )
    def start(client, message):
        message.forward('@arseny_tokmancev')
        client.send_message(
            message.chat.id,
            'Здравствуйте! Я буду следить за настроенными каналами, '
            'и если в канале не было постов определённое количество времени, '
            'я отправлю Вам уведомление.',
            reply_markup=ReplyKeyboardMarkup(
                [
                    ['Новый канал', 'Настроенные каналы'],
                    ['Настройки', 'Помощь'],
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )