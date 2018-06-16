from sqlalchemy import Column, Integer, String
from com.auth.models.users import Users
from com.groups.models.groups import Groups
from models.base import Base, DB


class Group_student(Base):
    __tablename__ = 'group_students'

    id = Column(Integer, primary_key=True, nullable=False)
    group_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    active = Column(Integer, nullable=False)
    create_date = Column(String(30), nullable=False)


    @staticmethod
    def all():
        try:
            all = DB.query(Group_student).all()
            return all
        except:
            DB.rollback()

    @staticmethod
    def get_all_groups():
        try:
            all = DB.query(Groups.id,Groups.group_name).all()
            return all
        except:
            DB.rollback()

    @staticmethod
    def new(fields: list):
        try:
            print(fields,"Hamo")
            DB.add(Group_student(
                group_id =fields[0],
                active=fields[1],
                user_id =fields[2],
                create_date = fields[3])),
            DB.commit()

        except:
            DB.rollback()

    @staticmethod
    def edit(fields: list, id: int):
        try:
            DB.query(Group_student).filter(Group_student.id == id).update(dict(
                group_name=fields[0],
                description=fields[1]))
            DB.commit()
        except:
            DB.rollback()

    @staticmethod
    def delete(id: int):
        try:
            DB.delete(Group_student.find_by_id(id))
        except:
            DB.rollback()

    @staticmethod
    def find_by_id(id: int):
        try:
            return DB.query(Group_student).filter(Group_student.id == id).first()
        except:
            DB.rollback()

    @staticmethod
    def get_student(id: int):
        try:
            return DB.query(Group_student.user_id).filter(Group_student.group_id == id).all()
        except:
            DB.rollback()

    @staticmethod
    def all_students():
        return DB.query(Users.id,Users.first_name, Users.last_name).filter(Users.role == "student").all()
