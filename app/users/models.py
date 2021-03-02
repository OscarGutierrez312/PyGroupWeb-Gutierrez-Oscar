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
    
class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    c_type = db.Column(db.String(100), nullable=False)
    c_number = db.Column(db.String(100), unique=True)
    date = db.Column(db.String(100), nullable=False)
    cvv=db.Column(db.Integer, nullable=False)
    n_tit=db.Column(db.String(100), nullable=False)
    mark = db.Column(db.String(100), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ["email", "name", "role"]

class CardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Card
        fields =["id", "c_type", "c_number", "n_tit", "mark"]

def get_user_by_id(id):
    user_qs = User.query.filter_by(id=id).first()
    user_schema = UserSchema()
    p = user_schema.dump(user_qs)
    return p

def add_user_card(typ, number, date, code, name, mark, user_id):
    card=Card(c_type=typ, c_number=number, date=date, cvv=code, n_tit=name, mark=mark, id_user=user_id)
    db.session.add(card)
    if db.session.commit():
        return card

def get_card_by_user(id):
    card_qs=Card.query.filter_by(id_user=id).all()
    card_schema = CardSchema()
    card_serialization = [card_schema.dump(card) for card in
                              card_qs]
    return card_serialization

def delete_user_card(id):
    Card.query.filter_by(id=id).delete()
    db.session.commit()




