from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from filters import add_chat_to_update

from data.models import Channel


def register(app):
    @app.on_message(
        (filters.private | filters.group) &
        add_chat_to_update &
        filters.regex('Настроенные каналы')
    )
    def my_channels(client, message):
        message.data_chat.wait_for_choose_channel = True
        message.data_chat.save()
        channel_list = ''
        for i, channel in enumerate(message.data_chat.channel_set.all()):
            channel_list += f'\n{i+1} {client.get_chat(channel.id).title}'
        if channel_list:
            text = f'Отправьте мне ответным сообщением номер канала, который Вы выбрали:{channel_list}'
        else:
            text = 'У Вас нет привязанных каналов. Чтобы продолжить, привяжите канал.'
        client.send_message(
            message.chat.id,
            text
        )
        print(message.data_chat.channel_set.all())


    @app.on_message(
        (filters.private | filters.group) &
        filters.incoming &
        add_chat_to_update &
        filters.regex('\d+')
    )
    def choose_channel(client, message):
        try:
            channel = message.data_chat.channel_set.all()[1-int(message.text)]
        except Exception as e:
            print(e)
            client.send_message(
                message.chat.id,
                'Отправьте число из списка.'
            )
            return
        message.data_chat.current_channel_id = channel.id
        message.data_chat.save()
        client.send_message(
            message.chat.id,
            f'Выберите действие для {client.get_chat(channel.id).title}:\n',
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton('Удалить', f'delete {channel.id}')],
            ])
        )


    @app.on_callback_query(
        filters.regex('delete ')
    )
    def delete_channel(client, update):
        try:
            channel_id = int(update.data.split(' ')[1])
            Channel.objects.get(id=channel_id).delete()
            client.send_message(
                update.message.chat.id,
                'Привязка к каналу удалена.'
            )
        except Exception as e:
            print(e)
            client.send_message(
                update.message.chat.id,
                'Произошла ошибка при попытке удаления.'
            )