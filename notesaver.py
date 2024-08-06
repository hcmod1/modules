__version__ = (1, 0, 0)

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
        "notes_list": "<emoji document_id=5413879192267805083>🗓</emoji> <b>Saved Notes:</b>\n\n{}",
        "note_deleted": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Note deleted!</b>",
        "spec_invalid_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Please specify the note number to delete.</b>",
        "invalid_note_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Invalid note number.</b>",
        "cleared_all_notes": "<emoji document_id=5206607081334906820>✔️</emoji> <b>All notes cleared!</b>",
        "please_reply": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Please reply to a message to save it as a note.</b>"
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
        "_cmd_doc_sn": "- сохранить заметку. Использование: sn <ответ на сообщение>",
        "_cmd_doc_ln": "- перечислить все сохраненные заметки",
        "_cmd_doc_dn": "- удалить заметку. Использование: dn <номер заметки>",
        "_cmd_doc_cn": "- очистить все сохраненные заметки",
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
        "_cmd_doc_sn": "- enregistrer une note. Utilisation: sn <réponse à un message>",
        "_cmd_doc_ln": "- lister toutes les notes enregistrées",
        "_cmd_doc_dn": "- supprimer une note. Utilisation: dn <numéro de note>",
        "_cmd_doc_cn": "- effacer toutes les notes enregistrées",
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
        "_cmd_doc_sn": "- salva una nota. Uso: sn <rispondi a un messaggio>",
        "_cmd_doc_ln": "- elenca tutte le note salvate",
        "_cmd_doc_dn": "- elimina una nota. Uso: dn <numero di nota>",
        "_cmd_doc_cn": "- cancella tutte le note salvate",
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
        "_cmd_doc_sn": "- speichere eine Notiz. Verwendung: sn <Antwort auf eine Nachricht>",
        "_cmd_doc_ln": "- alle gespeicherten Notizen auflisten",
        "_cmd_doc_dn": "- lösche eine Notiz. Verwendung: dn <Notiznummer>",
        "_cmd_doc_cn": "- alle gespeicherten Notizen löschen",
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
        "_cmd_doc_sn": "- bir notu kaydet. Kullanım: sn <mesaja yanıt ver>",
        "_cmd_doc_ln": "- kaydedilen tüm notları listele",
        "_cmd_doc_dn": "- bir notu sil. Kullanım: dn <not numarası>",
        "_cmd_doc_cn": "- tüm kaydedilen notları temizle",
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
        "_cmd_doc_sn": "- eslatma saqlash. Foydalanish: sn <xabarga javob bering>",
        "_cmd_doc_ln": "- saqlangan eslatmalar ro'yxati",
        "_cmd_doc_dn": "- elslatmani o'chirib tashlash. Foydalanish: dn <eslatma raqami>",
        "_cmd_doc_cn": "- barcha saqlangan eslatmalarni tozalash",
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
        "_cmd_doc_sn": "- guardar una nota. Uso: sn <responder a un mensaje>",
        "_cmd_doc_ln": "- mostrar todas las notas guardadas",
        "_cmd_doc_dn": "- eliminar una nota. Uso: dn <número de nota>",
        "_cmd_doc_cn": "- limpiar todas las notas guardadas",
        "_cls_doc": "Un módulo para guardar y gestionar tus notas de manera eficiente."
    }

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.notes = self.db.get(self.strings["name"], "notes", [])

    @loader.command()
    async def sn(self, message: Message):
        """- save a note. Usage: sn <reply to a message>"""
        reply = await message.get_reply_message()
        if not reply:
            await utils.answer(message, self.strings["please_reply"])
            await asyncio.sleep(5)
            await message.delete()
            return
        self.notes.append(reply.text)
        self.db.set(self.strings["name"], "notes", self.notes)
        await utils.answer(message, self.strings["note_saved"])
        await asyncio.sleep(5)
        await message.delete()

    @loader.command()
    async def ln(self, message: Message):
        """- list all saved notes"""
        if not self.notes:
            await utils.answer(message, self.strings["no_notes"])
            await asyncio.sleep(5)
            await message.delete()
            return
        notes = "\n\n".join([f"<b>{i+1}.</b> {n}" for i, n in enumerate(self.notes)])
        await utils.answer(message, self.strings["notes_list"].format(notes))

    @loader.command()
    async def dn(self, message: Message):
        """- delete a note. Usage: dn <note number>"""
        args = utils.get_args_raw(message)
        if not args.isdigit():
            await utils.answer(message, self.strings["spec_invalid_number"])
            await asyncio.sleep(5)
            await message.delete()
            return
        index = int(args) - 1
        if 0 <= index < len(self.notes):
            self.notes.pop(index)
            self.db.set(self.strings["name"], "notes", self.notes)
            await utils.answer(message, self.strings["note_deleted"])
            await asyncio.sleep(5)
            await message.delete()
        else:
            await utils.answer(message, self.strings["invalid_note_number"])
            await asyncio.sleep(5)
            await message.delete()

    @loader.command()
    async def cn(self, message: Message):
        """- clear all saved notes"""
        self.notes = []
        self.db.set(self.strings["name"], "notes", [])
        await utils.answer(message, self.strings["cleared_all_notes"])
        await asyncio.sleep(5)
        await message.delete()
