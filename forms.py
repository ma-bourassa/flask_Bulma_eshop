from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField("Nom d'utilisateur", validators=[
                           DataRequired(), Length(min=3, max=20)])
    email = StringField('Courriel', validators=[DataRequired(), Email()])
    password = PasswordField('Mot de passe', validators=[DataRequired(), Length(
        min=6, message="Le mot de passe doit contenir au moins 6 caractères")])
    passwordConfirmation = PasswordField('Confirmer le mot de passe',
                                         validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Inscription')


class LoginForm(FlaskForm):
    username = StringField("Nom d'utilisateur", validators=[
                           DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    remember = BooleanField('Se souvenir de moi')
    submit = SubmitField('Se connecter')
