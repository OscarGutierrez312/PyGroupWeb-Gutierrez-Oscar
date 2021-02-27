from app.db import db, ma
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
    authenticated = db.Column(db.Boolean, default=False, nullable=False)
    role= db.Column(db.Integer, default=ACCESS['user'])
    

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ["email", "name", "role"]

def get_user_by_id(id):
    user_qs = User.query.filter_by(id=id).first()
    user_schema = UserSchema()
    p = user_schema.dump(user_qs)
    return p

def is_admin(id):
    user_qs = User.query.filter_by(id=id).first()
    user_schema = UserSchema()
    user_qs.role = ACCESS['admin']
    db.session.commit()
    return user_qs

def allowed(id, access_level):
    user_qs = User.query.filter_by(id=id).first()
    return user_qs.role >= access_level

