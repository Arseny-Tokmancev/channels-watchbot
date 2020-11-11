from pyrogram import filters

from chanel_watchbot.utils import add_chat_to_update

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
                'добавлен в администраторы канала. '
            )
            return
        channel, created = message.data_chat.channel_set.get_or_create(
            channel_id=message.forward_from_chat.id,
        )
        if created:
            message.data_chat.wait_forward = False
            message.data_chat.wait_time = True
            message.data_chat.current_channel_id = channel.id
            message.data_chat.save()
            client.send_message(
                message.chat.id,
                'Канал привязан. '
                'Теперь напишите, как как часто канал '
                'должен отправлять сообщения, в минутах.'
            )
        else:
            client.send_message(
                message.chat.id,
                'Этот канал уже был привязан! '
                'Привязать канал два раза невозможно. '
                'Отправьте сообщение из нового канала, пожалуйста.'
            )