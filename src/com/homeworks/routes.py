from flask import Blueprint
from datetime import datetime
from flask import render_template, request, url_for, flash, redirect
from com.lessons.controller import LessonsController
from com.homeworks.controller import HomeworksController
from com.auth import login_required, role_required


homeworks = Blueprint('homeworks', __name__, url_prefix='/homeworks',
                      template_folder='templates', static_folder='static')


@homeworks.route('/')
@login_required
@role_required('teacher')
def all():
    homeworks = HomeworksController().all()
    return render_template('all_homeworks.html', homeworks=homeworks)


@homeworks.route('/add', methods=['GET', 'POST'])
@login_required
@role_required('teacher')
def add():
    lessons = LessonsController().get_all()
    fields = []
    if request.method == 'POST':
        form = request.form
        lesson_id = form.get('lesson_id')
        title = form.get('title')
        description = form.get('description')
        file_path = HomeworksController().upload(request.files.get('file_path'))
        deadline = form.get('deadline')
        try:
            HomeworksController().add(lesson_id, title, description, file_path, deadline)
            return redirect(url_for('homeworks.all'))
        except Exception as ex:
            flash(ex)
    return render_template('add_homework.html', lessons=lessons, fields=fields)


@homeworks.route('/edit/<id>/', methods=['GET', 'POST'])
@login_required
@role_required('teacher')
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
            return redirect(url_for('homeworks.all'))
        except Exception as ex:
            flash(ex)
    return render_template('edit_homework.html', lessons=lessons, homework=homework)


@homeworks.route('/remove/<id>')
@login_required
@role_required('teacher')
def remove(id):
    HomeworksController().remove(id)
    return redirect(url_for('homeworks.all'))


@homeworks.route('/<id>')
@login_required
def show_one(id):
    homework = HomeworksController().find_by_id(id)
    return render_template('one_homework.html', homework=homework)
