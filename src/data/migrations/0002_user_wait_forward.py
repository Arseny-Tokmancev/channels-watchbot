# Generated by Django 3.1.3 on 2020-11-07 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='wait_forward',
            field=models.BooleanField(default=False),
        ),
    ]