from pyrogram import Client
import os
from dotenv import load_dotenv
load_dotenv()

api_id = os.getenv("APP_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


app.run()