import os
from os import error
import logging
import pyrogram
import time
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

KINGAMDA = Client(
    "king-amda",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

PM_START_IMG = "https://telegra.ph/file/adf7012cd758c00642bd1.jpg"

PM_START_TEXT = """
Hᴇʏ Sɪʀ ! 
I Aᴍ Nɪᴘᴜɴs's Mᴀɴᴀɢᴇʀ Bᴏᴛ.. 
Yᴏᴜ Cᴀɴ Cᴏɴᴛᴀᴄᴛ Nɪᴘᴜɴ Oɴ Tʜɪs Bᴏᴛ..
"""

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Tᴇʟᴇɢʀᴀᴍ ❤️',url='https://t.me/NiupunDinujaya'),
        InlineKeyboardButton('WʜᴀᴛsAᴘᴘ🧡',url='https:t.me/hi'),
        InlineKeyboardButton('Tᴡɪᴛᴛᴇʀ🖤',url='https://twitter.com/Amda3King') 
        ],
        [
        InlineKeyboardButton('Gɪᴛʜᴜʙ 💚',url='https://github.com/Nipun-Manager'),
        InlineKeyboardButton('WᴇʙSɪᴛᴇ 💙',url='https://github.com/Nipun-Manager'),
        ],
        [InlineKeyboardButton('Cʀᴇᴅɪᴛs 💕', url='https://t.me/MrItzme')
        ]]
)

@KINGAMDA.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_photo(
        PM_START_IMG,
        caption=PM_START_TEXT,
        reply_markup=(START_BUTTON),
        quote=True
)
    
KINGAMDA.run()        
