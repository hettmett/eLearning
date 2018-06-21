from flask import Blueprint
from datetime import datetime
from flask import render_template, request, session, url_for, flash, redirect
from com.groups.controller import GroupsController
from com.auth.controller import AuthController
<<<<<<< Updated upstream
from com.groups.controller import GroupsController
from datetime import datetime
from com.auth import login_required
=======
from com.auth import login_required, role_required
>>>>>>> Stashed changes

auth = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates', static_folder='static')


<<<<<<< Updated upstream
@auth.route('/')
@login_required
def index():
    return render_template('index.html')


=======
>>>>>>> Stashed changes
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email').strip()
        password = request.form.get('password').strip()
        try:
            if AuthController().login(email, password):
                return redirect(url_for('dashboard.Dashboard'))
            else:
                raise Exception(f"`{email}` user not found !")
        except Exception as ex:
            flash(str(ex))
    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    del session['user']
    return redirect(url_for('auth.login'))


@auth.route('/users/add', methods=["GET", "POST"])
<<<<<<< Updated upstream
=======
@role_required('admin')
>>>>>>> Stashed changes
def add():
    if request.method == "POST":
        first_name = request.form.get('first_name').strip().strip('\n')
        last_name = request.form.get('last_name').strip().strip('\n')
        email = request.form.get('email').strip().strip('\n')
        role = request.form.get('role').strip().strip('\n')
        fields = [first_name, last_name, email, role]
        try:
            print(fields)
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
@role_required('admin')
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
                print("ch_pas")
                AuthController().change_password(id, password)
                return redirect(url_for('auth.login'))
            else:
                raise Exception('The password does not match. Please try again.')
        except Exception as ex:
            flash(ex)
    return render_template('reset_password.html')


@auth.route('/users')
@login_required
@role_required('admin')
def show_all():
    all = AuthController().get_all()
    return render_template('users_table.html', users=all)


@auth.route('/edit/<id>', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def edit(id):
    user = AuthController().find_by_id(id)
    print(user)
    if request.method == 'POST':
        email = request.form.get( 'email' )
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        middle_name = request.form.get('middle_name')
        birth_date = request.form.get('birth_date')
        role = request.form.get('role')
        modified = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        fields_list = [email, first_name, last_name, middle_name, birth_date, role, modified]
        try:
            AuthController().edit(fields_list, id)
            return redirect(url_for('auth.show_all'))
        except Exception as ex:
            flash(ex)
    groups = GroupsController().all()
    return render_template('edit_user.html', user=user, groups=groups)


@auth.route('/delete/<id>')
@login_required
@role_required('admin')
def delete(id):
    AuthController().delete(id)
    return redirect(url_for('auth.show_all'))
