from django.db import models

class Chat(models.Model):
    id = models.IntegerField(primary_key=True)
    wait_forward = models.BooleanField(default=False)

class Channel(models.Model):
    id = models.IntegerField(primary_key=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)