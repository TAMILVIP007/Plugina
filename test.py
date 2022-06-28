
import logging

from telethon.tl.types import Message

from .. import loader

logger = logging.getLogger(__name__)


class HiMod(loader.Module):
    string = {"name": "HiMod", "help": ".hi"}

    async def client_ready(self, client, db):
        self.client = client
        self.db = db

    async def hi(self, message: Message):
        """.hi - Hi"""
        await message.edit("Hi")
