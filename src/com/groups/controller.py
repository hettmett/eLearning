import re
from com.groups.models.groups import Groups
from com.groups.models.group_student import Group_student

class GroupsController(object):
    def __init__(self):
        super().__init__()

    def all(self):
        return Groups.all()

    def get_all(self):
        return Groups.get_all()

    def new(self, fields: list):
        self.form_is_valid(fields)
        return Groups.new(fields)

    def edit(self, fields: list, id: int):
        self.form_is_valid(fields)
        return Groups.edit(fields, id)

    def delete(self, id: int):
        return Groups.delete(id)

    def find_by_id(self, id):
        return Groups.find_by_id(id)

    def all_teachers(self):
        return Groups.all_teachers()

    def get_all_groups(self):
        return Group_student.get_all_groups()

    def all_students(self):
        return Group_student.all_students()

    def all_students_in(self,id: int):
        return Group_student.all_students_in(id)

    def new_student(self, fields: list):
         return Group_student.new(fields)

    @staticmethod
    def form_is_valid(fields: list):
        if len(fields[0].strip()) == 0:
            raise Exception('title required')
        if len(fields[1].strip()) == 0:
            raise Exception('description required')

<<<<<<< Updated upstream
=======
    def delete_user_in_group(self, id: int):
        return Group_student.delete(id)

>>>>>>> Stashed changes
    # ******************************************************
    @staticmethod
    def get_all_groups_by_teacher(teacher_id: int):
        return Groups.get_all_groups_by_teacher(teacher_id)

    @staticmethod
    def get_course_name(teacher_id: int):
        return Groups.get_course_name(teacher_id)
<<<<<<< Updated upstream
=======

    @staticmethod
    def get_group(id: int):
        return Group_student.get_group(id)

    # newwww
    @staticmethod
    def get_coures(id: int):
        return Group_student.get_coures(id)

    #newwww
    @staticmethod
    def get_coures_for_user(id: int):
        return Group_student.get_coures_for_user(id)

    @staticmethod
    def take_edit_group(id: int):
        return Groups.take_edit_group(id)
>>>>>>> Stashed changes
