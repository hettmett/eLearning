from os import path
from flask import Blueprint, session
from datetime import datetime
from flask import render_template, request, url_for, flash, redirect, send_from_directory
from com.completed_homeworks.controller import CompletedHomeworksController
from com.homeworks.controller import HomeworksController
from com.auth import login_required, role_required
from werkzeug.utils import secure_filename
from conf import files_conf


completed_homeworks = Blueprint('completed_homeworks', __name__, url_prefix='/completed_homeworks',
                                template_folder='templates', static_folder='static')


@completed_homeworks.route('/by_lesson/<lesson_id>')
@login_required
@role_required('student', 'teacher')
def get_all_by_lesson_id(lesson_id: int):
    homeworks = CompletedHomeworksController().get_all_by_lesson_id(lesson_id)
    return render_template('lesson_all_homeworks.html', homeworks=homeworks, user_id=session.get('user', {}).get('id'))

@completed_homeworks.route('/by_student/<user_id>')
@login_required
@role_required('student', 'teacher')
def get_all_by_user_id(user_id: int):
    user_id = session.get( 'user', {} ).get( 'id' )
    homeworks = CompletedHomeworksController().get_all_by_user_id(user_id)
    return render_template('user_all_homeworks.html', homeworks=homeworks, user_id=user_id)

@completed_homeworks.route('/by_homework/<homework_id>')
@login_required
@role_required('student', 'teacher')
def get_all(homework_id: int):
    homeworks = CompletedHomeworksController().get_all(homework_id)
    print(homework_id, session.get('user', {}).get('id'))
    return render_template('hw_all_homeworks.html', homeworks=homeworks, user_id=session.get('user', {}).get('id'))


@completed_homeworks.route('/<user_id>/<homework_id>/add', methods=['GET', 'POST'])
@login_required
@role_required('student', 'teacher')
def add(user_id: int, homework_id: int):
    if request.method == 'POST':
        form = request.form
        file_path = CompletedHomeworksController().upload(request.files.get('file'))
        description = form.get('description')
        submission_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            CompletedHomeworksController().add(homework_id, user_id, file_path, description, submission_date)
            flash('file attached successfully')
            return redirect(url_for('dashboard.Dashboard'))
        except Exception as ex:
            flash(ex)
    return render_template('submit_homework.html')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in files_conf.get('allowed_extensions')


@completed_homeworks.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for('auth.index'))
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(files_conf.get('upload_folder'), filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))


@completed_homeworks.route("/by_id/<id>", methods=["GET", "POST"])
@login_required
def show(id):
    homework = CompletedHomeworksController().find_by_id(id)
    filename = "file not attached"
    if homework.file_path is not None:
        filename = path.basename( homework.file_path )
    return render_template('user_one_homework.html',  homework=homework, filename=filename)


@completed_homeworks.route('files/<filename>', methods=['GET', 'POST'])
@login_required
def download(group_id, filename):
    dir = 'C:\\Program Files\\Python36\\Python_projects\\FLASK\\ACA\\eLearning\\src\\static\\uploaded_files'
    return send_from_directory(directory=dir, filename=filename)
