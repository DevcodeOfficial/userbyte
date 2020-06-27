import threading

from sqlalchemy import Column, String, Boolean, UnicodeText, Integer, func, distinct

from userbyte.sql import SESSION, BASE


class Notes(BASE):
    __tablename__ = "notes"
    chat_id = Column(String(14), primary_key=True)
    name = Column(UnicodeText)

    def __init__(self, chat_id, name):
        self.chat_id = str(chat_id)  # ensure string
        self.name = name

    def __repr__(self):
        return "<Note %s>" % self.name


Notes.__table__.create(checkfirst=True)

NOTES_INSERTION_LOCK = threading.RLock()


def add_note_to_db(chat_id, note_name):
    with NOTES_INSERTION_LOCK:
        prev = SESSION.query(Notes).get((str(chat_id)))
        if prev:
            SESSION.delete(prev)
        note = Notes(str(chat_id), note_name)
        SESSION.add(note)
        SESSION.commit()


def get_note(chat_id):
    try:
        return SESSION.query(Notes).get((str(chat_id)))
    finally:
        SESSION.close()
