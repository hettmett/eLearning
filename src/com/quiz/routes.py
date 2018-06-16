from flask import Blueprint
from flask import render_template, request, session, url_for, flash, redirect
from com.auth import login_required, role_required
from .quiz_controller import QuizController
from datetime import datetime


quizes = Blueprint('quizes', __name__, url_prefix='/quizes',
                   template_folder='templates', static_folder='static')


@quizes.route('/')
@login_required
def all():
    all_quizes = QuizController().get_all(session['user']['id'])
    return render_template('all_quizes.html', quizes=all_quizes)


@quizes.route('/new', methods=['GET', 'POST'])
@login_required
#@role_required('teacher')
def add():
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        group_id = form.get('group_id')
        lesson_ids = form.get('lesson_ids')
        count = form.get('count')
        start_time = form.get('start_time')
        duration = form.get('duration')
        create_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        modified_date = ""
        teacher_id = session['user']['id']
        print(type(teacher_id))
        lessons = list(map(int, lesson_ids.split(',')))

        try:
            QuizController().generate_quiz(teacher_id, int(group_id), title,
                                               lessons, start_time, create_date,
                                               modified_date, duration, int(count))

            return redirect(url_for('quizes.all'))
        except Exception as ex:
            flash(ex)
    return render_template('new_quiz.html')


@quizes.route('/edit/<hw_id>/', methods=['GET', 'POST'])
@login_required
#@role_required('teacher')
def edit(hw_id):
    quiz = QuizController().find_by_id(hw_id)
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        group_id = form.get('group_id')
        lesson_ids = form.get('lessons')
        #count = form.get('count')
        start_time = form.get('start_time')
        duration = form.get('duration')
        modified_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        teacher_id = session['user']['id']
        #lessons = list(map(int, lesson_ids.split(',')))
        try:
            QuizController().edit(int(hw_id), int(teacher_id), int(group_id), title,
                                  lesson_ids, start_time,
                                  modified_date, duration)
            # QuizController().generate_quiz(hw_id, teacher_id, int(group_id), title,
            #                                    lessons, start_time, create_date,
            #                                    modified_date, duration, int(count))
            return redirect(url_for('quizes.all'))
        except Exception as ex:
            flash(ex)
    return render_template('edit_quiz.html', quiz=quiz)


'''
@quizes.route('/delete/<id>')
@login_required
def remove(id):
    QuizController().remove(id)
    return redirect(url_for('quizes.all'))
'''
