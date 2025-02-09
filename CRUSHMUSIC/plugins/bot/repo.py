from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from  CRUSHMUSIC import app
from config import BOT_USERNAME




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
     
            [ 
            InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙᴇs✪", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
     
            [
             InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/Forever_Crush"),
             InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/Crush_Forever"),
             ],
     
             [
             #InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/Crush_Forever_Support"),          
             #InlineKeyboardButton("︎ᴍᴜsɪᴄ", url=f"https://github.com/MrDevloaper/CRUSHMUSIC"),
             ],
     
              ]
 
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://envs.sh/y9e.mp4",
        caption=start_txt,
        reply_markup=reply_markup
    )
