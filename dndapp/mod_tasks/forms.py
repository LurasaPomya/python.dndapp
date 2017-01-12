from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


# Form to create task
class CreateTaskForm(FlaskForm):
    title = StringField('Task Title', [DataRequired(message='Please enter a Task Title!')])
    description = TextAreaField('Description', [DataRequired(message='Please enter a Description!')])
    priority = StringField('Priority', [DataRequired(message='Please Enter a Priority!')])
