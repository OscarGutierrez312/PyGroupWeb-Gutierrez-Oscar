from flask import Blueprint, render_template, url_for, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

from app.db import db
from app.Products.models import *
from app.users.models import *
from app.orders.models import *

from http import HTTPStatus

from flask_login import login_user, logout_user, login_required, current_user

RESPONSE_BODY = {"message": "", "data": [], "errors": [], "metadata": []}

cart = Blueprint('cart', __name__, url_prefix='/cart')

@cart.route("/MyCart", methods=["GET", "POST"])
@login_required
def get():
    """
        Return the Orders Cart and SubTotal Price from a user Logged In
        ---
        tags:
            - Orders

        responses:
            200:
                description: Cart of User
        
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
    return render_template('cart.html', contx=[cart, role, products, subt])

@cart.route("/add/<int:id>")
@login_required
def add(id):
    """
        Add a product to a User Cart
        ---
        tags:
            - Orders
        parameters:
            - in: path
              name: id
              description: Id of the Product to Add
              required: true
              type: integer

        responses:
            200:
                description: Product Added to Cart
        
    """
    product = get_product_by_id(int(id))
    p=add_product_to_car(current_user.get_id(), product['id'])

    return get()

@cart.route("/add-in-car", methods=["GET", "POST"])
@login_required
def add_in_car():
    """
        Add a product in User Cart Page
        ---
        tags:
            - Orders

        responses:
            200:
                description: Product Returned
        
    """
    if request.method=="POST":
        id=request.form.get("product_id")
        product = get_product_by_id(int(id))
        p=add_product_to_car(current_user.get_id(), product['id'])
    return get()


@cart.route("/<int:id>")
def delete(id):
    """
        Delete a Product of a User Cart
        ---
        tags:
            - Orders
        parameters:
            - in: path
              name: id
              description: Id of the Product
              required: true
              type: integer

        responses:
            200:
                description: Product Deleted from the cart
        
    """
    delete_car_product(id)
    return get()


