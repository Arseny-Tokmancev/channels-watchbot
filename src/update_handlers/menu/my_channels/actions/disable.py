import asyncio
from pyrogram import filters
from pyrogram.raw.functions.messages import EditMessage

from data.models import Channel
from ..show_channel import show_channel

def register(app):
    pass
    @app.on_callback_query(
        filters.regex('disable ')
    )
    def disable(client, update):
        try:
            channel_id = update.data.split(' ')[1]
            channel = Channel.objects.get(id=channel_id)
            channel.disabled = not channel.disabled
            channel.save()
            update.answer(f'Канал {"остановлен ⏸" if channel.disabled else "запущен ▶"}')
            text, buttons = show_channel(client, channel)
            update.edit_message_text(
                text,
                reply_markup = buttons
            )
        except Exception as e:
            print(e)
            update.answer('Произошла ошибка при попытке изменить состояние канала.')