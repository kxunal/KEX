from pymongo import MongoClient
from config import MONGO_DB_URI
import asyncio
import random
import os

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InputMediaAnimation, InputMediaPhoto
from src import app

def add_user_database(user_id: int):
    check_user = collection.find_one({"user_id": user_id})
    if not check_user:
        return collection.insert_one({"user_id": user_id})

@app.on_message(filters.command("start"))
async def start(_, m: Message):
    add_user_database(m.from_user.id)
    await m.reply_text(
        f"""ʜᴇʟʟᴏ {m.from_user.mention}! 👋 ɪ'ᴍ ʏᴏᴜʀ ᴇᴅɪᴛ ɢᴜᴀʀᴅɪᴀɴ ʙᴏᴛ 🤖, ʜᴇʀᴇ ᴛᴏ ᴍᴀɪɴᴛᴀɪɴ ᴀ ꜱᴇᴄᴜʀᴇ ᴇɴᴠɪʀᴏɴᴍᴇɴᴛ ꜰᴏʀ ᴏᴜʀ ᴅɪꜱᴄᴜꜱꜱɪᴏɴꜱ.,
        
🚫 ᴇᴅɪᴛᴇᴅ ᴍᴇꜱꜱᴀɢᴇ ᴅᴇʟᴇᴛɪᴏɴ: ɪ'ʟʟ ʀᴇᴍᴏᴠᴇ ᴇᴅɪᴛᴇᴅ ᴍᴇꜱꜱᴀɢᴇꜱ ᴛᴏ ᴍᴀɪɴᴛᴀɪɴ ᴛʀᴀɴꜱᴘᴀʀᴇɴᴄʏ.
        
📣 ɴᴏᴛɪꜰɪᴄᴀᴛɪᴏɴꜱ: ʏᴏᴜ'ʟʟ ʙᴇ ɪɴꜰᴏʀᴍᴇᴅ ᴇᴀᴄʜ ᴛɪᴍᴇ ᴀ ᴍᴇꜱꜱᴀɢᴇ ɪꜱ ᴅᴇʟᴇᴛᴇᴅ.

🌟 ɢᴇᴛ ꜱᴛᴀʀᴛᴇᴅ:
: ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
: ᴜꜱᴀɢᴇ: /editmode on/off

➡️ ᴄʟɪᴄᴋ ᴏɴ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴀᴅᴅ ᴍᴇ ᴀɴᴅ ᴋᴇᴇᴘ ᴏᴜʀ ɢʀᴏᴜᴘ ꜱᴀꜰᴇ!""",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{app.me.username}?startgroup=new")],
            [InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ 🤝", url="https://t.me/STORM_TECHH")]
        ])
    )
