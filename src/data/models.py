import asyncio
from django.db import models
import pyrogram
from pyrogram.raw.functions import channels
from pyrogram.raw.types import InputPeerChannel
from pyrogram.types import Chat as PyrogramChat


class Chat(models.Model):
    wait_forward       = models.BooleanField(default=False)
    wait_time          = models.BooleanField(default=False)
    wait_alerts        = models.BooleanField(default=False)
    current_channel_id = models.IntegerField(null=True, default=None)


ALERT_TIMES = 2

class Channel(models.Model):
    channel_id     = models.IntegerField()
    alert_times    = models.IntegerField(default=ALERT_TIMES-1)
    alerts_left    = models.IntegerField(default=ALERT_TIMES)
    disabled       = models.BooleanField(default=False)
    chat           = models.ForeignKey(Chat, on_delete=models.CASCADE)
    period         = models.IntegerField(default=30)
    last_message_time = models.DateTimeField(auto_now_add=True)


    def get_input_channel(self, client):
        return client.get_chat(self.channel_id)
