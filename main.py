import os
from os import error
import logging
import pyrogram
import time
from configs import Config
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
        InlineKeyboardButton('WʜᴀᴛsAᴘᴘ🧡',url='https://whatsapp.com'),
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
    
@KINGAMDA.on_message(filters.private & filters.text)
async def pm_text(bot, message):
    if message.from_user.id == Config.BOT_OWNER:
        await reply_text(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.send_message(
        chat_id=Config.BOT_OWNER,
        text=IF_TEXT.format(reference_id, info.first_name, message.text),
        parse_mode="html"
    )

@KINGAMDA.on_message(filters.private & filters.media)
async def pm_media(bot, message):
    if message.from_user.id == Config.BOT_OWNER:
        await replay_media(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.copy_message(
        chat_id=Config.BOT_OWNER,
        from_chat_id=message.chat.id,
        message_id=message.message_id,
        caption=IF_CONTENT.format(reference_id, info.first_name),
        parse_mode="html"
    )

@KINGAMDA.on_message(filters.user(Config.BOT_OWNER) & filters.text & filters.private)
async def reply_text(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.send_message(
            text=message.text,
            chat_id=int(reference_id)
        )    


@KINGAMDA.on_message(filters.user(Config.BOT_OWNER) & filters.media & filters.private)
async def replay_media(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.copy_message(
            chat_id=int(reference_id),
            from_chat_id=message.chat.id,
            message_id=message.message_id,
            parse_mode="html"
        )          
    
KINGAMDA.run()        
