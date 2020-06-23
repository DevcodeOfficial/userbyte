from userbyte import logger

def __list_all_modules():
    from os.path import dirname, basename, isfile
    import glob

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    return all_modules


ALL_MODULES = sorted(__list_all_modules())
logger.info("Succefully Loaded Plugins: {}\n".format(" × ".join(ALL_MODULES)))

from userbyte import byte, cmd
from pyrogram import Filters, Message

@byte.on_message(Filters.command("help", cmd) & Filters.me)
async def _alive(byte, message):
	ALL_MODULES = sorted(__list_all_modules())
	await message.edit("**⚙ Available Plugins : {}**".format(" × ".join(ALL_MODULES)))
