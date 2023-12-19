# Don't Remove Credit @movie_file_20
# Subscribe YouTube Channel For Amazing Bot @movie_file_20
# Ask Doubt on telegram @KingVJ01

import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("𝖡𝗎𝖽𝖽𝗒 𝖨 𝖺𝗆 𝖠𝗅𝗂𝗏𝖾 :) 𝖧𝗂𝗍 /start.\n\n𝖧𝗂𝗍 /group_rule 𝖥𝗈𝗋 Group Rules\n\n𝖧𝗂𝗍 /ping 𝖳𝗈 𝖢𝗁𝖾𝖼𝗄 𝖡𝗈𝗍 𝖯𝗂𝗇𝗀 😉")

@Client.on_message(filters.command("group_rule", CMD))
async def check_alive(_, message):
    await message.reply_text("♨️ 𝗚𝗥𝗢𝗨𝗣 𝗥𝗨𝗟𝗘𝗦 ♨️\n\n🔹 Sᴇᴀʀᴄʜ Mᴏᴠɪᴇ Wɪᴛʜ Cᴏʀʀᴇᴄᴛ Sᴘᴇʟʟɪɴɢ :\n› ᴀᴠᴀᴛᴀʀ 2009 ✅\n› ᴀᴠᴀᴛᴀʀ ʜɪɴᴅɪ ✅\n› ᴀᴠᴀᴛᴀʀ ᴍᴏᴠɪᴇ ❌\n› ᴀᴠᴀᴛᴀʀ ʜɪɴᴅɪ ᴅᴜʙʙᴇᴅ..❌\n\n🔹Sᴇᴀʀᴄʜ Wᴇʙ Sᴇʀɪᴇs Iɴ ᴛʜɪs Fᴏʀᴍᴀᴛᴇ : \n› ᴠɪᴋɪɴɢs S01 ✅\n› ᴠɪᴋɪɴɢs S01E01 ✅\n› ᴠɪᴋɪɴɢs S01 ʜɪɴᴅɪ ✅\n› ᴠɪᴋɪɴɢs S01 ʜɪɴᴅɪ ᴅᴜʙʙ. ❌\n› ᴠɪᴋɪɴɢs sᴇᴀsᴏɴ 1 ❌\n› ᴠɪᴋɪɴɢs ᴡᴇʙ sᴇʀɪᴇs❌ \n🔹 ᴅᴏɴ'ᴛ ᴅᴏ ᴀɴʏ sᴇʟғ ᴘʀᴏᴍᴏᴛɪᴏɴ.\n\n🔹 ᴅᴏɴ'ᴛ sᴇɴᴅ ᴀɴʏ ᴋɪɴᴅ ᴏғ ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ ᴅᴏᴄᴜᴍᴇɴᴛs, ᴜʀʟ ᴇᴛᴄ..\n\n🔹 ᴅᴏɴ'ᴛ ʀᴇǫᴜᴇsᴛ ᴀɴʏ ᴛʜɪɴɢs ᴏᴛʜᴇʀ ᴛʜᴀɴ ᴍᴏᴠɪᴇ sᴇʀɪᴇs ᴀɴɪᴍᴇs..\n\n⚙️ 𝖭ᴏᴛᴇ :- 𝖠ʟʟ ᴍᴇ𝗌𝗌ᴀɢᴇ𝗌 ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇᴅ ᴀғᴛᴇʀ 𝟷𝟶 ᴍɪɴᴜᴛᴇ𝗌 ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪ𝗌𝗌ᴜᴇ𝗌.")

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"🏓 ᴘɪɴɢ:\n{time_taken_s:.3f} ms")
