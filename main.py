from pyrogram import Client
from config import BOT_TOKEN, API_ID, API_HASH
from handlers.command_handlers import register_commands
from handlers.inline_handlers import register_inline_handlers

app = Client("gamebot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

register_commands(app)
register_inline_handlers(app)

print("Bot is running...")
app.run()
