from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from spelllist import db, lm
from spelllist.mod_auth.forms import LoginForm, CreateUserForm
from spelllist.mod_auth.models import User
from flask_login import login_user, login_required, logout_user

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
            session['username'] = user.username;
            session['user_level'] = user.role

            if request.form.get('remember_me'):
                login_user(user, remember=True)
            else:
                login_user(user)

            next = request.args.get('next')

            return redirect(next or url_for('spell_list'))

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
            user = User(form.username.data, form.email.data, password)
            user.active = True
            user.role = 1
            db.session.add(user)
            db.session.commit()

            return "User Added"
    else:
        return "You can't do this!"


    return render_template("auth/signup.html", form=form)

def check_user_level(user_id):
    user = User.query.filter_by(id=user_id)
    return user.role