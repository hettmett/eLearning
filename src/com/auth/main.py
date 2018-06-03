from flask import Blueprint
from flask import render_template, request, session, url_for, flash, redirect
from auth import login_required
from .loginController import UserController

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static')
user = UserController()


@auth.route('/')
@login_required
def index():
    return render_template('index.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            email = request.form.get('email').strip().strip('\n\t').strip()
            password = request.form.get('password').strip().strip('\n\t').strip()
            if email == '' or len(email) > 30:
                raise Exception('email not required')
            if password == '' or len(password) > 20:
                raise Exception('password is required')
            if user.user_login(email, password):
                flash(f"[{email}]logged in successfully !")
                return redirect(url_for('auth.index'))
            else:
                raise Exception(f"<<{email}>> user not found !!!")
        except Exception as ex:
            flash(str(ex))
    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    del session['user_id']
    return redirect(url_for('auth.login'))


# NAREK ******************************************************

@auth.route('/create_user', methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        role = request.form.get('role')
        user.add_user(first_name, last_name, email, role)
    return render_template("create_user.html")


@auth.route('/<token>', methods=["GET", "POST"])
def sign_up(token):
    if user.check_token(token) != 0:
        id = user.check_token(token)
        return redirect(url_for('auth.reset_password', token=token, id=id))
    else:
        flash("token is incorrect")
    return


@auth.route('/reset_password/<token>/<id>', methods=["GET", "POST"])
def reset_password(token=None, id=None):
    if request.method == "POST":
        password = request.form.get('password')
        rep_password = request.form.get('repeat_password')
        if password == rep_password:
            user.change_password(id, password)
            return redirect(url_for('auth.index'))
        else:
            flash('The password does not match. Please try again.')
    return render_template('reset_password.html')
