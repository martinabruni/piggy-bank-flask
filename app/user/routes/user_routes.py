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
from app.user.services.auth_service import AuthService
from app import bcrypt
from app.user.services.profile_service import ProfileService

user_bp = Blueprint("user_bp", __name__)

proService = ProfileService()


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
    return jsonify(profile_details=proService.getProfileDetails(current_user.id))
