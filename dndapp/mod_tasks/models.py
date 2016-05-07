from dndapp import db
from flask_login import UserMixin

# Base Class
class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class Task(Base, UserMixin):

    __tablename__ = 'tasks'

    title = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text(), nullable=False)
    priority = db.Column(db.String(5), nullable=False)

    def __init__(self, title, desc, priority):
        self.title = title
        self.description = desc
        self.priority = priority

