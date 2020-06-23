# Copyright (C) 2020 by Team Devcode(Ayan Ansari, Adnan Ahmad) < https://github.com/DevcodeOfficial >.
#
# This file is part of project < https://github.com/DevcodeOfficial/UserByte > 
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevcodeOfficial/UserByte/blob/master/LICENSE >
#
# All rights reserved.

import sys, importlib, asyncio

from userbyte import __version__, byte, logger
from userbyte.plugins import ALL_MODULES
import pyrogram
from pyrogram import *

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("userbyte.plugins." + module_name)

async def main():
        await byte.start()
        logger.info(f"\n××××××××××××××××××××××××××××××××××××××××××××××××××××××××\n××××××××××××× Boooom Your Userbot Is Alive ×××××××××××××\n××××××××××××× And Your Bot Version is: {__version__} ×××××××××××\n××××××××××××××××××××××××××××××××××××××××××××××××××××××××\n×× Created By: Team Devcode(Ayan Ansari, Adnan Ahmad) ××\n××××××××××××××××××××××××××××××××××××××××××××××××××××××××")
        await byte.idle()
        print("\nUserbot Stopped\n")
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
