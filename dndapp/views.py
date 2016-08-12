from dndapp import app, lm
from functools import wraps
from flask import render_template, session
from .mod_auth.models import User


# Error Page Handlers
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Default Route
@app.route('/')
def index():
    return render_template('index.html')


# Needed for Login Manager
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


# Custom functions and routes
def check_verified():

    user = User.query.filter_by(id=session['user_id']).first()

    if user.is_verified:
        return True
    else:
        return False


def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        user = User.query.filter_by(id=session['user_id']).first()
        if not user.is_admin:
            return render_template('403.html'), 403
        return func(*args, **kwargs)

    return decorated_view

def verified_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        user = User.query.filter_by(id=session['user_id']).first()
        if not user.is_verified:
            return render_template('403.html'), 403
        return func(*args, **kwargs)

    return decorated_view
