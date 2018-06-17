from os import path
from werkzeug.utils import secure_filename
from com.completed_homeworks.models.completed_homeworks import CompletedHomeworks


class CompletedHomeworksController(object):
    def __init__(self):
        super().__init__()

    def add(self, homework_id: int, user_id: int, file_path: str, description: str, submission_date: str):
        completed_homework = CompletedHomeworks.add(homework_id, user_id, file_path, description, submission_date)
        return completed_homework

    def upload(self, file):
        up_folder = 'C:\\Python36\\Projects\\FLASK\\ACA\\eLearning\\src\\static\\uploaded_files'
        file_path = 'file not attached'
        if file:
            fname = secure_filename(file.filename)
            file_path = path.join(up_folder, fname)
            file.save(file_path)
        return file_path

    def find_by_id(self, id):
        return CompletedHomeworks.find_by_id(id)
