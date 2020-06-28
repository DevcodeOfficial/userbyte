from git import Repo
from pyrogram import Filters
from userbyte import byte, cmd

@byte.on_message(Filters.command('update', cmd) & Filters.me)
async def updater(byte, message):
  
  await message.edit("`Checking for updates, please wait....`")
  repo = Repo()
  off_repo = 'https://github.com/Devcodeofficial/Userbyte.git'
  branch = repo.active_branch.name
  repo.create_remote('upstream', off_repo)
  ups_rem = repo.remote('upstream')
  ups_rem.fetch(branch)
  ups_rem.pull(branch)
  await message.edit('👍 Updating Started ! Restart Me After 2 Minutes')
