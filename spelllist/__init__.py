from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

# import here to prevent circular imports
from spelllist.mod_auth.controllers import mod_auth as auth_module
app.register_blueprint(auth_module)

# Creates db's if we need them
db.create_all()

# import here to prevent circular imports
import spelllist.views

