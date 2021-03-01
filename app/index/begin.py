from flask import Blueprint, render_template, url_for, redirect, request, flash

from app.db import db
from app.auth.views import *
from app.home.views import *

from flask_login import login_user, logout_user, login_required, current_user

begin = Blueprint('', __name__, url_prefix='/')

@begin.route("/")
def index():
    return redirect(url_for('home.index'))