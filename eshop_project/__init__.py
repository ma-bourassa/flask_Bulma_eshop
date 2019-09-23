from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from eshop_project.config import Config


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'is-warning'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)

    from eshop_project.users.routes import users
    from eshop_project.main.routes import main
    app.register_blueprint(main)
    app.register_blueprint(users)

    return app
