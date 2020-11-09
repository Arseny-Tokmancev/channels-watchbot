import start_django
import os
from channels_watchbot.main import main


api_id, api_hash = os.environ['telegram_api'].split(':')
api_id = int(api_id)

bot_token = os.environ['bot_token']


if __name__=='__main__':
    main(api_id, api_hash, bot_token)