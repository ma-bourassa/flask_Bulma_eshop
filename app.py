from flask import Flask, escape, request, render_template, url_for, redirect, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '5f1935debf3fa66cd472b4d2fec883fa'


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
        flash(
            f'Membership created successfully for {form.username.data}!', 'is-primary')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f'Membership created successfully for {form.username.data}!', 'is-primary')
        return redirect(url_for('home'))
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
