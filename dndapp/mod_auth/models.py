from dndapp import db
from flask_login import UserMixin

# Base Class
class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class User(Base, UserMixin):

    __tablename__ = 'users'

    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)
    role = db.Column(db.SmallInteger, nullable=False, default=0)


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
