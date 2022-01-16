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

PM_START_STICKER = "CAACAgEAAxkBAAEGuU5h3v5XAAFBZBNscH9lJfI8s5qmm5MAAsUBAAJKYnlFMGvOnsDF3wEjBA"

PM_START_TEXT = """
ʜᴇʏ sɪʀ 
ɪ ᴀᴍ ɴɪᴘᴜɴ's ᴀssɪsᴛᴀɴᴛ ʙᴏᴛ.. 
ʏᴏᴜ ᴄᴀɴ ᴄᴏɴᴛᴀᴄᴛ ɴɪᴘᴜɴ ᴏɴ ᴛʜɪs ʙᴏᴛ..
ᴍʏ ᴍᴀsᴛᴇʀ ᴡɪʟʟ ʀᴇᴘʟʏ ᴡɪᴛʜɪɴ 5 ʜᴏᴜʀs..  
ᴛʜᴀɴᴋ ʏᴏᴜ ᴅᴇᴀʀ ꜰʀɪᴇɴᴅ 
"""



IF_TEXT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
IF_CONTENT = "<b>Message from:</b> {} \n<b>Name:</b> {}"


START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ɪɴʙᴏx',url='https://t.me/NiupunDinujaya'),
        InlineKeyboardButton('ɪɴʙᴏx',url='https://t.me/NipunDinujayaOffline'),
        InlineKeyboardButton('ɪɴʙᴏx',url='https://t.me/MrImSantha')
        ],
        [
        InlineKeyboardButton('ᴍᴏʀᴇ ᴀʙᴏᴜᴛ',url='https://t.me/AboutSantha/2'),
        InlineKeyboardButton('ᴡᴇʙsɪᴛᴇ',url='https://telegra.ph/file/7d5ce36a275474f38c418.jpg')
        ],
        [
        InlineKeyboardButton('➕ ᴀᴅᴅ ᴛᴏ ɢʀᴏᴜᴘ ➕',url='http://t.me/TheNiupunDinujaya_Bot?startgroup=true')
        ]]
)

@KINGAMDA.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_sticker(
        PM_START_STICKER,
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
