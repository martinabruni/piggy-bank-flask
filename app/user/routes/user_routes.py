from flask import (
    Blueprint,
    redirect,
    jsonify,
)
from flask_login import current_user
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
        return redirect("/html/login")
    return redirect("/html/profile")


@user_bp.route("/profile", methods=["GET"])
def profile():
    """
    Renders the user's profile page.

    If the user is not authenticated, they are redirected to the home page.

    Returns:
        Rendered template of the profile page.
    """
    if not current_user.is_authenticated:
        return jsonify(
            {
                "message": "You must be logged in",
                "success": False,
                "redirect": "/",
            }
        )
    return jsonify(
        profile_details=proService.getProfileDetails(current_user.id),
        success=True,
        redirect="/html/profile",
    )
