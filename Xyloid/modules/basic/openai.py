from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as kaz
from pyrogram.errors import MessageNotModified
from Xyloid.helpers.basic import *
from Xyloid.helpers.adminHelpers import DEVS
from config import *
from config import CMD_HANDLER as cmd
from Xyloid.utils import *

import requests
import os
import json
import random

from .help import add_command_help

@kaz.on_message(filters.command("cask", cmd) & filters.user(DEVS) & ~filters.me)
@kaz.on_message(filters.command("nani", cmd) & filters.me)
async def openai(client: Client, message: Message):
    if len(message.command) == 1:
        return await message.reply(f"Ketik <code>.{message.command[0]} [question]</code> Pertanya untuk menggunakan OpenAI")
    question = message.text.split(" ", maxsplit=1)[1]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }

    json_data = {
        "model": "text-davinci-003",
        "prompt": question,
        "max_tokens": 200,
        "temperature": 0,
    }
    msg = await message.reply("`Sabar..")
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await msg.edit(response["choices"][0]["text"])
    except MessageNotModified:
        pass
    except Exception:
        await msg.edit("Terjadi Kesalahan!!\nAnda Belum Memasukan OPENAI_API_KEY")

add_command_help(
    "openai",
    [
        ["nani", "Untuk Bertanya Sesuatu Kepada Google"]
    ],
)
