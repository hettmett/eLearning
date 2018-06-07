from src.com.homeworks.models.homeworks import Homeworks


class HomeworksController(object):
    def __init__(self):
        pass

    def all(self):
        return Homeworks.all()

    def new(self, lesson_id, title, description, file_path, deadline, created):
        if len(lesson_id) == 0:
            raise Exception('lesson_id required')
        if not int(lesson_id):
            raise Exception('type lesson_id INT')

        return Homeworks.new(lesson_id, title, description, file_path, deadline, created)

    def edit(self, fields: list, id: int):
        return Homeworks.edit(fields, id)

    def delete(self, id: int):
        return Homeworks.delete(id)

    def find_by_id(self, id):
        return Homeworks.find_by_id(id)
