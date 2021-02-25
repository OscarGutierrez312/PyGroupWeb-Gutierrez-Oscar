from app.db import db
from flask_login import UserMixin

ACCESS = {
    'guest': 0,
    'user': 1,
    'admin': 2
}

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    authenticated = db.Column(db.Boolean,default=False, nullable=False)
    role=ACCESS['user']

def is_admin(self):
    return self.access == ACCESS['admin']

def allowed(self, access_level):
    return self.access >= access_level

