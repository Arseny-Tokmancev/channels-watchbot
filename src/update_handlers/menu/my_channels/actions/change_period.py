from pyrogram import filters

from data.models import Chat


def register(app):
    @app.on_callback_query(
        filters.regex('change_period ')
    )
    def change_period(client, update):
        chat = Chat.objects.get(id=update.message.chat.id)
        chat.current_channel_id = int(update.data.split(' ')[1])
        chat.wait_time = True
        chat.save()
        update.edit_message_text('Введите число, как часто сообщения должны отправляться в канал, в минутах.')