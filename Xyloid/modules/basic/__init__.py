import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Kazu"])

async def join(client):
    try:
        await client.join_chat("Xyloidsupport")
        await client.join_chat("pscsb0yz")
        await client.join_chat("ShicyyXCode")
        await client.join_chat("kynansupport")
    except BaseException:
        pass
