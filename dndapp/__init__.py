from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)



# import here to prevent circular imports
from dndapp.mod_auth.controllers import mod_auth as auth_module
from dndapp.mod_spelllist.controllers import mod_spells as spell_module
from dndapp.mod_tasks.controllers import mod_tasks as tasks_module

app.register_blueprint(auth_module)
app.register_blueprint(spell_module)
app.register_blueprint(tasks_module)


# Creates db's if we need them
db.create_all()

# import here to prevent circular imports
import dndapp.views

