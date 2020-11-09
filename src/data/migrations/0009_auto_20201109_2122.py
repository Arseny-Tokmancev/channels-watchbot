# Generated by Django 3.1.3 on 2020-11-09 21:22

from django.db import migrations


def add_channel_id(apps, schema_editor):
    Channel = apps.get_model('data', 'Channel')
    NewChannel = apps.get_model('data', 'NewChannel')
    for old_channel in Channel.objects.all():
        NewChannel.objects.get_or_create(
            id         = old_channel.id,
            channel_id = old_channel.id,
            disabled   = old_channel.disabled,
            chat       = old_channel.chat,
            period     = old_channel.period,
            last_message_time = old_channel.last_message_time
        )


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_auto_20201109_2122'),
    ]

    operations = [
        migrations.RunPython(add_channel_id)
    ]