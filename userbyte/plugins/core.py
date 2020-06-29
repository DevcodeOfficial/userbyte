# Copyright (C) 2020 by Team Devcode(Ayan Ansari, Adnan Ahmad) < https://github.com/DevcodeOfficial >.
#
# This file is part of project < https://github.com/DevcodeOfficial/UserByte > 
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevcodeOfficial/UserByte/blob/master/LICENSE >
#
# All rights reserved.

# Credits : @Spechide

import os
from importlib import import_module, reload
from pathlib import Path
from pyrogram import Client, Filters
from pyrogram.client.handlers.handler import Handler
from userbyte import logger, byte, cmd, set_help

set_help('core', '📲 **Install Plugins \n\n👉 Command :** `.install (reply to any plugin)`')

@byte.on_message(Filters.command("install", cmd) & Filters.me)
async def _core(byte, message):
	await message.edit("`🕹 Trying To Install...`")
	try:
	    if message.reply_to_message is not None:
	        down_loaded_plugin_name = await message.reply_to_message.download(
	            file_name="./plugins/"
	        )
	        if down_loaded_plugin_name is not None:
	            # logger.info(down_loaded_plugin_name)
	            relative_path_for_dlpn = os.path.relpath(
	                down_loaded_plugin_name,
	                os.getcwd()
	            )
	            # logger.info(relative_path_for_dlpn)
	            path = Path(relative_path_for_dlpn)
	            module_path = ".".join(
	                path.parent.parts + (path.stem,)
	            )
	            # logger.info(module_path)
	            module = reload(import_module(module_path))
	            # https://git.io/JvlNL
	            for name in vars(module).keys():
	                # noinspection PyBroadException
	                try:
	                    handler, group = getattr(module, name).handler
	
	                    if isinstance(handler, Handler) and isinstance(group, int):
	                        client.add_handler(handler, group)
	                        logger.info(
	                            '[{}] [LOAD] {}("{}") in group {} from "{}"'.format(
	                                client.session_name,
	                                type(handler).__name__,
	                                name,
	                                group,
	                                module_path
	                            )
	                        )
	                except Exception:
	                    pass
	            await message.edit(
	                f"✔️ Plugin Successfully Installed"
	            )
	except Exception as error:
	    await message.edit(
	        f"ERROR: {error}"
	    )
