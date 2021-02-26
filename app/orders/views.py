from flask import Blueprint, render_template, url_for, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

from app.db import db
from app.auth.models import User

from flask_login import login_user, logout_user, login_required, current_user

cart = Blueprint('cart', __name__, url_prefix='/cart')

@cart.route("/MyCart", methods=["GET", "POST"])
@login_required
def get():
    return render_template('cart.html')