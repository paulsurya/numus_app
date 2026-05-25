from flask_login import UserMixin
from .extension import db 

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

    def __repr__(self):
        return f'<User {User.username}>'
