import html
from pyrogram import Client as Deadpool, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from database.connections_mdb import active_connection
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup)


@Deadpool.on_message(filters.command("pin"))
async def pin(client: Deadpool, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"You are anonymous admin. Use /connect {message.chat.id} in PM")
    chat_type = message.chat.type

    if chat_type == ChatType.PRIVATE:
        grpid = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply("Make sure I'm present in your group!!", quote=True)
                return
        else:
            await message.reply_text("I'm not connected to any groups!", quote=True)
            return

    elif chat_type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        grp_id = message.chat.id
        title = message.chat.title

    else:
        return

    st = await client.get_chat_member(grp_id, userid)
    if (
            st.status != ChatMemberStatus.ADMINISTRATOR
            and st.status != ChatMemberStatus.OWNER
            and str(userid) not in ADMINS
    ):
        return
         
    if not message.reply_to_message:
        await message.reply(
            "You need to reply to a message to pin it!"
        )
        return

    pin_message_id = message.reply_to_message_id
    message_link = f"http://t.me/c/{str(grp_id).replace(str(-100), '')}/{pin_message_id}"

    if (
        len(message.command) == 1
        or (
            len(message.command) >= 2
            and message.command[1] in (
                'silent',
                'quiet'
            )
        )
    ):
        await client.pin_chat_message(
            chat_id=message.chat.id,
            message_id=pin_message_id,
            disable_notification=True
        )
        await message.reply(
            f"I have pinned [this message]({message_link})."
        )
    
    elif (
        len(message.command) >= 2
        and message.command[1] in (
            'loud',
            'notify',
            'violent'
        )
    ):
        await client.pin_chat_message(
            chat_id=message.chat.id,
            message_id=pin_message_id,
            disable_notification=False
        )
        await message.reply(
            f"I have pinned [this message]({message_link}) and notified all members."
        )
    
    elif (
        len(message.command) >= 2
    ):
        await sts.edit(
            f"'{message.command[1]}' was not recognised as a valid pin option. Please use one of: loud/violent/notify/silent/quiet"
        )



@Deadpool.on_message(filters.command('unpin'))
async def unpin(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"You are anonymous admin. Use /connect {message.chat.id} in PM")
    chat_type = message.chat.type

    if chat_type == ChatType.PRIVATE:
        grpid = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply("Make sure I'm present in your group!!", quote=True)
                return
        else:
            await message.reply_text("I'm not connected to any groups!", quote=True)
            return

    elif chat_type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        grp_id = message.chat.id
        title = message.chat.title

    else:
        return

    st = await client.get_chat_member(grp_id, userid)
    if (
            st.status != ChatMemberStatus.ADMINISTRATOR
            and st.status != ChatMemberStatus.OWNER
            and str(userid) not in ADMINS
    ):
        return
    
    if message.reply_to_message:
        pinned_message_id = message.reply_to_message_id
        message_link = f"http://t.me/c/{str(message.chat.id).replace(str(-100), '')}/{pinned_message_id}"
        await client.unpin_chat_message(
            chat_id=message.chat.id,
            message_id=pinned_message_id
        )
        await message.reply(
            f"Unpinned [this message]({message_link})."
        )
    else:
        chat_data = await client.get_chat(
            chat_id=message.chat.id
        )
        if chat_data.pinned_message:
            pinned_message_id = chat_data.pinned_message.message_id
            await client.unpin_chat_message(
                chat_id=message.chat.id,
                message_id=pinned_message_id
            )
            await message.reply(
                f"Unpinned the last pinned message."
            )
        else:
            await message.reply(
                "There are no pinned messages. What are you trying to unpin?"
            )

@Deadpool.on_message(filters.command('pinned'))
async def pinned(client, message):

    chat_id = message.chat.id
    chat_title = message.chat.title

    chat_data = await client.get_chat(
        chat_id=chat_id
    )
    if chat_data.pinned_message:
        pinned_message_id = chat_data.pinned_message.id
        message_link = f"http://t.me/c/{str(chat_id).replace(str(-100), '')}/{pinned_message_id}"
        await message.reply(
            (
                f"The pinned message in {html.escape(chat_title)} is [here]({message_link})."
            )
        )
    else:
        await message.reply(
            (
                f"There is no pinned message in {html.escape(chat_title)}."
            )
        )
