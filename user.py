from flask_login import UserMixin

from __main__ import db


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(120), nullable=False, unique=True)
    hash = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.login}')"

