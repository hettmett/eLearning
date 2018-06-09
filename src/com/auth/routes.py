from flask import Blueprint
from flask import render_template, request, session, url_for, flash, redirect
from src.com.auth import login_required
from src.com.auth.controller import AuthController


auth = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates', static_folder='static')


@auth.route('/')
@login_required
def index():
    id = int(session.get('user_id'))
    user = AuthController.find_by_id(id)
    user_name = f'{user[0]} {user[1]}'
    return render_template('index.html', user_name=user_name)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            if AuthController().login(email, password):
                flash(f"{email} logged in successfully")
                return redirect(url_for('auth.index'))
            else:
                raise Exception(f"`{email}` user not found !")
        except Exception as ex:
            flash(str(ex))
    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    del session['user_id']
    return redirect(url_for('auth.login'))


@auth.route('/users/new', methods=["GET", "POST"])
def new():
    if request.method == "POST":
        first_name = request.form.get('first_name').strip().strip('\n')
        last_name = request.form.get('last_name').strip().strip('\n')
        email = request.form.get('email').strip().strip('\n')
        role = request.form.get('role').strip().strip('\n')
        fields = [first_name, last_name, email, role]
        try:
            AuthController().new(fields)
        except Exception as ex:
            flash(ex)
    return render_template("create_user.html")


@auth.route('/<token>', methods=["GET", "POST"])
def sign_up(token):
    if AuthController().check_token(token) != 0:
        id = AuthController().check_token(token)
        return redirect(url_for('auth.reset_password', token=token, id=id))
    else:
        flash("token is incorrect")


@auth.route('/reset-password/<token>/<id>', methods=["GET", "POST"])
def reset_password(token=None, id=None):
    if request.method == "POST":
        password = request.form.get('password').strip().strip('\n')
        rep_password = request.form.get('repeat_password').strip().strip('\n')
        try:
            if len(password) == 0:
                raise Exception('Password required')
            if len(rep_password) == 0:
                raise Exception('Repeat password required')
            if password == rep_password:
                AuthController().change_password(id, password)
                return redirect(url_for('auth.login'))
            else:
                raise Exception('The password does not match. Please try again.')
        except Exception as ex:
            flash(ex)
    return render_template('reset_password.html')
