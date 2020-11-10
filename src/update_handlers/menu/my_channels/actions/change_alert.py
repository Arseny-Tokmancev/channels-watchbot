from pyrogram import filters

from data.models import Chat
from channels_watchbot.utils import add_chat_to_update

def register(app):
    @app.on_callback_query(
        filters.regex('change_alerts ')
    )
    def change_alerts(client, update):
        chat = Chat.objects.get(id=update.message.chat.id)
        chat.current_channel_id = int(update.data.split(' ')[1])
        chat.wait_alerts = True
        chat.save()
        update.edit_message_text('Как часто нужно повторять  отправку уведомлений?')


    @app.on_message(
        (filters.private | filters.group) &
        add_chat_to_update &
        filters.text &
        filters.create(lambda a,b,x: x.data_chat.wait_alerts)
        # filters.regex('\d+')
    )
    def wait_alerts(client, message):
        print('wait_alerts')
        try:
            new_alerts = int(message.text)
        except Exception as e:
            print(e)
            client.send_message(
                message.chat.id,
                'Отправьте, пожалуйста, число.'
            )
            return
        channel = message.data_chat.channel_set.get(id=message.data_chat.current_channel_id)
        channel.alert_times = new_alerts
        channel.save()
        message.data_chat.wait_alerts = False
        message.data_chat.save()
        message.edit_text(f'Теперь уведомления повторно будут отправляться **{channel.alert_times}** раз')
