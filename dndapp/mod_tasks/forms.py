from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class CreateTaskForm(Form):
    title = StringField('Task Title', [DataRequired(message='Please enter a Task Title!')])
    description = StringField('Description', [DataRequired(message='Please enter a Description!')])
    priority = TextAreaField('Priority', [DataRequired(message='Please Enter a Priority!')])
