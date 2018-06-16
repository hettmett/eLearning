from sqlalchemy import Column, Integer, String, ForeignKey
from com.homeworks.models.homeworks import Homeworks
from sqlalchemy.orm import relationship
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

    # homeworks = relationship("Homeworks", foreign_keys=['homeworks_id'])
    # users = relationship("Users", foreign_keys=['users_id'])

    @staticmethod
    def add(homework_id: int, user_id: int, file_path: str, description: str, submission_date: str):
        try:
            completed_homework = CompletedHomeworks(
                homework_id=homework_id,
                user_id=user_id,
                file_path=file_path,
                description=description,
                submission_date=submission_date)

            print(f'id = {completed_homework.id}')
            print(f'user_id = {completed_homework.user_id}')
            print(f'homework_id = {completed_homework.homework_id}')
            print(f'file_path = {completed_homework.file_path}')
            print(f'description = {completed_homework.description}')
            print(f'submission_date = {completed_homework.submission_date}')

            DB.add(completed_homework)
            DB.commit()
            return completed_homework
        except:
            DB.rollback()
            print('rollback')

    #
    # @staticmethod
    # def edit(id: int, lesson_id: int, title: str, description: str, file_path: str, deadline: str, modified: str):
    #     try:
    #         DB.query(CompletedHomeworks).filter(CompletedHomeworks.id == id).update(dict(
    #             lesson_id=lesson_id,
    #             title=title,
    #             description=description,
    #             file_path=file_path,
    #             deadline=deadline,
    #             modified=modified))
    #         DB.commit()
    #     except:
    #         DB.rollback()
    #
    #
    # @staticmethod
    # def remove(id: int):
    #     try:
    #         DB.remove(CompletedHomeworks.find_by_id(id))
    #     except:
    #         DB.rollback()
    #

    @staticmethod
    def find_by_id(id: int):
        try:
            return DB.query(CompletedHomeworks).filter_by(id == id).first()
        except:
            DB.rollback()
