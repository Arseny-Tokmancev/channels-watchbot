from pyrogram import filters
from data.models import Chat

def add_chat_to_update(me, client, update):
    chat, created = Chat.objects.get_or_create(id=update.chat.id)
    update.data_chat = chat
    return True

add_chat_to_update = filters.create(add_chat_to_update)