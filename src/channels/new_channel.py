from pyrogram import filters

from filters import add_chat_to_update

def register(app):
    @app.on_message(add_chat_to_update & filters.regex('Новый канал'))
    def new_channel_command(client, message, matches = None):
        message.data_chat.wait_forward = True
        message.data_chat.save()
        client.send_message(
            message.chat.id,
            'Отлично, привязываем новый канал. '
            'Добавьте меня в участники канала, к которому хотите меня привязать, '
            'и перешлите любое сообщение из этого канала в этот чат.'
        )

    def is_waiting_forward(me, client, update):
        return update.data_chat.wait_forward

    @app.on_message(add_chat_to_update & filters.text & filters.forwarded & filters.create(is_waiting_forward))
    def forwarded_message(client, message):
        message.data_chat.channel_set.create(id=message.forward_from_chat.id)
