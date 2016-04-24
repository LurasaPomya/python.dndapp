from spelllist import db
from flask_login import UserMixin

# Base Class
class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class User(Base, UserMixin):

    __tablename__ = 'users'

    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)
    role = db.Column(db.SmallInteger, nullable=False, default=0)


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class Spell(Base):

    __tablename = 'spells'

    name = db.Column(db.String(255), unique=True, nullable=False)
    level = db.Column(db.SmallInteger, nullable=False)
    school = db.Column(db.String(255), nullable=False)
    spell_class = db.Column(db.String(255), nullable=False)
    casting_time = db.Column(db.String(255), nullable=False)
    spell_range = db.Column(db.String(50))
    duration = db.Column(db.String(50))
    page = db.Column(db.String(10))
    saving_throw = db.Column(db.String(25))
    damage_type = db.Column(db.String(50))
    damage = db.Column(db.String(50))
    description = db.Column(db.Text)
    at_higher = db.Column(db.Text)
    
    ritual = db.Column(db.Boolean, default=False)
    concentration = db.Column(db.Boolean, default=False)
