from sqlalchemy import Column, Integer, String, ForeignKey
from src.models.base import Base, DB


class Groups(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    course_id = Column(Integer, ForeignKey('courses.id'))
    start_date = Column(String(20))
    end_date = Column(String(20))
    teacher_id = Column(Integer, ForeignKey('users.id'))
    created = Column(String(20))
    modified = Column(String(20))

    @property
    def __repr__(self):
        return "<Group(name = {}, course_id = {}, start_date = {}, " \
                "end_date = {}, teacher_id = {}, created = {}, modified = {} )>".format(
                self.name, self.course_id, self. start_date,
                self.end_date, self.teacher_id, self.created, self.modified)

    @staticmethod
    def get_all_groups(id):
        return DB.session.query(Groups).filter(Groups.teacher_id == id).all()

    @staticmethod
    def new(group_name, course_id, start_date, end_date, teacher_id, modified):
        try:
            DB.add(Groups(
                group_name=group_name,
                course_id=course_id,
                start_date=start_date,
                end_date=end_date,
                teacher_id=teacher_id,
                modified=modified
            ))
        except:
            DB.rollback()

    @staticmethod
    def get_lessons(group_id):
        return DB.query(Groups).filter(Groups.group_id == group_id).all()
