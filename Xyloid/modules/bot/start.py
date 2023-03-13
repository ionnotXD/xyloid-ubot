#Credit Bye Geez|Ram
#Thanks To All Dev


from Xyloid import app
from pyrogram import filters


@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
   await message.reply_text("Xyloid-Userbot Telah Aktif")
