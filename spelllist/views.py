from flask import render_template
from spelllist import app, db
from mod_auth.models import User

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spelllist')
def spell_list():
    return render_template('spell_list.html')