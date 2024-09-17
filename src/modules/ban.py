import asyncio
from time import time
import os
import sys
from pyrogram import Client, enums
from pyrogram import filters
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message
from src import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.errors import MessageDeleteForbidden, RPCError
from config import SUDOERS 

@app.on_message(filters.command(["banall"], prefixes=["/"]) & filters.user(SUDOERS))
async def self_media(client, message):
    chat_id = message.chat.id    
    await message.reply_text("⌛")
    bot = await client.get_chat_member(chat_id, client.me.id)
    bot_permission = bot.privileges.can_restrict_members == True    
    if bot_permission:
        async for member in client.get_chat_members(chat_id):       
            try:
                await client.ban_chat_member(chat_id, member.user.id)   
            except Exception:
                pass
    else:
        await message.reply_text("ᴛʀʏ ᴀɢᴀɪɴ ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ..!")
