from dndapp.mod_spelllist.models import Spell
from dndapp.mod_auth.models import User
from dndapp.views import verified_required, check_verified
from flask import render_template, Blueprint, session
from flask_login import login_required


# Blueprint name
mod_spells = Blueprint('spells', __name__, url_prefix='/spelllist')


# Default route, spell list route, spell list by class route
@mod_spells.route('/')
@mod_spells.route('/<char_class>')
@login_required
def spell_list(char_class=None, sortby=None):

    if char_class is None:
        spells = Spell.query.all()
    else:
        spells = Spell.query.filter(Spell.spell_class.contains(char_class)).order_by(Spell.level)

    verified = check_verified()

    return render_template('spelllist/spell_list.html', spells=spells,verified=verified)


# Individual spell route
@mod_spells.route('/spell/<spell_name>')
@login_required
@verified_required
def spell_desc(spell_name=None):
    if spell_name is None:
        return render_template('404.html'), 404
    else:
        spell = Spell.query.filter_by(name=spell_name).first()

        if spell:
            return render_template('spelllist/spell_desc.html', spell=spell)
        else:
            return render_template('404.html'), 404
