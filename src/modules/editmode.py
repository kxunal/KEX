from pymongo import MongoClient
from config import MONGO_DB_URI
from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from src import app

DATABASE = MongoClient(MONGO_DB_URI)
DB = DATABASE["MAIN"]["delenable"]

ADMIN = []

async def group_admins(chat_id):
    admins = []
    async for member in app.get_chat_members(chat_id, filter=ChatMembersFilter.ADMINISTRATORS):
        admins.append(member.user.id)
    return admins

def check_groups_enable(group_id: int):
    return DB.find_one({"group_id": group_id}) is not None

def add_group_enable(group_id: int):
    if not check_groups_enable(group_id):
        DB.insert_one({"group_id": group_id})

def remove_group_enable(group_id: int):
    if check_groups_enable(group_id):
        DB.delete_one({"group_id": group_id})

@app.on_message(filters.command("editmode"))
async def editfunctions(_, message):
    group_admin = await group_admins(message.chat.id)
    if message.from_user.id not in group_admin:
        return await message.reply("ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ.")
    
    if len(message.command) == 1:
        return await message.reply("Usᴀɢᴇ: /editmode on/off")

    status = message.command[1]
    if status == "on":
        if not check_groups_enable(message.chat.id):
            add_group_enable(message.chat.id)
            await message.reply("ᴇᴅɪᴛ ᴍᴏᴅᴇ ᴛᴜʀɴᴇᴅ ᴏɴ !")
        else:
            await message.reply("ᴇᴅɪᴛ ᴍᴏᴅᴇ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ !")
    elif status == "off":
        if check_groups_enable(message.chat.id):
            remove_group_enable(message.chat.id)
            await message.reply("ᴇᴅɪᴛ ᴍᴏᴅᴇ ᴛᴜʀɴᴇᴅ ᴏғғ !")
        else:
            await message.reply("ᴇᴅɪᴛ ᴍᴏᴅᴇ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ !")
    else:
        await message.reply("ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ. ᴛʀʏ /editmode on/off")

@app.on_edited_message(filters.text)
async def workdelete(_, message):
    if not check_groups_enable(message.chat.id):
        return

    group_admin = await group_admins(message.chat.id)
    if message.from_user.id not in group_admin:
        # Since `edit_hide` does not exist, we check if the message has been edited
        if message.edit_date:  # Check if `edit_date` is present
            await message.reply(f"{message.from_user.mention} Jᴜsᴛ ᴇᴅɪᴛᴇᴅ ᴀ ᴍᴇssᴀɢᴇ ᴛʜᴀᴛ's ᴡʜʏ I ᴅᴇʟᴇᴛᴇᴅ 🤡")
            await message.delete()  # Delete the message
