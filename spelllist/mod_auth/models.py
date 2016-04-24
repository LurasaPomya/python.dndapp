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
    authenticated = db.Column(db.Boolean, default=False)
    anonymous = True


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


def __repr__(self):
    return '<User %r>' % self.username


def get_id(self):
    return self.email


@property
def is_active(self):
    # True, as all users are active.
    return True

@property
def is_authenticated(self):
    return self.authenticated


@property
def is_anonymous(self):
    return self.anonomous

