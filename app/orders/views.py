from flask import Blueprint, render_template, url_for, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

from app.db import db
from app.Products.models import *
from app.auth.models import *
from app.orders.models import *

from http import HTTPStatus

from flask_login import login_user, logout_user, login_required, current_user

RESPONSE_BODY = {"message": "", "data": [], "errors": [], "metadata": []}

cart = Blueprint('cart', __name__, url_prefix='/cart')

@cart.route("/MyCart", methods=["GET", "POST"])
@login_required
def get():
    cart=get_cart_by_user(current_user.get_id())    
    user=get_user_by_id(current_user.get_id())
    role=user['role']
    return render_template('cart.html', contx=[cart, role])

@cart.route("/add/<int:id>")
@login_required
def add(id):
    product = get_product_by_id(int(id))
    p=add_product_to_car(current_user.get_id(), product['id'])

    if(p):        
        RESPONSE_BODY["data"] = p
    return RESPONSE_BODY, 200