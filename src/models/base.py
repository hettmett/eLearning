from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from conf import db_conf


Base = declarative_base()  # Base mapping class

# create database engine and establish connection
engine = create_engine(db_conf['path'])
Session = sessionmaker(bind=engine)
DB = Session()