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
        up_folder = 'C:\\Program Files\\Python36\\Python_projects\\FLASK\\eLearning\\src\\static\\uploaded_files'
        file_path = 'file not attached'
        if file:
            fname = secure_filename(file.filename)
            file_path = path.join(up_folder, fname)
            file.save(file_path)
        return file_path

    def find_by_id(self, id):
        return CompletedHomeworks.find_by_id(id)

    # def edit(self, id: int, lesson_id: int, title: str, description: str, file_path: str, deadline: str, modified: str):
    #     self.form_is_valid(lesson_id, title, description, file_path, deadline)
    #     return CompletedHomeworks.edit(id, lesson_id, title, description, file_path, deadline, modified)
    #
    # def remove(self, id: int):
    #     return CompletedHomeworks.remove(id)


    # @staticmethod
    # def form_is_valid(homework_id: int, user_id: int, rate: int, checked: bool,
    #         file_path: str, description: str, submission_date: str):
    #     if len(str(homework_id)) == 0:
    #         raise Exception('homework_id required')
    #     if not re.match(re.compile("[0-9/*]"), str(homework_id)):
    #         raise Exception('type Lesson_id INT')
    #     if len(.strip()) == 0:
    #         raise Exception('Title required')
    #     if len(description.strip()) == 0:
    #         raise Exception('Description required')
    #     if len(file_path.strip()) == 0:
    #         raise Exception('File path required')
    #     if len(deadline.strip()) == 0:
    #         raise Exception('Deadline required')
