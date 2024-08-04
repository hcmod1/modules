__version__ = (1, 0, 0)

# meta developer: @hcmod

import asyncio
from .. import loader, utils

@loader.tds
class ARM(loader.Module):
    """Auto-reply module: You can customize the configuration."""
    strings = {"name": "ARM"}

    async def client_ready(self, client, db):
        self.client = client

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "replies",
                {"привет": "Привет", "hello": "Hello"},
                "Dictionary of replies"
            ),
            loader.ConfigValue(
                "delay",
                0,
                "Delay in seconds before replying"
            ),
            loader.ConfigValue(
                "reply_mode",
                True,
                "If true, bot replies to the message; if false, bot sends a new message",
                validator=loader.validators.Boolean()
            )
        )

    @loader.unrestricted
    async def watcher(self, message):
        """This function will monitor incoming messages"""
        if message.is_private:
            sender = await message.get_sender()
            if sender.bot or message.sender_id == (await self.client.get_me()).id:
                return
            
            text = message.raw_text.lower()
            for keyword, reply in self.config["replies"].items():
                if keyword in text:
                    await asyncio.sleep(self.config["delay"])
                    if self.config["reply_mode"]:
                        await message.reply(reply)
                    else:
                        await message.respond(reply)
                    break
