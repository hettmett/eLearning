import re
import hashlib
from uuid import uuid4
from datetime import datetime
from flask_mail import Mail, Message
from flask import session, current_app as app
from src.com.auth.models.users import Users
from src.config import conf
from src.models.base import DB


class AuthController(object):
    def __init__(self):
        super().__init__()

    def user_login(self, email: str, pwd: str):
        password = hashlib.sha512(pwd.encode('utf-8')).hexdigest()
        user = DB.query(Users).filter(Users.email == email, Users.password == password).first()
        DB.commit()
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

        host = conf['general']['HOST']
        port = conf['general']['PORT']
        with app.app_context():
            msg = Message('Hello', sender='elearning.aca2018@gmail.com',
                          recipients=[email])
            msg.body = "Hello. Follow the link to enter: {}:{}/{}".format(host, port, token)
            mail.send(msg)
        return "Sent"

    def add_user(self, first_name, last_name, email, role):
        user = Users(
            first_name=first_name,
            last_name=last_name,
            email=email,
            role=role,
            token=str(uuid4()),
            created=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        DB.add(user)
        DB.commit()
        self.send_mail(user.email, user.token)

    def check_token(self, token):
        our_user = DB.query(Users).filter_by(token=token).first()
        if our_user is not None:
            return our_user.id
        return 0

    def change_password(self, id, password):
        our_user = DB.query(Users).filter_by(id=id).first()
        if our_user is not None:
            our_user.password = hashlib.sha512(password.encode('utf-8')).hexdigest()
            DB.commit()

    def is_valid_email(self, email):
        if len(email) > 7:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\."
                        "([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
                return True
        return False