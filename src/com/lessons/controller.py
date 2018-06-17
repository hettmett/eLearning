from com.lessons.models.lessons import Lessons
#from com.quiz.models.quiz import Questions, Answers
from werkzeug.utils import secure_filename
from os import path
#from conf import up_conf


class LessonsController(object):

    def new(self, group_id, title, description, file_path, lesson_date):
        return Lessons.new(group_id, title, description, file_path, lesson_date)

    def upload(self, file):
        UPLOAD_FOLDER = 'C:\\Python36\\Projects\\FLASK\\ACA\\eLearning\\src\\static\\uploaded_files'
        if file:
            filename = secure_filename(file.filename)
            file_path = path.join(UPLOAD_FOLDER, filename)
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
