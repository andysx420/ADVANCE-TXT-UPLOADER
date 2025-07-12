# Don't Remove Credit Tg - @AndySX25

from os import environ

API_ID = int(environ.get("API_ID")) #Replace with your api id
API_HASH = environ.get("API_HASH") #Replace with your api hash
BOT_TOKEN = environ.get("BOT_TOKEN") #Replace with your bot token

if not all([API_ID, API_HASH, BOT_TOKEN]):
    raise EnvironmentError("❌ Please set all required environment variables: API_ID, API_HASH, BOT_TOKEN")
