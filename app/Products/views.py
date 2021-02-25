import sys
from http import HTTPStatus
from flask import Blueprint, Response, request, render_template, redirect

from app.Products.models import *
from app.Products.forms.Product_form import *

from flask_login import login_required

products=Blueprint('products', __name__, url_prefix='/products')

EMPTY_SHELVE_TEXT = "Empty shelve!"
PRODUCTS_TITLE = "<h1> Products </h1>"
DUMMY_TEXT = "Dummy method to show how Response works"
RESPONSE_BODY = {"message": "", "data": [], "errors": [], "metadata": []}


@products.route("/categories")
@login_required
def get_categories():
    """
        Verificar que si get_all_categories es [] 400, message = "No hay nada"
    :return:
    """
    categories = get_all_categories()
    status_code = HTTPStatus.OK

    if categories:
        RESPONSE_BODY["message"] = "OK. Categories List"
        RESPONSE_BODY["data"] = categories
    else:
        RESPONSE_BODY["message"] = "OK. No categories found"
        RESPONSE_BODY["data"] = categories
        status_code = HTTPStatus.NOT_FOUND

    return RESPONSE_BODY, status_code


@products.route("/add-category", methods=["POST"])
def create_category():
    """

    :return:
    """
    RESPONSE_BODY["message"] = "Method not allowed"
    status_code = HTTPStatus.METHOD_NOT_ALLOWED
    if request.method == "POST":
        data = request.json
        category = create_new_category(data["name"])
        RESPONSE_BODY["message"] = "OK. Category created!"
        RESPONSE_BODY["data"] = category
        status_code = HTTPStatus.CREATED

    return RESPONSE_BODY, status_code

@products.route("/add-product", methods=("GET","POST"))
def create_product():
    
    form = MyForm()
    
    if form.validate_on_submit():
        create_new_product(form.name.data, form.price.data, form.color.data, form.description.data, form.category_id.data)

        return redirect('/products/success')
    return render_template('product_ex.html', form=form)

    
@products.route("/success")
def success():
    return render_template('success.html')

@products.route("/")
def get_products():
    products_obj = get_all_products()

    RESPONSE_BODY["data"] = products_obj
    RESPONSE_BODY["message"] = "Products list"

    return RESPONSE_BODY, 200


@products.route("/product/<int:id>")
def get_product(id):
    product = get_product_by_id(id)

    RESPONSE_BODY["data"] = product
    return RESPONSE_BODY, 200


@products.route("/product-stock/<int:product_id>")
def get_product_stock(product_id):
    product_stock = get_stock_by_product(product_id)
    RESPONSE_BODY["message"] = "Product stock"
    RESPONSE_BODY["data"] = product_stock

    return RESPONSE_BODY, HTTPStatus.OK


@products.route("/need-restock")
def get_products_that_need_restock():
    products_low_stock = get_products_with_low_stock()
    RESPONSE_BODY["message"] = "This products need to be re-stocked"
    RESPONSE_BODY["data"] = products_low_stock

    return RESPONSE_BODY, HTTPStatus.OK


@products.route("/register-product-stock/<int:id>", methods=["PUT", "POST"])
def register_product_refund_in_stock(id):

    # TODO Complete this view to update stock for product when a register for
    # this products exists. If not create the new register in DB

    if request.method == "PUT":
        data=request.json
        stock=update_stock(id, data["quantity"])
        RESPONSE_BODY["message"] = \
            "Stock for this product were updated successfully!"
        RESPONSE_BODY["data"]=stock
        status_code = HTTPStatus.OK
    elif request.method == "POST":
        data=request.json

        stock=create_stock(id ,data["quantity"])
        RESPONSE_BODY["message"] = \
            "Stock for this product were created successfully!"
        RESPONSE_BODY["data"]=stock
        status_code = HTTPStatus.CREATED
        
    else:
        RESPONSE_BODY["message"] = "Method not Allowed"
        status_code = HTTPStatus.METHOD_NOT_ALLOWED

    return RESPONSE_BODY, status_code
