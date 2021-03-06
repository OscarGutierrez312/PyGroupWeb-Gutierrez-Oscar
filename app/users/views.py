from flask import Blueprint, render_template, url_for, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

from app.db import db
from app.users.models import *
from app.Products.models import *
from app.orders.models import *

from flask_login import login_user, logout_user, login_required, current_user

usr = Blueprint('usr', __name__, url_prefix='/usr')

@usr.route("/MyProfile", methods=["GET", "POST"])
@login_required
def get():
    """
        Return the Profile User Page
        ---
        tags:
            - Users

        responses:
            200:
                description: User Page
        
    """
    user=get_user_by_id(current_user.get_id())
    role=user['role']
    cards=get_card_by_user(current_user.get_id())
    return render_template('user.html', contx=[user, role, cards])

@usr.route("/add-card", methods=["GET", "POST"])
@login_required
def add_card():
    """
        Add a card to User Payment Methods
        ---
        tags:
            - Users

        responses:
            200:
                description: Payment Method Added to User
        
    """
    user=get_user_by_id(current_user.get_id())
    role=user['role']

    if request.method == "POST":

        typ=request.form.get("type")
        number=request.form.get("number")
        date=request.form.get("date")
        code=request.form.get("code")
        name=request.form.get("name")
        mark=request.form.get("mark")
        user_id=current_user.get_id()

        card=add_user_card(typ, number, date, code, name, mark, user_id)

        return get()

    return render_template('card.html', contx=[user, role])

@usr.route("/delete-card/<int:id>")
@login_required
def delete_card(id):
    """
        Delete a Card from User Payment Methods
        ---
        tags:
            - Users
        parameters:
            - in: path
              name: id
              description: Id of the Card
              required: true
              type: integer

        responses:
            200:
                description: Card Deleted
        
    """
    delete_user_card(id)
    return get()

@usr.route("/pre-pay")
@login_required
def pre_pay():
    """
        Return Pre-pay Page
        ---
        tags:
            - Users
        responses:
            200:
                description: Pre-pay Page
        
    """
    user=get_user_by_id(current_user.get_id())
    role=user['role']
    cards=get_card_by_user(current_user.get_id())
    return render_template('pre_pay.html', contx=[cards, role])

@usr.route("/pay/<int:id>")
@login_required
def pay(id):
    """
        Return the Payment Page
        ---
        tags:
            - Users
        parameters:
            - in: path
              name: id
              description: Id of the Card for Pay the order
              required: true
              type: integer

        responses:
            200:
                description: Pay Successful
        
    """
    products=[]
    subt=0
    cart=get_cart_by_user(current_user.get_id())    
    for c in cart:
        products.append(get_product_by_id(c['id_product'])) 
    user=get_user_by_id(current_user.get_id())
    role=user['role']
    for p in products:
        subt+=p['price']
    
    cards=get_card_by_user(current_user.get_id())
    for c in cards:
        if(c['id']==id):card=c
    return render_template('pay.html', contx=[card, role, products, subt, cart])

@usr.route("/success")
@login_required
def success():
    """
        Successful Payment Page
        ---
        tags:
            - Users

        responses:
            200:
                description: Successful Payment
        
    """
    user=get_user_by_id(current_user.get_id())
    role=user['role']
    cards=get_card_by_user(current_user.get_id())
    return render_template('success_pay.html', contx=[user, role, cards])
