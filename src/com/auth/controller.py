import re
from flask_mail import Mail, Message
from flask import session, current_app as app
from src.com.auth.models.users import Users
from src.config import sys_conf
from src.models.base import DB


class AuthController(object):
    def __init__(self):
        super().__init__()

    def login(self, email: str, pwd: str):
        if len(email) == 0:
            raise Exception('Email required')
        if not self.is_valid_email(email):
            raise Exception('Email not valid')
        if len(pwd) == 0:
            raise Exception('Password required')
        user = Users.login(email, pwd)
        if user is not None:
            session['user_id'] = user.id
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
        print(user.email)
        self.send_mail(user.email, user.token)
        return

    def check_token(self, token):
        our_user = DB.query(Users).filter_by(token=token).first()
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
