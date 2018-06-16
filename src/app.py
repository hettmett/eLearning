from flask import Flask
from conf import sys_conf, sec_conf
from com.auth.routes import auth
from com.quiz.routes import quizes
from com.groups.routes import groups
from com.lessons.routes import lessons
from com.courses.routes import courses
from com.homeworks.routes import homeworks
from com.dashboard.routes import dashboard
from com.completed_homeworks.routes import completed_homeworks


app = Flask(__name__)
app.secret_key = sec_conf.get('secret_key')

# Registering Blueprints
app.register_blueprint(auth)
app.register_blueprint(groups)
app.register_blueprint(quizes)
app.register_blueprint(lessons)
app.register_blueprint(courses)
app.register_blueprint(homeworks)
app.register_blueprint(dashboard)
app.register_blueprint(completed_homeworks)


if __name__ == '__main__':
    app.run(sys_conf['host'], int(sys_conf['port']), sys_conf['debug'])
