# Copyright (C) 2020 by Team Devcode(Ayan Ansari, Adnan Ahmad) < https://github.com/DevcodeOfficial >.
#
# This file is part of project < https://github.com/DevcodeOfficial/UserByte > 
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevcodeOfficial/UserByte/blob/master/LICENSE >
#
# All rights reserved.

# Special Thanks to Spechide
import os
from pyrogram import Client, Filters, InlineKeyboardMarkup, InlineKeyboardButton
from userbyte import logger, cmd
from userbyte.config import DB_URI
import userbyte.sql.notes as sql
from userbyte.helpers.msg_types import get_file_id, get_note_type, Types
from userbyte.helpers.admin import is_admin

TG_URI = os.environ.get("TG_URI", "-100")
MAX_MESSAGE_LENGTH = 4096


@byte.on_message(Filters.command("savenote", cmd))
async def save_note(client, message):
    if not await is_admin:
        return
    await message.edit("`🛠 Saving Note...`")
    if message.reply_to_message and message.reply_to_message.reply_markup is not None:
        fwded_mesg = await message.reply_to_message.forward(
            chat_id=TG_URI,
            disable_notification=True
        )
        chat_id = message.chat.id
        note_name = " ".join(message.command[1:])
        note_message_id = fwded_mesg.message_id
        sql.add_note_to_db(
            chat_id,
            note_name,
            note_message_id
        )
        await message.edit(f"✅ Note **{note_name}** Saved")
    else:
        note_name, text, data_type, content, buttons = get_note_type(message)

        if data_type is None:
            await message.edit("😒 Note Text Is Empty")
            return

        if not note_name:
            await message.edit("🙄 No Note Name Found")
            return

        # construct message using the above parameters
        fwded_mesg = None
        reply_markup = None
        if len(buttons) > 0:
            reply_markup = InlineKeyboardMarkup(buttons)
        if data_type in (Types.BUTTON_TEXT, Types.TEXT):
            fwded_mesg = await client.send_message(
                chat_id=TG_URI,
                text=text,
                parse_mode="md",
                disable_web_page_preview=True,
                disable_notification=True,
                reply_to_message_id=1,
                reply_markup=reply_markup
            )
        elif data_type is not None:
            fwded_mesg = await client.send_cached_media(
                chat_id=TG_URI,
                file_id=content,
                caption=text,
                parse_mode="md",
                disable_notification=True,
                reply_to_message_id=1,
                reply_markup=reply_markup
            )

        # save to db 🤔
        if fwded_mesg is not None:
            chat_id = message.chat.id
            note_message_id = fwded_mesg.message_id
            sql.add_note_to_db(
                chat_id,
                note_name,
                note_message_id
            )
            await message.edit(f"✅ Note **{note_name}** Saved")
        else:
            await message.edit("🥺 This Might Be An Error")
            
            
@byte.on_message(Filters.command("clear", cmd))
async def clear_note(_, message):
    if not await is_admin:
    	return
    await message.edit("`🚫 Processing...`")
    note_name = " ".join(message.command[1:])
    sql.rm_note(message.chat.id, note_name)
    await status_message.edit_text(
        f"📵 Note **{note_name}** Deleted")
        
        
async def get_note_with_command(message, note_name):
    note_d = sql.get_note(message.chat.id, note_name)
    if not note_d:
        return
    note_message_id = note_d.d_message_id
    note_message = await message._client.get_messages(
        chat_id=TG_URI,
        message_ids=note_message_id,
        replies=0
    )
    n_m = message
    if message.reply_to_message:
        n_m = message.reply_to_message
    # 🥺 check two conditions 🤔🤔
    if note_message.media:
        _, file_id = get_file_id(note_message)
        caption = note_message.caption
        if caption:
            caption = caption.html
        await n_m.reply_cached_media(
            file_id=file_id,
            caption=caption,
            parse_mode="html",
            reply_markup=note_message.reply_markup
        )
    else:
        caption = note_message.text
        if caption:
            caption = caption.html
        disable_web_page_preview = True
        if "gra.ph" in caption or "youtu" in caption:
            disable_web_page_preview = False
        await n_m.reply_text(
            text=caption,
            disable_web_page_preview=disable_web_page_preview,
            parse_mode="html",
            reply_markup=note_message.reply_markup
        )
        
        
@byte.on_message(Filters.command(["getnote", "get"], cmd))
async def get_note(_, message):
    note_name = " ".join(message.command[1:])
    await get_note_with_command(message, note_name)


@byte.on_message(Filters.regex(pattern=r"#(\w+)"))
async def get_hash_tag_note(_, message):
    note_name = message.matches[0].group(1)
    await get_note_with_command(message, note_name)
        
        
@byte.on_message(Filters.command("list", cmd))
async def list_note(_, message):
    await message.edit("`🔎 Checking...`")

    note_list = sql.get_all_chat_notes(message.chat.id)

    msg = "<b>Notes in {}:</b>\n".format("the current chat")
    msg_p = msg

    for note in note_list:
        note_name = " - {}\n".format(note.name)
        if len(msg) + len(note_name) > MAX_MESSAGE_LENGTH:
            await message.reply_text(msg)
            msg = ""
        msg += note_name

    if msg == msg_p:
        await message.edit("😞 No Note Found In This Chat ")

    elif len(msg) != 0:
        await message.reply_text(msg)
        await message.delete()
