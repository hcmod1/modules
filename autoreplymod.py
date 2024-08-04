__version__ = (1, 0, 0)

# meta developer: @hcmod

import asyncio
from .. import loader, utils

@loader.tds
class ARM(loader.Module):
    """Auto-reply module: You can customize the configuration."""
    strings = {
        "name": "ARM",
        "reply_error": "🚫 <b>Unable to send reply</b>",
        "_cfg_doc_replies": "Dictionary of replies",
        "_cfg_doc_delay": "Delay in seconds before replying",
        "_cfg_doc_reply_mode": "If set to true, will reply to messages; if set to false, it will not.",
        "_cls_doc": "Auto-reply module: You can customize the configuration."
    }

    strings_ru = {
        "name": "АРМ",
        "reply_error": "🚫 <b>Невозможно отправить ответ</b>",
        "_cfg_doc_replies": "Словарь ответов",
        "_cfg_doc_delay": "Задержка в секундах перед ответом",
        "_cfg_doc_reply_mode": "Если значение true, будет отвечать на сообщения, если false — не будет.",
        "_cls_doc": "Модуль авто-ответчик: Вы можете настроить конфигурацию."
    }

    strings_fr = {
        "name": "ARM",
        "reply_error": "🚫 <b>Impossible d'envoyer une réponse</b>",
        "_cfg_doc_replies": "Dictionnaire des réponses",
        "_cfg_doc_delay": "Délai en secondes avant de répondre",
        "_cfg_doc_reply_mode": "Si la valeur est true, répondra aux messages ; si la valeur est false, il ne le fera pas.",
        "_cls_doc": "Module de réponse automatique : Vous pouvez personnaliser la configuration."
    }

    strings_it = {
        "name": "ARM",
        "reply_error": "🚫 <b>Impossibile inviare una risposta</b>",
        "_cfg_doc_replies": "Dizionario delle risposte",
        "_cfg_doc_delay": "Ritardo in secondi prima di rispondere",
        "_cfg_doc_reply_mode": "Se impostato su true, risponderà ai messaggi; se impostato su false, non lo farà.",
        "_cls_doc": "Modulo di risposta automatica: È possibile personalizzare la configurazione."
    }

    strings_de = {
        "name": "ARM",
        "reply_error": "🚫 <b>Antwort kann nicht gesendet werden</b>",
        "_cfg_doc_replies": "Wörterbuch der Antworten",
        "_cfg_doc_delay": "Verzögerung in Sekunden vor der Antwort",
        "_cfg_doc_reply_mode": "Wenn auf true gesetzt, wird auf Nachrichten geantwortet; wenn auf false gesetzt, nicht.",
        "_cls_doc": "Modul zur automatischen Antwort: Sie können die Konfiguration anpassen."
    }

    strings_tr = {
        "name": "ARM",
        "reply_error": "🚫 <b>Yanıt gönderilemiyor</b>",
        "_cfg_doc_replies": "Yanıtlar sözlüğü",
        "_cfg_doc_delay": "Yanıt vermeden önce saniye cinsinden gecikme",
        "_cfg_doc_reply_mode": "True olarak ayarlandığında, mesajlara yanıt verir; false olarak ayarlandığında, yanıt vermez.",
        "_cls_doc": "Otomatik yanıt modülü: Yapılandırmayı özelleştirebilirsiniz."
    }

    strings_uz = {
        "name": "ARM",
        "reply_error": "🚫 <b>Javob yuborib bo'lmadi</b>",
        "_cfg_doc_replies": "Javoblar lug'ati",
        "_cfg_doc_delay": "Javob berishdan oldin kechikish soniyalarda",
        "_cfg_doc_reply_mode": "Agar true qilib sozlansa, xabarlarga javob beradi; agar false qilib sozlansa, javob bermaydi.",
        "_cls_doc": "Avto-javob moduli: Siz sozlamalarni moslashtirishingiz mumkin."
    }

    strings_es = {
        "name": "ARM",
        "reply_error": "🚫 <b>No se pudo enviar la respuesta</b>",
        "_cfg_doc_replies": "Diccionario de respuestas",
        "_cfg_doc_delay": "Retraso en segundos antes de responder",
        "_cfg_doc_reply_mode": "Si se establece en true, responderá a los mensajes; si se establece en false, no lo hará.",
        "_cls_doc": "Módulo de respuesta automática: Puede personalizar la configuración."
    }

    async def client_ready(self, client, db):
        self.client = client

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "replies",
                {"привет": "Привет", "hello": "Hello"},
                doc=lambda: self.strings["_cfg_doc_replies"]
            ),
            loader.ConfigValue(
                "delay",
                0,
                doc=lambda: self.strings["_cfg_doc_delay"]
            ),
            loader.ConfigValue(
                "reply_mode",
                True,
                doc=lambda: self.strings["_cfg_doc_reply_mode"],
                validator=loader.validators.Boolean()
            )
        )

    @loader.unrestricted
    async def watcher(self, message):
        if message.is_private:
            sender = await message.get_sender()
            if sender.bot or message.sender_id == (await self.client.get_me()).id:
                return
            
            text = message.raw_text.lower()
            for keyword, reply in self.config["replies"].items():
                if keyword in text:
                    await asyncio.sleep(self.config["delay"])
                    try:
                        if self.config["reply_mode"]:
                            await message.reply(reply)
                        else:
                            await message.respond(reply)
                    except:
                        await message.reply(self.strings["reply_error"])
                    break
