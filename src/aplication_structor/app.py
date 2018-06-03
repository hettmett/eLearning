from flask import Flask
from config import conf
# from com.auth.route import auth


app = Flask(__name__)
app.register_blueprint(auth, )
# register blueprints for components
# app.register_blueprint(auth, url_prefix='/auth')


if __name__ == '__main__':
    app.run(conf['general']['HOST'], conf['general'].getint('PORT'), conf['general']['DEBUG'])
