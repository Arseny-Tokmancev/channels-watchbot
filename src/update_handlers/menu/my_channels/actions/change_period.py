from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.models import Chat, Channel
from channels_watchbot.utils import add_chat_to_update
from ..show_channel import show_channel


def register(app):
    @app.on_callback_query(
        filters.regex('change_period ')
    )
    def change_period(client, update):
        chat = Chat.objects.get(id=update.message.chat.id)
        channel_id = int(update.data.split(' ')[1])
        channel = Channel.objects.get(id=channel_id)
        chat.current_channel_id = channel_id
        chat.wait_time = True
        chat.save()

        update.edit_message_text(
            f'Текущая частота отправки: **{channel.period}** минут\n'
            'Отправьте мне ответным сообщением новую частоту',
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton('Отменить ❌', f'cancel_period {channel_id}')],
            ])
        )


    @app.on_message(
        (filters.private | filters.group)
        & add_chat_to_update
        & filters.text
        & filters.create(lambda a, b, x: x.data_chat.wait_time)
        & filters.regex(r'\d+')
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

        text, buttons = show_channel(client, channel)
        text = '**Частота сохранена**\n\n' + text
        client.send_message(
            message.chat.id,
            text,
            reply_markup = buttons
        )


    @app.on_callback_query(
        filters.regex('cancel_period ')
    )
    def cancel_period(client, update):
        chat = Chat.objects.get(id=update.message.chat.id)
        channel_id = int(update.data.split(' ')[1])
        channel = Channel.objects.get(id=channel_id)
        chat.current_channel_id = channel_id
        chat.wait_time = False
        chat.save()

        update.answer('Отменено')

        text, buttons = show_channel(client, channel)
        update.edit_message_text(
            text,
            reply_markup = buttons
        )