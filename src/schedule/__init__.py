from apscheduler.schedulers.background import BlockingScheduler
from django.utils import timezone
import datetime
from pyrogram import Client

from data.models import Channel


def start_scheduler(api_id, api_hash, bot_token):
    scheduler = BlockingScheduler()
    scheduler.add_job(check_channels(api_id, api_hash, bot_token), 'interval', seconds=30)
    scheduler.start()


def check_channels(api_id, api_hash, bot_token):
    alerter = Client('alerter', api_id, api_hash, bot_token=bot_token).start()
    def handler():
        for channel in Channel.objects.all().exclude(alerts_left=0).exclude(disabled=True):
            alert_time = channel.last_message_time + datetime.timedelta(0, (channel.period * 60))
            if channel.period and timezone.now() >= alert_time:
                tg_channel = alerter.get_chat(channel.channel_id)
                alerter.send_message(
                    channel.chat.id,
                    f'**{tg_channel.title}** не постился уже {channel.period} минут. '
                )
                channel.last_message_time = timezone.now()
                channel.alerts_left -= 1
                channel.save()
    return handler
