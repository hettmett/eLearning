import re
from flask_mail import Mail, Message
from flask import session, current_app as app, flash
from com.auth.models.users import Users
from com.groups.controller import GroupsController
from conf import sys_conf
from com.groups.controller import GroupsController


class AuthController(object):
    def __init__(self):
        super().__init__()

    def login(self, email: str, pwd: str):
        if len(pwd) == 0:
            raise Exception('Password required')
        if len(email) == 0:
            raise Exception('Email required')
        if not self.is_valid_email(email):
            raise Exception('Email not valid')
        user = Users.login(email, pwd)

<<<<<<< Updated upstream
        # group_name = GroupsController.get_all_groups_by_teacher(user.id)
        # course_name = GroupsController.get_course_name(user.id)
        # print(f'course_name = {course_name}, group_name = {group_name}')

        if user is not None:
            session['user'] = {'id': user.id,
                               'role': user.role,
                               'fnm': user.first_name,
                               'lnm': user.last_name}
            print(f'session = {session["user"]}')
=======
        if user is not None:
            session['user'] = {
                'id': user.id,
                'role': user.role,
                'fnm': user.first_name,
                'lnm': user.last_name}

            if user.role == 'teacher':
                group = GroupsController.get_all_groups_by_teacher(user.id)
                course = GroupsController.get_coures(user.id)
                session['group'] = {
                    'id': group.id,
                    'nm': group.group_name}
                session['course'] = {
                    'cm': course.course_name}

            if user.role == 'student':
                student_group = GroupsController.get_group(user.id)
                course = GroupsController.get_coures_for_user(user.id)
                session['group'] = {
                    'id': student_group.id,
                    'nm': student_group.group_name}
                session['course'] = {
                    'cm': course.course_name}

                # student_group = GroupsController.get_group(user.id)
                # for i, sg in enumerate(student_group):
                #     tmp = {i: [sg.id, sg.group_name]}
                #     session['group'].update(tmp)
                # print(session['group'])
>>>>>>> Stashed changes
            return True
        return False
    def send_mail(self, email, token):
        app.config['MAIL_SERVER'] = 'smtp.gmail.com'
        app.config['MAIL_PORT'] = 465
        app.config['MAIL_USERNAME'] = 'elearning.aca2018@gmail.com'
        app.config['MAIL_PASSWORD'] = 'acapython'
        app.config['MAIL_USE_TLS'] = False
        app.config['MAIL_USE_SSL'] = True
        mail = Mail(app)

        host = sys_conf['host']
        port = sys_conf['port']
        with app.app_context():
            msg = Message('Hello', sender='elearning.aca2018@gmail.com', recipients=[email])
            msg.body = "Hello. Follow the link to enter: {}:{}/{}/{}".format(host, port, 'auth', token)
            mail.send(msg)
        return "Sent"

    def new(self, fields):
        if len(fields[0]) == 0:
            raise Exception('First name required')
        if len(fields[1]) == 0:
            raise Exception('Last name required')
        if len(fields[2]) == 0:
            raise Exception('Email required')
        if not self.is_valid_email(fields[2]):
            raise Exception('Email not valid')
        user = Users.new(fields)

        print(fields[0])
        print(fields[1])
        print(fields[2])
        print(fields[3])
        self.send_mail(user.email, user.token)
        return

    def check_token(self, token):
        our_user = Users.check_token(token)
        if our_user is not None:
            return our_user.id
        return 0

    def change_password(self, id, password):
        return Users.change_password(id, password)

    def is_valid_email(self, email):
        if len(email) > 7:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.""([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
                return True
        return False

    @staticmethod
    def find_by_id(id: int):
        return Users.find_by_id(id)

    def get_all(self):
        return Users.get_all()

    def edit(self, fields: list, id: int):
        return Users.edit(fields, id)

    def delete(self, id: int):
        return Users.delete(id)
