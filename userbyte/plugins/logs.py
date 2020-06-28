import pyrogram
from pyrogram import Filters
from userbyte import byte, cmd
import heroku3
from userbyte.config import HEROKU_APP_NAME, HEROKU_API_KEY

@byte.on_message(Filters.command('logs', cmd) & Filters.me)
async def looogs(byte, message):
	await message.edit('`🤟 Fetching Logs.....`')
	heroku = heroku3.from_key(HEROKU_API_KEY)
	app = heroku.app(HEROKU_APP_NAME)
	
	with open('userbyte_logs.txt', 'w') as log:
		log.write(app.get_log())
		await byte.send_document(chat_id=message.chat.id, document='userbyte_logs.text', caption='😁 Here Is Your Logs File')
		await message.delete()
