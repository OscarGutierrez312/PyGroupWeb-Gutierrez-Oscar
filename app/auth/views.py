from flask import Blueprint, render_template, url_for, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

from app.db import db
from app.users.models import User

from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route("/login", methods=["GET", "POST"])
def login():
    """
        Checks if user does not exists in DB or if the password is invalid. Redirects to login and shows error if this happens.
        ---
        tags:
            - Authentication

        responses:
            200:
                description: Login Successful
        
    """
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        remember = True if request.form.get("remember") else False

        user = User.query.filter_by(email=email).first()


        if not user or not check_password_hash(user.password, password):
            flash("Please check your login details and try again.")
            return redirect(url_for("auth.login"))

        login_user(user, remember=remember)
        return redirect(url_for("home.index"))
    return render_template("login.html")


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    """
        If user exists shows an error and redirects to signup to try with other user.
        ---
        tags:
            - Authentication

        responses:
            200:
                description: Sign Up Successful
        
    """
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")

        user = User.query.filter_by(
            email=email
        ).first()


        if user:
            flash("Email address already exists")
            return redirect(url_for("auth.signup"))


        new_user = User(
            email=email,
            name=name,
            password=generate_password_hash(password, method="sha256"),
        )

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("signup.html")

@auth.route("")
def logged():
    """
        Verify if a user is logged in the Application
        ---
        tags:
            - Authentication

        responses:
            description:
              schema:
                type: boolean
        
    """
    user = current_user
    return user.is_authenticated

@auth.route("/logout")
@login_required
def logout():
    """
        Log Out the Current User.
        ---
        tags:
            - Authentication

        responses:
            200:
                description: Log Out Successful
        
    """
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for("auth.login"))
