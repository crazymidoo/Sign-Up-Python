# Questo file py rende il folder 'website' un package
# Creazione l'app Flask

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'coseacaso'

    from .views import views
    from .auth import auth

    from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'coseacaso'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='')

    return app