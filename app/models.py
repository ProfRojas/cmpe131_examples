# same as
# from app import db
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=False)
    email = db.Column(db.String(32), unique=True, nullable=False, index=True)
    password = db.Column(db.String(200), unique=False)

    def __repr__(self):
        return f'<{self.username}>'

