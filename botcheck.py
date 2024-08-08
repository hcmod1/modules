# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @hcmod
# scope: hikka_only
# scope: hikka_min 1.2.10

import datetime
from telethon.tl.types import Message
from .. import loader, utils

@loader.tds
class BotCheck(loader.Module):
    """Module to check if the userbot is working."""
    
    strings = {
        "name": "BotCheck",
        "bot_response": "{emoji} <b>Userbot is working!</b>\n<i>~ {uptime}</i>",
        "_cfg_doc_emoji": "Emoji in text"
    }

    strings_ru = {
        "bot_response": "{emoji} <b>Юзербот работает!</b>\n<i>~ {uptime}</i>",
        "_cls_doc": "Модуль для проверки работоспособности юзербота.",
        "_cmd_doc_bot": "- используйте эту команду для проверки работоспособности.",
        "_cfg_doc_emoji": "Эмодзи в тексте"
    }

    strings_fr = {
        "bot_response": "{emoji} <b>Le bot utilisateur fonctionne!</b>\n<i>~ {uptime}</i>",
        "_cls_doc": "Module pour vérifier si le bot utilisateur fonctionne.",
        "_cmd_doc_bot": "- utilisez cette commande pour vérifier le fonctionnement.",
        "_cfg_doc_emoji": "Emoji dans le texte"
    }

    strings_it = {
        "bot_response": "{emoji} <b>Il bot utente funziona!</b>\n<i>~ {uptime}</i>",
        "_cls_doc": "Modulo per verificare se l'utente bot funziona.",
        "_cmd_doc_bot": "- usa questo comando per controllare il funzionamento.",
        "_cfg_doc_emoji": "Emoji nel testo"
    }

    strings_de = {
        "bot_response": "{emoji} <b>Benutzerbot funktioniert!</b>\n<i>~ {uptime}</i>",
        "_cls_doc": "Modul zur Überprüfung der Funktionsfähigkeit des Benutzerbots.",
        "_cmd_doc_bot": "- Verwenden Sie diesen Befehl, um die Funktionsfähigkeit zu überprüfen.",
        "_cfg_doc_emoji": "Emoji im Text"
    }

    strings_rt = {
        "bot_response": "{emoji} <b>Benutzerbot funktioniert!</b>\n<i>~ {uptime}</i>",
        "_cls_doc": "Modul zur Überprüfung der Funktionsfähigkeit des Benutzerbots.",
        "_cmd_doc_bot": "- Verwenden Sie diesen Befehl, um die Funktionsfähigkeit zu überprüfen.",
        "_cfg_doc_emoji": "Metin içinde emoji"
    }

    strings_uz = {
        "bot_response": "{emoji} <b>Foydalanuvchi bot ishlayapti!</b>\n<i>~ {uptime}</i>",
        "_cls_doc": "Foydalanuvchi botining ishlashini tekshirish uchun modul.",
        "_cmd_doc_bot": "- ishlashini tekshirish uchun ushbu buyruqni ishlating.",
        "_cfg_doc_emoji": "Matndagi emodji"
    }

    strings_es = {
        "bot_response": "{emoji} <b>¡El bot de usuario está funcionando!</b>\n<i>~ {uptime}</i>",
        "_cls_doc": "Módulo para verificar si el bot de usuario está funcionando.",
        "_cmd_doc_bot": "- utilice este comando para verificar el funcionamiento.",
        "_cfg_doc_emoji": "Emoji en el texto"
    }

    strings_kk = {
        "bot_response": "{emoji} <b>Юзербот жұмыс істеп тұр!</b>\n<i>~ {uptime}</i>",
        "_cls_doc": "Юзерботтың жұмыс істеп тұрғанын тексеру модулі.",
        "_cmd_doc_bot": "- жұмыс істеуін тексеру үшін осы команданы қолданыңыз.",
        "_cfg_doc_emoji": "Мәтіндегі эмодзи"
    }

    strings_tt = {
        "bot_response": "{emoji} <b>Юзербот эшли!</b>\n<i>~ {uptime}</i>",
        "_cls_doc": "Юзерботның эшләвен тикшерү модуле.",
        "_cmd_doc_bot": "- эшләүне тикшерү өчен бу команданы кулланыгыз.",
        "_cfg_doc_emoji": "Тексттагы эмодзи"
    }

    async def client_ready(self, client, db):
        self.client = client

    def init(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "emoji",
                "<emoji document_id=5206607081334906820>✔️</emoji>",
                doc=lambda: self.strings["_cfg_doc_emoji"]
            )
        )

    @loader.command()
    async def bot(self, message: Message):
        """- use this command to check the functionality."""
        uptime = utils.formatted_uptime()
        emoji = self.config["emoji"]
        response = self.strings["bot_response"].format(emoji=emoji, uptime=uptime)
        await utils.answer(message, response)
