from flask import render_template, flash
from spelllist import app, lm, db
from .mod_auth.models import User
from models import Spell
from flask_login import login_required



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spelllist')
@app.route('/spellist/<char_class>')
@login_required
def spell_list(char_class=None):

    if char_class == None:
        spells = Spell.query.all()
    else:
        spells = Spell.query.filter(Spell.spell_class.contains(char_class)).order_by(Spell.level)

    return render_template('spell_list.html', spells=spells)

@app.route('/spell/<spell_name>')
def spell_desc(spell_name=None):
    if spell_name == None:
        return "No Spell Selected!"
    else:
        spell = Spell.query.filter_by(name=spell_name).first()
        return render_template('spell_desc.html', spell=spell)


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))