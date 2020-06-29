from pyrogram import Client, Filters, InlineKeyboardMarkup
from userbyte import cmd, byte
from userbyte.config import DB_URI
from userbyte.helpers.msg_types import get_note_type, Types, get_file_id

TG_URI = -1001436299899

if DB_URI is not None:
    import userbyte.sql.notes as sql

@byte.on_message(Filters.command("save", cmd))
async def save_note(client, message):
	await message.edit("`🤟 Saving Note......`")
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
	    await message.edit(
	        f"👍 Added **{note_name}** to notes.\n👉 Get it with `.get {note_name}`  |  `#{note_name}`"
	        # f"<a href='https://'>{message.chat.title}</a>"
	    )
	else:
	    note_name, text, data_type, content, buttons = get_note_type(message, 2)
	
	    if data_type is None:
	        await message.edit("🙄 There Is No Note Text")
	        return
	
	    if not note_name:
	        await message.edit("😕 There Is No Note Name")
	        return
	
	    # construct message using the above parameters
	    fwded_mesg = None
	    rep_ly_markup = None
	    if len(buttons) > 0:
	        rep_ly_markup = InlineKeyboardMarkup(buttons)
	    if data_type in (Types.BUTTON_TEXT, Types.TEXT):
	        fwded_mesg = await client.send_message(
	            chat_id=TG_URI,
	            text=text,
	            parse_mode="md",
	            disable_web_page_preview=True,
	            disable_notification=True,
	            reply_to_message_id=1,
	            reply_markup=rep_ly_markup
	        )
	    elif data_type is not None:
	        fwded_mesg = await client.send_cached_media(
	            chat_id=TG_URI,
	            file_id=content,
	            caption=text,
	            parse_mode="md",
	            disable_notification=True,
	            reply_to_message_id=1,
	            reply_markup=rep_ly_markup
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
	        await message.edit(
	            f"👍 Added **{note_name}** to notes.\nGet it with `.get {note_name}`, `#{note_name}`"
	            # f"<a href='https://'>{message.chat.title}</a>"
	        )
	    else:
	        await message.edit("😖 Something Went Wrong")
	        
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
        
@byte.on_message(Filters.command("get", cmd))
async def get_note(_, message):
    note_name = " ".join(message.command[1:])
    await get_note_with_command(message, note_name)

@byte.on_message(Filters.regex(pattern=r"#(\w+)"))
async def get_hash_tag_note(_, message):
    note_name = message.matches[0].group(1)
    await get_note_with_command(message, note_name)
