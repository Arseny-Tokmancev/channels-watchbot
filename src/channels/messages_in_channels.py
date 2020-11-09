from pyrogram import filters
from django.utils import timezone

from data.models import Channel

def register(app):
    @app.on_message(filters.channel)
    def update_time(client, message):
        for channel in Channel.objects.filter(channel_id=message.chat.id):
            channel.last_message_time = timezone.now()
            channel.alerts_left       = channel.alert_times + 1
            channel.save()