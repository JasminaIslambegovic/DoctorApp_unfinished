from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms. validators import Length, EqualTo, Email, DataRequired, ValidationError
from doctorApp.models import Doctor

class LoginForm(FlaskForm):
    email_address = StringField(label = 'Email:', validators=[DataRequired()])
    password = PasswordField(label = 'Password:', validators=[DataRequired()])
    submit = SubmitField(label='Log in')

