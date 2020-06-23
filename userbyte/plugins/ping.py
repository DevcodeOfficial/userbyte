# Copyright (C) 2020 by Team Devcode(Ayan Ansari, Adnan Ahmad) < https://github.com/DevcodeOfficial >.
#
# This file is part of project < https://github.com/DevcodeOfficial/UserByte > 
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevcodeOfficial/UserByte/blob/master/LICENSE >
#
# All rights reserved.

import pyrogram
from pyrogram import Filters
from userbyte import byte, cmd
from datetime import datetime

@byte.on_message(Filters.command('ping', cmd) & Filters.me)
async def piiing(byte, message):
      start = datetime.now()
      await message.edit("Pong!")
      end = datetime.now()
      ms = (end - start).microseconds / 1000
      await message.edit("Pong!\n{} ms".format(ms))
