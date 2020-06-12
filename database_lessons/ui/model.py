from event import Event
from notify_property import NotifyProperty


class MainModel:

    db_path_changed = Event(str)
    tables_changed = Event(tuple)

    def __init__(self):
        self._db_path = NotifyProperty('db_path')
        self._db_path += self.db_path_changed.emit
        self._tables = NotifyProperty('tables')
        self._tables += self.tables_changed.emit

    @property
    def db_path(self):
        return self._db_path.get()

    @db_path.setter
    def db_path(self, value):
        self._db_path.set(value)

    def set_tables(self, value):
        self._tables.set(value)
