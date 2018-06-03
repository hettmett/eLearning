import hashlib
from uuid import uuid4
from flask import session, current_app as app
from .user import User
from datetime import datetime
from flask_mail import Mail, Message
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///auth.db')
Session = sessionmaker(bind=engine)
db_session = Session()


class UserController(object):
    def __init__(self):
        pass

    def user_login(self, email: str, password: str):
        user = db_session.query(User).filter(User.email == email, User.password == password).first()
        db_session.commit()
        if user is not None:
            session['user_id'] = user.id
            return True
        return False

    def send_mail(self, email, token):


        mail = Mail(app)
        app.config['MAIL_SERVER'] = 'smtp.gmail.com'
        app.config['MAIL_PORT'] = 465
        app.config['MAIL_USERNAME'] = 'elearning.aca2018@gmail.com'
        app.config['MAIL_PASSWORD'] = 'acapython'
        app.config['MAIL_USE_TLS'] = False
        app.config['MAIL_USE_SSL'] = True
        mail = Mail(app)
        with app.app_context():
            msg = Message('Hello', sender='elearning.aca2018@gmail.com',
                          recipients=[email])
            msg.body = "Hello. Follow the link to enter:  127.0.0.1:5555/{}".format(token)
            mail.send(msg)
        return "Sent"

    def add_user(self, first_name, last_name, email, role):
        user = User()
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.role = role
        user.token = str(uuid4())
        user.created = datetime.now()
        Session = sessionmaker(bind=engine)
        db_session = Session()
        db_session.add(user)
        db_session.commit()
        self.send_mail(user.email, user.token)

    def check_token(self, token):
        Session = sessionmaker(bind=engine)
        db_session = Session()
        our_user = db_session.query(User).filter_by(token=token).first()
        if our_user is not None:
            return our_user.id
        return 0

    def change_password(self, id, password):
        Session = sessionmaker(bind=engine)
        db_session = Session()
        our_user = db_session.query(User).filter_by(id=id).first()
        if our_user is not None:
            our_user.password = hashlib.sha512(password.encode('utf-8')).hexdigest()
            print(our_user.password)
            db_session.commit()