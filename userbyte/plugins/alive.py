from userbyte import byte, cmd
from pyrogram import Filters, Message


ALIVE = """░█─░█ █▀▀ █── █── █▀▀█ 
░█▀▀█ █▀▀ █── █── █──█ 
░█─░█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀"""

@byte.on_message(Filters.command("alive", cmd) & Filters.me)
async def _alive(byte, message):
      await message.edit(ALIVE)
