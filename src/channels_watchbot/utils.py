from pyrogram import filters
from data.models import Chat

@filters.create
def add_chat_to_update(me, client, update):
    chat, created = Chat.objects.get_or_create(id=update.chat.id)
    update.data_chat = chat
    return True


def edit_message_text_with_reply_markup():
    pass