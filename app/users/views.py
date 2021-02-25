from flask import Blueprint, render_template, url_for, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

from app.db import db
from app.auth.models import User

from flask_login import login_user, logout_user, login_required, current_user

usr = Blueprint('usr', __name__, url_prefix='/usr')

@usr.route("/MyProfile", methods=["GET", "POST"])
def get():
    return render_template('user.html')


