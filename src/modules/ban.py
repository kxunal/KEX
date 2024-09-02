import asyncio
import logging
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantsAdmins, ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from config import SUDOERS, API_HASH, API_ID, BOT_TOKEN

# Define ban rights
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

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize the bot client but don't start it yet
Riz = TelegramClient('Riz', API_ID, API_HASH)

# List of sudo users
SUDO_USERS = [int(user_id) for user_id in SUDOERS]

# Helper function to check if the bot has admin rights
async def has_admin_rights(event):
    chat_info = await event.get_chat()
    return chat_info.admin_rights or chat_info.creator

# Function to handle /kickall command
async def kickall_handler(event):
    if event.sender_id in SUDO_USERS:
        if not event.is_group:
            await event.reply("Please use this command in a group.")
            return

        if not await has_admin_rights(event):
            await event.reply("I don't have sufficient rights to perform this action.")
            return

        await event.delete()  # Delete the triggering message
        notification_message = await Riz.send_message(event.chat_id, "⚠️ Starting to kick non-admin members...")

        # Fetch the list of admins
        admins = await Riz.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
        admins_id = [admin.id for admin in admins]

        all_users = 0
        kicked_users = 0
        async for user in Riz.iter_participants(event.chat_id):
            all_users += 1
            if user.id not in admins_id:
                try:
                    await Riz.kick_participant(event.chat_id, user.id)
                    kicked_users += 1
                    await asyncio.sleep(0.1)  # Slight delay to avoid flood limits
                except Exception as e:
                    logging.error(str(e))
                    await asyncio.sleep(0.1)

        await notification_message.edit(f"Kicked {kicked_users}/{all_users} non-admin members.")

# Function to handle /banall command
async def banall_handler(event):
    if event.sender_id in SUDO_USERS:
        if not event.is_group:
            await event.reply("Please use this command in a group.")
            return

        if not await has_admin_rights(event):
            await event.reply("I don't have sufficient rights to perform this action.")
            return

        await event.delete()  # Delete the triggering message
        notification_message = await Riz.send_message(event.chat_id, "⚠️ Starting to ban non-admin members...")

        # Fetch the list of admins
        admins = await Riz.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
        admins_id = [admin.id for admin in admins]

        all_users = 0
        banned_users = 0
        async for user in Riz.iter_participants(event.chat_id):
            all_users += 1
            if user.id not in admins_id:
                try:
                    await Riz(EditBannedRequest(event.chat_id, user.id, RIGHTS))
                    banned_users += 1
                    await asyncio.sleep(0.1)  # Slight delay to avoid flood limits
                except Exception as e:
                    logging.error(str(e))
                    await asyncio.sleep(0.1)

        await notification_message.edit(f"Banned {banned_users}/{all_users} non-admin members.")

# Main function to start the client and add event handlers
async def main():
    # Start the client
    await Riz.start(bot_token=BOT_TOKEN)
    
    # Add event handlers once the client is fully started
    Riz.add_event_handler(kickall_handler, events.NewMessage(pattern="^/kickall"))
    Riz.add_event_handler(banall_handler, events.NewMessage(pattern="^/banall"))
    
    # Keep the bot running
    print("Bot is running...")
    await Riz.run_until_disconnected()

# Run the main event loop
if __name__ == "__main__":
    asyncio.run(main())
