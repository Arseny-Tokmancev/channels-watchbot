import asyncio
from pyrogram import filters
from pyrogram.raw.functions.messages import EditMessage

from .show_channel import show_channel

from data.models import Channel


def register(app):
    @app.on_callback_query(
        # (filters.private | filters.group) &
        # filters.incoming &
        # add_chat_to_update &
        filters.regex('choose_channel ')
    )
    def choose_channel(client, update):
        channel = Channel.objects.get(id=int(update.data.split(' ')[1]))
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