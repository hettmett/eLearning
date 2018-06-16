from flask import Blueprint
from datetime import datetime
from flask import render_template, request, url_for, flash, redirect
from com.groups.controller import GroupsController
from com.courses.controller import CoursesController
from com.auth.controller import AuthController
from com.courses.models.courses import Courses
from com.auth.models.users import Users
from com.auth import login_required


groups = Blueprint('groups', __name__, url_prefix='/groups',
                    template_folder='templates', static_folder='static')


@groups.route('/')
#@login_required
def get_all():
    group_name = GroupsController().all()
    courses_name = Courses().all()
    #tacher = Courses().all()
    #print(courses_name,"cursessssss")
    print(group_name, "group_name")
    return render_template('all_groups.html', group_name=group_name)


@groups.route('/new', methods=['GET', 'POST'])
#@login_required
def new():
    fields = []
    if request.method == 'POST':
        form = request.form
        group_name = form.get('groups_name')
        role = form.get('role')
        start_date = form.get('start_date')
        end_date = form.get('end_date')
        created = datetime.now().strftime('%Y-%m-%d')
       # modified = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        teacher_id = form.get('teacher_id')
        fields = [group_name,role,start_date,end_date,created,teacher_id]
        print(fields[1],'sssssssssss')
        try:
            GroupsController().new(fields)
            return redirect(url_for('groups.get_all'))
        except Exception as ex:
            flash(ex)
    courses = CoursesController().all()
    teacher = GroupsController().all_teachers()
    #for teacher in teacher:
    print(teacher,"aaaaaaaaaa")
    return render_template('new_group.html', courses=courses,teacher=teacher)


@groups.route('/edit/<id>', methods=['GET', 'POST'])
#@login_required
def edit(id):
    fields = GroupsController().find_by_id(id)
    if request.method == 'POST':
        form = request.form
        group_name = form.get('groups_name')
        role = form.get('role')
        start_date = form.get('start_date')
        end_date = form.get('end_date')
        modified = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        fields_list = [group_name, role,start_date,end_date,modified]
        try:
            GroupsController().edit(fields_list, id)
            return redirect(url_for('groups.get_all'))
        except Exception as ex:
            flash(ex)
    return render_template('edit_group.html', fields=fields)


@groups.route('/delete/<id>')
#@login_required
def delete(id):
    GroupsController().delete(id)
    return redirect(url_for('groups.get_all'))


@groups.route('/<id>')
#@login_required
def show_one(id):
    groups = GroupsController().find_by_id(id)
    return render_template('one_group.html', groups=groups)

@groups.route('/new_student',methods=['GET', 'POST'])
def new_student():
    fields = []
    if request.method == 'POST':
        form = request.form
        status = form.get('status')
        role = form.get('role')
        student_id = form.get('student_id')
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        fields = [role,status,student_id,created]
        print(fields,'sssssssssss')
        try:
            GroupsController().new_student(fields)
            return redirect(url_for('groups.get_all'))
        except Exception as ex:
            flash(ex)
    groups = GroupsController().get_all_groups()
    students = GroupsController().all_students()
    #for teacher in teacher:
    print(groups,"aaaaaaaaaa")
    return render_template('new_group_student.html', groups=groups,students=students)