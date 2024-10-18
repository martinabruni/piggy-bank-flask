from app import bcrypt
from flask import Blueprint, jsonify, request
from flask_login import current_user

from app.user.services.auth_service import AuthService
from app.user.forms.login_form import LoginForm
from app.user.forms.registration_form import RegistrationForm


auth_bp = Blueprint("auth_bp", __name__)
auth_service = AuthService(bcrypt)


@auth_bp.route("/register", methods=["POST"])
def register():
    """
    Endpoint to register a new user.

    Handles POST requests:
        - POST request processes the form data, validates it, and registers the user.

    POST Data:
        - username: The username of the new user.
        - email: The email address of the new user.
        - pwd: The password of the new user.

    Returns:
        JSON response with the registration status and username if successful,
        or form errors if validation fails.
    """
    form = RegistrationForm(request.form)

    # Validate and process the registration form
    if form.validate_on_submit():
        user = auth_service.register_user(
            form.username.data, form.email.data, form.pwd.data
        )
        return (
            jsonify(
                {
                    "message": "User registered successfully",
                    "user": user.username,
                    "success": True,
                    "redirect": "/html/profile",
                }
            ),
            201,
        )
    return (
        jsonify(
            {
                "message": form.errors,
                "success": False,
                "redirect": "/",
            }
        ),
        400,
    )


@auth_bp.route("/login", methods=["POST"])
def login():
    """
    Endpoint to log in a user.

    Handles both GET and POST requests:
        - GET request renders the login form.
        - POST request processes the form data, validates it, and attempts user authentication.

    POST Data:
        - email: The email address of the user.
        - pwd: The password of the user.

    Returns:
        JSON response indicating success or failure of login.
        - Success: Message indicating login success.
        - Failure: Message indicating invalid credentials.
    """
    if current_user.is_authenticated:
        auth_service.logout()
    form = LoginForm(request.form)
    # Validate and process the login form
    if form.validate_on_submit():
        user = auth_service.authenticate_user(form.email.data, form.pwd.data)
        if user:
            auth_service.login(user)
            return (
                jsonify(
                    {
                        "message": "Logged in successfully",
                        "success": True,
                        "redirect": "/html/profile",
                    }
                ),
                200,
            )
        return (
            jsonify(
                {
                    "message": "Invalid email or password",
                    "success": False,
                    "redirect": "/",
                }
            ),
            401,
        )

    return (
        jsonify(
            {
                "message": form.errors,
                "success": False,
                "redirect": "/",
            }
        ),
        400,
    )


@auth_bp.route("/logout", methods=["POST"])
def logout():
    """
    Endpoint to log out the current user.

    This route handles POST requests where the user logs out, and if they are
    not logged in, an error message is returned.

    Returns:
        JSON response indicating the success or failure of the logout process.
        - Success: Message indicating the user was logged out successfully.
        - Failure: Message indicating the user needs to be logged in to log out.
    """
    if not current_user.is_authenticated:
        return (
            jsonify(
                {
                    "message": "You must be logged in to logout",
                    "success": False,
                    "redirect": "/",
                }
            ),
            400,
        )
    auth_service.logout()
    return (
        jsonify(
            {
                "message": "Logged out successfully",
                "success": True,
                "redirect": "/",
            }
        ),
        200,
    )


@auth_bp.route("/delete_user", methods=["DELETE"])
def delete_user():
    """
    Route to delete the currently authenticated user.

    This route deletes the user associated with the current session, based on
    their email. The user must be authenticated to perform this action.

    Returns:
        JSON response:
            - Success: A message confirming that the user was deleted.
            - Failure: An error message if the user is not logged in.
    """
    if not current_user.is_authenticated:
        return (
            jsonify(
                {
                    "message": "You must be logged in",
                    "success": False,
                    "redirect": "/",
                }
            ),
            400,
        )
    auth_service.delete_user(current_user.email)
    return (
        jsonify(
            {
                "message": "User deleted successfully",
                "success": True,
                "redirect": "/",
            }
        ),
        200,
    )
