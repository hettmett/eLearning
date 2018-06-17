from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base, DB


class Homeworks(Base):
    __tablename__ = 'homeworks'

    id = Column(Integer, primary_key=True, nullable=False)
    lesson_id = Column(Integer, nullable=False)  # foreign_key
    title = Column(String(50), nullable=False)
    description = Column(String(100), nullable=False)
    file_path = Column(String(50), nullable=False)
    deadline = Column(String(30), nullable=False)

    @staticmethod
    def all():
        try:
            return DB.query(Homeworks).all()
        except:
            DB.rollback()

    @staticmethod
    def add(lesson_id: int, title: str, description: str, file_path: str, deadline: str):
        try:
            homework = Homeworks(
                lesson_id=lesson_id,
                title=title,
                description=description,
                file_path=file_path,
                deadline=deadline)
            DB.add(homework)
            DB.commit()
        except:
            DB.rollback()

    @staticmethod
    def edit(id: int, lesson_id: int, title: str, description: str, file_path: str, deadline: str):
        DB.query(Homeworks).filter(Homeworks.id == id).update(dict(
            lesson_id=lesson_id,
            title=title,
            description=description,
            file_path=file_path,
            deadline=deadline))
        try:
            DB.commit()
        except:
            DB.rollback()

    @staticmethod
    def remove(id: int):
        try:
            DB.remove(Homeworks.find_by_id(id))
        except:
            DB.rollback()

    @staticmethod
    def find_by_id(id: int):
        try:
            return DB.query(Homeworks).filter(Homeworks.id == id).first()
        except:
            DB.rollback()
