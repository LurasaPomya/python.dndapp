from dndapp import db
from flask_login import UserMixin


# Base Class
class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


# Task Class
class Task(Base, UserMixin):

    __tablename__ = 'tasks'

    title = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text(), nullable=False)
    priority = db.Column(db.String(10), nullable=False)
    finished = db.Column(db.Boolean, default=False)

    def __init__(self, title, desc, priority, finished):
        self.title = title
        self.description = desc
        self.priority = priority
        self.finished = finished

