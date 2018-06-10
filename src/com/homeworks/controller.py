import re
from com.homeworks.models.homeworks import Homeworks


class HomeworksController(object):
    def __init__(self):
        super().__init__()

    def all(self):
        return Homeworks.all()

    def new(self, fields: list):
        self.form_is_valid(fields)
        return Homeworks.new(fields)

    def edit(self, fields: list, id: int):
        self.form_is_valid(fields)
        return Homeworks.edit(fields, id)

    def delete(self, id: int):
        return Homeworks.delete(id)

    def find_by_id(self, id):
        return Homeworks.find_by_id(id)

    @staticmethod
    def form_is_valid(fields: list):
        if len(fields[0].strip()) == 0:
            raise Exception('Lesson_id required')
        if not re.match(re.compile("[0-9/*]"), fields[0].strip()):
            raise Exception('type Lesson_id INT')
        if len(fields[1].strip()) == 0:
            raise Exception('Title required')
        if len(fields[2].strip()) == 0:
            raise Exception('Description required')
        if len(fields[3].strip()) == 0:
            raise Exception('File path required')
        if len(fields[4].strip()) == 0:
            raise Exception('Deadline required')
