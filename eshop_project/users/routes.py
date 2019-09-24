from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from eshop_project.users.forms import LoginForm, RegistrationForm
from eshop_project.users.services import UserServices

users = Blueprint('users', __name__)

@users.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        UserServices.createUser(form)
        flash(
            f'Your account has been created. You can now log in {form.username.data}!', 'is-primary')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)


@users.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        if UserServices.authenticateUser(form):
            flash(f'Welcome back {form.username.data}!', 'is-primary')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash(
                f'Failed to login. Please check your username and password.', 'is-danger')
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@users.route('/logout')
def logout():
    UserServices.logoutUser()
    return redirect(url_for('main.home'))


@users.route('/account')
@login_required
def account():
    return render_template('account.html')
