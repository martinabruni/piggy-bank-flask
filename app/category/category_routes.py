from flask import Blueprint


# Defining a blueprint
category_bp = Blueprint(
    "category_bp", __name__, template_folder="templates", static_folder="static"
)
