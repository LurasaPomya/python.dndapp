from spelllist import app
from flask import render_template
from sqlalchemy import create_engine

eng = create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'))


@app.route('/testing')
def testing():
    return app.config.get("TEST_VAR")


@app.route('/userlist')
def list_users():
    return User.query.all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/spelllist')
@app.route('/spelllist/<char_class>')
def spell_list(char_class=None):
    return render_template('spell_list.html', char_class=char_class)


@app.route('/spell/<spell_name>')
def spell_desc(spell_name):
    return render_template('spell_desc.html', spell_name=spell_name)