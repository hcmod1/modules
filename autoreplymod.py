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
        "_cfg_doc_reply_mode": "If true, bot replies to the message; if false, bot sends a new message"
    }

    strings_ru = {
        "name": "АРМ",
        "reply_error": "🚫 <b>Невозможно отправить ответ</b>",
        "_cfg_doc_replies": "Словарь ответов",
        "_cfg_doc_delay": "Задержка в секундах перед ответом",
        "_cfg_doc_reply_mode": "Если true, бот отвечает на сообщение; если false, бот отправляет новое сообщение",
        "_cls_doc": "Модуль авто-ответчик: Вы можете настроить конфигурацию."
    }

    strings_fr = {
        "name": "ARM",
        "reply_error": "🚫 <b>Impossible d'envoyer une réponse</b>",
        "_cfg_doc_replies": "Dictionnaire des réponses",
        "_cfg_doc_delay": "Délai en secondes avant de répondre",
        "_cfg_doc_reply_mode": "Si vrai, le bot répond au message ; si faux, le bot envoie un nouveau message",
        "_cls_doc": "Module de réponse automatique : Vous pouvez personnaliser la configuration."
    }

    strings_it = {
        "name": "ARM",
        "reply_error": "🚫 <b>Impossibile inviare una risposta</b>",
        "_cfg_doc_replies": "Dizionario delle risposte",
        "_cfg_doc_delay": "Ritardo in secondi prima di rispondere",
        "_cfg_doc_reply_mode": "Se vero, il bot risponde al messaggio; se falso, il bot invia un nuovo messaggio",
        "_cls_doc": "Modulo di risposta automatica: È possibile personalizzare la configurazione."
    }

    strings_de = {
        "name": "ARM",
        "reply_error": "🚫 <b>Antwort kann nicht gesendet werden</b>",
        "_cfg_doc_replies": "Wörterbuch der Antworten",
        "_cfg_doc_delay": "Verzögerung in Sekunden vor der Antwort",
        "_cfg_doc_reply_mode": "Wenn true, antwortet der Bot auf die Nachricht; wenn false, sendet der Bot eine neue Nachricht",
        "_cls_doc": "Modul zur automatischen Antwort: Sie können die Konfiguration anpassen."
    }

    strings_tr = {
        "name": "ARM",
        "reply_error": "🚫 <b>Yanıt gönderilemiyor</b>",
        "_cfg_doc_replies": "Yanıtlar sözlüğü",
        "_cfg_doc_delay": "Yanıt vermeden önce saniye cinsinden gecikme",
        "_cfg_doc_reply_mode": "Eğer true ise, bot mesaja yanıt verir; false ise, bot yeni bir mesaj gönderir",
        "_cls_doc": "Otomatik yanıt modülü: Yapılandırmayı özelleştirebilirsiniz."
    }

    strings_uz = {
        "name": "ARM",
        "reply_error": "🚫 <b>Javob yuborib bo'lmadi</b>",
        "_cfg_doc_replies": "Javoblar lug'ati",
        "_cfg_doc_delay": "Javob berishdan oldin kechikish soniyalarda",
        "_cfg_doc_reply_mode": "Agar true bo'lsa, bot xabariga javob beradi; agar false bo'lsa, bot yangi xabar yuboradi",
        "_cls_doc": "Avto-javob moduli: Siz sozlamalarni moslashtirishingiz mumkin."
    }

    strings_es = {
        "name": "ARM",
        "reply_error": "🚫 <b>No se pudo enviar la respuesta</b>",
        "_cfg_doc_replies": "Diccionario de respuestas",
        "_cfg_doc_delay": "Retraso en segundos antes de responder",
        "_cfg_doc_reply_mode": "Si es verdadero, el bot responde al mensaje; si es falso, el bot envía un nuevo mensaje",
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
