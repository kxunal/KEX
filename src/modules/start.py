from pymongo import MongoClient
from config import MONGO_DB_URI
import asyncio
import random
import os

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InputMediaAnimation, InputMediaPhoto
from src import app

@app.on_message(filters.command("start"))
async def start(_, m: Message):
    add_user_database(m.from_user.id)
    await m.reply_text(f"""ʜᴇʟʟᴏ {m.from_user.mention}! 👋 ɪ'ᴍ ʏᴏᴜʀ ᴇᴅɪᴛ ɢᴜᴀʀᴅɪᴀɴ ʙᴏᴛ 🤖, ʜᴇʀᴇ ᴛᴏ ᴍᴀɪɴᴛᴀɪɴ ᴀ ꜱᴇᴄᴜʀᴇ ᴇɴᴠɪʀᴏɴᴍᴇɴᴛ ꜰᴏʀ ᴏᴜʀ ᴅɪꜱᴄᴜꜱꜱɪᴏɴꜱ.,\n\n🚫 ᴇᴅɪᴛᴇᴅ ᴍᴇꜱꜱᴀɢᴇ ᴅᴇʟᴇᴛɪᴏɴ: ɪ'ʟʟ ʀᴇᴍᴏᴠᴇ ᴇᴅɪᴛᴇᴅ ᴍᴇꜱꜱᴀɢᴇꜱ ᴛᴏ ᴍᴀɪɴᴛᴀɪɴ ᴛʀᴀɴꜱᴘᴀʀᴇɴᴄʏ.\n\n📣 ɴᴏᴛɪꜰɪᴄᴀᴛɪᴏɴꜱ: ʏᴏᴜ'ʟʟ ʙᴇ ɪɴꜰᴏʀᴍᴇᴅ ᴇᴀᴄʜ ᴛɪᴍᴇ ᴀ ᴍᴇꜱꜱᴀɢᴇ ɪꜱ ᴅᴇʟᴇᴛᴇᴅ.\n\n🌟 ɢᴇᴛ ꜱᴛᴀʀᴛᴇᴅ:\n: ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ.\n: ᴜꜱᴀɢᴇ: /editmode on/off\n\n➡️ ᴄʟɪᴄᴋ ᴏɴ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴀᴅᴅ ᴍᴇ ᴀɴᴅ ᴋᴇᴇᴘ ᴏᴜʀ ɢʀᴏᴜᴘ ꜱᴀꜰᴇ!"""",
                         reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{app.me.username}?startgroup=new")],
        [InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ 🤝", url=f"https://t.me/STORM_TECHH")]
    ]))
