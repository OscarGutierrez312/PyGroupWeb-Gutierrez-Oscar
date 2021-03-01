from flask import Blueprint, Response, request, render_template, redirect

from app.Products.models import *
from app.Products.forms.Product_form import *

from app.users.models import User
from flask_login import login_user, logout_user, login_required, current_user

admin=Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/")
@login_required
def index():
    """
        Get the Admin Module
        ---
        tags:
            - Admin
        
        responses:
            200:
                description: Admin Module
        
    """
    return render_template('admin.html')