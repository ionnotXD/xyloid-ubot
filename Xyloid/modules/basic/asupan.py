from asyncio import gather
from random import choice

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from Xyloid.helpers.basic import edit_or_reply
from Xyloid.helpers.PyroHelpers import ReplyCheck

from .help import add_command_help


@Client.on_message(filters.command(["asupan", "ptl"], cmd) & filters.me)
async def asupan_cmd(client: Client, message: Message):
    Xyloid = await edit_or_reply(message, "Tunggu Sebentar Yah Ajg Asupan Lo Lagi Load...")
    await gather(
        Xyloid.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "tedeasupancache", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )


add_command_help(
    "asupan",
    [
        [
            f"asupan atau {cmd}ptl",
            "Untuk Mengirim video asupan secara random.",
        ]
    ],
)
