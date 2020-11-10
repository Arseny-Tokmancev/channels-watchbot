from pyrogram import filters

from data.models import Channel


def register(app):
    @app.on_callback_query(
        filters.regex('delete ')
    )
    def delete_channel(client, update):
        try:
            channel_id = int(update.data.split(' ')[1])
            Channel.objects.get(id=channel_id).delete()
            update.answer('Привязка к каналу удалена.')
            update.message.delete()
        except Exception as e:
            print(e)
            update.answer('Произошла ошибка при попытке удаления.')