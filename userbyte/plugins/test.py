import userbyte.sql.test as sql
from userbyte import byte, cmd

@byte.on_message(Filters.command("test", cmd))
async def save_note(client, message):
	msg = message.command[1]
	sql.add_note_to_db(msg)
	await message.edit("message savd to db")
	result = sql.get_note(msg)
	await message.edit()
