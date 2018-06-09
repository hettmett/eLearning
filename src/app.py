from flask import Flask
from config import sys_conf, sec_conf
from com.auth.routes import auth
from com.homeworks.routes import homeworks


app = Flask(__name__)
app.secret_key = sec_conf['secret_key']

# Registering Blueprints
app.register_blueprint(auth)
app.register_blueprint(homeworks)


if __name__ == '__main__':
    app.run(sys_conf['host'], int(sys_conf['port']), sys_conf['debug'])