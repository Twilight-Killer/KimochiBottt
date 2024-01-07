import requests
from .. import pbot as Mukesh,BOT_NAME,BOT_USERNAME
import time
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
@Mukesh.on_message(filters.command(["chatgpt","dmin","ask"],  prefixes=["A", ".", "/", "-", "?", "$","#","a"]))
async def chat(bot, message):
    
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/chatgpt apa itu jeruk?`")
        else:
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://mukesh-api.vercel.app/chatgpt/{a}') 
            x=response.json()["results"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f" {x}\n\n✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ  {telegram_ping} \n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{BOT_USERNAME} ", parse_mode=ParseMode.MARKDOWN)     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")

__mod_name__ = "Cʜᴀᴛɢᴘᴛ"
__help__ = """
 ᴄʜᴀᴛɢᴘᴛ ᴅᴀᴘᴀᴛ ᴍᴇɴᴊᴀᴡᴀʙ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴀɴᴅᴀ ᴅᴀɴ ᴍᴇɴᴜɴᴊᴜᴋᴋᴀɴ ʜᴀꜱɪʟɴʏᴀ

 ❍ /chatgpt  *:* ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ ᴀᴛᴀᴜ ᴍᴇᴍʙᴇʀɪᴋᴀɴ ʙᴇʙᴇʀᴀᴘᴀ ᴛᴇᴋꜱ
 
 """
