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