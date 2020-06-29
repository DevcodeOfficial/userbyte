# Copyright (C) 2020 by Team Devcode(Ayan Ansari, Adnan Ahmad) < https://github.com/DevcodeOfficial >.
#
# This file is part of project < https://github.com/DevcodeOfficial/UserByte > 
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevcodeOfficial/UserByte/blob/master/LICENSE >
#
# All rights reserved.

import os, sys, logging, importlib, asyncio, pickledb
from pathlib import Path
from datetime import datetime
from pyrogram import Client, Filters
from userbyte.config import STRING_SESSION, API_ID, API_HASH, PRIVATE_GROUP_ID
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARN)
logger = logging.getLogger(__name__)

__version__ = '0.0.1'
__author__ = 'Team Devcode(Ayan Ansari, Adnan Ahmad)'
__source__ = 'https://github.com/devcodeofficial/userbyte'
__copyright__ = f"UserByte v{__version__} Copyright (c) 2020 {__author__}"

byte = Client(STRING_SESSION, api_id=API_ID, api_hash=API_HASH)

cmd_help = pickledb.load('helper.db', False)
get_help = cmd_help.get

def set_help(plugin_name, help_text):
	cmd_help.set(plugin_name, help_text)
	cmd_help.dump

LOGGER_GROUP = PRIVATE_GROUP_ID
LOG = True
cmd = [".","!","$"]
