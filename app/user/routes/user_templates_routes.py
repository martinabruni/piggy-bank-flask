from flask import Blueprint, redirect, render_template
from flask_login import current_user


user_templates_bp = Blueprint("user_templates_bp", __name__)


@user_templates_bp.route("/html/profile", methods=["GET"])
def render_profile():
    if current_user.is_authenticated:
        return render_template("profile.html")
    else:
        return redirect("/html/login")


@user_templates_bp.route("/html/register", methods=["GET"])
def render_register():
    return render_template("register.html")


@user_templates_bp.route("/html/login", methods=["GET"])
def render_login():
    return render_template("login.html")
