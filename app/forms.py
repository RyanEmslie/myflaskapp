from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Who dis?', validators=[DataRequired()])
    password = PasswordField('Say the Magic Word', validators=[DataRequired()])
    remember_me = BooleanField('Come here often?')
    submit = SubmitField('Sign In')
