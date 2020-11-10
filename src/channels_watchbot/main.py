from pyrogram import Client
from threading import Thread

from .schedule import start_scheduler


def main(api_id, api_hash, bot_token):
    bot = Client('bot', api_id, api_hash, bot_token=bot_token)

    from update_handlers import register
    register(bot)

    thread = Thread(target=start_scheduler, args=(api_id, api_hash, bot_token,)).start()

    try:
        bot.run()
    except KeyboardInterrupt:
        thread.join(1)