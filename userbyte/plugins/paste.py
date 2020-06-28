import pyrogram
from pyrogram import Filters
from userbyte import byte, cmd

@byte.on_message(Filters.command('paste', cmd) & Filters.me)

async def peste(byte, message):
	replied = message.reply_to_message
	if replied.document:
		text = download_media(replied.document)
		await byte.send_document(text)
