# from com.auth import role_required
# from com.lessons.controller import LessonsController
from flask import Blueprint, render_template, session, flash, redirect, url_for


dashboard = Blueprint("dashboard", __name__, template_folder="templates", static_folder="static")

#
# @dashboard.route("/")
# @role_required('admin')
# def admin():
#     lessons = LessonsController()
#     pass
#
#
# @dashboard.route("/")
# @role_required('teacher')
# def teacher():
#     pass
#


@dashboard.route("/")
# @role_required('student')
def student():
    role = session['user']['role']
    if role == 'admin':
        return render_template("admin.html")
    elif role == "teacher":
        return render_template("teacher.html")
    elif role == "student":
        return render_template("student.html")
    return redirect(url_for('auth.index'))
