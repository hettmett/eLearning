from sqlalchemy import Column, Integer, String
from src.models.base import Base, DB


class Homeworks(Base):
    __tablename__ = 'homeworks'

    id = Column(Integer, primary_key=True, nullable=False)
    lesson_id = Column(Integer, nullable=False)  # foreign_key
    title = Column(String(50), nullable=False)
    description = Column(String(100), nullable=False)
    file_path = Column(String(50), nullable=False)
    deadline = Column(String(30), nullable=False)
    created = Column(String(30), nullable=False)
    modified = Column(String(30), nullable=True)

    @staticmethod
    def all():
        try:
            return DB.query(Homeworks).order_by(Homeworks.id.desc()).limit(10).all()
        except:
            DB.rollback()

    @staticmethod
    def new(lesson_id, title, description, file_path, deadline, created):
        try:
            DB.add(Homeworks(
                lesson_id=lesson_id,
                title=title,
                description=description,
                file_path=file_path,
                deadline=deadline,
                created=created))
            DB.commit()
        except:
            DB.rollback()

    @staticmethod
    def edit(fields: list, id: int):
        try:
            DB.query(Homeworks).filter(Homeworks.id == id).update(dict(
                lesson_id=fields[0],
                title=fields[1],
                description=fields[2],
                file_path=fields[3],
                deadline=fields[4],
                modified=fields[5]))
            DB.commit()
        except:
            DB.rollback()

    @staticmethod
    def delete(id: int):
        try:
            DB.delete(Homeworks.find_by_id(id))
        except:
            DB.rollback()

    @staticmethod
    def find_by_id(id: int):
        try:
            return DB.query(Homeworks).filter(Homeworks.id == id).first()
        except:
            DB.rollback()
