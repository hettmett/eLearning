from sqlalchemy import Column, Integer, String,Date, select, literal, and_, exists
from sqlalchemy.sql import table, column, select, update, insert
from sqlalchemy.schema import ForeignKey
from models.base import Base, DB
from com.courses.models.courses import Courses
from com.auth.models.users import Users
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker

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
    def all():
            #all = DB.query(Groups).all()
            result = DB.execute("select groups.group_name,users.first_name,courses.course_name from groups INNER JOIN "
                               "users ON groups.teacher_id = users.id JOIN courses ON groups.course_id = courses.id")


            #query = DB.query(Groups, Users, Courses)
            #query = query.join(Groups, Groups.teacher_id == Users.id)
           # query = query.join(Courses, Groups.course_id == Courses.id)
            #records = query.all()
            return result

    @staticmethod
    def new(fields: list):
        #try:
        print(fields,"kkkkkkkkkkk")

        DB.add(Groups(
            group_name =fields[0],
            course_id =fields[1],
            start_date =fields[2],
            end_date=fields[3],
            create_date = fields[4],
            teacher_id = fields[5]))
        """
        DB.execute("INSERT INTO groups (group_name,course_id, start_date, end_date, create_date, teacher_id)"
                   "VALUES ("+fields[0]+","+fields[1]+","+fields[2]+","+fields[3]+","+fields[4]+","+fields[5]+")")
        """
        DB.commit()
       # except:
       #     DB.rollback()

    @staticmethod
    def edit(fields: list, id: int):
        try:
            DB.query(Groups).filter(Groups.id == id).update(dict(
                group_name=fields[0],
                description=fields[1]))
            DB.commit()
        except:
            DB.rollback()

    @staticmethod
    def delete(id: int):
        try:
            DB.delete(Groups.find_by_id(id))
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
    def all_students():
        return DB.query(Users.id, Users.first_name, Users.last_name).filter(Users.role == "student").all()

    def get_all_groups():
        try:
            all = DB.query(Groups.id,Groups.group_name).all()
            return all
        except:
            DB.rollback()

#sql_cmd = DB.text("select groups.group_name,users.first_name,courses.course_name from groups INNER JOIN "
 #                               "users ON groups.teacher_id = users.id JOIN courses ON groups.course_id = courses.id")
  #          results = db.execute(sql_cmd).fetchall()