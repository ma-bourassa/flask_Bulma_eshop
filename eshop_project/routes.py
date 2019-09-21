from flask import request, render_template, url_for, redirect, flash, request
from eshop_project.forms import RegistrationForm, LoginForm
from eshop_project import app
from eshop_project.services import UserServices
from flask_login import current_user, login_required


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        UserServices.createUser(form)
        flash(
            f'Your account has been created. You can now log in. {form.username.data}!', 'is-primary')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        if UserServices.authenticateUser(form):
            flash(f'Welcome back {form.username.data}!', 'is-primary')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(
                f'Failed to login. Please check your username and password.', 'is-danger')
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    UserServices.logoutUser()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html')
