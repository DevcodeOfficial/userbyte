from pyrogram import Client, Filters, InlineKeyboardMarkup
from userbyte import cmd, byte, set_help
from userbyte.helpers.msg_types import get_file_id, get_note_type, Types
from userbyte.helpers.string_handling import format_welcome_caption
from userbyte.config import CHANNEL_ID, DB_URI
if DB_URI is not None:
    import userbyte.sql.welcome as sql
    
set_help('welcome', '🎉 **Welcome New Users\n\n👉 Save : ** `.savewelcome` __(reply to any media/text/gif/sticker to save a new welcome message)__\n\n👉 **Clear :** `.clearwelcome` __(use this command to clear current welcome)__')
TG_URI = int(CHANNEL_ID)
MAX_MESSAGE_LENGTH = 4096

async def delete_prev_welcome(message, previous_w_message_id):
    await message._client.delete_messages(
        chat_id=message.chat.id,
        message_ids=previous_w_message_id,
        revoke=True
    )


async def get_note_with_command(message):
    note_d = sql.get_current_welcome_settings(message.chat.id)
    if not note_d:
        return
    #
    note_message_id = int(note_d.f_mesg_id)
    note_message = await message._client.get_messages(
        chat_id=TG_URI,
        message_ids=note_message_id,
        replies=0
    )
    n_m = message
    # 🥺 check two conditions 🤔🤔
    for c_m in message.new_chat_members:
        if note_d.should_clean_welcome:
            await delete_prev_welcome(message, int(note_d.previous_welcome))
        if note_message.media:
            _, file_id = get_file_id(note_message)
            caption = note_message.caption
            if caption:
                caption = format_welcome_caption(caption.html, c_m)
            n_m = await n_m.reply_cached_media(
                file_id=file_id,
                caption=caption,
                parse_mode="html",
                reply_markup=note_message.reply_markup
            )
        else:
            caption = note_message.text
            if caption:
                caption = format_welcome_caption(caption.html, c_m)
            disable_web_page_preview = True
            if "gra.ph" in caption or "youtu" in caption:
                disable_web_page_preview = False
            n_m = await n_m.reply_text(
                text=caption,
                disable_web_page_preview=disable_web_page_preview,
                parse_mode="html",
                reply_markup=note_message.reply_markup
            )
        #
        sql.update_previous_welcome(message.chat.id, n_m.message_id)


@byte.on_message(Filters.new_chat_members)
async def new_welcome(_, message):
    await get_note_with_command(message)


@byte.on_message(Filters.command(".savewelcome", cmd))
async def save_wlcm(client, message):
    await message.edit('`🥳 Saving Welcome....`')
    if len(message.command) == 2:
        chat_id = message.chat.id
        note_message_id = int(message.command[1])
        sql.add_welcome_setting(
            chat_id,
            True,
            0,
            note_message_id
        )
        await message.edit('✅ New Welcome Message Saved')
    elif message.reply_to_message and message.reply_to_message.reply_markup is not None:
        fwded_mesg = await message.reply_to_message.forward(
            chat_id=TG_URI,
            disable_notification=True
        )
        chat_id = message.chat.id
        note_message_id = fwded_mesg.message_id
        sql.add_welcome_setting(
            chat_id,
            True,
            0,
            note_message_id
        )
        await message.edit('✅ New Welcome Message Saved')
    else:
        note_name, text, data_type, content, buttons = get_note_type(message, 1)

        if data_type is None:
            await message.edit("🙄 Welcome Text Is Empty")
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
            sql.add_welcome_setting(
                chat_id,
                bool(note_name),
                0,
                note_message_id
            )
            await message.edit('✅ New Welcome Message Saved')
            
@byte.on_message(Filters.command(".clearwelcome", cmd))
async def clear_wlcm(_, message):
    await message.edit('`🚫 Deleting Current Welcome....`')
    sql.rm_welcome_setting(message.chat.id)
    await message.edit('🗑 Welcome Message Deleted')
