from flask import request, render_template, url_for, redirect, flash
from eshop_project.forms import RegistrationForm, LoginForm
from eshop_project import app
from eshop_project.services import UserServices


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        UserServices.createUser(form)
        flash(
            f'Your account has been created. You can now log in. {form.username.data}!', 'is-primary')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f'Membership created successfully for {form.username.data}!', 'is-primary')
        return redirect(url_for('home'))
    return render_template('login.html', form=form)
