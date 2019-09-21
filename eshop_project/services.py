from eshop_project.models import User
from eshop_project import db


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