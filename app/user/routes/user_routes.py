from flask import Blueprint, redirect, render_template, request, jsonify, url_for
from flask_login import current_user, login_required
from app.user.forms.login_form import LoginForm
from app.user.forms.registration_form import RegistrationForm
from app.user.services.auth_service import AuthService
from app import bcrypt

user_bp = Blueprint("user_bp", __name__)

auth_service = AuthService(bcrypt)


@user_bp.route("/", methods=["GET"])
def index():
    if current_user.is_authenticated:
        return redirect(url_for("profile"))
    return render_template("login.html")


@user_bp.route("/profile", methods=["GET"])
@login_required
def profile():
    return render_template("profile.html")


@user_bp.route("/register", methods=["GET"])
def register_page():
    return render_template("register.html")


@user_bp.route("/register", methods=["POST"])
def register():
    """
    Endpoint to register a new user.

    POST Data:
        - username: The username of the new user.
        - email: The email address of the new user.
        - pwd: The password of the new user.

    Returns:
        JSON response with the registration status and username.
    """
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        user = auth_service.register_user(
            form.username.data, form.email.data, form.pwd.data
        )
        return (
            jsonify({"message": "User registered successfully", "user": user.username}),
            201,
        )
    return jsonify({"errors": form.errors}), 400


@user_bp.route("/login", methods=["POST"])
def login():
    """
    Endpoint to log in a user.

    POST Data:
        - email: The email address of the user.
        - pwd: The password of the user.

    Returns:
        JSON response indicating success or failure of login.
    """
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = auth_service.authenticate_user(form.email.data, form.pwd.data)
        if user:
            auth_service.login(user)
            return jsonify({"message": "Logged in successfully"}), 200
        return jsonify({"message": "Invalid email or password"}), 401
    return jsonify({"errors": form.errors}), 400


@user_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    """
    Endpoint to log out the current user.

    Returns:
        JSON response indicating the success of the logout process.
    """
    auth_service.logout()
    return jsonify({"message": "Logged out successfully"}), 200
