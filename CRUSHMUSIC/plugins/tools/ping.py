from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from config import *
from  CRUSHMUSIC import app
from  CRUSHMUSIC.core.call import PRASHANT
from  CRUSHMUSIC.utils import bot_sys_stats
from  CRUSHMUSIC.utils.decorators.language import language
from  CRUSHMUSIC.utils.inline import supp_markup
from config import BANNED_USERS


@app.on_message(filters.command("ping", prefixes=["/"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_video(
        video="https://envs.sh/ysj.mp4",
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await PRASHANT.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
