from pyrogram import Client
from threading import Thread

from schedule import start_scheduler


def main(api_id, api_hash, bot_token):
    Thread(target=start_scheduler, args=(api_id, api_hash, bot_token, )).start()

    bot = Client('bot', api_id, api_hash, bot_token=bot_token)

    from channels import register as channels_register
    channels_register(bot)

    from start import register as start_register
    start_register(bot)

    bot.run()
