import re
from flask_mail import Mail, Message
from flask import session, current_app as app
from com.auth.models.users import Users
from config import sys_conf


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
        if user is not None:
            session['user'] = {'id': user.id, 'role': user.role, 'fnm': user.first_name, 'lnm': user.last_name}
            print(f'session = {session["user"]}')
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

    def add(self, first_name, last_name, email, role):
        if len(first_name) == 0:
            raise Exception('First name required')
        if len(last_name) == 0:
            raise Exception('Last name required')
        if len(email) == 0:
            raise Exception('Email required')
        if not self.is_valid_email(email):
            raise Exception('Email not valid')
        user = Users.add(first_name, last_name, email, role)
        self.send_mail(user.email, user.token)

    def check_token(self, token: str):
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
