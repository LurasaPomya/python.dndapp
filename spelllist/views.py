from flask import render_template, flash
from spelllist import app, lm
from .mod_auth.models import User
from flask_login import login_required



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spelllist')
@login_required
def spell_list():
    return render_template('spell_list.html')

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))