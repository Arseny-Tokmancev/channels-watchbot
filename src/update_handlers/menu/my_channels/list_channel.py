from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from channels_watchbot.utils import add_chat_to_update



def register(app):
    @app.on_message(
        (filters.private | filters.group) &
        add_chat_to_update &
        filters.regex('Настроенные каналы')
    )
    def my_channels(client, message):
        message.data_chat.wait_for_choose_channel = True
        message.data_chat.save()
        channel_list = []
        for channel in message.data_chat.channel_set.all().exclude(period=0):
            title = client.get_chat(channel.channel_id).title
            channel_list.append([InlineKeyboardButton(title, f'choose_channel {channel.id}')])
        if channel_list:
            text = f'Выберите канал:'
        else:
            text = 'У Вас нет привязанных каналов. Чтобы продолжить, привяжите канал.'
        client.send_message(
            message.chat.id,
            text,
            reply_markup=InlineKeyboardMarkup(channel_list),
        )