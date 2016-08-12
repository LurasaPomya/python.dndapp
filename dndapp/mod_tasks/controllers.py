from flask import Blueprint, render_template, session, request, url_for, redirect, flash
from flask_login import login_required
from dndapp.mod_tasks.models import Task
from dndapp.mod_tasks.forms import CreateTaskForm
from dndapp.mod_auth.models import User
from dndapp import db
from dndapp.views import admin_required, check_verified

# Blueprint name
mod_tasks = Blueprint('tasks', __name__, url_prefix='/tasks')


# Tasks list route
@mod_tasks.route('/list/')
@login_required
def task_list():

    tasks = Task.query.all()
    admin = check_admin()

    return render_template('tasks/task_list.html',task_list=tasks, admin=admin)


# Create task route
@mod_tasks.route('/add_task/', methods=['GET', 'POST'])
@login_required
@admin_required
def add_task():

    user = User.query.filter_by(id=session['user_id']).first()
    form = CreateTaskForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        priority = form.priority.data

        task = Task(title,description,priority)

        db.session.add(task)
        db.session.commit()

        return redirect(url_for('tasks.task_list'))
    return render_template("tasks/create_task.html", form=form)


# delete task route
@mod_tasks.route('/modify_task/del/<taskid>')
@login_required
@admin_required
def task_del(taskid=None):

    if taskid is None:
        flash("Problem removing task! PANIC!")

        return redirect(url_for('tasks.task_list'))
    else:
        task = Task.query.filter_by(id=taskid).first()
        db.session.delete(task)
        db.session.commit()
        flash("Task Deleted!")

        return redirect(url_for('tasks.task_list'))

# view task route
@mod_tasks.route('/view/<taskid>')
@login_required
def task_view(taskid=None):

    if taskid is None:
        return render_template('404.html'), 404
    else:
        task = Task.query.filter_by(id=taskid).first()

        if task:
            return render_template('tasks/task_desc.html', task=task)
        else:
            return render_template('404.html'), 404