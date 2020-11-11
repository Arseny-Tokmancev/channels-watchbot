from pyrogram import filters

from channels_watchbot.utils import add_chat_to_update

from ..my_channels.show_channel import show_channel

def register(app):
    @app.on_message(
        (filters.private | filters.group) &
        add_chat_to_update &
        filters.forwarded &
        filters.create(lambda a, b, x: x.data_chat.wait_forward)
    )
    def forwarded_message(client, message):
        try:
            chat = client.get_chat(message.forward_from_chat.id)
            assert (chat.type == 'channel')
            assert (client.get_chat_member(chat.id, 'me').status == 'administrator')
        except Exception as e:
            print(e)
            client.send_message(
                message.chat.id,
                'Для продолжения бот должен быть '
                'добавлен в администраторы канала.💂'
            )
            return
        channel, created = message.data_chat.channel_set.get_or_create(
            channel_id=message.forward_from_chat.id,
        )
        message.data_chat.wait_forward = False
        message.data_chat.current_channel_id = channel.id
        message.data_chat.save()

        text, buttons = show_channel(client, channel)
        if created:
            text = '**Канал привязан**\n\n' + text
        else:
            text = '**Этот канал уже был привязан к текущему чату**\n\n' + text
        client.send_message(
            message.chat.id,
            text,
            reply_markup = buttons
        )