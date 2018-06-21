from sqlalchemy import Column, Integer, String
from com.auth.models.users import Users
from models.base import Base, DB


class Groups(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, nullable=False)
    group_name = Column(String(30), nullable=False)
    course_id = Column(Integer, nullable=False)
    start_date = Column(String(100), nullable=False)
    end_date = Column(String(100), nullable=False)
    create_date = Column(String(30), nullable=False)
    teacher_id = Column(Integer)

    @staticmethod
    def get_all():
        try:
            return DB.query(Groups).all()
        except Exception:
            DB.rollback()


    @staticmethod
    def all():
        result = DB.execute(
            "SELECT groups.id,groups.group_name,users.first_name,courses.course_name FROM groups INNER JOIN "
            "users ON groups.teacher_id = users.id JOIN courses ON groups.course_id = courses.id")
        return result

    @staticmethod
    def new(fields: list):
        DB.add(Groups(
            group_name=fields[0],
            course_id=fields[1],
            start_date=fields[2],
            end_date=fields[3],
<<<<<<< Updated upstream
            create_date = fields[4],
            teacher_id = fields[5]))
        #
        # DB.execute("INSERT INTO groups (group_name,course_id, start_date, end_date, create_date, teacher_id)"
        #            "VALUES ("+fields[0]+","+fields[1]+","+fields[2]+","+fields[3]+","+fields[4]+","+fields[5]+")")

=======
            create_date=fields[4],
            teacher_id=fields[5]))
>>>>>>> Stashed changes
        DB.commit()

    @staticmethod
    def edit(fields: list, id: int):
        try:
            DB.query(Groups).filter(Groups.id == id).update(dict(
                group_name=fields[0],
                course_id=fields[1],
                start_date=fields[2],
                end_date=fields[3],
                create_date=fields[4],
                teacher_id=fields[5]))
            DB.commit()
        except:
            DB.rollback()

    @staticmethod
    def delete(id: int):
        try:
            # DB.delete(Groups).filter_by(id=id)
            DB.execute("DELETE FROM groups WHERE groups.id = {};".format(id))
        except:
            DB.rollback()

    @staticmethod
    def find_by_id(id: int):
        try:
            return DB.query(Groups).filter(Groups.id == id).first()
        except:
            DB.rollback()

    @staticmethod
    def all_teachers():
        return DB.query(Users.id, Users.first_name, Users.last_name).filter(Users.role == "teacher").all()

    @staticmethod
<<<<<<< Updated upstream
    def all_students():
        return DB.query(Users.id, Users.first_name, Users.last_name).filter(Users.role == "student").all()

    @staticmethod
=======
>>>>>>> Stashed changes
    def get_all_groups():
        try:
            all = DB.query(Groups.id, Groups.group_name).all()
            return all
        except:
            DB.rollback()

    # **********************************************************************************************
    @staticmethod
<<<<<<< Updated upstream
    def get_course_name(teacher_id: int):
        course_id = DB.query(Groups.course_id).filter_by(teacher_id=teacher_id).first()
        course_name = DB.query(Courses.course_name).filter_by(id=course_id).first()
        # course_name = DB.execute("select groups.group_name, courses.course_name from groups "
        #                     "INNER JOIN courses ON groups.course_id = courses.id "
        #                     "where  groups.teacher_id = ?", teacher_id)
        return course_name

    @staticmethod
    def get_all_groups_by_teacher(teacher_id: int):
        return DB.query(Groups.group_name).filter_by(teacher_id=teacher_id).all()
=======
    def get_all_groups_by_teacher(teacher_id: int):
        # res = DB.execute("select groups.id,groups.group_name from groups WHERE groups.teacher_id="+teacher_id)
        res = DB.query(Groups).filter_by(teacher_id=teacher_id).first()
        return res

    @staticmethod
    def get_course_name(teacher_id):
        return DB.execute("SELECT courses.id, courses.course_name FROM groups INNER JOIN courses ON "
                          "groups.course_id = courses.id WHERE groups.teacher_id={}".format(teacher_id))

    @staticmethod
    def get_teacher_courses(id):
        print(id)
        course = DB.execute(
            "SELECT courses.course_name FROM groups INNER JOIN courses ON groups.course_id = courses.id where groups.teacher_id = " + id)
        return course

    @staticmethod
    def take_edit_group(id):
        return DB.query(Groups.group_name, Groups.course_id, Groups.start_date, Groups.end_date,
                        Groups.teacher_id).filter(Groups.id == id).all()
>>>>>>> Stashed changes
