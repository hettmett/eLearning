from flask import Blueprint, send_from_directory, session
from datetime import datetime
from flask import render_template, request, url_for, flash, redirect
from com.lessons.controller import LessonsController
from com.homeworks.controller import HomeworksController
from com.auth import login_required, role_required
from os import path

homeworks = Blueprint('homeworks', __name__, url_prefix='/homeworks',
                      template_folder='templates', static_folder='static')


@homeworks.route('/')
@login_required
<<<<<<< Updated upstream
@role_required('teacher')
def all():
    homeworks = HomeworksController().all()
    return render_template('all_homeworks.html', homeworks=homeworks)
=======
@role_required('teacher', 'student')
def all(lesson_id: int):
    homeworks = HomeworksController().all(lesson_id)
    return render_template('all_homeworks.html', homeworks=homeworks, lesson_id=lesson_id)
>>>>>>> Stashed changes


@homeworks.route('/add', methods=['GET', 'POST'])
@login_required
@role_required('teacher', 'student')
def add():
    lessons = LessonsController().get_all()
    fields = []
    print(session)
    if request.method == 'POST':
        form = request.form
        lesson_id = form.get('lesson_id')
        title = form.get('title')
        description = form.get('description')
        file_path = HomeworksController().upload(request.files.get('file_path'))
        deadline = form.get('deadline')
        try:
            HomeworksController().add(lesson_id, title, description, file_path, deadline)
<<<<<<< Updated upstream
            return redirect(url_for('homeworks.all'))
        except Exception as ex:
            flash(ex)
    return render_template('add_homework.html', lessons=lessons, fields=fields)
=======
            return redirect(url_for('lessons.get_all'))
        except Exception as ex:
            flash(ex)
    return render_template('add_homework.html', lessons=lessons, fields=fields, group_id=session['group']['id'])
>>>>>>> Stashed changes


@homeworks.route('/edit/<id>/', methods=['GET', 'POST'])
@login_required
@role_required('teacher', 'student')
def edit(id):
    lessons = LessonsController().get_all()
    homework = HomeworksController().find_by_id(id)
    if request.method == 'POST':
        form = request.form
        lesson_id = form.get('lesson_id')
        title = form.get('title')
        description = form.get('description')
        file_path = HomeworksController().upload(request.files.get('file_path'))
        deadline = form.get('deadline')
        try:
            HomeworksController().edit(id, lesson_id, title, description, file_path, deadline)
<<<<<<< Updated upstream
            return redirect(url_for('homeworks.all'))
=======
            return redirect(url_for('dashboard.Dashboard'))
>>>>>>> Stashed changes
        except Exception as ex:
            flash(ex)
    return render_template('edit_homework.html', lessons=lessons, homework=homework)


@homeworks.route('/remove/<id>')
@login_required
@role_required('teacher', 'student')
def remove(id):
    HomeworksController().remove(id)
    return redirect(url_for('homeworks.all'))


@homeworks.route("/<lesson_id>/<homework_id>", methods=["GET", "POST"])
@login_required
def show(lesson_id, homework_id):
    homework = HomeworksController().find_by_id(homework_id)
    filename = path.basename(homework.file_path)
    return render_template("homework.html", lesson_id=lesson_id, homework=homework, filename=filename)


@homeworks.route('/<lesson_id>/files/<filename>', methods=['GET', 'POST'])
@login_required
def download(lesson_id, filename):
    dir = 'C:\\Program Files\\Python36\\Python_projects\\FLASK\\ACA\\eLearning\\src\\static\\uploaded_files'
    return send_from_directory(directory=dir, filename=filename)
