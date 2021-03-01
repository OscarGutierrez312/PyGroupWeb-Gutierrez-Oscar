from flask import Flask, jsonify
from app.Products.views import *
from app.auth.views import *
from app.index.begin import *
from app.home.views import *
from app.orders.views import *
from app.users.views import *
from app.admin.views import *
from app.users.models import User

from flask_login import LoginManager
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

from app.db import db, ma
from flask_migrate import Migrate
from app.conf.config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect

ACTIVE_ENDPOINTS = [('/products', products), 
                    ('/auth', auth), 
                    ('/', begin), 
                    ('/home', home), 
                    ('/usr', usr), 
                    ('/cart', cart),
                    ('/admin', admin)]

SWAGGER_URL='/swagger'
API_URL='/spec'


swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app-name':"pygroup-webed-shop"
    }
)

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

    @app.route("/spec")
    def spec():
        swag=swagger(app)
        swag['info']['version']="1.0.0"
        swag['info']['title']= "pygroup-webed-shop"
        swag['info']['description']= "my shop example using flask"
        return jsonify(swag)
    
    

    with app.app_context():
        db.create_all()

    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)

    app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)

    return app

if __name__ == "__main__":
    app_flask = create_app()
    app_flask.run()

