from sqlalchemy import Column, Integer, String, ForeignKey
from com.groups.models.groups import Groups
from sqlalchemy.orm import relationship
from models.base import Base, DB


class Lessons(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer) #, ForeignKey('groups.id')
    title = Column(String(255))
    file_path = Column(String(50))
    description = Column(String(255))
    lesson_date = Column(String(30))
    # group = relationship(Groups)

    @staticmethod
    def get_lessons_by_group_id(group_id):
        return DB.query(Lessons).filter(Lessons.group_id == group_id).all()

    @staticmethod
    def new(group_id, title, description, file_path, lesson_date):
        lesson = Lessons(
            group_id = group_id,
            title=title,
            description=description,
            file_path=file_path,
            lesson_date=lesson_date
        )
        DB.add(lesson)
        DB.commit()

    @staticmethod
    def get_all():
        return DB.query(Lessons).all()


    @staticmethod
    def edit(title, description, file_path, lesson_date):
        try:
            DB.query(Lessons).filter(Lessons.id == id).update(dict(title=title,
                                                                   description=description,
                                                                   file_path=file_path,
                                                                   lesson_date=lesson_date
                                                                   ))
            DB.commit()
        except:
            DB.rollback()

    @staticmethod
    def delete(id: int):
        try:
            DB.delete(Lessons.find_by_id(id))
        except:
            DB.rollback()

    @staticmethod
    def find_by_id(id):
        return DB.query(Lessons).filter(Lessons.id == id).first()

    @staticmethod
<<<<<<< Updated upstream
    def get_all():
        try:
            DB.query(Lessons).all()
        except Exception:
            DB.rollback()
=======
    def get_all_by_teacher_id(teacher_id: int):
        return DB.query(Lessons).filter(Lessons.id == id).first()

>>>>>>> Stashed changes
