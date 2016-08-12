from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# Create Flask App
app = Flask(__name__)
app.config.from_object('config')

# Attach database to it
db = SQLAlchemy(app)

# Initialize and attach login manager
lm = LoginManager()
lm.init_app(app)


# Import blueprints here to avoid circular imports
from dndapp.mod_auth.controllers import mod_auth as auth_module
from dndapp.mod_spelllist.controllers import mod_spells as spell_module
from dndapp.mod_tasks.controllers import mod_tasks as tasks_module

# Register blueprints
app.register_blueprint(auth_module)
app.register_blueprint(spell_module)
app.register_blueprint(tasks_module)


# Creates db's if we need them
db.create_all()

# import default views here to prevent circular imports
import dndapp.views

