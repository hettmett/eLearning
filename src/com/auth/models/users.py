import hashlib
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, Integer, String
from models.base import Base, DB


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(64), unique=True)
    last_name = Column(String(30))
    first_name = Column(String(30))
    middle_name = Column(String(30))
    birth_date = Column(String(30))
    role = Column(String(10))
    token = Column(String(64), unique=True)
    create_date = Column(String(30))

    def __init__(self, name=None, email=None, password=None, last_name=None,
                 first_name=None, middle_name=None, birth_date=None, role=None,
                 token=None, create_date=None):
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
        self.create_date = create_date

    def __repr__(self):
        return "<User(email = {}, first_name = {}, middle_name = {} ," \
               "last_name = {}, birth_date = {}, role = {}," \
               "token = {}, create_date = {})>".format(
            self.email, self.first_name, self.middle_name, self.last_name,
            self.birth_date, self.role, self.token,
            self.create_date
        )

    @staticmethod
    def login(email: str, pwd: str):
        password = hashlib.sha512(pwd.encode('utf-8')).hexdigest()
        user = DB.query(Users).filter(Users.email == email, Users.password == password).first()
        return user

    @staticmethod
    def new(fields: list):
        try:
            user = Users(
                first_name=fields[0],
                last_name=fields[1],
                email=fields[2],
                role=fields[3],
                token=str(uuid4()),
                create_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            DB.add(user)
            DB.commit()
            return user
        except:
            DB.rollback()

    @staticmethod
    def change_password(id: int, password: str):
        try:
            our_user = DB.query(Users).filter_by(id=id).first()
            if our_user is not None:
                print(id,password)
                print(our_user.first_name)
                our_user.password = hashlib.sha512(password.encode('utf-8')).hexdigest()
                DB.commit()
                return our_user
        except:
            DB.rollback()

    @staticmethod
    def check_token(token: str):
        return DB.query(Users).filter_by(token=token).first()

    @staticmethod
    def get_all():
        try:
            return DB.query(Users).all()
        except:
            DB.rollback()

    @staticmethod
    def edit(fields: list, id: int):
        try:
            DB.query( Users ).filter( Users.id == id ).update( dict(
                email=fields[0],
                first_name=fields[1],
                last_name=fields[2],
                middle_name=fields[3],
                birth_date=fields[4],
                role=fields[5]))
            DB.commit()
        except:
            DB.rollback()

    @staticmethod
    def delete(id: int):
        try:
            DB.delete(Users.find_by_id(id))
            DB.commit()
        except:
            DB.rollback()

    @staticmethod
    def find_by_id(id: int):
        try:
            return DB.query(Users).filter(Users.id == id ).first()
        except:
            DB.rollback()
