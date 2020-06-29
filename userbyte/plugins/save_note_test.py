from pyrogram import Client, Filters, InlineKeyboardMarkup
from userbyte import cmd, DB_URI, byte
from userbyte.helpers.admin import admin_check
from userbyte.msg_types import get_note_type, Types

TG_URI = -100

if DB_URI is not None:
    import userbyte.sql.notes as sql

@byte.on_message(Filters.command("save", cmd))
async def save_note(client, message):
	is_admin = await admin_check(message)
	if not is_admin:
	    return
	await message.edit('`saving note...`')
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
	        f"note <u>{note_name}</u> added"
	        # f"<a href='https://'>{message.chat.title}</a>"
	    )
	else:
	    note_name, text, data_type, content, buttons = get_note_type(message, 2)
	
	    if data_type is None:
	        await message.edit("🤔 maybe note text is empty")
	        return
	
	    if not note_name:
	        await message.edit("no note name found")
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
	        await message.edit(
	            f"note <u>{note_name}</u> added"
	            # f"<a href='https://'>{message.chat.title}</a>"
	        )
	    else:
	        await message.edit("🥺 this might be an error 🤔")
