from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src import config

SQLALCHEMY_DATABASE_URL = config.INVISO_DB_CONN

engine = create_engine(SQLALCHEMY_DATABASE_URL, future=True) # todo remove future from sqlalchemy >= 2.0
SessionLocal = sessionmaker(autoflush=False, bind=engine) # autocommit deprecated from sqlalchemy 2.0

Base = declarative_base()