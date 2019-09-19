from flask import Flask, escape, request, render_template, url_for, redirect
from forms import RegistrationForm

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=["GET"])
def register():
    return render_template('register.html')
    #     form = RegistrationForm()


# @app.route('/login', methods=["GET", "POST"])
# def login():
#     form = RegistrationForm()
#     if form.validate_on_submit():

#         # Check the password and log the user in
#         # [...]

#         return redirect(url_for('home'))
#     return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
