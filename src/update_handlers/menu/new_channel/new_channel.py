from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from channels_watchbot.utils import add_chat_to_update

def register(app):
    @app.on_message(
        (filters.private | filters.group) &
        add_chat_to_update &
        filters.text &
        filters.create(lambda a,b,x: x.data_chat.wait_time)
    )
    def needed_time(client, message):
        try:
            period = int(message.text)
        except Exception as e:
            print(e)
            client.send_message(
                message.chat.id,
                'Отправьте, пожалуйста, число.'
            )
            return
        channel = message.data_chat.channel_set.get(id=message.data_chat.current_channel_id)
        channel.period = period
        channel.save()
        message.data_chat.wait_time = False
        message.data_chat.save()

        title = channel.get_input_channel(client).title
        client.send_message(
            message.chat.id,
            'Время сохранено! '
            'Теперь я буду отправлять Вам уведомления, '
            f'если канал **{title}** '
            f'не будет отправлять сообщения в течение **{period}** минут.'
        )
