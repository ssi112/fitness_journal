"""
model.py - interface to DB

FINALLY FOUND THE F-ING MEANS TO SPECIFY THE SCHEMA IN THE MODEL DEFINITION
https://stackoverflow.com/questions/11873959/flask-sqlalchemy-postgresql-define-specific-schema-for-table

Additional info:
https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/table_config.html

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
    __tablename__ = 'customers'
    __table_args__ = {"schema": "fitness_log"}
    customer_id = Column(Integer, primary_key = True)
    first_name = Column(String(55))
    last_name = Column(String(55))
    email = Column(String(55), unique = True)
    #activebool = Column(BOOLEAN)
    #create_date = Column(DATETIME)
    #last_update = Column(DATETIME)
    birthdate = Column(DATE)
    pwdhash = Column(String(100))

    def __init__(self, first_name, last_name, birthdate, email, password):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.birthdate = birthdate.data
        self.email = email.lower()
        self.set_password(password)

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)


