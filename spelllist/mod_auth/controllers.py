from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from spelllist import db
from spelllist.mod_auth.forms import LoginForm, CreateUserForm
from spelllist.mod_auth.models  import User

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():

    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):

            session['user_id'] = user.id
            flash('Welcome %s' % user.username)

            return redirect(url_for('spell_list'))

        flash('Wrong email or password', 'error-message')

    return render_template("auth/signin.html", form=form)

# @mod_auth.route('/createuser/', methods=['GET', 'POST'])
# def createuser():
# 
#     # Check if form submitted
#     form = CreateUserForm(request.form)
#
#     if form.validate_on_submit():
#         password = generate_password_hash(form.password.data)
#         user = User('dectala', form.email.data, password)
#         user.active = 0
#         user.role = 0
#         db.session.add(user)
#         db.session.commit()
#
#         return "User Added"
#
#     return render_template("auth/signup.html", form=form)