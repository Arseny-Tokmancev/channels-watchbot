# Generated by Django 3.1.3 on 2020-11-09 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_delete_channel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewChannel',
            new_name='Channel',
        ),
    ]