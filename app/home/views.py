from flask import Blueprint, render_template, url_for, redirect, request, flash

from app.Products.views import *

from app.db import db

from flask_login import login_required, current_user

home = Blueprint('home', __name__, url_prefix='/home')

@home.route("/")
@login_required
def index():
    return redirect(url_for('products.get_products'))
    