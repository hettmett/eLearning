import re
from com.courses.models.courses import Courses


class CoursesController(object):
    def __init__(self):
        super().__init__()

    def all(self):
        return Courses.all()

    def new(self, fields: list):
        self.form_is_valid(fields)
        return Courses.new(fields)

    def edit(self, fields: list, id: int):
        self.form_is_valid(fields)
        return Courses.edit(fields, id)

    def delete(self, id: int):
        return Courses.delete(id)

    def find_by_id(self, id):
        return Courses.find_by_id(id)

    @staticmethod
    def form_is_valid(fields: list):
        if len(fields[0].strip()) == 0:
            raise Exception('title required')
        if len(fields[1].strip()) == 0:
            raise Exception('description required')


