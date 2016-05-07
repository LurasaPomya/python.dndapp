from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from dndapp import db, lm
from dndapp.mod_auth.forms import LoginForm, CreateUserForm, ChangeUserPassword
from dndapp.mod_auth.models import User


mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

@mod_auth.route("/logout")
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('auth.login'))


@mod_auth.route('/signin/', methods=['GET', 'POST'])
def login():

    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if user and check_password_hash(user.password, form.password.data):

            session['user_id'] = user.id
            session['username'] = user.username
            session['user_level'] = user.role

            if request.form.get('remember_me'):
                login_user(user, remember=True)
            else:
                login_user(user)

            next = request.args.get('next')

            return redirect(next or url_for('spells.spell_list'))

        flash('Wrong email or password', 'error')

    return render_template("auth/login.html", form=form)

@mod_auth.route('/createuser/', methods=['GET', 'POST'])
@login_required
def create_user():

    user = User.query.filter_by(id=session['user_id']).first()


    if user.role  == 0:
        # Check if form submitted
        form = CreateUserForm(request.form)
        if form.validate_on_submit():
            password = generate_password_hash(form.password.data)
            user = User(form.username.data, form.email.data, password, form.access_level.data)
            user.active = True
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('auth.list_users'))
    else:
        return "You can't do this!"


    return render_template("auth/signup.html", form=form)

@mod_auth.route('/user/change_password/', methods=['GET', 'POST'])
@login_required
def change_user_password():

    form = ChangeUserPassword(request.form)

    if form.validate_on_submit():
        user = User.query.filter_by(id=session['user_id']).first()

        if form.new_password.data != form.new_password_repeat.data:
            return " New passwords do not match, try again!"

        if check_password_hash(user.password, form.current_password.data):
            user.password = generate_password_hash(form.new_password.data)
            db.session.commit()
            return "User Updated!"
        else:
            return "Wrong Current Password"

    return render_template("auth/changepass.html", form=form)

@mod_auth.route('/user/list/')
@login_required
def list_users():

    user = User.query.filter_by(id=session['user_id']).first()
    if user.role == 0:
        users = User.query.all()

        return render_template('auth/user_list.html',users=users)
    else:
        return "You can't do this!"

@mod_auth.route('/user/del/<userid>')
@login_required
def del_user(userid=None):
    if userid is None:
        return redirect(url_for('auth.list_users'))
    else:
        user = User.query.filter_by(id=userid).first()
        db.session.delete(user)
        db.session.commit()

        return redirect(url_for('auth.list_users'))

