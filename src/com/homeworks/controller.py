import re
from com.homeworks.models.homeworks import Homeworks
from os import path
from werkzeug.utils import secure_filename


class HomeworksController(object):
    def __init__(self):
        super().__init__()

    def all(self):
        return Homeworks.all()

    def upload(self, file):
        up_folder = 'C:\\Python36\\Projects\\FLASK\\ACA\\eLearning\\src\\static\\uploaded_files'
        file_path = 'file not attached'
        if file:
            fname = secure_filename(file.filename)
            file_path = path.join(up_folder, fname)
            file.save(file_path)
        return file_path

    def add(self, lesson_id: int, title: str, description: str, file_path: str, deadline: str):
        self.form_is_valid(lesson_id, title, description, file_path, deadline)
        return Homeworks.add(lesson_id, title, description, file_path, deadline)

    def edit(self, id: int, lesson_id: int, title: str, description: str, file_path: str, deadline: str):
        self.form_is_valid(lesson_id, title, description, file_path, deadline)
        return Homeworks.edit(id, lesson_id, title, description, file_path, deadline)

    def remove(self, id: int):
        return Homeworks.remove(id)

    def find_by_id(self, id):
        return Homeworks.find_by_id(id)

    @staticmethod
    def form_is_valid(lesson_id: int, title: str, description: str, file_path: str, deadline: str):
        if len(str(lesson_id)) == 0:
            raise Exception('Lesson_id required')
        if not re.match(re.compile("[0-9/*]"), str(lesson_id)):
            raise Exception('type Lesson_id INT')
        if len(title.strip()) == 0:
            raise Exception('Title required')
        if len(description.strip()) == 0:
            raise Exception('Description required')
        if len(file_path.strip()) == 0:
            raise Exception('File path required')
        if len(deadline.strip()) == 0:
            raise Exception('Deadline required')
