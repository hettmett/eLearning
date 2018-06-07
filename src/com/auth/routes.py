from flask import Blueprint
from flask import render_template, request, session, url_for, flash, redirect
from src.com.auth import login_required
from src.com.auth.controller import AuthController


auth = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates', static_folder='static')


@auth.route('/')
@login_required
def index():
    return render_template('index.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            email = request.form.get('email').strip().strip('\n')
            password = request.form.get('password').strip().strip('\n')
            if email == '' or len(email) > 30:
                raise Exception('email not required')
            if password == '' or len(password) > 20:
                raise Exception('password is required')
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
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        role = request.form.get('role')
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
        password = request.form.get('password')
        rep_password = request.form.get('repeat_password')
        try:
            if len(password) < 6:
                raise Exception('password required')
            if len(rep_password) < 6:
                raise Exception('rep_password required')
            if password == rep_password:
                AuthController().change_password(id, password)
                return redirect(url_for('auth.login'))
            else:
                raise Exception('The password does not match. Please try again.')
        except Exception as ex:
            flash(ex)
    return render_template('reset_password.html')
