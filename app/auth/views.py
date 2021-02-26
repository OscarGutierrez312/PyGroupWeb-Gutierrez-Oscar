from flask import Blueprint, render_template, url_for, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

from app.db import db
from app.auth.models import User

from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        remember = True if request.form.get("remember") else False

        user = User.query.filter_by(email=email).first()

        """ Checks if user does not exists in DB or if the password is 
        invalid. Redirects to login and shows error if this happens."""
        if not user or not check_password_hash(user.password, password):
            flash("Please check your login details and try again.")
            return redirect(url_for("auth.login"))

        login_user(user, remember=remember)
        return redirect(url_for("home.index"))
    return render_template("login.html")


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")

        user = User.query.filter_by(
            email=email
        ).first()

        """If user exists shows an error and redirects to signup to try
        with other user.
        """

        if user:
            flash("Email address already exists")
            return redirect(url_for("auth.signup"))

        """Creates new user in DB with hashed password for security reasons"""
        new_user = User(
            email=email,
            name=name,
            password=generate_password_hash(password, method="sha256"),
        )

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("signup.html")


@auth.route("/logout")
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for("auth.login"))
