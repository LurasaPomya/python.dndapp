from dndapp.mod_spelllist.models import Spell
from dndapp.mod_auth.models import User
from flask import render_template, Blueprint, session
from flask_login import login_required


mod_spells = Blueprint('spells', __name__, url_prefix='/spelllist')


@mod_spells.route('/')
@mod_spells.route('/<char_class>')
@login_required
def spell_list(char_class=None):

    if char_class == None:
        spells = Spell.query.all()
    else:
        spells = Spell.query.filter(Spell.spell_class.contains(char_class)).order_by(Spell.level)

    user = User.query.filter_by(id=session['user_id']).first()

    if user.role < 5:
        show_desc = True
    else:
        show_desc = False

    return render_template('spelllist/spell_list.html', spells=spells,show_desc=show_desc)

@mod_spells.route('/spell/<spell_name>')
def spell_desc(spell_name=None):
    if spell_name == None:
        return "No Spell Selected!"
    else:
        spell = Spell.query.filter_by(name=spell_name).first()
        return render_template('spelllist/spell_desc.html', spell=spell)
