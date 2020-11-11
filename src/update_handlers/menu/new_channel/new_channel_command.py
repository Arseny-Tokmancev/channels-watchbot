from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from channels_watchbot.utils import add_chat_to_update

from data.models import Chat


NEW_CHANNEL_TEXT = 'Отлично, привязываем новый канал. ' \
            'Добавьте меня в участники канала, который хотите привязать, ' \
            'и перешлите любое сообщение из канала в этот чат.'

CANCEL_TEXT = 'Отменить ❌'

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
            NEW_CHANNEL_TEXT,
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(CANCEL_TEXT, 'new_cancel')],
            ])
        )

    @app.on_callback_query(
        filters.regex('new_cancel')
    )
    def cancel_new_channel(client, update):
        chat = Chat.objects.get(id=update.message.chat.id)
        chat.wait_forward = False
        chat.save()
        update.edit_message_text(
            'Привязка канала отменена.',
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton('Всё-таки привязываем ↩', 'new_channel')]
            ])
        )

    @app.on_callback_query(
        filters.regex('new_channel')
    )
    def new_channel_callback(client, update):
        chat = Chat.objects.get(id=update.message.chat.id)
        chat.wait_forward = True
        chat.save()
        update.edit_message_text(
            NEW_CHANNEL_TEXT,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(CANCEL_TEXT, 'new_cancel')],
            ])
        )