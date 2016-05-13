from dndapp import app, lm
from flask import render_template
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
def check_user_level(user_id):
    user = User.query.filter_by(id=user_id)
    return user.role