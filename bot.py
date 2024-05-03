from pyrogram import Client, filters
from pyrogram.types import (
    MenuButtonCommands,
    BotCommand,
    BotCommandScopeChat
)

app = Client("my_bot")

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    
    commands = [
        BotCommand("start", "Start the bot"),
        BotCommand("about", "About the bot")
    ]
    await app.set_bot_commands(
        commands,
        scope=BotCommandScopeChat(chat_id=message.chat.id)
    )
    
    await app.set_chat_menu_button(
        chat_id=message.chat.id,
        menu_button=MenuButtonCommands()
    ) 
    
    await message.reply_text(
        "Hello! I'm your AI Life Coach..."
    )

@app.on_message(filters.command("about") & filters.private)
async def about(client, message):
    await message.reply_text("More about me...")


app.run()