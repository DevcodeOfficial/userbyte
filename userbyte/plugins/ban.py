from pyrogram import Filters
from userbyte import byte, cmd
from userbyte.helpers.admin import can_ban

@byte.on_message(Filters.command('ban', cmd) & Filters.me)
async def ban_user(byte, message):
	
	chat_id = message.chat.id
	banned_msg = "**😈 New Ban 😈**\n"
	grp_info = await byte.get_chat(chat_id)
	admin_info = message.from_user
	
	if not await can_ban(message):
		await message.edit("`🥵 Sorry you don't have enough rights to ban someone`")
	else:
		if message.reply_to_message:
		  user_id = message.reply_to_message.from_user.id
		else:
		  user_id = message.text[5:]
		  
		if not user_id:
		  await message.edit("`📌 No Valid User ID or Message Specified`")
		else:
			info = await byte.get_chat_member(chat_id, user_id)
			await byte.kick_chat_member(chat_id, user_id)
			banned_msg += f"🤴**Admin:** [{admin_info.first_name}](tg://user?id={admin_info.id})\n"
			banned_msg += f"👤**User:** [{info.user.first_name}](tg://user?id={info.user.id})\n"
			banned_msg += f"👥**Chat: {grp_info.title}**\n"
			await message.edit(banned_msg)