from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5f1935debf3fa66cd472b4d2fec883fa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sql.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'is-warning'

from eshop_project import routes
