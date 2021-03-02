import sys
from http import HTTPStatus
from flask import Blueprint, Response, request, render_template, redirect

from app.Products.models import *
from app.Products.forms.Product_form import *

from app.users.models import *
from flask_login import login_user, logout_user, login_required, current_user

products=Blueprint('products', __name__, url_prefix='/products')

EMPTY_SHELVE_TEXT = "Empty shelve!"
PRODUCTS_TITLE = "<h1> Products </h1>"
DUMMY_TEXT = "Dummy method to show how Response works"
RESPONSE_BODY = {"message": "", "data": [], "errors": [], "metadata": []}


@products.route("/add-category", methods=("GET","POST"))
def create_category():
    """
        Add a Category
        ---
        tags:
            - Products
        parameters:
            - in: path  
              name: name
              description: Name of the Category
              required: false
              type: string
        description: Allows to add a new category on the DB

        responses:
            200:
                description: Category Create Successful
        
    """

    if request.method == "POST":
        name=request.form.get('Name')
        category = create_new_category(name)
        return redirect('/products/success/'+name)

    return render_template("category.html")

@products.route("/add-product", methods=("GET","POST"))
def create_product():
    """
        Allows to add a new product of a category on the DB
        ---
        tags:
            - Products

        responses:
            200:
                description: Product Create Successful
        
    """
    form = MyForm()
    
    if form.validate_on_submit():
        create_new_product(form.name.data, form.image.data, form.price.data, form.marca.data, form.description.data, form.category_id.data)

        return redirect('/products/success/'+form.name.data)
    return render_template('product_ex.html', form=form)

    
@products.route("/success/<string:name>")
def success(name):
    """
        Return a message with the product or category created
        ---
        tags:
            - Products
        parameters:
            - in: path 
              name: name
              description: Name of the Product or Category
              required: true
              type: string
              
        responses:
            200:
                description: Category/Product Create Successful
       
    """
    return render_template('success.html', name=name)

@products.route("/list/<int:id>")
def get_products(id):
    """
        Return the products in a category from the database
        ---
        tags:
            - Products
        parameters:
            - in: path  
              name: Product ID
              description: Id of a category 
              required: true
              type: integer


        responses:
            200:
                description: Products List on Screen
        
    """
    products_obj = get_all_products(id)

    user=get_user_by_id(current_user.get_id())
    if(user):        
        role=user['role']   
    else:
        role=0
    return render_template('catalogue.html', contx=[current_user, role, products_obj])


@products.route("/product/<int:id>")
def get_product(id):
    """
        Get a Product
        ---
        tags:
            - Products
        parameters:
            - in: path
              name: id
              description: Id of the Product
              required: true
              type: integer


        responses:
            200:
                description: Product Returned
        
    """
    product = get_product_by_id(id)

    RESPONSE_BODY["data"] = product
    return product, 200


