import json
from flask import Blueprint
from flask import render_template, request, session, url_for, flash, redirect
from com.auth import login_required, role_required
from .controller import QuizController
from com.lessons.controller import LessonsController
from com.groups.controller import GroupsController
from datetime import datetime


quizes = Blueprint('quizes', __name__, url_prefix='/quizes',
                   template_folder='templates', static_folder='static')


@quizes.route('/')
@login_required
@role_required('teacher', 'student')
def all():
    role = session['user']['role']
    if role == 'teacher':
<<<<<<< Updated upstream
        all_quizes = QuizController().get_all_by_teacher_id(
                                        session['user']['id']
                                        )
    elif role == 'student':
        all_quizes = QuizController().get_all_by_student_id(
                                        session['user']['id']
                                        )
=======
        all_quizes = QuizController().get_all_by_teacher_id(session['user']['id'])
    elif role == 'student':
        all_quizes = QuizController().get_all_by_student_id(session['user']['id'])
>>>>>>> Stashed changes
    return render_template('all_quizes.html', role=role, quizes=all_quizes)


@quizes.route('/new', methods=['GET', 'POST'])
@login_required
# @role_required('teacher')
def add():
<<<<<<< Updated upstream
    groups = GroupsController().get_all()
=======
    groups = GroupsController().get_all_groups()
    lessons = LessonsController().get_all_by_teacher_id(session['user']['id'])
>>>>>>> Stashed changes
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        group_id = form.get('group_id')
        lesson_ids = form.get('lesson_ids')
        count = form.get('count')
        start_time = form.get('start_time')
        duration = form.get('duration')
        create_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        teacher_id = session['user']['id']
<<<<<<< Updated upstream
        #lessons = LessonController().get_all()
=======
>>>>>>> Stashed changes
        lessons = list(map(int, lesson_ids.split(',')))

        try:
            QuizController().generate_quiz(teacher_id, int(group_id), title,
                                           lessons, start_time, create_date,
                                           duration, int(count))

            return redirect(url_for('quizes.all'))
        except Exception as ex:
            flash(ex)
    return render_template('new_quiz.html', groups=groups)


@quizes.route('/edit/<id>/', methods=['GET', 'POST'])
@login_required
# @role_required('teacher')
def edit(id):
    groups = GroupsController().get_all()
    quiz = QuizController().find_by_id(id)
    group = GroupsController().find_by_id(quiz.group_id)
    lesson_ids = ','.join(map(str, json.loads(quiz.lessons)))

    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        group_id = form.get('group_id')
<<<<<<< Updated upstream
        lesson_ids = form.get('lessons')
=======
        lessons = form.get('lessons')
>>>>>>> Stashed changes
        count = form.get('count')
        start_time = form.get('start_time')
        duration = form.get('duration')
        modified_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        teacher_id = session['user']['id']
<<<<<<< Updated upstream
        lessons = list(map(int, lesson_ids.split(',')))
=======
        lessons = list(map(int, lessons.split(',')))
>>>>>>> Stashed changes
        try:
            QuizController().edit(int(id), int(teacher_id), int(group_id),
                                  title, lessons, start_time,
                                  modified_date, duration, int(count))
            return redirect(url_for('quizes.all'))
        except Exception as ex:
            flash(ex)
    return render_template('edit_quiz.html', groups=groups, group=group,
                           quiz=quiz, lesson_ids=lesson_ids)


@quizes.route('/delete/<id>')
@login_required
# @role_required('teacher')
def remove(id):
    QuizController().remove(id)
    return redirect(url_for('quizes.all'))
<<<<<<< Updated upstream
=======


@quizes.route('/pass/<id>', methods=['GET', 'POST'])
@login_required
# @role_required('teacher')
def quiz_online(id):
    data = QuizController().get_quiz_data(id)
    return render_template('quiz0.html', data=data)
>>>>>>> Stashed changes
