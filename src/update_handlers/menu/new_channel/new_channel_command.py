from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from channels_watchbot.utils import add_chat_to_update

from data.models import Chat


def register(app):
    @app.on_message(
        (filters.private | filters.group) &
        add_chat_to_update &
        filters.regex('Новый канал')
    )
    def new_channel_command(client, message):
        message.data_chat.wait_forward = True
        message.data_chat.save()
        client.send_message(
            message.chat.id,
            'Отлично, привязываем новый канал. '
            'Добавьте меня в участники канала, который хотите привязать, '
            'и перешлите любое сообщение из канала в этот чат.',
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton('Отменить', 'new_cancel')],
            ])
        )

    @app.on_callback_query(
        filters.regex('new_cancel')
    )
    def cancel_new_channel(client, update):
        chat = Chat.objects.get(id=update.message.chat.id)
        chat.wait_forward = False
        chat.save()
        update.edit_message_text('Привязка канала отменена.')