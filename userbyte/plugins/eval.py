# Copyright (C) 2020 by Team Devcode(Ayan Ansari, Adnan Ahmad) < https://github.com/DevcodeOfficial >.
#
# This file is part of project < https://github.com/DevcodeOfficial/UserByte > 
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevcodeOfficial/UserByte/blob/master/LICENSE >
#
# All rights reserved.

# ♥️ to Hasibul Kobir


import inspect
import traceback
import asyncio
import sys
import io
import pyrogram
from pyrogram import Filters, Client
from userbyte.helpers.deldog import haste, paste
from userbyte import byte, cmd, set_help

set_help('eval', '💻 **Run Python Code\n\n👉 Command :** `.eval [your code]`\n\n**👉Example :** `.eval await byte.send_poll(message.chat.id, "Userbyte is best ?", ["Yes", "No"])`')

@byte.on_message(Filters.command(["eval"],cmd) & Filters.me)
async def ev_al(client, message):
      cmd = message.text.split(" ", maxsplit=1)[1]
      reply_to_id = message.message_id
      if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
      
      old_stderr = sys.stderr
      old_stdout = sys.stdout
      redirected_output = sys.stdout = io.StringIO()
      redirected_error = sys.stderr = io.StringIO()
      stdout, stderr, exc = None, None, None
      
      try:
         await aexec(cmd, message)
      except Exception:
         exc = traceback.format_exc()
      
      stdout = redirected_output.getvalue()
      stderr = redirected_error.getvalue()
      sys.stdout = old_stdout
      sys.stderr = old_stderr
      
      evaluation = ""
      if exc:
            evaluation = exc
      elif stderr:
            evaluation = stderr
      elif stdout:
            evaluation = stdout
      else:
            evaluation = "Success"
            
      final_output = "**EVAL**: `{}` \n\n **OUTPUT**: \n`{}` \n".format(cmd, evaluation)
      if len(final_output) > 4096:
         LINK=haste(final_output)
         await message.edit(LINK)
      else:
         await message.edit(final_output)
      
      
      
      
      
async def aexec(code, message):
    exec(
        f'async def __aexec(message): ' +
        ''.join(f'\n {l}' for l in code.split('\n'))
    )
    return await locals()['__aexec'](message)

