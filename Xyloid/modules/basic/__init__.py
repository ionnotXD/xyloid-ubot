import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Xyloid"])

async def join(client):
    try:
        await client.join_chat("Xyloidsupport")
        await client.join_chat("pscsb0yz")
        await client.join_chat("ShicyyXCode")
        await client.join_chat("kynansupport")
        await client.join_chat("kazusupportgrp")
    except BaseException:
        pass
