from flask import Blueprint
from datetime import datetime
from flask import render_template, request, url_for, flash, redirect, session
from com.courses.controller import CoursesController
from com.groups.controller import GroupsController
from com.auth import login_required, role_required


groups = Blueprint('groups', __name__, url_prefix='/groups',
                   template_folder='templates', static_folder='static')


@groups.route('/')
@login_required
@role_required('admin')
def get_all():
    group_name = GroupsController().all()
    print(group_name, "group_name")
    return render_template('all_groups.html', group_name=group_name)


@groups.route('/new', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def new():
    fields = []
    if request.method == 'POST':
        form = request.form
        group_name = form.get('groups_name')
        role = form.get('role')
        start_date = form.get('start_date')
        end_date = form.get('end_date')
        created = datetime.now().strftime('%Y-%m-%d')
        teacher_id = form.get('teacher_id')
        fields = [group_name, role, start_date, end_date, created, teacher_id]
        try:
            GroupsController().new(fields)
            return redirect(url_for('groups.get_all'))
        except Exception as ex:
            flash(ex)
    courses = CoursesController().all()
    teacher = GroupsController().all_teachers()
    return render_template('new_group.html', courses=courses, teacher=teacher, fields=fields)

#neww
@groups.route('/edit/<id>', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def edit(id):
    fields = []
    if request.method == 'POST':
        form = request.form
        group_name = form.get('groups_name')
        role = form.get('role')
        start_date = form.get('start_date')
        end_date = form.get('end_date')
        created = datetime.now().strftime('%Y-%m-%d')
        teacher_id = form.get('teacher_id')
        fields = [group_name, role, start_date, end_date, created, teacher_id]
        try:
            GroupsController().edit(fields, id)
            return redirect(url_for('groups.get_all'))
        except Exception as ex:
            flash(ex)

    group_edit = GroupsController().take_edit_group(id)
    courses = CoursesController().all()
    teacher = GroupsController().all_teachers()
    print(group_edit, 'hasav')
    return render_template('edit_group.html', courses=courses, teacher=teacher, group_edit=group_edit)


@groups.route('/delete/<id>')
@login_required
@role_required('admin')
def delete(id: int):
    GroupsController().delete(id)
    return redirect(url_for('groups.get_all'))


@groups.route('/all_students_in/delete/<id>/<group_id>')
@login_required
@role_required('admin')
def delete_user_in_group(id, group_id):
    GroupsController().delete_user_in_group(id)
    return redirect('/groups/all_students_in/' + group_id)


@groups.route('/<id>')
@login_required
def show_one(id):
    groups = GroupsController().delete_user_in_group(id)
    return render_template('one_group.html', groups=groups)


@groups.route('/all_students_in/<id>')
@login_required
def all_students_in(id):
    student = GroupsController().all_students_in(id)
    return render_template('all_group_student.html', student=student)


@groups.route('/all_students_in/new_student', methods=['GET', 'POST'])
def new_student():
    fields = []
    if request.method == 'POST':
        form = request.form
        status = form.get('status')
        role = form.get('role')
        student_id = form.get('student_id')
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        fields = [role, status, student_id, created]
        try:
            GroupsController().new_student(fields)
            return redirect(url_for('groups.get_all'))
        except Exception as ex:
            flash(ex)
    groups = GroupsController().get_all_groups()
    students = GroupsController().all_students()
    return render_template('new_group_student.html', groups=groups, students=students, fields=fields)
