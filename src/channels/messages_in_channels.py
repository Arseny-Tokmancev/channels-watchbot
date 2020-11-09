from pyrogram import filters
from django.utils import timezone

from data.models import Channel

def register(app):
    @app.on_message(filters.channel)
    def update_time(client, message):
        try:
            channel = Channel.objects.get(id=message.chat.id)
        except Exception as e:
            print(e)
        channel.last_message_time = timezone.now()
        channel.save()