# Generated by Django 3.1.3 on 2020-11-10 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_auto_20201110_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='wait_alerts',
            field=models.BooleanField(default=False),
        ),
    ]
