from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.models import Channel, Chat
from ..show_channel import show_channel
from ..list_channel import list_channels


def register(app):
    @app.on_callback_query(
        filters.regex('delete ')
    )
    def delete_channel(client, update):
        channel_id = int(update.data.split(' ')[1])
        channel = Channel.objects.get(id=channel_id)
        input_channel = channel.get_input_channel(client)
        update.edit_message_text(
            f'Вы уверены, что хотите удалить канал **{input_channel.title}**?',
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton('Да ✅', f'yes_sure {channel_id}')],
                [InlineKeyboardButton('Нет ❌', f'not_sure {channel_id}')],
            ])
        )


    @app.on_callback_query(
        filters.regex('yes_sure ')
    )
    def sure_delete(client, update):
        chat = Chat.objects.get(id=update.message.chat.id)
        try:
            channel_id = int(update.data.split(' ')[1])
            channel = Channel.objects.get(id=channel_id)
            input_channel = channel.get_input_channel(client)
            channel.delete()
        except Exception as e:
            print(e)
            update.answer('При попытке удаления произошла ошибка')
        else:
            text, buttons = list_channels(client, chat)
            text = f'Канал **{input_channel.title}** удалён\n\n' + text
            update.edit_message_text(
                text,
                reply_markup = buttons,
            )

    @app.on_callback_query(
        filters.regex('not_sure ')
    )
    def not_sure_delete(client, update):
        channel_id = int(update.data.split(' ')[1])
        channel = Channel.objects.get(id=channel_id)
        update.answer('Удаление отменено')
        text, buttons = show_channel(client, channel)
        update.edit_message_text(
            text,
            reply_markup = buttons
        )