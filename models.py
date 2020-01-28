"""
model.py - interface to DB
"""
from sqlalchemy import Column, ForeignKey, Integer, String, BOOLEAN, DATE, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from werkzeug import generate_password_hash, check_password_hash

# inherit features from sqlalchemy classes that correspond to tables in DB
Base = declarative_base()

# OOP representation of tables in DB
class Customers(Base):
    __tablename__ = 'customer'
    customer_id = Column(Integer, primary_key = True)
    first_name = Column(String(55))
    last_name = Column(String(55))
    email = Column(String(55), unique = True)
    activebool = Column(BOOLEAN)
    create_date = Column(DATETIME)
    last_update = Column(DATETIME)
    birthdate = Column(DATE)
    pwdhash = Column(String(100))

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email.lower()
        self.set_password(password)

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)


