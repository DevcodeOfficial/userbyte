import threading

from sqlalchemy import Column, String, Boolean, UnicodeText, Integer, func, distinct

from userbyte.sql import SESSION, BASE


class Notes(BASE):
    __tablename__ = "notes"
    name = Column(UnicodeText, primary_key=True)
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return "<Note %s>" % self.name


Notes.__table__.create(checkfirst=True)

NOTES_INSERTION_LOCK = threading.RLock()


def add_note_to_db(note_name):
    with NOTES_INSERTION_LOCK:
        prev = SESSION.query(Notes).get((note_name))
        if prev:
            SESSION.delete(prev)
        note = Notes(note_name)
        SESSION.add(note)
        SESSION.commit()


def get_note(note_name):
    try:
        return SESSION.query(Notes).get((note_name))
    finally:
        SESSION.close()
