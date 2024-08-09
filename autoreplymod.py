import asyncio
from .. import loader, utils

@loader.tds
class AutoReplyMod(loader.Module):
    """Module for auto-replies in private messages and groups."""
    strings = {
        "name": "AutoReplyMod",
        "_cfg_doc_delay": "Delay in seconds before replying",
        "_cfg_doc_reply_mode": "If set to true, will reply to messages; if set to false, it will not.",
        "_cfg_doc_private": "If set to true, will work in private messages; if set to false, it will not.",
        "_cfg_doc_group": "If set to true, will work in groups; if set to false, it will not.",
        "_cfg_doc_match_type": "Reply matching type: 1 for equals, 2 for contains, 3 for starts with",
        "_cfg_doc_timer": "Time in seconds after which the message will be deleted.",
        "format": "<emoji document_id=5210952531676504517>❌</emoji> <b>Format:</b> <code>question:answer</code>",
        "added_question": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Added question:</b> <code>{question}</code>\n\n<emoji document_id=5443038326535759644>💬</emoji> <b>With answer:</b> <code>{answer}</code>",
        "specify_question_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Please specify the question number.</b>",
        "invalid_question_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Invalid question number.</b>",
        "question_removed": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Question number</b> <code>{index_removed}</code> <b>removed.</b>",
        "dictionary_empty": "<emoji document_id=5210952531676504517>❌</emoji> <b>The replies dictionary is empty.</b>",
        "current_list": "<emoji document_id=5334544901428229844>ℹ️</emoji> <b>Current list:</b>\n\n{reply_str}"
    }    
    
    strings_ru = {
        "_cfg_doc_delay": "Задержка в секундах перед ответом",
        "_cfg_doc_reply_mode": "Если значение true, будет отвечать на сообщения; если значение false, не будет.",
        "_cfg_doc_private": "Если значение true, будет работать в личных сообщениях; если значение false, не будет.",
        "_cfg_doc_group": "Если значение true, будет работать в группах; если значение false, не будет.",
        "_cfg_doc_match_type": "Тип соответствия ответа: 1 для равенства, 2 для содержания, 3 для начала с",
        "_cfg_doc_timer": "Время в секундах, по истечении которого сообщение будет удалено.",
        "_cls_doc": "Модуль для автоответов в личных сообщениях и группах.",
        "_cmd_doc_addqa": "- добавить новый вопрос и ответ. Формат: вопрос:ответ",
        "_cmd_doc_delqa": "- удалить существующий вопрос по номеру",
        "_cmd_doc_listqa": "- показать текущий список вопросов и ответов",
        "_cmd_doc_cfgarm": "- открыть конфигурацию",
        "format": "<emoji document_id=5210952531676504517>❌</emoji> <b>Формат:</b> <code>вопрос:ответ</code>",
        "added_question": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Добавлен вопрос:<b> <code>{question}</code>\n\n<emoji document_id=5443038326535759644>💬</emoji> <b>С ответом:</b> <code>{answer}</code>",
        "specify_question_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Пожалуйста, укажите номер вопроса.</b>",
        "invalid_question_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Неправильный номер вопроса.</b>",
        "question_removed": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Вопрос номер</b> <code>{index_removed}</code> <b>удалён.</b>",
        "dictionary_empty": "<emoji document_id=5210952531676504517>❌</emoji> <b>Словарь ответов пуст.</b>",
        "current_list": "<emoji document_id=5334544901428229844>ℹ️</emoji> <b>Текущий список:</b>n{reply_str}"
    }

    strings_fr = {
        "_cfg_doc_delay": "Délai en secondes avant de répondre",
        "_cfg_doc_reply_mode": "Si true, répondra aux messages; si false, non.",
        "_cfg_doc_private": "Si true, fonctionnera dans les messages privés; si false, non.",
        "_cfg_doc_group": "Si true, fonctionnera dans les groupes; si false, non.",
        "_cfg_doc_match_type": "Type de correspondance pour la réponse : 1 pour l'égalité, 2 pour le contenu, 3 pour commence par",
        "_cfg_doc_timer": "Temps en secondes après lequel le message sera supprimé.",
        "_cls_doc": "Module pour les réponses automatiques dans les messages privés et les groupes.",
        "_cmd_doc_addqa": "- ajouter une nouvelle question et réponse. Format: question:réponse",
        "_cmd_doc_delqa": "- supprimer une question existante par numéro",
        "_cmd_doc_listqa": "- afficher la liste actuelle des questions et réponses",
        "_cmd_doc_cfgarm": "- ouvrir la configuration",
        "format": "<emoji document_id=5210952531676504517>❌</emoji> <b>Format :</b> <code>question:réponse</code>",
        "added_question": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Question ajoutée :</b> <code>{question}</code>\n\n<emoji document_id=5443038326535759644>💬</emoji> <b>Avec réponse :</b> <code>{answer}</code>",
        "specify_question_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Veuillez spécifier le numéro de la question.</b>",
        "invalid_question_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Numéro de question invalide.</b>",
        "question_removed": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Question numéro</b> <code>{index_removed}</code> <b>supprimée.</b>",
        "dictionary_empty": "<emoji document_id=5210952531676504517>❌</emoji> <b>Le dictionnaire de réponses est vide.</b>",
        "current_list": "<emoji document_id=5334544901428229844>ℹ️</emoji> <b>Liste actuelle :</b>\n{reply_str}"
    }

    strings_it = {
        "_cfg_doc_delay": "Ritardo in secondi prima di rispondere",
        "_cfg_doc_reply_mode": "Se true, risponderà ai messaggi; se false, no.",
        "_cfg_doc_private": "Se true, funzionerà nei messaggi privati; se false, no.",
        "_cfg_doc_group": "Se true, funzionerà nei gruppi; se false, no.",
        "_cfg_doc_match_type": "Tipo di corrispondenza per la risposta: 1 per uguaglianza, 2 per contiene, 3 per inizia con",
        "_cfg_doc_timer": "Tempo in secondi dopo il quale il messaggio verrà eliminato.",
        "_cls_doc": "Modulo per risposte automatiche nei messaggi privati e nei gruppi.",
        "_cmd_doc_addqa": "- aggiungi una nuova domanda e risposta. Formato: domanda:risposta",
        "_cmd_doc_delqa": "- elimina una domanda esistente per numero",
        "_cmd_doc_listqa": "- mostra l'elenco corrente delle domande e risposte",
        "_cmd_doc_cfgarm": "- apri la configurazione",
        "format": "<emoji document_id=5210952531676504517>❌</emoji> <b>Formato:</b> <code>domanda:risposta</code>",
        "added_question": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Domanda aggiunta:</b> <code>{question}</code>\n\n<emoji document_id=5443038326535759644>💬</emoji> <b>Con risposta:</b> <code>{answer}</code>",
        "specify_question_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Si prega di specificare il numero della domanda.</b>",
        "invalid_question_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Numero di domanda non valido.</b>",
        "question_removed": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Domanda numero</b> <code>{index_removed}</code> <b>rimossa.</b>",
        "dictionary_empty": "<emoji document_id=5210952531676504517>❌</emoji> <b>Il dizionario delle risposte è vuoto.</b>",
        "current_list": "<emoji document_id=5334544901428229844>ℹ️</emoji> <b>Elenco corrente:</b>\n{reply_str}"
    }

    strings_de = {
        "_cfg_doc_delay": "Verzögerung in Sekunden vor der Antwort",
        "_cfg_doc_reply_mode": "Wenn true, wird auf Nachrichten geantwortet; wenn false, nicht.",
        "_cfg_doc_private": "Wenn true, funktioniert es in privaten Nachrichten; wenn false, nicht.",
        "_cfg_doc_group": "Wenn true, funktioniert es in Gruppen; wenn false, nicht.",
        "_cfg_doc_match_type": "Der Typ der Übereinstimmung für die Antwort: 1 für Gleichheit, 2 für enthält, 3 für beginnt mit",
        "_cfg_doc_timer": "Zeit in Sekunden, nach der die Nachricht gelöscht wird.",        
        "_cls_doc": "Modul für automatische Antworten in privaten Nachrichten und Gruppen.",
        "_cmd_doc_addqa": "- eine neue Frage und Antwort hinzufügen. Format: frage:antwort",
        "_cmd_doc_delqa": "- eine bestehende Frage nach Nummer löschen",
        "_cmd_doc_listqa": "- die aktuelle Liste der Fragen und Antworten anzeigen",
        "_cmd_doc_cfgarm": "- die Konfiguration öffnen",
        "format": "<emoji document_id=5210952531676504517>❌</emoji> <b>Format:</b> <code>frage:antwort</code>",
        "added_question": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Frage hinzugefügt:</b> <code>{question}</code>\n\n<emoji document_id=5443038326535759644>💬</emoji> <b>Mit Antwort:</b> <code>{answer}</code>",
        "specify_question_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Bitte geben Sie die Frage Nummer an.</b>",
        "invalid_question_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Ungültige Frage Nummer.</b>",
        "question_removed": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Frage Nummer</b> <code>{index_removed}</code> <b>entfernt.</b>",
        "dictionary_empty": "<emoji document_id=5210952531676504517>❌</emoji> <b>Das Antwortwörterbuch ist leer.</b>",
        "current_list": "<emoji document_id=5334544901428229844>ℹ️</emoji> <b>Aktuelle Liste:</b>\n{reply_str}"
    }
    
    strings_tr = {
        "_cfg_doc_delay": "Cevap vermeden önce saniye cinsinden gecikme",
        "_cfg_doc_reply_mode": "Eğer true ise, mesajlara cevap verir; eğer false ise, cevap vermez.",
        "_cfg_doc_private": "Eğer true ise, özel mesajlarda çalışır; eğer false ise, çalışmaz.",
        "_cfg_doc_group": "Eğer true ise, gruplarda çalışır; eğer false ise, çalışmaz.",
        "_cfg_doc_match_type": "Cevap için eşleşme türü: 1 eşitlik, 2 içerir, 3 ile başlar",
        "_cfg_doc_timer": "Mesajın silineceği süre saniye cinsindendir.",
        "_cls_doc": "Özel mesajlarda ve gruplarda otomatik cevaplar için modül.",
        "_cmd_doc_addqa": "- yeni bir soru ve cevap ekleyin. Format: soru:cevap",
        "_cmd_doc_delqa": "- mevcut bir soruyu numaraya göre silin",
        "_cmd_doc_listqa": "- mevcut soru ve cevap listesini gösterin",
        "_cmd_doc_cfgarm": "- yapılandırmayı açın",
        "format": "<emoji document_id=5210952531676504517>❌</emoji> <b>Format:</b> <code>soru:cevap</code>",
        "added_question": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Soru eklendi:</b> <code>{question}</code>\n\n<emoji document_id=5443038326535759644>💬</emoji> <b>Cevap ile:</b> <code>{answer}</code>",
        "specify_question_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Lütfen soru numarasını belirtin.</b>",
        "invalid_question_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Geçersiz soru numarası.</b>",
        "question_removed": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Soru numarası</b> <code>{index_removed}</code> <b>silindi.</b>",
        "dictionary_empty": "<emoji document_id=5210952531676504517>❌</emoji> <b>Cevap sözlüğü boş.</b>",
        "current_list": "<emoji document_id=5334544901428229844>ℹ️</emoji> <b>Geçerli liste:</b>\n{reply_str}"
    }
    
    strings_uz = {
        "_cfg_doc_delay": "Javob bermasdan oldingi sekundlarda kechikish",
        "_cfg_doc_reply_mode": "Agar true bo'lsa, xabarlarga javob beradi; agar false bo'lsa, bermaydi.",
        "_cfg_doc_private": "Agar true bo'lsa, shaxsiy xabarlarda ishlaydi; agar false bo'lsa, ishlamaydi.",
        "_cfg_doc_group": "Agar true bo'lsa, guruhlarda ishlaydi; agar false bo'lsa, ishlamaydi.",
        "_cfg_doc_match_type": "Javob uchun moslik turi: 1 tenglik, 2 tarkib, 3 bilan boshlanadi",
        "_cfg_doc_timer": "Xabar o'chiriladigan vaqt (soniyada).",
        "_cls_doc": "Shaxsiy xabarlar va guruhlarda avtomatik javoblar uchun modul.",
        "_cmd_doc_addqa": "- yangi savol va javob qo'shish. Format: savol:javob",
        "_cmd_doc_delqa": "- mavjud savolni raqam bo'yicha o'chirish",
        "_cmd_doc_listqa": "- joriy savollar va javoblar ro'yxatini ko'rsatish",
        "_cmd_doc_cfgarm": "- sozlamalarni ochish",
        "format": "<emoji document_id=5210952531676504517>❌</emoji> <b>Format:</b> <code>savol:javob</code>",
        "added_question": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Savol qo'shildi:</b> <code>{question}</code>\n\n<emoji document_id=5443038326535759644>💬</emoji> <b>Javob bilan:</b> <code>{answer}</code>",
        "specify_question_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Iltimos, savol raqamini ko'rsating.</b>",
        "invalid_question_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Yaroqsiz savol raqami.</b>",
        "question_removed": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Savol raqami</b> <code>{index_removed}</code> <b>o'chirildi.</b>",
        "dictionary_empty": "<emoji document_id=5210952531676504517>❌</emoji> <b>Javob lug'ati bo'sh.</b>",
        "current_list": "<emoji document_id=5334544901428229844>ℹ️</emoji> <b>Joriy ro'yxat:</b>\n{reply_str}"
    }

    strings_es = {
        "_cfg_doc_delay": "Retraso en segundos antes de responder",
        "_cfg_doc_reply_mode": "Si es true, responderá a los mensajes; si es false, no lo hará.",
        "_cfg_doc_private": "Si es true, funcionará en mensajes privados; si es false, no lo hará.",
        "_cfg_doc_group": "Si es true, funcionará en grupos; si es false, no lo hará.",
        "_cfg_doc_match_type": "El tipo de coincidencia para la respuesta: 1 para igualdad, 2 para contiene, 3 para comienza con",
        "_cfg_doc_timer": "Tiempo en segundos después del cual el mensaje será eliminado.",
        "_cls_doc": "Módulo para respuestas automáticas en mensajes privados y grupos.",
        "_cmd_doc_addqa": "- añadir una nueva pregunta y respuesta. Formato: pregunta:respuesta",
        "_cmd_doc_delqa": "- eliminar una pregunta existente por número",
        "_cmd_doc_listqa": "- mostrar la lista actual de preguntas y respuestas",
        "_cmd_doc_cfgarm": "- abrir la configuración",
        "format": "<emoji document_id=5210952531676504517>❌</emoji> <b>Formato:</b> <code>pregunta:respuesta</code>",
        "added_question": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Pregunta añadida:</b> <code>{question}</code>\n\n<emoji document_id=5443038326535759644>💬</emoji> <b>Con respuesta:</b> <code>{answer}</code>",
        "specify_question_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Por favor, especifique el número de la pregunta.</b>",
        "invalid_question_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Número de pregunta inválido.</b>",
        "question_removed": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Pregunta número</b> <code>{index_removed}</code> <b>eliminada.</b>",
        "dictionary_empty": "<emoji document_id=5210952531676504517>❌</emoji> <b>El diccionario de respuestas está vacío.</b>",
        "current_list": "<emoji document_id=5334544901428229844>ℹ️</emoji> <b>Lista actual:</b>\n{reply_str}"
    }

    strings_kk = {
        "_cfg_doc_delay": "Жауап бермес бұрын секундтармен кідірту",
        "_cfg_doc_reply_mode": "Егер true болса, хабарламаларға жауап береді; егер false болса, жауап бермейді.",
        "_cfg_doc_private": "Егер true болса, жеке хабарламаларда жұмыс істейді; егер false болса, жұмыс істемейді.",
        "_cfg_doc_group": "Егер true болса, топтарда жұмыс істейді; егер false болса, жұмыс істемейді.",
        "_cfg_doc_match_type": "Жауапқа сәйкестік түрі: теңділік үшін 1, құрамында болуы үшін 2, X басталады үшін 3",
        "_cfg_doc_timer": "Хабарлама жойылатын уақыт (секунда).",
        "_cls_doc": "Жеке хабарламалар мен топтарда автоматты жауаптар үшін модуль.",
        "_cmd_doc_addqa": "- жаңа сұрақ пен жауап қосу. Формат: сұрақ:жауап",
        "_cmd_doc_delqa": "- ағымдағы сұрақты номер бойынша жою",
        "_cmd_doc_listqa": "- сұрақтар мен жауаптардың ағымдағы тізімін көрсету",
        "_cmd_doc_cfgarm": "- баптауларды және т.б.",
        "format": "<emoji document_id=5210952531676504517>❌</emoji> <b>Формат:</b> <code>сұрақ:жауап</code>",
        "added_question": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Сұрақ қосылды:</b> <code>{question}</code>\n\n<emoji document_id=5443038326535759644>💬</emoji> <b>Жауаппен:</b> <code>{answer}</code>",
        "specify_question_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Сұрақты анықтаңыз.</b>",
        "invalid_question_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Қате сұрақ нөмірі.</b>",
        "question_removed": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Нөмірмен сұрақ</b> <code>{index_removed}</code> <b>жойылды.</b>",
        "dictionary_empty": "<emoji document_id=5210952531676504517>❌</emoji> <b>Жауап сөздігі бос.</b>",
        "current_list": "<emoji document_id=5334544901428229844>ℹ️</emoji> <b>Ағымдағы тізім:</b>\n{reply_str}"
    }

    strings_tt = {
        "_cfg_doc_delay": "Җавап бирү алдындагы секундларда тоткарлык",
        "_cfg_doc_reply_mode": "Әгәр true булса, хәбәрләргә җавап бирәчәк; әгәр false булса, җавап бирмәячәк.",
        "_cfg_doc_private": "Әгәр true булса, шәхси хәбәрләрдә эшләячәк; әгәр false булса, эшләмәячәк.",
        "_cfg_doc_group": "Әгәр true булса, төркемнәрдә эшләячәк; әгәр false булса, эшләмәячәк.",
        "_cfg_doc_match_type": "Җавапка туры килү төре: тигез булу өчен 1, эчтәлекне белдерү өчен 2, башлану өчен 3",
        "_cfg_doc_timer": "Хәбәр юкка чыгачак вакыт (секундлар).",
        "_cls_doc": "Шәхси хәбәрләр һәм төркемнәр өчен автоматик җаваплар модуле.",
        "_cmd_doc_addqa": "- яңа сорау һәм җавап өстәү. Формат: сорау:җавап",
        "_cmd_doc_delqa": "- бар булган сорауны номер буенча бетерү",
        "_cmd_doc_listqa": "- сораулар һәм җавапларның барлык исемлеген күрсәтү",
        "_cmd_doc_cfgarm": "- көйләүләрне ачу",
        "format": "<emoji document_id=5210952531676504517>❌</emoji> <b>Формат:</b> <code>сорау:җавап</code>",
        "added_question": "<emoji document_id=5206607081334906820>✔️</emoji> <b>Сорау өстәлде:</b> <code>{question}</code>\n\n<emoji document_id=5443038326535759644>💬</emoji> <b>Җавап белән:</b> <code>{answer}</code>",
        "specify_question_number": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Сорау номерыгызны күрсәтегез.</b>",
        "invalid_question_number": "<emoji document_id=5210952531676504517>❌</emoji> <b>Ярлы сорау номеры.</b>",
        "question_removed": "<emoji document_id=5445267414562389170>🗑</emoji> <b>Сорау номеры</b> <code>{index_removed}</code> <b>бетерелде.</b>",
        "dictionary_empty": "<emoji document_id=5210952531676504517>❌</emoji> <b>Җавап сүзлек буш.</b>",
        "current_list": "<emoji document_id=5334544901428229844>ℹ️</emoji> <b>Хәзерге исемлек:</b>\n{reply_str}"
    }

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.replies = self.db.get(self.strings["name"], "replies", {})

    def config_complete(self):
        self.config = loader.ModuleConfig(
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
                True,
                doc=lambda: self.strings["_cfg_doc_group"],
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "reply_mode",
                True,
                doc=lambda: self.strings["_cfg_doc_reply_mode"],
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "match_type",
                1,
                doc=lambda: self.strings["_cfg_doc_match_type"],
                validator=loader.validators.Integer(minimum=1, maximum=3)
            ),
            loader.ConfigValue(
                "timer",
                10,
                doc=lambda: self.strings["_cfg_doc_timer"],
                validator=loader.validators.Integer(minimum=0)
            )
        )

    @loader.command()
    async def addqa(self, message):
        """- add a new question and answer. Format: question:answer"""
        args = utils.get_args_raw(message)
        if ":" not in args:
            await message.edit(self.strings["format"])
            await asyncio.sleep(self.config["timer"])
            await message.delete()
            return
        
        question, answer = map(str.strip, args.split(":", 1))
        self.replies[question.lower()] = answer
        self.db.set(self.strings["name"], "replies", self.replies)
        await message.edit(self.strings["added_question"].format(question=question, answer=answer))
        await asyncio.sleep(self.config["timer"])
        await message.delete()

    @loader.command()
    async def delqa(self, message):
        """- remove an existing question by number"""
        args = utils.get_args_raw(message).strip()
        if not args.isdigit():
            await message.edit(self.strings["specify_question_number"])
            await asyncio.sleep(self.config["timer"])
            await message.delete()
            return
        
        index = int(args) - 1
        if index < 0 or index >= len(self.replies):
            await message.edit(self.strings["invalid_question_number"])
            await asyncio.sleep(self.config["timer"])
            await message.delete()
            return
        
        question = list(self.replies.keys())[index]
        del self.replies[question]
        self.db.set(self.strings["name"], "replies", self.replies)
        await message.edit(self.strings["question_removed"].format(index_removed=index + 1))
        await asyncio.sleep(self.config["timer"])
        await message.delete()

    @loader.command()
    async def listqa(self, message):
        """- show the current list of questions and answers"""
        if not self.replies:
            await message.edit(self.strings["dictionary_empty"])
            await asyncio.sleep(self.config["timer"])
            await message.delete()
            return

        reply_str = "\n".join([f"\n\n<b>{i + 1}.</b> <code>{k}</code>\n— <code>{v}</code>" for i, (k, v) in enumerate(self.replies.items())])
        await message.edit(self.strings["current_list"].format(reply_str=reply_str))

    @loader.command()
    async def cfgarm(self, message):
        """- open configuration"""
        await self.invoke("config", "AutoReplyMod", message.peer_id)
        await message.delete()

    @loader.unrestricted
    async def watcher(self, message):
        if (message.is_private and self.config["private"]) or (message.is_group and self.config["group"]):
            sender = await self.client.get_entity(message.sender_id)
            if hasattr(sender, 'bot') and (sender.bot or message.sender_id == (await self.client.get_me()).id):
                return
            text = message.raw_text.lower()
            match_type = self.config["match_type"]
            for keyword, reply in self.replies.items():
                if match_type == 1 and keyword == text:
                    await asyncio.sleep(self.config["delay"])
                    if self.config["reply_mode"]:
                        await message.reply(reply)
                    else:
                        await message.respond(reply)
                    break
                elif match_type == 2 and keyword in text:
                    await asyncio.sleep(self.config["delay"])
                    if self.config["reply_mode"]:
                        await message.reply(reply)
                    else:
                        await message.respond(reply)
                    break
                elif match_type == 3 and text.startswith(keyword):
                    await asyncio.sleep(self.config["delay"])
                    if self.config["reply_mode"]:
                        await message.reply(reply)
                    else:
                        await message.respond(reply)
                    break
