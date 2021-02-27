from app.db import db, ma
from datetime import datetime
from flask import jsonify

class Cart(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    quantity=db.Column(db.Integer, default=1)
    id_user=db.Column(db.Integer, db.ForeignKey('user.id'))
    id_product=db.Column(db.Integer, db.ForeignKey('product.id'))
    

class CartSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cart
        fields = ["quantity", "id_product"]

def get_cart_by_user(id):
    cart_qs = Cart.query.filter_by(id_user=id).all()
    cart_schema = CartSchema()
    p= [cart_schema.dump(car) for car in cart_qs]
    return p

def add_product_to_car(user_id, product_id):
    cart=Cart.query.filter_by(id_user=user_id, id_product=product_id).first()
    if(cart):
        update_product_quantity(user_id, product_id, cart.quantity+1)
    else:
        cart=Cart(id_user=user_id, id_product=product_id)
        db.session.add(cart)
        if db.session.commit():
            return cart
        

def update_product_quantity(user_id, product_id, quantity):
    cart=Cart.query.filter_by(id_user=user_id, id_product=product_id).first()
    cart.quantity=quantity
    db.session.commit()
    return cart
    
    