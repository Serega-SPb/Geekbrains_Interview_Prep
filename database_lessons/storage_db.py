from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, aliased

from models_db import Base, Category, Unit, Position, Good, Employee, Vendor


def transaction(func):
    def wrapper(*args, **kwargs):
        session = args[0].session
        try:
            res = func(*args, **kwargs)
        except Exception as ex:
            print(ex)
            session.rollback()
        else:
            session.commit()
            return res
    return wrapper


class DbManager:
    DB_PATH = 'storage.db'
    _session = None

    def __init__(self, db_file=None):
        self.set_database(db_file)

    def set_database(self, db_file):
        db_connection = f'sqlite:///{db_file if db_file else self.DB_PATH}'
        self.database_engine = create_engine(db_connection, echo=False, pool_recycle=7200)
        Base.metadata.create_all(self.database_engine)
        self.session_factory = sessionmaker(bind=self.database_engine)

    @property
    def session(self):
        if self._session is None:
            self._session = scoped_session(self.session_factory)()
        return self._session

    def get_table_data(self, table_cls):
        return self.session.query(table_cls).all()

    def select_by_key(self, table_cls, key):
        return self.session.query(table_cls).get(key)

    def select_by_column(self, table_cls, column, value):
        return self.session.query(table_cls).filter_by(**{column: value}).first()

    @transaction
    def insert_in_table(self, table_cls, data):
        ins = table_cls(*data)
        self.session.add(ins)
        return ins

    @transaction
    def clear_table(self, tbl_cls):
        self.session.query(tbl_cls).delete()

    @transaction
    def delete_by_key(self, tbl_cls, key):
        obj = self.session.query(tbl_cls).get(key)
        if obj:
            self.session.delete(obj)


def test_goods(db_man):
    import random

    def insert_and_select(cls, data):
        for d in data:
            db_man.insert_in_table(cls, tuple(d))
        print('\n'.join(map(str, db_man.get_table_data(cls))))

    keys_lamd = lambda x: x[0]

    categories = [
        ('test_1', 'test_desc_1'),
        ('test_2', 'test_desc_2'),
        ('test_3', 'test_desc_3'),
    ]

    units = [('unit_1',), ('unit_2',), ('unit_3',)]

    goods = [
        ('good_1',
         random.choice(list(map(keys_lamd, units))),
         random.choice(list(map(keys_lamd, categories)))
         ),
        ('good_2',
         random.choice(list(map(keys_lamd, units))),
         random.choice(list(map(keys_lamd, categories)))
         ),
        ('good_3',
         random.choice(list(map(keys_lamd, units))),
         random.choice(list(map(keys_lamd, categories)))
         ),
    ]
    print('Clear tables categories, units, goods')
    db_man.clear_table(Category)
    db_man.clear_table(Unit)
    db_man.clear_table(Good)
    print('-'*50)

    print('Fill categories')
    insert_and_select(Category, categories)
    print('Fill units')
    insert_and_select(Unit, units)
    print('Fill goods')
    insert_and_select(Good, goods)
    print('-' * 50)

    print('Select and delete random good')
    rand_good_name = random.choice(list(map(keys_lamd, goods)))
    print(f'Random good - {rand_good_name}')
    rand_good = db_man.select_by_column(Good, 'good_name', rand_good_name)
    print(rand_good)
    print('Delete...')
    db_man.delete_by_key(Good, rand_good.good_id)
    print('Test select:')
    print(db_man.select_by_key(Good, rand_good.good_id))
    print('-' * 50)


if __name__ == '__main__':
    db = DbManager()
    test_goods(db)


