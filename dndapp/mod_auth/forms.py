from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email


class LoginForm(Form):
    username = StringField('Username', [DataRequired(message='You need an Username!')])
    password = PasswordField('Password', [DataRequired(message='You need a Password!')])

class CreateUserForm(Form):
    email = StringField('Email Address', [Email(),DataRequired(message='Please enter your email!')])
    password = PasswordField('Password', [DataRequired(message='You need a Password!')])
    username = StringField('UserName', [DataRequired(message='You need a username')])
    access_level = IntegerField('Access Level', [DataRequired(message='You must set an access level')])

class ChangeUserPassword(Form):
    current_password = PasswordField('Current Password', [DataRequired(message='You must enter your current password!')])
    new_password = PasswordField('New Password', [DataRequired(message='Enter new password!')])
    new_password_repeat = PasswordField('New Password Again', [DataRequired(message='Enter new password Twice!')])
