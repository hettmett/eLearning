from sqlalchemy import Column, Integer, String
from com.homeworks.models.homeworks import Homeworks
from models.base import Base, DB


class CompletedHomeworks(Base):
    __tablename__ = 'completed_homeworks'
    id = Column(Integer, primary_key=True, nullable=False)
    homework_id = Column(Integer, nullable=False)#, ForeignKey('homeworks.id')
    user_id = Column(Integer, nullable=False)#, ForeignKey('users.id')
    file_path = Column(String(50), nullable=False)
    description = Column(String(256), nullable=False)
    submission_date = Column(String(20), nullable=False)
    checked = Column(Integer, nullable=True)
    rate = Column(Integer, nullable=True)

    @staticmethod
    def get_all(homework_id: int):
        return DB.query(CompletedHomeworks).filter_by(homework_id=homework_id).all()

    @staticmethod
    def get_all_by_lesson_id(lesson_id: int):
        hw_id = DB.query(Homeworks.id).filter_by(lesson_id=lesson_id).first()
        id = hw_id.id
        result = DB.query(CompletedHomeworks).filter_by(homework_id=id).all()
        return result

    @staticmethod
    def get_all_by_user_id(user_id: int):
        return DB.query(CompletedHomeworks).filter_by(user_id=user_id).all()




    @staticmethod
    def add(homework_id: int, user_id: int, file_path: str, description: str, submission_date: str):
        try:
            completed_homework = CompletedHomeworks(
                homework_id=homework_id,
                user_id=user_id,
                file_path=file_path,
                description=description,
                submission_date=submission_date)

            DB.add(completed_homework)
            DB.commit()
            return completed_homework
        except:
            DB.rollback()
            print('rollback')

    @staticmethod
    def find_by_id(id: int):
        try:
            return DB.query(CompletedHomeworks).filter_by(id=id).first()
        except:
            DB.rollback()
