from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import BooleanField

from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import Email
from wtforms.validators import EqualTo




# registration form  
class RegistrationForm(FlaskForm):

    username = StringField(
        'Username',
        validators = [
            DataRequired(),
            Length(min=2, max=20)
        ]
    )

    email = StringField(
        'Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        'Password',
        validators = [
            DataRequired()
        ]
    )

    confirm_password = PasswordField(
        'Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
    )

    submit = SubmitField( 'Sign Up' )




#   login form
class LoginForm(FlaskForm):

    email = StringField(
        'Email Address',
        validators = [
            DataRequired(),
            Email()
        ]
    )

    password = StringField(
        'Password',
        validators = [
            DataRequired()
        ]
    )

    remember = BooleanField( 'Remember Me' )

    login = SubmitField( 'Login' )