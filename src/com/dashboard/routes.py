from flask import Blueprint, render_template
from com.courses.controller import CoursesController
from com.groups.controller import GroupsController
from com.auth import login_required


dashboard = Blueprint("dashboard", __name__, template_folder="templates", static_folder="static")


@dashboard.route("/")
@login_required
def Dashboard():
    return render_template('base.html')
