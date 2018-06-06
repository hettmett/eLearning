from flask import Flask
from src.config import conf
from src.com.auth.routes import auth
from src.com.homeworks.routes import homeworks


app = Flask(__name__)
app.secret_key = conf['security']['SECRET_KEY']
app.register_blueprint(auth)
app.register_blueprint(homeworks)


if __name__ == '__main__':
    app.run(conf['general']['HOST'], conf['general'].getint('PORT'), conf['general']['DEBUG'])
