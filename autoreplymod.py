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
        "opened_cfg": "🔧 <b>Configuration opened.</b>",
        "_cfg_doc_replies": "Dictionary of replies",
        "_cfg_doc_delay": "Delay in seconds before replying",
        "_cfg_doc_reply_mode": (
            "If true, bot replies to the message; if false, bot sends a new message"
        ),
        "cfgarm_cmd_doc": "open config"
    }
    
    strings_ru = {
        "name": "ARM",
        "reply_error": "🚫 <b>Невозможно отправить ответ</b>",
        "opened_cfg": "🔧 <b>Конфигурация открыта.</b>",
        "_cls_doc": "Модуль автоматического ответа: Вы можете настроить конфигурацию.",
        "_cfg_doc_replies": "Словарь ответов",
        "_cfg_doc_delay": "Задержка в секундах перед ответом",
        "_cfg_doc_reply_mode": (
            "Если true, бот отвечает на сообщение; если false, бот отправляет новое сообщение"
        ),
        "cfgarm_cmd_doc": "открыть конфигурацию"
    }
    
    strings_de = {
        "name": "ARM",
        "reply_error": "🚫 <b>Antwort kann nicht gesendet werden</b>",
        "opened_cfg": "🔧 <b>Konfiguration geöffnet.</b>",
        "_cls_doc": "Automatisierter Antwortmodul: Sie können die Konfiguration anpassen.",
        "_cfg_doc_replies": "Wörterbuch der Antworten",
        "_cfg_doc_delay": "Verzögerung in Sekunden vor der Antwort",
        "_cfg_doc_reply_mode": (
            "Wenn true, antwortet der Bot auf die Nachricht; wenn false, sendet der Bot eine neue Nachricht"
        ),
        "cfgarm_cmd_doc": "Konfiguration öffnen"
    }
    
    strings_tr = {
        "name": "ARM",
        "reply_error": "🚫 <b>Yanıt gönderilemiyor</b>",
        "opened_cfg": "🔧 <b>Yapılandırma açıldı.</b>",
        "_cls_doc": "Otomatik yanıt modülü: Yapılandırmayı özelleştirebilirsiniz.",
        "_cfg_doc_replies": "Yanıtlar sözlüğü",
        "_cfg_doc_delay": "Yanıt vermeden önce saniye cinsinden gecikme",
        "_cfg_doc_reply_mode": (
            "Eğer true ise, bot mesaja yanıt verir; false ise, bot yeni bir mesaj gönderir"
        ),
        "cfgarm_cmd_doc": "yapılandırmayı aç"
    }

    strings_uz = {
        "name": "ARM",
        "reply_error": "🚫 <b>Javob yuborib bo'lmadi</b>",
        "opened_cfg": "🔧 <b>Sozlamalar ochildi.</b>",
        "_cls_doc": "Avto-javob moduli: Siz sozlamalarni moslashtirishingiz mumkin.",
        "_cfg_doc_replies": "Javoblar lug'ati",
        "_cfg_doc_delay": "Javob berishdan oldin kechikish soniyalarda",
        "_cfg_doc_reply_mode": (
            "Agar true bo'lsa, bot xabariga javob beradi; agar false bo'lsa, bot yangi xabar yuboradi"
        ),
        "cfgarm_cmd_doc": "sozlamalarni ochish"
    }

    async def client_ready(self, client, db):
        self.client = client

    def init(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "replies",
                {"привет": "Привет", "hello": "Hello"},
                self.strings["_cfg_doc_replies"]
            ),
            loader.ConfigValue(
                "delay",
                0,
                self.strings["_cfg_doc_delay"]
            ),
            loader.ConfigValue(
                "reply_mode",
                True,
                self.strings["_cfg_doc_reply_mode"],
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
                    try:
                        if self.config["reply_mode"]:
                            await message.reply(reply)
                        else:
                            await message.respond(reply)
                    except Exception:
                        await utils.answer(message, self.strings["reply_error"])
                    break

    @loader.command(ru_doc=strings_ru["cfgarm_cmd_doc"], de_doc=strings_de["cfgarm_cmd_doc"], tr_doc=strings_tr["cfgarm_cmd_doc"], uz_doc=strings_uz["cfgarm_cmd_doc"])
    async def cfgarm(self, message):
        """{cfgarm_cmd_doc}"""
        await message.delete()
        args = utils.get_args_raw(message)
        config_message = f".cfg {args or 'ARM'}"
        await self.client.send_message(message.to_id, config_message)
        await utils.answer(message, self.strings["opened_cfg"])        
