from sqlalchemy import Column, Integer, String
from models.base import Base, DB


class Courses(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, nullable=False)
    course_name = Column(String(30), nullable=False)
    description = Column(String(100), nullable=False)
    create_date = Column(String(30), nullable=False)

    @staticmethod
    def all():
        try:
            all = DB.query(Courses).all()
            return all
        except:
            DB.rollback()

    @staticmethod
    def new(fields: list):
        try:

            DB.add(Courses(
                course_name=fields[0],
                description=fields[1],
                create_date=fields[2]))

            DB.commit()
        except:
            DB.rollback()

    @staticmethod
    def edit(fields: list, id: int):
        try:
            DB.query(Courses).filter(Courses.id == id).update(dict(
                course_name=fields[0],
                description=fields[1]))
            DB.commit()
        except:
            DB.rollback()

    @staticmethod
    def delete(id: int):
        try:
            DB.delete(Courses.find_by_id(id))
        except:
            DB.rollback()

    @staticmethod
    def find_by_id(id: int):
        try:
            return DB.query(Courses).filter(Courses.id == id).first()
        except:
            DB.rollback()
