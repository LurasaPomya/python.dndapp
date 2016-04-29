from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email


class LoginForm(Form):
    username = StringField('Username', [DataRequired(message='You need an Username!')])
    password = PasswordField('Password', [DataRequired(message='You need a Password!')])

class CreateUserForm(Form):
    email = StringField('Email Address', [Email(),DataRequired(message='Please enter your email!')])
    password = PasswordField('Password', [DataRequired(message='You need a Password!')])
    username = StringField('UserName', [DataRequired(message='You need a username')])
