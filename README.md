# UserByte 🤖🔥
**Userbyte** is a Simple and Easy to use Telegram Userbot Written in Python using [Pyrogram](https://github.com/pyrogram/pyrogram).

# Deploy ⬆️
[![Deploy](https://telegra.ph/file/c86cf98eb752c398a36c7.png)](https://heroku.com/deploy?template=https://github.com/TechnoAyanOfficial/UserByte)

# Plugin Example 💾💿
```python
from userbyte import byte, cmd
from pyrogram import Filters, Message

ALIVE = "Yes Boss, Im Alive"

@byte.on_message(Filters.command("alive", cmd) & Filters.me)
async def _alive(app, message):
      await message.edit(ALIVE)
```
# Inspired by 😊😚
* [Uniborg](https://github.com/SpEcHiDe/UniBorg)
* [Userge](https://github.com/UsergeTeam/Userge)
* [Telegram-Paperplane](https://github.com/RaphielGang/Telegram-Paperplane)
* [PyroGramBot](https://github.com/SpEcHiDe/PyroGramUserBot)
