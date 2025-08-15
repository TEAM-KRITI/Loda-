from pyrogram.enums import ParseMode

from IstkharMusic import app
from IstkharMusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} ɱυʂιƈ ɾҽƈσԃʂ</b>

<b>ƈԋαƚ ιԃ :</b> <code>{message.chat.id}</code>
<b>ƈԋαƚ ɳαɱҽ:</b> {message.chat.title}
<b>ƈԋαƚ υʂҽɾɳαɱҽ :</b> @{message.chat.username}

<b>υʂҽɾ ιԃ:</b> <code>{message.from_user.id}</code>
<b>ɳαɱҽ :</b> {message.from_user.mention}
<b>υʂҽɾ ɳαɱҽ :</b> @{message.from_user.username}

<b>ϙυҽɾყ :</b> {message.text.split(None, 1)[1]}
<b>ʂƚɾҽαɱƚყρҽ :</b> {streamtype}"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
