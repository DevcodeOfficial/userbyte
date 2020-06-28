# Copyright (C) 2020 by Team Devcode(Ayan Ansari, Adnan Ahmad) < https://github.com/DevcodeOfficial >.
#
# This file is part of project < https://github.com/DevcodeOfficial/UserByte > 
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevcodeOfficial/UserByte/blob/master/LICENSE >
#
# All rights reserved.

from userbyte import byte, cmd, set_help
from pyrogram import Filters, Message

set_help('alive', '😝 **This plugin is just for fun\n\n👉 Command :**  `.alive`')
ALIVE = """░█─░█ █▀▀ █── █── █▀▀█ 
░█▀▀█ █▀▀ █── █── █──█ 
░█─░█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀"""

@byte.on_message(Filters.command("alive", cmd) & Filters.me)
async def _alive(byte, message):
      await message.edit(ALIVE)
