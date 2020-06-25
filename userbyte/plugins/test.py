import pyrogram
from pyrogram import Filters
import os
from userbyte import byte, cmd
from userbyte.helpers.welcome_msg import wlcm_msg
@byte.on_message(Filters.command('test', cmd) & Filters.me)
async def wlcm(byte, message):
  file = "userbyte/helpers/welcome_msg.py"
  input_str = message.command[1]
  file = open(f"{file}", "w")
  file.write(f"wlcm_msg = {input_str}")
  file.close()
  await message.edit({wlcm_msg})
  os.remove(file)
