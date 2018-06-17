from com.auth.routes import login_required
from flask import Blueprint, render_template, redirect, request, url_for, flash, send_from_directory
from com.lessons.controllers import LessonsController
from os import path

from com.quiz.quiz_controller import QuizController

lessons = Blueprint("lessons", __name__, template_folder="templates", static_folder="static",
                    url_prefix="/lessons")

@lessons.route('/<group_id>/<id>/add_question', methods=['GET', 'POST'])
@login_required
def add_question(group_id,id):
    if request.method == 'POST':
        answers = []
        form = request.form
        question = form.get("question")
        answer1 = form.get("answer1")
        answer2 = form.get("answer2")
        answer3 = form.get( "answer3" )
        answer4 = form.get( "answer4" )
        answers.extend([answer1, answer2, answer3, answer4])
        right_ans = form.get("right_ans")
        QuizController().add_question(id, question, answers, right_ans)
        return redirect( url_for( "lessons.add_question", group_id=group_id, id=id ) )
    return render_template("add_questions.html", group_id=group_id, id=id)


@lessons.route('/<group_id>/files/<filename>', methods=['GET', 'POST'])
@login_required
def download(group_id,filename):
    dir = 'C:\\Users\\nareh\\Desktop\\Narek\\Python\\final_project\\EL\\src\\static\\files'
    return send_from_directory( directory=dir, filename=filename)

@lessons.route("/<group_id>")
@login_required
def get_all(group_id):
    all_lessons = LessonsController().all(group_id)
    print(f'all_lessons = {all_lessons}')
    return render_template("all_lessons.html", all_lessons=all_lessons,group_id=group_id)

@lessons.route('/<group_id>/new', methods=['GET', 'POST'])
@login_required
def new(group_id):
    if request.method == 'POST':
        form = request.form
        group_id = group_id
        title = form.get( "title" )
        description = form.get( "description" )
        lesson_date = form.get( "lesson_date" )
        file = request.files['file']
        try:
            file_path = LessonsController().upload(file)
            LessonsController().new(group_id, title, description, file_path, lesson_date)
            return redirect(url_for("lessons.get_all", group_id=group_id))
        except Exception as exception:
            flash(exception)
    return render_template('new_lesson.html')


@lessons.route('/<group_id>/delete/<id>')
@login_required
def delete(group_id, id):
    LessonsController().delete(id)
    return redirect(url_for("lessons.get_all", group_id=group_id))



@lessons.route("/<group_id>/edit/<id>", methods=["GET", "POST"])
@login_required
def edit(group_id, id):
    lesson = LessonsController().find_by_id(id)
    if request.method == "POST":
        form = request.form
        title = form.get("title")
        description = form.get("description")
        file_path = form.get("file_path")
        lesson_date = form.get("lesson_date")
        try:
            LessonsController().edit(title, description, file_path, lesson_date)
            return redirect(url_for("lessons.get_all", group_id=group_id))
        except Exception as exception:
            flash(exception)
    return render_template("edit_lesson.html", group_id=group_id, lesson=lesson)

@lessons.route("/<group_id>/<id>", methods=["GET", "POST"])
@login_required
def show(group_id, id):
    lesson = LessonsController().find_by_id(id)
    filename = path.basename(lesson.file_path)
    return render_template("lesson.html", group_id=group_id, lesson=lesson, filename=filename)
