import pyrogram
from pyrogram import Filters
import os
from userbyte import byte, cmd

@byte.on_message(Filters.command('test', cmd) & Filters.me)
async def wlcm(byte, message):
  file = "userbyte/helpers/welcome_msg.py"
  input_str = message.command[1]
  os.remove(file)
  file = open(f"{file}", "w")
  file.write(f"wlcm_msg = {input_str}")
  file.close()
  from userbyte.helpers.welcome_msg import wlcm_msg
  await message.edit(wlcm_msg)
