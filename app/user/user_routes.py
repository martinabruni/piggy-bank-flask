from flask import (
    Blueprint,
    app,
    current_app,
    redirect,
    render_template,
    request,
    jsonify,
)
from flask_login import current_user, login_required, logout_user
from app.user.forms.login_form import LoginForm
from app.user.forms.registration_form import RegistrationForm
from app.user.auth_service import AuthService
from app import bcrypt

user_bp = Blueprint("user_bp", __name__)
auth_service = AuthService(bcrypt)


@user_bp.route("/", methods=["GET"])
def index():
    """
    Redirects the user to the appropriate page based on their authentication status.

    If the user is not authenticated, they are redirected to the login page.
    If the user is authenticated, they are redirected to their profile page.

    Returns:
        Redirect response to either /login or /profile.
    """
    if not current_user.is_authenticated:
        return redirect("/login")
    return redirect("/profile")


@user_bp.route("/profile", methods=["GET"])
def profile():
    """
    Renders the user's profile page.

    If the user is not authenticated, they are redirected to the home page.

    Returns:
        Rendered template of the profile page.
    """
    if not current_user.is_authenticated:
        return redirect("/")
    return render_template("profile.html")


@user_bp.route("/register", methods=["POST", "GET"])
def register():
    """
    Endpoint to register a new user.

    Handles both GET and POST requests:
        - GET request renders the registration form.
        - POST request processes the form data, validates it, and registers the user.

    POST Data:
        - username: The username of the new user.
        - email: The email address of the new user.
        - pwd: The password of the new user.

    Returns:
        JSON response with the registration status and username if successful,
        or form errors if validation fails.
    """
    if request.method == "GET":
        return render_template("register.html")

    form = RegistrationForm(request.form)

    # Validate and process the registration form
    if form.validate_on_submit():
        user = auth_service.register_user(
            form.username.data, form.email.data, form.pwd.data
        )
        return (
            jsonify({"message": "User registered successfully", "user": user.username}),
            201,
        )

    return jsonify({"errors": form.errors}), 400


@user_bp.route("/login", methods=["POST", "GET"])
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
    if request.method == "GET":
        return render_template("login.html")

    form = LoginForm(request.form)

    # Validate and process the login form
    if form.validate_on_submit():
        user = auth_service.authenticate_user(form.email.data, form.pwd.data)
        if user:
            auth_service.login(user)
            return jsonify({"message": "Logged in successfully"}), 200
        return jsonify({"message": "Invalid email or password"}), 401

    return jsonify({"errors": form.errors}), 400


@user_bp.route("/logout", methods=["POST"])
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
        return jsonify({"message": "You must be logged in to logout"}), 400

    auth_service.logout()
    return jsonify({"message": "Logged out successfully"}), 200
