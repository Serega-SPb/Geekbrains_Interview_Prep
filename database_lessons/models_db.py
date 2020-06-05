from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def get_repr(obj):
    fiels = obj.__mapper__.attrs.keys()
    fiels_str = ', '.join([f'{fld}={getattr(obj, fld)}' for fld in fiels])
    return f'<{obj.__class__.__name__}({fiels_str})>'


class Category(Base):
    __tablename__ = 'categories'

    category_name = Column(String, primary_key=True)
    category_description = Column(String)

    def __init__(self, name, desc):
        self.category_name = name
        self.category_description = desc

    def __repr__(self):
        return get_repr(self)


class Unit(Base):
    __tablename__ = 'units'

    unit = Column(String, primary_key=True)

    def __init__(self, unit):
        self.unit = unit

    def __repr__(self):
        return get_repr(self)


class Position(Base):
    __tablename__ = 'positions'

    position = Column(String, primary_key=True)

    def __init__(self, position):
        self.position = position

    def __repr__(self):
        return get_repr(self)


class Good(Base):
    __tablename__ = 'goods'

    good_id = Column(Integer, primary_key=True)
    good_name = Column(String)
    good_unit = Column(String, ForeignKey('units.unit'))
    good_cat = Column(String, ForeignKey('categories.category_name'))

    def __init__(self, name, unit, cat):
        self.good_name = name
        self.good_unit = unit
        self.good_cat = cat

    def __repr__(self):
        return get_repr(self)


class Employee(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True)
    employee_fio = Column(String)
    employee_position = Column(String, ForeignKey('positions.position'))

    def __init__(self, fio, position):
        self.employee_fio = fio
        self.employee_position = position

    def __repr__(self):
        return get_repr(self)


class Vendor(Base):
    __tablename__ = 'vendors'

    vendor_id = Column(Integer, primary_key=True)
    vendor_name = Column(String)
    vendor_ownerchipform = Column(String)
    vendor_address = Column(String)
    vendor_phone = Column(String)
    vendor_email = Column(String)

    def __init__(self, name, ownerchipform, address, phone, email):
        self.vendor_name = name
        self.vendor_ownerchipform = ownerchipform
        self.vendor_address = address
        self.vendor_phone = phone
        self.vendor_email = email

    def __repr__(self):
        return get_repr(self)
