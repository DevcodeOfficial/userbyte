import pyrogram
import userbyte.sql.test as sql
from pyrogram import Filters
from userbyte import byte, cmd

@byte.on_message(Filters.command("test", cmd))
async def save_note(client, message):
	chat_id = message.chat.id
	msg = message.command[1]
	sql.add_note_to_db(chat_id, msg)
	await message.edit("message savd to db")
	result = sql.get_note(chat_id)
	await message.edit(result)
