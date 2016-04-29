from dndapp import app, lm
from flask import render_template
from .mod_auth.models import User


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))