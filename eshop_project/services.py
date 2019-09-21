from eshop_project.models import User
from eshop_project import db
from flask_login import login_user, logout_user


class UserServices(object):
    @classmethod
    def createUser(cls, form):
        user = User(
            username=form.username.data,
            email=form.username.data
        )
        user.set_password(password=form.password.data)
        db.session.add(user)
        db.session.commit()

    @classmethod
    def authenticateUser(cls, form):
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user, remember=form.remember.data)
            return True
        return False

    @classmethod
    def logoutUser(cls):
        logout_user()            
