import os
from flask import Blueprint, session
from datetime import datetime
from flask import render_template, request, url_for, flash, redirect
from com.completed_homeworks.controller import CompletedHomeworksController
from com.homeworks.controller import HomeworksController
from com.auth import login_required, role_required
from werkzeug.utils import secure_filename
from conf import files_conf


completed_homeworks = Blueprint('completed_homeworks', __name__, url_prefix='/homeworks',
                                template_folder='templates', static_folder='static')


@completed_homeworks.route('/<lesson_id>')
@login_required
@role_required('student', 'teacher')
def all(lesson_id):
    homeworks = HomeworksController().all(lesson_id)
    return render_template('user_all_homeworks.html', homeworks=homeworks, user_id=session.get('user', {}).get('id'))


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
            return redirect(url_for('auth.index'))
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

#
#
# @homeworks.route('/edit/<id>/', methods=['GET', 'POST'])
# @login_required
# @role_required('teacher')
# def edit(id):
#     homework = HomeworksController().find_by_id(id)
#     if request.method == 'POST':
#         form = request.form
#         lesson_id = form.get('lesson_id')
#         title = form.get('title')
#         description = form.get('description')
#         file_path = form.get('file_path')
#         deadline = form.get('deadline')
#         modified = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         try:
#             HomeworksController().edit(id, lesson_id, title, description, file_path, deadline, modified)
#             return redirect(url_for('homeworks.all'))
#         except Exception as ex:
#             flash(ex)
#     return render_template('edit_homework.html', homework=homework)
#
#
# @homeworks.route('/delete/<id>')
# @login_required
# @role_required('teacher')
# def remove(id):
#     HomeworksController().remove(id)
#     return redirect(url_for('homeworks.all'))
#
#
# @homeworks.route('/<id>')
# @login_required
# def show_one(id):
#     homework = HomeworksController().find_by_id(id)
#     return render_template('one_homework.html', homework=homework)
