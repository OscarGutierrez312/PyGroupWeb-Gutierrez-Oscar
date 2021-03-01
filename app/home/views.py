from flask import Blueprint, render_template, url_for, redirect, request, flash

from app.Products.views import *

from app.db import db

from flask_login import login_required, current_user

home = Blueprint('home', __name__, url_prefix='/home')

@home.route("/")
def index():
    """
        Redirect to Product Catalogue Page
        ---
        tags:
            - Home

        responses:
            200:
                description: Products Catalogue
        
    """
    return redirect(url_for('products.get_products', id=1))
    