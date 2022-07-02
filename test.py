
import logging

from telethon.tl.types import Message

from .. import loader

logger = logging.getLogger(__name__)


class HiMod(loader.Module):
    string = {"name": "HiMod", "description": "Hi",
              "usage": ".hi", "developer": "Saber"}

    def __init__(self):
        self.config = loader.ModuleConfig(loader.ConfigValue(
            "Hi", "Hi"))

    async def client_ready(self, client, db):
        self.client = client
        self.db = db

    async def hicmd(self, message: Message):
        """.hi - Hi"""
        await message.edit("Hi")
