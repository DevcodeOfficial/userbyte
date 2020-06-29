from pyrogram import Message
from userbyte import byte
async def is_admin(message: Message):
    check_user = await byte.get_chat_member(message.chat.id, message.from_user.id)
    user_is = check_user.status
    if user_is == "member":
        return False
    if user_is == "administrator":
        return True
    if user_is == "creator":
        return True
    return False
    
async def can_ban(message: Message):
    check_user = await byte.get_chat_member(message.chat.id, message.from_user.id)
    user_is = check_user.status
    if user_is == "member":
        return False
    if user_is == "administrator":
        banperms = check_user.can_restrict_members
        if banperms:
            return True
        return False
    return True
    
async def can_promote(message: Message):
    check_user = await byte.get_chat_member(message.chat.id, message.from_user.id)
    user_is = check_user.status
    if user_is == "member":
        return False
    if user_is == "administrator":
        add_adminperm = check_user.can_promote_members
        if add_adminperm:
            return True
        return False
    return True
    
async def can_unban(message: Message):
    check_user = await byte.get_chat_member(message.chat.id, message.from_user.id)
    user_is = check_user.status
    if user_is == "member":
        return False
    if user_is == "administrator":
        return True
    if user_is == "creator":
        return True
    return False

async def admin_check(message: Message) -> bool:
    client = message._client
    chat_id = message.chat.id
    user_id = message.from_user.id

    check_status = await client.get_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )
    admin_strings = [
        "creator",
        "administrator"
    ]
    # https://git.colinshark.de/PyroBot/PyroBot/src/branch/master/pyrobot/modules/admin.py#L69
    if check_status.status not in admin_strings:
        return False
    else:
        return True
