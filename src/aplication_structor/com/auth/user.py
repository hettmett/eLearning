from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(64), unique=True)
    last_name = Column(String(30))
    first_name = Column(String(30))
    middle_name = Column(String(30))
    birth_date = Column(String(10))
    role = Column(String(10))
    token = Column(String(64), unique=True)
    rate = Column(Integer)
    created = Column(String(30))
    modified = Column(String(30))

    def __init__(self, name=None, email=None, password=None, last_name=None,
                 first_name=None, middle_name=None, birth_date=None, role=None,
                 token=None, rate=None, created=None, modified=None):
        super().__init__()
        self.name = name
        self.email = email
        self.password = password
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.birth_date = birth_date
        self.role = role
        self.token = token
        self.rate = rate
        self.created = created
        self.modified = modified

    def __repr__(self):
        return "<User(email = {}, first_name = {}, middle_name = {} ," \
               "last_name = {}, birth_date = {}, role = {}," \
               "token = {}, rate = {}, created = {}, modified = {} )>".format(
            self.email, self.first_name, self.middle_name, self.last_name,
            self.birth_date, self.role, self.token, self.rate,
            self.created, self.modified
        )
    
#
# user = User(email='gmail@mail.ru', password='4321', last_name='lnm2', first_name='fnm2', middle_name='mnm2',
#             birth_date='10-10-2000', role='student', token='564231a21we456erg2fh5t6y42f3dt56u4hg145',
#             created=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
# session.add(user)
# session.commit()
