from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from channels_watchbot.utils import add_chat_to_update
from data.models import Chat


def list_channels(client, chat):
    channel_list = []
    for channel in chat.channel_set.all():
        title = channel.get_input_channel(client).title
        channel_list.append([InlineKeyboardButton(title, f'choose_channel {channel.id}')])
    if channel_list:
        text = f'Выберите канал:'
    else:
        text = 'У Вас нет привязанных каналов. Чтобы продолжить, привяжите канал.'
    if channel_list:
        buttons = InlineKeyboardMarkup(channel_list)
    else:
        buttons = None
    return (
        text,
        buttons,
    )


def register(app):
    @app.on_message(
        (filters.private | filters.group) &
        add_chat_to_update &
        filters.regex('Настроенные каналы')
    )
    def my_channels(client, message):
        text, buttons = list_channels(client, message.data_chat)
        client.send_message(
            message.chat.id,
            text,
            reply_markup=buttons,
        )

    @app.on_callback_query(
        filters.regex('list_channels')
    )
    def my_channels_callback(client, update):
        chat = Chat.objects.get(id=update.message.chat.id)
        text, buttons = list_channels(client, chat)
        update.edit_message_text(
            text,
            reply_markup=buttons,
        )