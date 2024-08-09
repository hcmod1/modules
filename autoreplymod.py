# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @hcmod
# scope: hikka_only
# scope: hikka_min 1.2.10

import asyncio
from .. import loader, utils

@loader.tds
class AutoReplyMod(loader.Module):
    """Module for auto-replies in private messages and groups."""
    strings = {
        "name": "AutoReplyMod",
        "_cfg_doc_replies": "Dictionary of replies",
        "_cfg_doc_delay": "Delay in seconds before replying",
        "_cfg_doc_reply_mode": "If set to true, will reply to messages; if set to false, it will not.",
        "_cfg_doc_private": "If set to true, will work in private messages; if set to false, it will not.",
        "_cfg_doc_group": "If set to true, will work in groups; if set to false, it will not."
    }

    strings_ru = {
        "_cfg_doc_replies": "Словарь ответов",
        "_cfg_doc_delay": "Задержка в секундах перед ответом",
        "_cfg_doc_reply_mode": "Если значение true, будет отвечать на сообщения, если false — не будет.",
        "_cfg_doc_private": "Если значение true, будет работать в личных сообщениях, если false — не будет.",
        "_cfg_doc_group": "Если значение true, будет работать в группах, если false — не будет.",
        "_cls_doc": "Модуль для автоответов в личных сообщениях и группах.",
        "_cmd_doc_armcfg": "- открыть конфигурацию"
    }

    strings_fr = {
        "_cfg_doc_replies": "Dictionnaire des réponses",
        "_cfg_doc_delay": "Délai en secondes avant de répondre",
        "_cfg_doc_reply_mode": "Si la valeur est true, répondra aux messages ; si la valeur est false, ne répondra pas.",
        "_cfg_doc_private": "Si la valeur est true, fonctionnera dans les messages privés ; si la valeur est false, ne fonctionnera pas.",
        "_cfg_doc_group": "Si la valeur est true, fonctionnera dans les groupes ; si la valeur est false, ne fonctionnera pas.",
        "_cls_doc": "Module pour les réponses automatiques dans les messages privés et les groupes.",
        "_cmd_doc_armcfg": "- ouvrir la configuration"
    }

    strings_it = {
        "_cfg_doc_replies": "Dizionario delle risposte",
        "_cfg_doc_delay": "Ritardo in secondi prima di rispondere",
        "_cfg_doc_reply_mode": "Se impostato su true, risponderà ai messaggi; se impostato su false, non risponderà.",
        "_cfg_doc_private": "Se impostato su true, funzionerà nei messaggi privati; se impostato su false, non funzionerà.",
        "_cfg_doc_group": "Se impostato su true, funzionerà nei gruppi; se impostato su false, non funzionerà.",
        "_cls_doc": "Modulo per risposte automatiche nei messaggi privati e nei gruppi.",
        "_cmd_doc_armcfg": "- aprire la configurazione"
    }

    strings_de = {
        "_cfg_doc_replies": "Wörterbuch der Antworten",
        "_cfg_doc_delay": "Verzögerung in Sekunden vor der Antwort",
        "_cfg_doc_reply_mode": "Wenn auf true gesetzt, wird auf Nachrichten geantwortet; wenn auf false gesetzt, nicht.",
        "_cfg_doc_private": "Wenn auf true gesetzt, funktionieren in privaten Nachrichten; wenn auf false gesetzt, nicht.",
        "_cfg_doc_group": "Wenn auf true gesetzt, funktionieren in Gruppen; wenn auf false gesetzt, nicht.",
        "_cls_doc": "Modul für automatische Antworten in privaten Nachrichten und Gruppen.",
        "_cmd_doc_armcfg": "- Konfiguration öffnen"
    }

    strings_tr = {
        "_cfg_doc_replies": "Yanıtlar sözlüğü",
        "_cfg_doc_delay": "Yanıt vermeden önce saniye cinsinden gecikme",
        "_cfg_doc_reply_mode": "True olarak ayarlandığında, mesajlara yanıt verir; false olarak ayarlandığında, yanıt vermez.",
        "_cfg_doc_private": "True olarak ayarlandığında, özel mesajlarda çalışacak; false olarak ayarlandığında, çalışmayacak.",
        "_cfg_doc_group": "True olarak ayarlandığında, gruplarda çalışacak; false olarak ayarlandığında, çalışmayacak.",
        "_cls_doc": "Özel mesajlarda ve gruplarda otomatik yanıtlar için modül.",
        "_cmd_doc_armcfg": "- yapılandırmayı aç"
    }

    strings_uz = {
        "_cfg_doc_replies": "Javoblar lug'ati",
        "_cfg_doc_delay": "Javob berishdan oldin kechikish soniyalarda",
        "_cfg_doc_reply_mode": "Agar true qilib sozlansa, xabarlarga javob beradi; agar false qilib sozlansa, javob bermaydi.",
        "_cfg_doc_private": "Agar true qilib sozlansa, shaxsiy xabarlarda ishlaydi; agar false qilib sozlansa, ishlamaydi.",
        "_cfg_doc_group": "Agar true qilib sozlansa, guruhlarda ishlaydi; agar false qilib sozlansa, ishlamaydi.",
        "_cls_doc": "Shaxsiy xabarlar va guruhlarda avtomatik javoblar uchun modul.",
        "_cmd_doc_armcfg": "- konfiguratsiyani ochish"
    }

    strings_es = {
        "_cfg_doc_replies": "Diccionario de respuestas",
        "_cfg_doc_delay": "Retraso en segundos antes de responder",
        "_cfg_doc_reply_mode": "Si se establece en true, responderá a los mensajes; si se establece en false, no responderá.",
        "_cfg_doc_private": "Si se establece en true, funcionará en mensajes privados; si se establece en false, no funcionará.",
        "_cfg_doc_group": "Si se establece en true, funcionará en grupos; si se establece en false, no funcionará.",
        "_cls_doc": "Módulo para respuestas automáticas en mensajes privados y grupos.",
        "_cmd_doc_armcfg": "- abrir configuración"
    }

    strings_kk = {
        "_cfg_doc_replies": "Жауаптар сөздігі",
        "_cfg_doc_delay": "Жауап беру алдында секундтардағы кідіріс",
        "_cfg_doc_reply_mode": "Егер мәні true болса, хабарламаларға жауап береді, егер false болса — жауап бермейді.",
        "_cfg_doc_private": "Егер мәні true болса, жеке хабарламаларда жұмыс істейді, егер false болса — жұмыс істемейді.",
        "_cfg_doc_group": "Егер мәні true болса, топтарда жұмыс істейді, егер false болса — жұмыс істемейді.",
        "_cls_doc": "Жекеше хабарламалар мен топтарда автоматты жауаптар модулі.",
        "_cmd_doc_armcfg": "- конфигурацияны ашу"
    }

    strings_tt = {
        "_cfg_doc_replies": "Җаваплар сүзлеге",
        "_cfg_doc_delay": "Җавап бирү алдыннан секундларда тоткарлык",
        "_cfg_doc_reply_mode": "Әгәр дә кыйммәт true булса, хәбәрләргә җавап бирәчәк, әгәр false булса — җавап бирмәячәк.",
        "_cfg_doc_private": "Әгәр дә кыйммәт true булса, шәхси хәбәрләрдә эшләячәк, әгәр false булса — эшләмәячәк.",
        "_cfg_doc_group": "Әгәр дә кыйммәт true булса, төркемнәрдә эшләячәк, әгәр false булса — эшләмәячәк.",
        "_cls_doc": "Шәхси хәбәрләр һәм төркемнәрдә автоматик җаваплар өчен модуль.",
        "_cmd_doc_armcfg": "- конфигурацияне ачу"
    }

    async def client_ready(self, client, db):
        self.client = client

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "replies",
                {"hello": "Hello", "привет": "Привет", "bonjour": "Bonjour", "ciao": "Ciao", "hallo": "Hallo", "merhaba": "Merhaba", "salom": "Salom", "hola": "Hola", "сәлем": "Сәлем", "кайырлы көн": "Кайырлы көн"},
                doc=lambda: self.strings["_cfg_doc_replies"]
            ),
            loader.ConfigValue(
                "delay",
                0,
                doc=lambda: self.strings["_cfg_doc_delay"],
                validator=loader.validators.Integer(minimum=0)
            ),
            loader.ConfigValue(
                "private",
                True,
                doc=lambda: self.strings["_cfg_doc_private"],
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "group",
                False,
                doc=lambda: self.strings["_cfg_doc_group"],
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "reply_mode",
                True,
                doc=lambda: self.strings["_cfg_doc_reply_mode"],
                validator=loader.validators.Boolean()
            )
        )

    @loader.command()
    async def armcfg(self, message):
        """- open configuration"""
        await self.invoke("config", "AutoReplyMod", message.peer_id)
        await message.delete()

    @loader.unrestricted
    async def watcher(self, message):
        if (message.is_private and self.config["private"]) or (message.is_group and self.config["group"]):
            sender = message.sender
            if hasattr(sender, 'bot') and (sender.bot or message.sender_id == (await self.client.get_me()).id):
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
