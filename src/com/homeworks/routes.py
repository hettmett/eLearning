from flask import Blueprint
from datetime import datetime
from flask import render_template, request, url_for, flash, redirect
from src.com.homeworks.controller import HomeworksController
from src.com.auth import login_required


homeworks = Blueprint('homeworks', __name__, url_prefix='/homeworks', template_folder='templates',
                      static_folder='static')


@homeworks.route('/')
@login_required
def show_all():
    all = HomeworksController().all()
    return render_template('show_all.html', homeworks=all)


@homeworks.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    if request.method == 'POST':
        form = request.form
        lesson_id = form.get('lesson_id')
        title = form.get('title')
        description = form.get('description')
        file_path = form.get('file_path')
        deadline = form.get('deadline')
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            HomeworksController().new(lesson_id, title, description, file_path, deadline, created)
            return redirect(url_for('homeworks.show_all'))
        except Exception as ex:
            flash(ex)
    return render_template('new.html')


@homeworks.route('/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    # GET---------------------------------------------------------------
    fields = HomeworksController().find_by_id(id)
    # POST ******************************************************************************
    if request.method == 'POST':
        form = request.form
        try:
            lesson_id = form.get('lesson_id')
            title = form.get('title')
            description = form.get('description')
            file_path = form.get('file_path')
            deadline = form.get('deadline')
            modified = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            fields_list = [lesson_id, title, description, file_path, deadline, modified]
            for i, field in enumerate(fields_list):
                if 0 > len(field) > 255:
                    raise Exception(f"{field} required !")
            HomeworksController().edit(fields_list, fields.id)
            return redirect(url_for('homeworks.show_all'))
        except Exception as ex:
            flash(ex)
    # POST *******************************************************************************
    return render_template('edit.html', fields=fields)
    # GET---------------------------------------------------------------


@homeworks.route('/delete/<id>')
@login_required
def delete(id):
    HomeworksController().delete(id)
    return redirect(url_for('homeworks.show_all'))


@homeworks.route('/<id>')
@login_required
def show_one(id):
    homework = HomeworksController().find_by_id(id)
    return render_template('show_one.html', homework=homework)
