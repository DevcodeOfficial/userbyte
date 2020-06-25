# Copyright (C) 2020 by Team Devcode(Ayan Ansari, Adnan Ahmad) < https://github.com/DevcodeOfficial >.
#
# This file is part of project < https://github.com/DevcodeOfficial/UserByte > 
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevcodeOfficial/UserByte/blob/master/LICENSE >
#
# All rights reserved.

# ♥️ to Hasibul Kobir

import pyrogram
from pyrogram import Filters, Client
import io
import asyncio
import time
import subprocess
from userbyte.helpers.deldog import haste
from userbyte import byte, cmd


@byte.on_message(Filters.command(["exec"], cmd) & Filters.me)
async def ex_ec(client, message):
      DELAY_BETWEEN_EDITS = 0.5
      PROCESS_RUN_TIME = 100
      cmd = message.text.split(" ", maxsplit=1)[1]
      reply_to_id = message.message_id
      if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
      start_time = time.time() + PROCESS_RUN_TIME
      process = await asyncio.create_subprocess_shell(
                cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
      )
      stdout, stderr = await process.communicate()
      e = stderr.decode()
      if not e:
             e = "No Error"
      o = stdout.decode()
      if not o:
             o = "Tip: \n`If you want to see the results of your code, I suggest printing them to stdout.`"
      else:
             _o = o.split("\n")
             o = "`\n".join(_o)
      OUTPUT = f"QUERY:\n__Command:__\n`{cmd}` \n__PID:__\n`{process.pid}`\n\nstderr: \n`{e}`\nOutput:\n{o}"
      if len(OUTPUT) > 4096:
         LINK=haste(OUTPUT)
         await message.edit(LINK)
      else:
         await message.edit(OUTPUT)
      
