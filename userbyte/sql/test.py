import threading

from sqlalchemy import Column, String, Boolean, UnicodeText, Integer, func, distinct

from userbyte.sql import SESSION, BASE


class Notes(BASE):
    __tablename__ = "notes"
    chat_id = Column(String(14), primary_key=True)
    name = Column(UnicodeText, primary_key=True)
    d_message_id = Column(Integer)

    def __init__(self, chat_id, name, d_message_id):
        self.chat_id = str(chat_id)  # ensure string
        self.name = name
        self.d_message_id = d_message_id

    def __repr__(self):
        return "<Note %s>" % self.name


Notes.__table__.create(checkfirst=True)

NOTES_INSERTION_LOCK = threading.RLock()


def add_note_to_db(chat_id, note_name, note_message_id):
    with NOTES_INSERTION_LOCK:
        prev = SESSION.query(Notes).get((str(chat_id), note_name))
        if prev:
            SESSION.delete(prev)
        note = Notes(str(chat_id), note_name, note_message_id)
        SESSION.add(note)
        SESSION.commit()


def get_note(chat_id, note_name):
    try:
        return SESSION.query(Notes).get((str(chat_id), note_name))
    finally:
        SESSION.close()
