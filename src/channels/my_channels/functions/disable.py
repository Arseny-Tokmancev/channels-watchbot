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
            update.answer(f'Канал {"отключен" if channel.disabled else "включен"}')
            text, buttons = show_channel(client, channel)
            try:
                client.send(
                    EditMessage(
                        peer=client.resolve_peer(update.message.chat.id),
                        id=update.message.message_id,
                        reply_markup=buttons.write(),
                        **(asyncio.run(client.parser.parse(text, 'md')))
                    )
                )
            except:
                pass
        except Exception as e:
            print(e)
            update.answer(f'Произошла ошибка при попытке изменить состояние канала.')