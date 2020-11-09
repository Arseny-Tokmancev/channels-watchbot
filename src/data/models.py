from django.db import models


class Chat(models.Model):
    id = models.IntegerField(primary_key=True)
    wait_forward = models.BooleanField(default=False)
    wait_time = models.BooleanField(default=False)
    wait_for_choose_channel = models.BooleanField(default=False)
    current_channel_id = models.IntegerField(null=True, default=None)


class Channel(models.Model):
    id = models.IntegerField(primary_key=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    period = models.IntegerField(default=0)
    last_message_time = models.DateTimeField(auto_now_add=True)