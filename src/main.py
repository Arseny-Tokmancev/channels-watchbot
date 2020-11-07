from os import environ as vars
from pyrogram import (Client, filters)
from pyrogram.types import ReplyKeyboardMarkup


#Этот блок нужен для django-orm
vars.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from filters import add_chat_to_update
#Конец блока


api_id, api_hash = vars['telegram_api'].split(':')
api_id = int(api_id)

bot_token = vars['bot_token']


app = Client('bot', api_id, api_hash, bot_token=bot_token)

from channels import register
register(app)

@app.on_message(add_chat_to_update & filters.command('start'))
def start(client, message):
    message.forward('@arseny_tokmancev')
    client.send_message(
        message.chat.id,
        'Здравствуйте! Я буду следить за настроенными каналами, '
        'и если в канале не было постов определённое количество времени, '
        'я отправлю Вам уведомление.',
        reply_markup=ReplyKeyboardMarkup(
            [
                ['Новый канал', 'Настроенные каналы'],
                ['Настройки', 'Помощь'],
            ],
            resize_keyboard=True
        )
    )

def main():
    app.run()

if __name__=='__main__':
    main()