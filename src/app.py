from flask import Flask
from src.config import sys_conf, sec_conf
from src.com.auth.routes import auth
from src.com.homeworks.routes import homeworks


app = Flask(__name__)
app.secret_key = sec_conf['secret_key']
app.register_blueprint(auth)
app.register_blueprint(homeworks)


if __name__ == '__main__':
    app.run(sys_conf['host'], int(sys_conf['port']), sys_conf['debug'])
