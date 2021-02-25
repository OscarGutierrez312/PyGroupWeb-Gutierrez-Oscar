from flask import Flask
from app.Products.views import *
from app.auth.views import *
from app.index.begin import *
from app.home.views import *
from app.auth.models import User

from flask_login import LoginManager

from app.db import db, ma
from flask_migrate import Migrate
from app.conf.config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect

ACTIVE_ENDPOINTS = [('/products', products), ('/auth', auth), ('/', begin), ('/home', home)]

def create_app(config=DevelopmentConfig):

    app=Flask(__name__)

    migrate=Migrate(app, db)
    app.config.from_object(config)

    db.init_app(app)
    ma.init_app(app)

    csrf = CSRFProtect(app)
    csrf.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()

    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)

    return app

if __name__ == "__main__":
    app_flask = create_app()
    app_flask.run()

