from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.user.forms.login_form import login_form
from app.user.forms.registration_form import registration_form
from app.user.services.auth_service import AuthService
from app import bcrypt

user_bp = Blueprint("user_bp", __name__)

# Dependency injection
auth_service = AuthService(bcrypt)


@user_bp.route("/register", methods=["POST"])
def register():
    form = registration_form(request.form)
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
    form = login_form(request.form)
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
    auth_service.logout()
    return jsonify({"message": "Logged out successfully"}), 200
