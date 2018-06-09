from sqlalchemy import Column, Integer, String
from models.base import Base


class Users(Base):
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
