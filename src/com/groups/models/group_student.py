from sqlalchemy import Column, Integer, String
from com.courses.models.courses import Courses
from com.groups.models.groups import Groups
from com.auth.models.users import Users
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
            all = DB.query(Groups.id, Groups.group_name).all()
            return all
        except:
            DB.rollback()

    @staticmethod
    def new(fields: list):
        try:
            DB.add(Group_student(
                group_id=fields[0],
                active=fields[1],
                user_id=fields[2],
                create_date=fields[3])),
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

            DB.execute("DELETE FROM group_students WHERE group_students.user_id = " + id + ";")
            # DB.delete(Group_student.find_by_id(id))
        except:
            DB.rollback()

    @staticmethod
    def find_by_id(id: int):
        try:

            return DB.query(Group_student).filter(Group_student.user_id == id).first()
        except:
            DB.rollback()

    @staticmethod
    def get_student(id: int):
        try:
            return DB.query(Group_student).filter(Group_student.group_id == id).all()
        except:
            DB.rollback()

    @staticmethod
    def all_students():
        return DB.query(Users.id, Users.first_name, Users.last_name).filter(Users.role == "student").all()

    @staticmethod
    def all_students_in(id):
        return DB.execute(
            "SELECT users.id,users.first_name,users.last_name,groups.group_name,groups.create_date,group_students.group_id,group_students.active FROM group_students INNER JOIN "
            "users ON group_students.user_id = users.id JOIN groups ON groups.id = " + id + ""
                                                                                            " WHERE group_students.group_id = " + id)

    @staticmethod
    def get_group(id: int):
        gid = DB.query(Group_student).filter(Group_student.user_id == id).first()
        group_st = DB.query(Groups).filter(Groups.id == gid.group_id).first()

        # groups = []
        # for gid in group_st:
        #     groups.append(DB.query(Groups).filter(Groups.id == gid.group_id).first())
        return group_st
    #newwww
    @staticmethod
    def get_coures(id: int):
        print(id, 'ssssssssresult')
        #result = DB.execute("SELECT * FROM groups INNER JOIN "
        #                    "courses ON groups.course_id = courses.id where  groups.teacher_id =  {}".format(id))

        cid = DB.query(Groups).filter(Groups.teacher_id == id).first()
        course_st = DB.query(Courses).filter(Courses.id == cid.course_id).first()
        print(course_st,'result')
        # groups = []
        # for gid in group_st:
        #     groups.append(DB.query(Groups).filter(Groups.id == gid.group_id).first())
        return course_st
    #newwww
    @staticmethod
    def get_coures_for_user(id: int):
        print(id, 'ssssssssresult')
        # result = DB.execute("SELECT * FROM groups INNER JOIN "
        #                    "courses ON groups.course_id = courses.id where  groups.teacher_id =  {}".format(id))
        uid = DB.query(Group_student).filter(Group_student.user_id == id).first()
        cid = DB.query(Groups).filter(Groups.id == uid.group_id).first()
        course_st = DB.query(Courses).filter(Courses.id == cid.course_id).first()
        print(course_st, 'result')
        # groups = []
        # for gid in group_st:
        #     groups.append(DB.query(Groups).filter(Groups.id == gid.group_id).first())
        return course_st


