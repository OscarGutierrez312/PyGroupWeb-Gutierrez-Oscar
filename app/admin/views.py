from flask import Blueprint, Response, request, render_template, redirect

from app.Products.models import *
from app.Products.forms.Product_form import *

from app.auth.models import User
from flask_login import login_user, logout_user, login_required, current_user

admin=Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/")
def index():
    return render_template('admin.html')