from flask import Blueprint, render_template, session, request, url_for, redirect
from flask_login import login_required
from dndapp.mod_tasks.models import Task
from dndapp.mod_tasks.forms import CreateTaskForm
from dndapp.mod_auth.models import User
from dndapp import db


# Blueprint name
mod_tasks = Blueprint('tasks', __name__, url_prefix='/tasks')


# Tasks list route
@mod_tasks.route('/list/')
@login_required
def list_tasks():

    tasks = Task.query.all()

    return render_template('tasks/task_list.html',task_list=tasks)


# Create task route
@mod_tasks.route('/add_task/', methods=['GET', 'POST'])
@login_required
def add_task():

    user = User.query.filter_by(id=session['user_id']).first()
    form = CreateTaskForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():
        if user.role > 1:
            print "You Can't Do This!"
        else:
            title = form.title.data
            description = form.description.data
            priority = form.priority.data

            task = Task(title,description,priority)

            db.session.add(task)
            db.session.commit()

            return redirect(url_for('tasks.list_tasks'))
    return render_template("tasks/create_task.html", form=form)


# delete task route
@mod_tasks.route('/modify_task/del/<taskid>')
@login_required
def del_task(taskid=None):

    if taskid is None:
        return "Error!"
    else:
        task = Task.query.filter_by(id=taskid).first()
        db.session.delete(task)
        db.session.commit()

        return redirect(url_for('tasks.list_tasks'))