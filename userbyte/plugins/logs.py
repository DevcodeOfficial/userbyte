import pyrogram, os , requests, heroku3
from pyrogram import Filters
from userbyte import byte, cmd, set_help
from userbyte.config import HEROKU_APP_NAME, HEROKU_API_KEY

set_help('logs', '😊 **Get Userbyte Logs \n\n👉 Command :** `.logs`')
@byte.on_message(Filters.command('logs', cmd) & Filters.me)
async def looogs(byte, message):
	await message.edit('`🤟 Fetching Logs.....`')
	heroku = heroku3.from_key(HEROKU_API_KEY)
	app = heroku.app(HEROKU_APP_NAME)
	data = app.get_log()
	
	with open('userbyte_logs.txt', 'w') as log:
		log.write(data)
		key = requests.post('https://nekobin.com/api/documents', json={"content": data}).json().get('result').get('key')
		url = f'https://nekobin.com/{key}'
		await byte.send_document(chat_id=message.chat.id, document='userbyte_logs.txt', caption=f'😁 Here is Your Logs File\n [Click Here]({url}) to View on Nekobin')
		await message.delete()
		os.remove('userbyte_logs.txt')
