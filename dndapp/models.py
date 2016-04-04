from dndapp import db


class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(45), unique=True)
    email = db.Column(db.VARCHAR(45), unique=True)
    password = db.Column(db.VARCHAR(120))

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
