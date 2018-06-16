from flask import Blueprint
from datetime import datetime
from flask import render_template, request, url_for, flash, redirect
from com.courses.controller import CoursesController
from com.auth import login_required


courses = Blueprint('courses', __name__, url_prefix='/courses',
                    template_folder='templates', static_folder='static')


@courses.route('/')
#@login_required
def get_all():
    all = CoursesController().all()
    print(all,'ssssssssssss')
    return render_template('all_courses.html', courses=all)


@courses.route('/new', methods=['GET', 'POST'])
#@login_required
def new():
    fields = []
    if request.method == 'POST':
        form = request.form
        course_name = form.get('title')
        description = form.get('description')
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        fields = [course_name, description, created]
        try:
            CoursesController().new(fields)
            return redirect(url_for('courses.get_all'))
        except Exception as ex:
            flash(ex)
    return render_template('new_cours.html', fields=fields)


@courses.route('/edit/<id>', methods=['GET', 'POST'])
#@login_required
def edit(id):
    fields = CoursesController().find_by_id(id)
    if request.method == 'POST':
        form = request.form
        course_name = form.get('course_name')
        description = form.get('description')
        modified = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        fields_list = [course_name, description,modified]
        try:
            CoursesController().edit(fields_list, id)
            return redirect(url_for('courses.get_all'))
        except Exception as ex:
            flash(ex)
    return render_template('edit_cours.html', fields=fields)


@courses.route('/delete/<id>')
#@login_required
def delete(id):
    CoursesController().delete(id)
    return redirect(url_for('courses.get_all'))


@courses.route('/<id>')
#@login_required
def show_one(id):
    courses = CoursesController().find_by_id(id)
    return render_template('one_course.html', courses=courses)
