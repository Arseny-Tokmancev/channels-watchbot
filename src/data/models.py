from django.db import models


class Chat(models.Model):
    wait_forward       = models.BooleanField(default=False)
    wait_time          = models.BooleanField(default=False)
    wait_alerts        = models.BooleanField(default=False)
    wait_for_choose_channel = models.BooleanField(default=False)
    current_channel_id = models.IntegerField(null=True, default=None)


ALERT_TIMES = 2

class Channel(models.Model):
    channel_id     = models.IntegerField(null=False)
    alert_times    = models.IntegerField(null=False, default=ALERT_TIMES-1)
    alerts_left    = models.IntegerField(null=False, default=ALERT_TIMES)
    disabled       = models.BooleanField(default=False)
    chat           = models.ForeignKey(Chat, on_delete=models.CASCADE)
    period         = models.IntegerField(default=0)
    last_message_time = models.DateTimeField(auto_now_add=True)