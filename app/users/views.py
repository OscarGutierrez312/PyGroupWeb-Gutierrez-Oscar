from flask import Blueprint, render_template, url_for, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

from app.db import db
from app.auth.models import *

from flask_login import login_user, logout_user, login_required, current_user

usr = Blueprint('usr', __name__, url_prefix='/usr')

@usr.route("/MyProfile", methods=["GET", "POST"])
@login_required
def get():
    user=get_user_by_id(current_user.get_id())
    role=user['role']
    return render_template('user.html', contx=[user, role])


