from storage_db import DbManager


class TableModel:

    def __init__(self, db_man, table_name):
        self._db_man = db_man
        self._table_name = table_name
        self._columns = tuple(db_man.get_table_columns(table_name))

    @property
    def name(self):
        return self._table_name

    @property
    def columns(self):
        return self._columns

    @property
    def data(self):
        return self._db_man.get_table_data(self.name)

    def insert(self, data):
        return self._db_man.insert_in_table(self.name, data)

    def update(self, key, data_pair):
        self._db_man.update_data_in_table(self.name, key, data_pair)

    def delete(self, key):
        self._db_man.delete_by_key(self.name, key)


class MainController:

    def __init__(self, model):
        self.model = model
        self.db_man: DbManager = None

    def set_db_path(self, value):
        if self.db_man is None:
            self.db_man = DbManager(value)
        else:
            self.db_man.set_database(value)
        self.model.db_path = value
        self.load_db()

    def load_db(self):
        mods = []
        for tbl in self.db_man.tables:
            mods.append(TableModel(self.db_man, tbl))
        self.model.set_tables(tuple(mods))
