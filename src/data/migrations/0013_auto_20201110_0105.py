# Generated by Django 3.1.3 on 2020-11-10 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_auto_20201110_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='alert_times',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='channel',
            name='alerts_left',
            field=models.IntegerField(default=1),
        ),
    ]