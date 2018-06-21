from com.lessons.models.lessons import Lessons
#from com.quiz.models.quiz import Questions, Answers
from werkzeug.utils import secure_filename
from os import path
#from conf import up_conf


class LessonsController(object):

    def new(self, group_id, title, description, file_path, lesson_date):
        return Lessons.new(group_id, title, description, file_path, lesson_date)

    def upload(self, file):
        upload_path = 'C:\\Program Files\\Python36\\Python_projects\\FLASK\\ACA\\eLearning\\src\\static\\uploaded_files'
        file_path = 'file not attached'
        if file:
            filename = secure_filename(file.filename)
            file_path = path.join(upload_path, filename)
            file.save(file_path)
        return file_path

    def edit(self, title, description, file_path, lesson_date):
        return Lessons.edit(title, description, file_path, lesson_date)

    def delete(self, id):
        return Lessons.delete(id)

    def all(self, group_id):
        return Lessons.get_lessons_by_group_id(group_id)

    def get_all(self):
        return Lessons.get_all()

    def find_by_id(self, id):
        return Lessons.find_by_id(id)

<<<<<<< Updated upstream:src/com/lessons/controller.py
    def get_all(self):
        return Lessons().get_all()
=======
    def get_all_by_teacher_id(self, teacher_id: int):
        return Lessons.get_all_by_teacher_id(teacher_id)


>>>>>>> Stashed changes:src/com/lessons/controller.py
