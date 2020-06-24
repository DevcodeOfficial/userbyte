import pyrogram
from pyrogram import Filters
from userbyte import byte, cmd
from datetime import datetime

cmd_help = "Syntax: .ping"

@byte.on_message(Filters.command('ping', cmd) & Filters.me)
async def piiing(byte, message):
      start = datetime.now()
      await message.edit("Pong!")
      end = datetime.now()
      ms = (end - start).microseconds / 1000
      await message.edit("Pong!\n{} ms".format(ms))