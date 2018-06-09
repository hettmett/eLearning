from flask import Blueprint
from datetime import datetime
from flask import render_template, request, url_for, flash, redirect
from src.com.homeworks.controller import HomeworksController
from src.com.auth import login_required


homeworks = Blueprint('homeworks', __name__, url_prefix='/homeworks',
                      template_folder='templates', static_folder='/static')


@homeworks.route('/')
@login_required
def all():
    all = HomeworksController().all()
    return render_template('all_homeworks.html', homeworks=all)


@homeworks.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    fields = []
    if request.method == 'POST':
        form = request.form
        lesson_id = form.get('lesson_id')
        title = form.get('title')
        description = form.get('description')
        file_path = form.get('file_path')
        deadline = form.get('deadline')
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        fields = [lesson_id, title, description, file_path, deadline, created]
        try:
            HomeworksController().new(fields)
            return redirect(url_for('homeworks.all'))
        except Exception as ex:
            flash(ex)
    return render_template('new_homework.html', fields=fields)


@homeworks.route('/edit/<hw_id>/', methods=['GET', 'POST'])
@login_required
def edit(hw_id):
    homework = HomeworksController().find_by_id(hw_id)
    if request.method == 'POST':
        form = request.form
        lesson_id = form.get('lesson_id')
        title = form.get('title')
        description = form.get('description')
        file_path = form.get('file_path')
        deadline = form.get('deadline')
        modified = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        fields = [lesson_id, title, description, file_path, deadline, modified]
        try:
            HomeworksController().edit(fields, hw_id)
            return redirect(url_for('homeworks.all'))
        except Exception as ex:
            flash(ex)
    return render_template('edit_homework.html', homework=homework)


@homeworks.route('/delete/<id>')
@login_required
def delete(id):
    HomeworksController().delete(id)
    return redirect(url_for('homeworks.all'))


@homeworks.route('/<id>')
@login_required
def show_one(id):
    homework = HomeworksController().find_by_id(id)
    return render_template('one_homework.html', homework=homework)
