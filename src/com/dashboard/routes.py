<<<<<<< Updated upstream
from flask import Blueprint, render_template
from com.courses.controller import CoursesController
from com.groups.controller import GroupsController
=======
from flask import Blueprint, render_template, session, redirect, url_for
>>>>>>> Stashed changes
from com.auth import login_required


dashboard = Blueprint("dashboard", __name__, template_folder="templates", static_folder="static")


@dashboard.route("/")
@login_required
def Dashboard():
<<<<<<< Updated upstream
=======
    if session:
        role = session.get('user', {}).get('role')
        if role == 'admin':
            return redirect(url_for('auth.show_all'))
        if role == 'teacher':
            return redirect(url_for('groups.all_students_in', id=session.get('group', {}).get('id')))
        if role == 'student':
            return redirect(url_for('groups.all_students_in', id=session.get('group', {}).get('id')))
>>>>>>> Stashed changes
    return render_template('base.html')
