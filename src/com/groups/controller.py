import re
from com.groups.models.groups import Groups
from com.groups.models.group_student import Group_student

class GroupsController(object):
    def __init__(self):
        super().__init__()

    def all(self):
        return Groups.all()

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

    def new_student(self, fields: list):
         # self.form_is_valid(fields)
         return Group_student.new(fields)

    @staticmethod
    def form_is_valid(fields: list):
        if len(fields[0].strip()) == 0:
            raise Exception('title required')
        if len(fields[1].strip()) == 0:
            raise Exception('description required')
