"""Get info about the replied user
Syntax: .whois"""

from userbyte import byte, cmd
from pyrogram import Filters, Message
import os


@byte.on_message(Filters.command("whois", cmd))
async def who_is(byte, message):
    await message.edit("`Fetching Information`")
    if message.reply_to_message:
        from_user = message.reply_to_message.from_user
    else:
        await message.edit("📌 Reply To Any User's Message")
        return
    if from_user is not None:
        result = "<b>User Info (Fetched By Userbyte):</b>\n\n"
        result += f"🅰 First Name: <a href='tg://user?id={from_user.id}'>{from_user.first_name}</a>\n"
        result += f"🅱 Last Name: {from_user.last_name}\n"
        result += f"🕵‍♂ Username: @{from_user.username}\n"
        result += f"🤖 Is Bot: {from_user.is_bot}\n"
        result += f"✔️ Is Verified: {from_user.is_verified}\n"
        result += f"👁‍🗨 Last Seen: {from_user.status}\n"
        result += "🔗 Permanent Link To Profile: "
        result += f"<a href='tg://user?id={from_user.id}'>{from_user.first_name}</a>"
        
        if from_user.photo:
            local_user_photo = await byte.download_media(message=from_user.photo.big_file_id)
            await byte.send_photo(
            chat_id=message.chat.id,
            photo=local_user_photo,
            caption=result,
            parse_mode="html",
            disable_notification=True
            )
            os.remove(local_user_photo)
            await loading_msg.delete()
        else:
        	await loading_msg.edit(result)