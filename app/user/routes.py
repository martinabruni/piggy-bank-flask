from flask import Blueprint


# Defining a blueprint
user_bp = Blueprint(
    "user_bp", __name__, template_folder="templates", static_folder="static"
)
