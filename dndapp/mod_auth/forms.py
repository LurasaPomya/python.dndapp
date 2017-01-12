from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email


# Login form
class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired(message='You need an Username!')])
    password = PasswordField('Password', [DataRequired(message='You need a Password!')])


# Create user form
class CreateUserForm(FlaskForm):
    email = StringField('Email Address', [Email(),DataRequired(message='Please enter your email!')])
    password = PasswordField('Password', [DataRequired(message='You need a Password!')])
    username = StringField('UserName', [DataRequired(message='You need a username')])


# Change user form
class ChangeUserPassword(FlaskForm):
    current_password = PasswordField('Current Password', [DataRequired(message='You must enter your current password!')])
    new_password = PasswordField('New Password', [DataRequired(message='Enter new password!')])
    new_password_repeat = PasswordField('New Password Again', [DataRequired(message='Enter new password Twice!')])
