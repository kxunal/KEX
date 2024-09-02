import asyncio
from telethon import events
from telethon import TelegramClient
import logging
from telethon.tl.types import ChannelParticipantsAdmins, ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from config import SUDOERS, API_HASH, API_ID, BOT_TOKEN


RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

logging.basicConfig(level=logging.INFO)

Riz = TelegramClient('Riz', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

SUDO_USERS = [int(user_id) for user_id in SUDOERS]

async def has_admin_rights(chat):
    chat_info = await chat.get_chat()
    return chat_info.admin_rights or chat_info.creator

@Riz.on(events.NewMessage(pattern="^/kickall"))
async def kickall(event):
    if event.sender_id in SUDO_USERS:
        if not event.is_group:
            reply = "ɴᴏᴏʙ !! ᴜꜱᴇ ᴛʜɪꜱ ᴄᴍᴅ ɪɴ ɢʀᴏᴜᴘ."
            await event.reply(reply)
        else:
            await event.delete()
            if not await has_admin_rights(event.chat):
                return await event.reply("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ꜱᴜꜰꜰɪᴄɪᴇɴᴛ ʀɪɢʜᴛꜱ !!")
            RiZoeL = await Riz.send_message(event.chat_id, "**ʜᴇʟʟᴏ !! ɪ'ᴍ ᴀʟɪᴠᴇ**")
            admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
            admins_id = [i.id for i in admins]
            all_users = 0
            kicked_users = 0
            async for user in event.client.iter_participants(event.chat_id):
                all_users += 1
                if user.id not in admins_id:
                    try:
                        await event.client.kick_participant(event.chat_id, user.id)
                        kicked_users += 1
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        print(str(e))
                        await asyncio.sleep(0.1)
            await RiZoeL.edit(f"⌛️")

@Riz.on(events.NewMessage(pattern="^/banall"))
async def banall(event):
    if event.sender_id in SUDO_USERS:
        if not event.is_group:
            reply = "ɴᴏᴏʙ !! ᴜꜱᴇ ᴛʜɪꜱ ᴄᴍᴅ ɪɴ ɢʀᴏᴜᴘ."
            await event.reply(reply)
        else:
            await event.delete()
            if not await has_admin_rights(event.chat):
                return await event.reply("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ꜱᴜꜰꜰɪᴄɪᴇɴᴛ ʀɪɢʜᴛꜱ !!")
            RiZoeL = await Riz.send_message(event.chat_id, "**ʜᴇʟʟᴏ !! ɪ'ᴍ ᴀʟɪᴠᴇ**")
            admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
            admins_id = [i.id for i in admins]
            all_users = 0
            banned_users = 0
            async for user in event.client.iter_participants(event.chat_id):
                all_users += 1
                if user.id not in admins_id:
                    try:
                        await event.client(EditBannedRequest(event.chat_id, user.id, RIGHTS))
                        banned_users += 1
                        await asyncio.sleep(0.1)
                    except Exception as e:
                        print(str(e))
                        await asyncio.sleep(0.1)
            await RiZoeL.edit(f"⌛️")
