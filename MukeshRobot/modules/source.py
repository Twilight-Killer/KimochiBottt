from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from MukeshRobot import OWNER_ID, dispatcher
from MukeshRobot import pbot as client

Mukesh = "https://telegra.ph/file/d30ac2c7f39d404823823.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Mukesh,
        caption=f"""**​ʜᴀɪ {message.from_user.mention()}.\n» ꜱᴀʏᴀ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [ᴅᴇᴠ](tg://user?id={OWNER_ID})
**» ᴠᴇʀsɪ ᴩʏᴛʜᴏɴ :** `{y()}`
**» ᴠᴇʀsɪ ʟɪʙʀᴀʀʏ :** `{o}` 
**» ᴠᴇʀsɪ ᴛᴇʟᴇᴛʜᴏɴ :** `{s}` 
**» ᴠᴇʀsɪ ᴘʏʀᴏɢʀᴀᴍ :** `{z}`

**ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴏᴡɴᴇʀ ",user_id=OWNER_ID
                    ),
                    InlineKeyboardButton(
                        "• ʀᴇᴘᴏ •",
                        url="https://t.me/DarkiezZzz",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "Rᴇᴩᴏ"
_help__ = """
 /repo  ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 
 /source ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ
"""
