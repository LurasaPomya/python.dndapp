from spelllist import app, db
from flask import render_template
from spelllist.models import User


@app.route('/testing')
def testing():
    return app.config.get("TEST_VAR")


@app.route('/createdb')
def createdb():
    db.create_all()
    return "Database Created!"


@app.route('/createuser/<username>/<email>')
def create_user(username, email):
    temp_user = User(username, email)
    db.session.add(temp_user)
    db.session.commit()
    return "User Created!"


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