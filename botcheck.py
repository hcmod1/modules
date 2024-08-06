__version__ = (1, 0, 0)

# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @hcmod
# scope: hikka_only
# scope: hikka_min 1.2.10

from telethon.tl.types import Message
from .. import loader, utils

@loader.tds
class BotCheck(loader.Module):
    """Module to check if the userbot is working."""

    strings = {
        "name": "BotCheck",
        "bot_response": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Userbot is working!</b>"
    }

    strings_ru = {
        "bot_response": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Юзербот работает!</b>",
        "_cls_doc": "Модуль для проверки работоспособности юзербота.",
        "_cmd_doc_bot": "- используйте эту команду для проверки работоспособности."
    }

    strings_fr = {
        "bot_response": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Le bot utilisateur fonctionne!</b>",
        "_cls_doc": "Module pour vérifier si le bot utilisateur fonctionne.",
        "_cmd_doc_bot": "- utilisez cette commande pour vérifier le fonctionnement."
    }

    strings_it = {
        "bot_response": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Il bot utente funziona!</b>",
        "_cls_doc": "Modulo per verificare se l'utente bot funziona.",
        "_cmd_doc_bot": "- usa questo comando per controllare il funzionamento."
    }

    strings_de = {
        "bot_response": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Benutzerbot funktioniert!</b>",
        "_cls_doc": "Modul zur Überprüfung der Funktionsfähigkeit des Benutzerbots.",
        "_cmd_doc_bot": "- Verwenden Sie diesen Befehl, um die Funktionsfähigkeit zu überprüfen."
    }

    strings_rt = {
        "bot_response": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Benutzerbot funktioniert!</b>",
        "_cls_doc": "Modul zur Überprüfung der Funktionsfähigkeit des Benutzerbots.",
        "_cmd_doc_bot": "- Verwenden Sie diesen Befehl, um die Funktionsfähigkeit zu überprüfen."
    }

    strings_uz = {
        "bot_response": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Foydalanuvchi bot ishlayapti!</b>",
        "_cls_doc": "Foydalanuvchi botining ishlashini tekshirish uchun modul.",
        "_cmd_doc_bot": "- ishlashini tekshirish uchun ushbu buyruqni ishlating."
    }

    strings_es = {
        "bot_response": "<emoji document_id=5206607081334906820>✔️</emoji> <b>¡El bot de usuario está funcionando!</b>",
        "_cls_doc": "Módulo para verificar si el bot de usuario está funcionando.",
        "_cmd_doc_bot": "- utilice este comando para verificar el funcionamiento."
    }

    @loader.command()
    async def bot(self, message: Message):
        """- use this command to check the functionality."""
        await utils.answer(message, self.strings["bot_response"])
