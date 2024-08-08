# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @hcmod
# scope: hikka_only
# scope: hikka_min 1.2.10

import json
import asyncio
from telethon.tl.types import Message
from .. import loader, utils

@loader.tds
class NoteSaver(loader.Module):
    """A module to save and manage your notes efficiently."""

    strings = {
        "name": "NoteSaver",
        "note_saved": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Note saved!</b>",
        "no_notes": "<emoji document_id=5210952531676504517>❌</emoji> <b>No notes found.</b>",
        "notes_list": "<emoji document_id=5413879192267805083>🗓</emoji> <b>Saved notes:</b>\n\n{}",
        "note_deleted": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Note deleted!</b>",
        "spec_invalid_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Please specify the note number to delete.</b>",
        "invalid_note_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Invalid note number.</b>",
        "cleared_all_notes": "<emoji document_id=5206607081334906820>✔️</emoji> <b>All notes cleared!</b>",
        "please_reply": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Please reply to a message to save it as a note.</b>",
        "_cfg_doc_timer": "Time in seconds after which the message will be deleted."
    }

    strings_ru = {
        "note_saved": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Заметка сохранена!</b>",
        "no_notes": "<emoji document_id=5210952531676504517>❌</emoji> <b>Заметки не найдены.</b>",
        "notes_list": "<emoji document_id=5413879192267805083>🗓</emoji> <b>Сохраненные заметки:</b>\n\n{}",
        "note_deleted": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Заметка удалена!</b>",
        "spec_invalid_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Пожалуйста, укажите номер заметки для удаления.</b>",
        "invalid_note_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Неверный номер заметки.</b>",
        "cleared_all_notes": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Все заметки очищены!</b>",
        "please_reply": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Пожалуйста, ответьте на сообщение, чтобы сохранить его как заметку.</b>",
        "_cmd_doc_nsave": "- сохранить заметку. Использование: nsave <ответ на сообщение>",
        "_cmd_doc_nlist": "- перечислить все сохраненные заметки",
        "_cmd_doc_ndelete": "- удалить заметку. Использование: ndelete <номер заметки>",
        "_cmd_doc_nclear": "- очистить все сохраненные заметки",
        "_cfg_doc_timer": "Время в секундах, по истечении которого сообщение будет удалено.",
        "_cls_doc": "Модуль для сохранения и управления вашими заметками."
    }

    strings_fr = {
        "note_saved": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Note enregistrée!</b>",
        "no_notes": "<emoji document_id=5210952531676504517>❌</emoji> <b>Aucune note trouvée.</b>",
        "notes_list": "<emoji document_id=5413879192267805083>🗓</emoji> <b>Notes sauvegardées:</b>\n\n{}",
        "note_deleted": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Note supprimée!</b>",
        "spec_invalid_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Veuillez spécifier le numéro de la note à supprimer.</b>",
        "invalid_note_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Numéro de note invalide.</b>",
        "cleared_all_notes": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Toutes les notes ont été effacées!</b>",
        "please_reply": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Veuillez répondre à un message pour l'enregistrer en tant que note.</b>",
        "_cmd_doc_nsave": "- enregistrer une note. Utilisation: nsave <réponse à un message>",
        "_cmd_doc_nlist": "- lister toutes les notes enregistrées",
        "_cmd_doc_ndelete": "- supprimer une note. Utilisation: ndelete <numéro de note>",
        "_cmd_doc_nclear": "- effacer toutes les notes enregistrées",
        "_cfg_doc_timer": "Le délai en secondes après lequel le message sera supprimé.",
        "_cls_doc": "Un module pour enregistrer et gérer vos notes efficacement."
    }

    strings_it = {
        "note_saved": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Nota salvata!</b>",
        "no_notes": "<emoji document_id=5210952531676504517>❌</emoji> <b>Nessuna nota trovata.</b>",
        "notes_list": "<emoji document_id=5413879192267805083>🗓</emoji> <b>Note salvate:</b>\n\n{}",
        "note_deleted": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Nota eliminata!</b>",
        "spec_invalid_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Per favore, specifica il numero della nota da eliminare.</b>",
        "invalid_note_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Numero di nota non valido.</b>",
        "cleared_all_notes": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Tutte le note sono state cancellate!</b>",
        "please_reply": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Rispondi a un messaggio per salvarlo come nota.</b>",
        "_cmd_doc_nsave": "- salva una nota. Uso: nsave <rispondi a un messaggio>",
        "_cmd_doc_nlist": "- elenca tutte le note salvate",
        "_cmd_doc_ndelete": "- elimina una nota. Uso: ndelete <numero di nota>",
        "_cmd_doc_nclear": "- cancella tutte le note salvate",
        "_cfg_doc_timer": "Il tempo in secondi dopo il quale il messaggio sarà eliminato.",
        "_cls_doc": "Un modulo per salvare e gestire le tue note in modo efficiente."
    }

    strings_de = {
        "note_saved": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Notiz gespeichert!</b>",
        "no_notes": "<emoji document_id=5210952531676504517>❌</emoji> <b>Keine Notizen gefunden.</b>",
        "notes_list": "<emoji document_id=5413879192267805083>🗓</emoji> <b>Gespeicherte Notizen:</b>\n\n{}",
        "note_deleted": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Notiz gelöscht!</b>",
        "spec_invalid_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Bitte gib die Nummer der zu löschenden Notiz an.</b>",
        "invalid_note_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Ungültige Notiznummer.</b>",
        "cleared_all_notes": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Alle Notizen wurden gelöscht!</b>",
        "please_reply": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Bitte antworte auf eine Nachricht, um sie als Notiz zu speichern.</b>",
        "_cmd_doc_nsave": "- speichere eine Notiz. Verwendung: nsave <Antwort auf eine Nachricht>",
        "_cmd_doc_nlist": "- alle gespeicherten Notizen auflisten",
        "_cmd_doc_ndelete": "- lösche eine Notiz. Verwendung: ndelete <Notiznummer>",
        "_cmd_doc_nclear": "- alle gespeicherten Notizen löschen",
        "_cfg_doc_timer": "Die Zeit in Sekunden, nach der die Nachricht gelöscht wird.",
        "_cls_doc": "Ein Modul, um Notizen effizient zu speichern und zu verwalten."
    }

    strings_tr = {
        "note_saved": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Not kaydedildi!</b>",
        "no_notes": "<emoji document_id=5210952531676504517>❌</emoji> <b>Hiç not bulunamadı.</b>",
        "notes_list": "<emoji document_id=5413879192267805083>🗓</emoji> <b>Kaydedilen Notlar:</b>\n\n{}",
        "note_deleted": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Not silindi!</b>",
        "spec_invalid_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Lütfen silmek için not numarasını belirtin.</b>",
        "invalid_note_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Geçersiz not numarası.</b>",
        "cleared_all_notes": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Tüm notlar temizlendi!</b>",
        "please_reply": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Lütfen bir mesajı not olarak kaydetmek için cevaplayın.</b>",
        "_cmd_doc_nsave": "- bir notu kaydet. Kullanım: nsave <mesaja yanıt ver>",
        "_cmd_doc_nlist": "- kaydedilen tüm notları listele",
        "_cmd_doc_ndelete": "- bir notu sil. Kullanım: ndelete <not numarası>",
        "_cmd_doc_nclear": "- tüm kaydedilen notları temizle",
        "_cfg_doc_timer": "Mesajın silineceği süre saniye cinsinden.",
        "_cls_doc": "Notlarınızı verimli bir şekilde kaydetmek ve yönetmek için bir modül."
    }
    
    strings_uz = {
        "note_saved": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Eslatma saqlandi!</b>",
        "no_notes": "<emoji document_id=5210952531676504517>❌</emoji> <b>Hech qanday eslatma topilmadi.</b>",
        "notes_list": "<emoji document_id=5413879192267805083>🗓</emoji> <b>Saqlangan eslatmalar:</b>\n\n{}",
        "note_deleted": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Eslatma o‘chirildi!</b>",
        "spec_invalid_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Iltimos, o'chirish uchun eslatma raqamini kiriting.</b>",
        "invalid_note_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Noto'g'ri eslatma raqami.</b>",
        "cleared_all_notes": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Barcha eslatmalar tozalandi!</b>",
        "please_reply": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Iltimos, eslatma sifatida saqlash uchun xabarni javob bering.</b>",
        "_cmd_doc_nsave": "- eslatma saqlash. Foydalanish: nsave <xabarga javob bering>",
        "_cmd_doc_nlist": "- saqlangan eslatmalar ro'yxati",
        "_cmd_doc_ndelete": "- elslatmani o'chirib tashlash. Foydalanish: ndelete <eslatma raqami>",
        "_cmd_doc_nclear": "- barcha saqlangan eslatmalarni tozalash",
        "_cfg_doc_timer": "Xabar o‘chiriladigan vaqt (soniyalarda).",
        "_cls_doc": "Eslatmalarni samarali saqlash va boshqarish uchun modul."
    }

    strings_es = {
        "note_saved": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Nota guardada!</b>",
        "no_notes": "<emoji document_id=5210952531676504517>❌</emoji> <b>No se encontraron notas.</b>",
        "notes_list": "<emoji document_id=5413879192267805083>🗓</emoji> <b>Notas guardadas:</b>\n\n{}",
        "note_deleted": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Nota eliminada!</b>",
        "spec_invalid_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Por favor, especifique el número de la nota a eliminar.</b>",
        "invalid_note_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Número de nota inválido.</b>",
        "cleared_all_notes": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Todas las notas han sido eliminadas!</b>",
        "please_reply": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Por favor, responde a un mensaje para guardarlo como nota.</b>",
        "_cmd_doc_nsave": "- guardar una nota. Uso: nsave <responder a un mensaje>",
        "_cmd_doc_nlist": "- mostrar todas las notas guardadas",
        "_cmd_doc_ndelete": "- eliminar una nota. Uso: ndelete <número de nota>",
        "_cmd_doc_nclear": "- limpiar todas las notas guardadas",
        "_cfg_doc_timer": "El tiempo en segundos después del cual el mensaje será eliminado.",
        "_cls_doc": "Un módulo para guardar y gestionar tus notas de manera eficiente."
    }

    strings_kk = {
        "note_saved": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Ескертпе сақталды!</b>",
        "no_notes": "<emoji document_id=5210952531676504517>❌</emoji> <b>Ескертпелер табылмады.</b>",
        "notes_list": "<emoji document_id=5413879192267805083>🗓</emoji> <b>Сақталған ескертпелер:</b>\n\n{}",
        "note_deleted": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Ескертпе жойылды!</b>",
        "spec_invalid_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Жою үшін ескертпе нөмірін көрсетіңіз.</b>",
        "invalid_note_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Қате ескертпе нөмірі.</b>",
        "cleared_all_notes": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Барлық ескертпелер тазартылды!</b>",
        "please_reply": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Ескертпе ретінде сақтау үшін хабарламаға жауап беріңіз.</b>",
        "_cmd_doc_nsave": "- ескертпені сақтау. Қолдану: nsave <хабарламаға жауап>",
        "_cmd_doc_nlist": "- барлық сақталған ескертпелерді атау",
        "_cmd_doc_ndelete": "- ескертпені жою. Қолдану: ndelete <ескертпе нөмірі>",
        "_cmd_doc_nclear": "- барлық сақталған ескертпелерді тазарту",
        "_cfg_doc_timer": "Хабарлама жойылатын уақыт секундта.",
        "_cls_doc": "Сіздің ескертпелеріңізді сақтап, басқаруға арналған модуль."
    }

    strings_tt = {
        "note_saved": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Искәрмә сакланды!</b>",
        "no_notes": "<emoji document_id=5210952531676504517>❌</emoji> <b>Искәрмәләр табылмады.</b>",
        "notes_list": "<emoji document_id=5413879192267805083>🗓</emoji> <b>Сакланган искәрмәләр:</b>\n\n{}",
        "note_deleted": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Искәрмә бетерелде!</b>",
        "spec_invalid_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Бетерү өчен искәрмә номерын күрсәтегез.</b>",
        "invalid_note_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Ялгыш искәрмә номеры.</b>",
        "cleared_all_notes": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Барлык искәрмәләр чистартылды!</b>",
        "please_reply": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Искәрмә итеп саклау өчен хәбәргә җавап бирегез.</b>",
        "_cmd_doc_nsave": "- искәрмәне саклау. Куллану: nsave <хәбәргә җавап>",
        "_cmd_doc_nlist": "- барлык сакланган искәрмәләрне ату",
        "_cmd_doc_ndelete": "- искәрмәне бетерү. Куллану: ndelete <искәрмә номеры>",
        "_cmd_doc_nclear": "- барлык искәрмәләрне чистарту",
        "_cfg_doc_timer": "Хәбәр бетерелгәннән соң вакыт секундларда.",
        "_cls_doc": "Искәрмәләрегезне саклау һәм идарә итү өчен модуль."
    }

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.notes = self.db.get(self.strings["name"], "notes", [])

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "timer",
                10,
                doc=lambda: self.strings["_cfg_doc_timer"],
                validator=loader.validators.Integer(minimum=0)
            )
        )

    @loader.command()
    async def nsave(self, message: Message):
        """- save a note. Usage: nsave <reply to a message>"""
        reply = await message.get_reply_message()
        if not reply:
            await utils.answer(message, self.strings["please_reply"])
            await asyncio.sleep(self.config["timer"])
            await message.delete()
            return
        self.notes.append(reply.text)
        self.db.set(self.strings["name"], "notes", self.notes)
        await utils.answer(message, self.strings["note_saved"])
        await asyncio.sleep(self.config["timer"])
        await message.delete()

    @loader.command()
    async def nlist(self, message: Message):
        """- list all saved notes"""
        if not self.notes:
            await utils.answer(message, self.strings["no_notes"])
            await asyncio.sleep(self.config["timer"])
            await message.delete()
            return
        notes = "\n\n".join([f"<b>{i+1}.</b> {n}" for i, n in enumerate(self.notes)])
        await utils.answer(message, self.strings["notes_list"].format(notes))

    @loader.command()
    async def ndelete(self, message: Message):
        """- delete a note. Usage: ndelete <note number>"""
        args = utils.get_args_raw(message)
        if not args.isdigit():
            await utils.answer(message, self.strings["spec_invalid_number"])
            await asyncio.sleep(self.config["timer"])
            await message.delete()
            return
        index = int(args) - 1
        if 0 <= index < len(self.notes):
            self.notes.pop(index)
            self.db.set(self.strings["name"], "notes", self.notes)
            await utils.answer(message, self.strings["note_deleted"])
            await asyncio.sleep(self.config["timer"])
            await message.delete()
        else:
            await utils.answer(message, self.strings["invalid_note_number"])
            await asyncio.sleep(self.config["timer"])
            await message.delete()

    @loader.command()
    async def nclear(self, message: Message):
        """- clear all saved notes"""
        self.notes = []
        self.db.set(self.strings["name"], "notes", [])
        await utils.answer(message, self.strings["cleared_all_notes"])
        await asyncio.sleep(self.config["timer"])
        await message.delete()
        
