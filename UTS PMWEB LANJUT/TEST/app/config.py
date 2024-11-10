import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///books.db'  # Atau gunakan MySQL URI seperti 'mysql+mysqlconnector://username:password@localhost/db_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
