import os
from sqlalchemy import create_engine
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS =True

class LocalDevelopmentConfig(Config):
    SQLITE_DB_DIR = os.path.join(basedir, "db_directory")
    SQLALCHEMY_DATABASE_URI = "sqlite:///./db_directory/database.sqlite3"
    DEBUG = False
    engine = create_engine(SQLALCHEMY_DATABASE_URI)

